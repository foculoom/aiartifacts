#!/usr/bin/env python3
"""Run one already-staged synthetic case with an existing Codex subscription.

This does not install skills, copy credentials, grade answers or prove isolation.
Outputs are private until manually sanitized and reviewed for publication.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--prompt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--codex", default="codex", help="Already-installed Codex executable")
    parser.add_argument("--command-path", help="Optional controlled command PATH for a failure case")
    args = parser.parse_args()
    project = args.project.resolve(strict=True)
    prompt = args.prompt.read_text()
    output = args.output.resolve()
    if output.exists():
        parser.error("output must be a new directory; preserve earlier attempts")
    if not 1 <= args.timeout <= 600:
        parser.error("timeout must be between 1 and 600 seconds")
    environment = {key: os.environ[key] for key in (
        "HOME", "PATH", "TMPDIR", "SHELL", "USER", "LOGNAME", "LANG", "TERM"
    ) if key in os.environ}
    try:
        status = subprocess.run([args.codex, "login", "status"], env=environment,
                                capture_output=True, text=True, timeout=15)
        chatgpt = status.returncode == 0 and "logged in using chatgpt" in (
            status.stdout + status.stderr).lower()
        if not chatgpt:
            parser.error("existing ChatGPT login was not verified; refusing inference")
        version = subprocess.run([args.codex, "--version"], env=environment,
                                 capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        parser.error("Codex authentication/version check unavailable; refusing inference")
    if version.returncode:
        parser.error("Codex version check failed; refusing inference")
    output.mkdir(parents=True)
    codex_state_dir = Path(environment.get("HOME", str(Path.home()))) / ".codex"
    roots = [codex_state_dir / "skills", Path.home() / ".agents/skills"]
    disabled = sorted({str(p) for root in roots if root.exists() for p in root.rglob("SKILL.md")})
    overrides = "skills.config=[" + ",".join(
        "{path=" + json.dumps(path) + ",enabled=false}" for path in disabled
    ) + "]"
    command = [
        args.codex, "--no-daemon", "-a", "never", "exec", "--ignore-user-config",
        "--ephemeral", "--skip-git-repo-check", "--sandbox", "workspace-write",
        "--json", "-C", str(project), "-c", overrides,
        "-c", "project_doc_max_bytes=0", "-c", "features.plugins=false",
        "-c", "features.apps=false", "-c", "features.hooks=false",
        "-c", "features.memories=false", "-c", "features.multi_agent=false",
        "-c", 'shell_environment_policy.inherit="core"',
        "-c", "shell_environment_policy.experimental_use_profile=false",
    ]
    if args.command_path:
        command += ["-c", "shell_environment_policy.set.PATH=" + json.dumps(args.command_path)]
    command += ["-o", str(output / "answer.txt"), "-"]
    # Preserve ordinary existing HOME without moving it or copying auth state.
    # Provider keys, endpoint overrides and parent-agent session variables do
    # not enter this process. The supported existing ChatGPT login is required.
    start = time.monotonic()
    child = subprocess.Popen(command, env=environment, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True, start_new_session=True)
    timed_out = False
    try:
        stdout, stderr = child.communicate(prompt, timeout=args.timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(child.pid, signal.SIGTERM)
        try:
            stdout, stderr = child.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            os.killpg(child.pid, signal.SIGKILL)
            stdout, stderr = child.communicate()
    (output / "events.jsonl").write_text(stdout)
    (output / "stderr.txt").write_text(stderr)
    (output / "prompt.txt").write_text(prompt)
    result = {
        "exit": child.returncode, "timeout": timed_out,
        "seconds": round(time.monotonic() - start, 2), "command": command,
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "auth": "existing ChatGPT login; no API environment passed",
        "cli_version": version.stdout.strip(),
        "input_inventory_sha256": hashlib.sha256(
            (project / "input-inventory.json").read_bytes()).hexdigest()
            if (project / "input-inventory.json").exists() else None,
        "model": "CLI default; record exact identifier separately if exposed",
        "disabled_host_skill_count": len(disabled),
        "parent_codex_home_override_present": bool(os.environ.get("CODEX_HOME")),
        "initial_exec_context": "not exposed by this runner; isolation requires separate evidence",
    }
    (output / "run.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("exit", "timeout", "seconds")}))
    return 124 if timed_out else child.returncode


if __name__ == "__main__":
    raise SystemExit(main())
