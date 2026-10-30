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
import shutil
import stat
import subprocess
import time
import uuid


def file_hash(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_codex_home(path, project):
    """Select an existing physical profile; never create it or inspect auth."""
    if ".." in path.parts:
        raise ValueError("codex home must not contain parent-directory components")
    selected = path.absolute()
    if any(part.is_symlink() for part in (selected, *selected.parents)):
        raise ValueError("codex home must not use symlink aliases")
    if not selected.is_dir():
        raise ValueError("codex home must be an existing directory")
    if selected.resolve(strict=True) != selected:
        raise ValueError("codex home must be a physical directory")
    if selected == project or project in selected.parents:
        raise ValueError("codex home must be outside the evaluator project")
    if not os.access(selected, os.R_OK | os.W_OK | os.X_OK):
        raise ValueError("codex home must be readable, writable and searchable")
    return selected


def validate_external_inventory(path, project):
    """Select measurement metadata without staging it in the model's project."""
    if ".." in path.parts:
        raise ValueError("inventory must not contain parent-directory components")
    selected = path.absolute()
    if any(part.is_symlink() for part in (selected, *selected.parents)):
        raise ValueError("inventory must not use symlink aliases")
    if selected == project or project in selected.parents:
        raise ValueError("inventory must be outside the evaluator project")
    if not selected.is_file() or selected.resolve(strict=True) != selected:
        raise ValueError("inventory must be an existing physical regular file")
    return selected


def discover_host_skills(roots, limit=10000):
    """Follow installed links, retaining alias/canonical paths; fail closed."""
    found, visited = set(), 0

    def visit(path, ancestors):
        nonlocal visited
        visited += 1
        if visited > limit:
            raise ValueError("skill enumeration limit exceeded")
        info = path.stat()  # Dangling links and unreadable entries are errors.
        if stat.S_ISDIR(info.st_mode):
            identity = (info.st_dev, info.st_ino)
            if identity in ancestors:
                raise ValueError("skill directory link cycle")
            for child in sorted(path.iterdir()):
                visit(child, ancestors | {identity})
        elif path.name == "SKILL.md" and stat.S_ISREG(info.st_mode):
            found.update((str(path.absolute()), str(path.resolve(strict=True))))

    for root in roots:
        if root.exists() or root.is_symlink():
            visit(root, set())
    return sorted(found)


def capture_session(stdout, state_dir, project, cli_version, output, started):
    """Read only this run's UUID-bound local rollout; never inspect other chats."""
    result = {"status": "unavailable", "runtime_models": [], "runtime_efforts": [],
              "backend_model": None, "isolation": "requires independent context review"}
    try:
        events = [json.loads(line) for line in stdout.splitlines() if line.strip()]
        if any(not isinstance(event, dict) for event in events):
            raise ValueError("invalid event record")
        ids = {event["thread_id"] for event in events if event.get("type") == "thread.started"}
        if len(ids) != 1:
            raise ValueError("expected one emitted thread identity")
        thread_id = ids.pop()
        if not isinstance(thread_id, str) or str(uuid.UUID(thread_id)) != thread_id:
            raise ValueError("invalid thread identity")
        sessions = state_dir / "sessions"
        matches = list(sessions.glob("*/*/*/*-" + thread_id + ".jsonl"))
        if len(matches) != 1:
            raise ValueError("expected one matching rollout")
        source = matches[0]
        if any(p.is_symlink() for p in (source, *source.parents)):
            raise ValueError("linked rollout is not accepted")
        info = source.stat()
        if not stat.S_ISREG(info.st_mode) or info.st_size > 20_000_000 or info.st_mtime < started - 1:
            raise ValueError("rollout is not a fresh bounded regular file")
        raw = source.read_bytes()
        records = [json.loads(line) for line in raw.splitlines() if line.strip()]
        if any(not isinstance(r, dict) or not isinstance(r.get("payload"), dict) for r in records):
            raise ValueError("invalid rollout record")
        metas = [r["payload"] for r in records if r.get("type") == "session_meta"]
        if len(metas) != 1:
            raise ValueError("expected one rollout session identity")
        meta = metas[0]
        if (meta.get("id") != thread_id or Path(meta.get("cwd", "")).resolve() != project
                or meta.get("cli_version") != cli_version.removeprefix("codex-cli ")):
            raise ValueError("rollout identity, directory or version mismatch")
        (output / "session.jsonl").write_bytes(raw)
        contexts = [r["payload"] for r in records if r.get("type") == "turn_context"]
        result.update(status="captured", sha256=hashlib.sha256(raw).hexdigest(),
                      runtime_models=sorted({c["model"] for c in contexts if c.get("model")}),
                      runtime_efforts=sorted({c.get("effort", c.get("reasoning_effort"))
                                             for c in contexts
                                             if c.get("effort", c.get("reasoning_effort"))}),
                      source="runtime rollout; not provider-returned model identity")
    except (OSError, ValueError, KeyError, TypeError) as error:
        result["error"] = str(error)
    return result


def identity_status(requested_model, requested_effort, capture):
    models, efforts = capture["runtime_models"], capture["runtime_efforts"]
    if not requested_model or not requested_effort or not models or not efforts:
        return "unknown"
    return "matches_runtime_record" if (models == [requested_model]
        and efforts == [requested_effort]) else "mismatch"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--prompt", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--input-inventory", type=Path,
                        help="Existing external inventory file; required for new controlled trials")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--codex", default="codex", help="Already-installed Codex executable")
    parser.add_argument("--codex-home", type=Path,
                        help="Explicit existing Codex profile outside the project; ambient CODEX_HOME is ignored")
    parser.add_argument("--command-path", help="Optional controlled command PATH for a failure case")
    parser.add_argument("--model", help="Explicit model; never silently substitute on failure")
    parser.add_argument("--reasoning-effort", choices=("none", "minimal", "low", "medium", "high", "xhigh"))
    parser.add_argument("--capture-session", action="store_true",
                        help="Retain this run's local rollout to inspect resolved model and context")
    args = parser.parse_args()
    project = args.project.resolve(strict=True)
    prompt = args.prompt.read_text()
    output = args.output.resolve()
    if output.exists():
        parser.error("output must be a new directory; preserve earlier attempts")
    if output == project or project in output.parents:
        parser.error("output must be outside the evaluator project")
    if not 1 <= args.timeout <= 600:
        parser.error("timeout must be between 1 and 600 seconds")
    inventory_path = project / "input-inventory.json"
    inventory_source = "legacy_project_path" if inventory_path.exists() else "not_provided"
    try:
        if args.input_inventory is not None:
            inventory_path = validate_external_inventory(args.input_inventory, project)
            inventory_source = "explicit_external"
        inventory_hash = file_hash(inventory_path) if inventory_source != "not_provided" else None
    except (OSError, ValueError) as error:
        parser.error("invalid input inventory: " + str(error))
    environment = {key: os.environ[key] for key in (
        "HOME", "PATH", "TMPDIR", "SHELL", "USER", "LOGNAME", "LANG", "TERM"
    ) if key in os.environ}
    codex_state_dir = Path(environment.get("HOME", str(Path.home()))) / ".codex"
    if args.codex_home is not None:
        try:
            codex_state_dir = validate_codex_home(args.codex_home, project)
        except (OSError, ValueError) as error:
            parser.error("invalid explicit Codex profile: " + str(error))
        environment["CODEX_HOME"] = str(codex_state_dir)
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
    executable = shutil.which(args.codex, path=environment.get("PATH"))
    if not executable:
        parser.error("Codex executable could not be resolved; refusing inference")
    executable_hash, runner_hash = file_hash(executable), file_hash(__file__)
    roots = [codex_state_dir / "skills", Path.home() / ".agents/skills", Path("/etc/codex/skills")]
    roots += [parent / ".agents/skills" for parent in project.parents]
    try:
        disabled = discover_host_skills(roots)
        project_skills = discover_host_skills([project / ".agents/skills"])
        if set(disabled) & set(project_skills):
            parser.error("staged skill aliases a disabled host skill")
    except (OSError, ValueError) as error:
        parser.error("host skill enumeration incomplete: " + str(error))
    output.mkdir(parents=True, mode=0o700)
    overrides = "skills.config=[" + ",".join(
        "{path=" + json.dumps(path) + ",enabled=false}" for path in disabled
    ) + "]"
    command = [
        args.codex, "--no-daemon", "-a", "never", "exec", "--ignore-user-config",
        "--skip-git-repo-check", "--sandbox", "workspace-write",
        "--json", "-C", str(project), "-c", overrides,
        "-c", "project_doc_max_bytes=0", "-c", "features.plugins=false",
        "-c", "features.apps=false", "-c", "features.hooks=false",
        "-c", "features.memories=false", "-c", "features.multi_agent=false",
        "-c", 'shell_environment_policy.inherit="core"',
        "-c", "shell_environment_policy.experimental_use_profile=false",
    ]
    if not args.capture_session:
        command.append("--ephemeral")
    if args.model:
        command += ["--model", args.model]
    if args.reasoning_effort:
        command += ["-c", "model_reasoning_effort=" + json.dumps(args.reasoning_effort)]
    if args.command_path:
        command += ["-c", "shell_environment_policy.set.PATH=" + json.dumps(args.command_path)]
    command += ["-o", str(output / "answer.txt"), "-"]
    # Preserve HOME and use only an explicitly selected CODEX_HOME override;
    # never create a profile or move/copy authentication state.
    # Provider keys, endpoint overrides and parent-agent session variables do
    # not enter this process. The supported existing ChatGPT login is required.
    start = time.monotonic()
    started = time.time()
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
    capture = capture_session(stdout, codex_state_dir, project, version.stdout.strip(), output, started) if args.capture_session else {
        "status": "not_requested", "runtime_models": [], "runtime_efforts": [], "backend_model": None}
    result = {
        "exit": child.returncode, "timeout": timed_out,
        "seconds": round(time.monotonic() - start, 2), "command": command,
        "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
        "auth": "existing ChatGPT login; no API environment passed",
        "cli_version": version.stdout.strip(),
        "cli_executable_sha256": executable_hash, "runner_sha256": runner_hash,
        "input_inventory_sha256": inventory_hash,
        "input_inventory_source": inventory_source,
        "input_inventory_path": str(inventory_path) if inventory_hash is not None else None,
        "requested_model": args.model, "requested_reasoning_effort": args.reasoning_effort,
        "session_capture": capture,
        "model_identity": identity_status(args.model, args.reasoning_effort, capture),
        "disabled_host_skills": disabled,
        "disabled_host_skill_count": len(disabled),
        "parent_codex_home_override_present": bool(os.environ.get("CODEX_HOME")),
        "codex_home": str(codex_state_dir),
        "codex_home_source": "explicit_argument" if args.codex_home is not None else "default_home",
        "initial_exec_context": "inspect captured rollout independently; no automatic isolation verdict",
    }
    (output / "run.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("exit", "timeout", "seconds")}))
    return 124 if timed_out else child.returncode


if __name__ == "__main__":
    raise SystemExit(main())
