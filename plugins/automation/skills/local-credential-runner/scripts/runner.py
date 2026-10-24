#!/usr/bin/env python3
"""Local reviewed-task launcher. Requires a private, owner-reviewed profile.

No shell execution, interactive fallback, inherited provider credentials, raw
child output, or unreviewed command overrides. This is not a same-user sandbox.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import stat
import subprocess
import sys
import uuid
from datetime import datetime, timezone


class Blocked(Exception):
    pass


def require(condition, code):
    if not condition:
        raise Blocked(code)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def base_env():
    return {"HOME": str(Path.home()), "PATH": "/usr/bin:/bin",
            "LANG": "en_US.UTF-8"}


def run(args, env=None, data=None, timeout=60):
    try:
        return subprocess.run(args, input=data, stdin=None if data is not None else subprocess.DEVNULL,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                              env=env or base_env(), timeout=timeout, close_fds=True)
    except (OSError, subprocess.TimeoutExpired):
        raise Blocked("process_unavailable_or_timeout") from None


def load_profile(path):
    p = Path(path)
    require(p.is_absolute() and not p.is_symlink(), "profile_path_invalid")
    s = p.stat()
    require(s.st_uid == os.getuid() and stat.S_IMODE(s.st_mode) == 0o600,
            "profile_requires_owner_mode_0600")
    parent = p.parent.stat()
    require(parent.st_uid == os.getuid() and not parent.st_mode & 0o077,
            "profile_directory_requires_owner_only_access")
    cfg = json.loads(p.read_text())
    require(cfg.get("version") == 1, "profile_version_unsupported")
    verify_file(cfg["op"]["path"], cfg["op"]["sha256"])
    require(re.fullmatch(r"[a-z0-9]{26}", cfg["service_account_id"]) is not None,
            "service_identity_invalid")
    require(bool(cfg["vault_ids"]) and all(re.fullmatch(r"[a-z0-9]{26}", v)
            for v in cfg["vault_ids"]), "vault_allowlist_invalid")
    return cfg


def verify_file(path, sha):
    p = Path(path)
    require(p.is_absolute() and p.is_file() and not p.is_symlink(), "reviewed_file_missing_or_linked")
    require(re.fullmatch(r"[0-9a-f]{64}", sha or "") is not None and digest(p) == sha,
            "reviewed_file_changed")
    require(not p.stat().st_mode & 0o022, "reviewed_file_writable_by_others")


def op_json(cfg, args, token=None):
    env = base_env()
    if token is not None:
        env.update(OP_SERVICE_ACCOUNT_TOKEN=token, OP_BIOMETRIC_UNLOCK_ENABLED="false")
    result = run([cfg["op"]["path"], *args, "--format=json"], env=env)
    require(result.returncode == 0, "vault_access_failed_check_expiry_revocation_or_scope")
    try:
        return json.loads(result.stdout)
    except (ValueError, UnicodeError):
        raise Blocked("vault_response_invalid") from None


def verify_identity(cfg, token):
    require(isinstance(token, str) and 20 <= len(token) < 32768 and
            not any(c.isspace() for c in token), "service_credential_malformed")
    who = op_json(cfg, ["user", "get", "--me"], token)
    require(who.get("type") == "SERVICE_ACCOUNT" and
            str(who.get("id", "")).lower() == cfg["service_account_id"] and
            who.get("state") == "ACTIVE", "service_identity_or_state_mismatch")
    vaults = op_json(cfg, ["vault", "list"], token)
    require({str(v["id"]).lower() for v in vaults} == set(cfg["vault_ids"]),
            "service_vault_scope_mismatch")


def resolve_field(cfg, ref, token):
    require(ref["vault_id"] in cfg["vault_ids"], "credential_vault_not_allowed")
    require(re.fullmatch(r"[a-z0-9]{26}", ref["item_id"]) is not None,
            "credential_item_id_invalid")
    item = op_json(cfg, ["item", "get", ref["item_id"], "--vault", ref["vault_id"]], token)
    require(item.get("id") == ref["item_id"] and
            str(item.get("vault", {}).get("id", "")).lower() == ref["vault_id"],
            "credential_item_mismatch")
    fields = [f for f in item.get("fields", []) if f.get("id") == ref["field_id"]]
    require(len(fields) == 1 and fields[0].get("type") == "CONCEALED",
            "credential_requires_one_concealed_field")
    value = fields[0].get("value")
    require(isinstance(value, str) and bool(value) and len(value) < 32768 and
            not any(c.isspace() for c in value), "credential_malformed")
    require(re.fullmatch(ref["pattern"], value) is not None, "credential_shape_mismatch")
    return value


def bootstrap(cfg):
    ref = cfg["bootstrap_source"]
    # Desktop access is used once, only for the already-authorized service item.
    item = op_json(cfg, ["item", "get", ref["item_id"], "--vault", ref["vault_id"]])
    require(item.get("id") == ref["item_id"] and
            str(item.get("vault", {}).get("id", "")).lower() == ref["vault_id"],
            "bootstrap_item_mismatch")
    fields = [f for f in item.get("fields", []) if f.get("id") == ref["field_id"]
              and f.get("type") == "CONCEALED"]
    require(len(fields) == 1, "bootstrap_field_invalid")
    token = fields[0].get("value")
    verify_identity(cfg, token)
    helper = Path(cfg["keychain_helper"])
    require(helper.is_absolute() and helper.is_file() and not helper.stat().st_mode & 0o077,
            "keychain_helper_requires_owner_only_executable")
    result = run([str(helper), "store"], data=token.encode())
    require(result.returncode == 0, "keychain_store_failed_or_item_exists")
    return {"operation": "bootstrap", "status": "passed", "code": "service_identity_and_vault_scope_verified"}


def execute(cfg, name, token):
    require(name in cfg["tasks"], "task_not_reviewed")
    task = cfg["tasks"][name]
    require(task.get("authorization") and task.get("source_revision"), "task_review_missing")
    require(isinstance(task["argv"], list) and bool(task["argv"]) and
            all(isinstance(a, str) for a in task["argv"]), "task_command_invalid")
    files = task["reviewed_files"]
    require(task["argv"][0] in files, "task_executable_not_pinned")
    for arg in task["argv"][1:]:
        if Path(arg).is_absolute() and Path(arg).is_file():
            require(arg in files, "task_file_argument_not_pinned")
    for path, sha in files.items():
        verify_file(path, sha)
    require(Path(task["cwd"]).is_absolute() and Path(task["cwd"]).is_dir(), "task_directory_missing")
    # cwd must not change Python's imports by accident; reviewed child should use
    # isolated mode and pin all imports/config inputs relevant to its authority.
    verify_identity(cfg, token)
    env = base_env()
    for key, ref in task.get("credentials", {}).items():
        require(re.fullmatch(r"[A-Z][A-Z0-9_]+", key) and key not in
                {"HOME", "PATH", "LANG", "OP_SERVICE_ACCOUNT_TOKEN", "OP_CONNECT_TOKEN", "OP_CONNECT_HOST"}
                and not key.startswith(("LD_", "DYLD_", "PYTHON")), "credential_environment_name_invalid")
        env[key] = resolve_field(cfg, ref, token)
    token = None
    contract = task["result_contract"]
    directory = Path(contract["directory"])
    require(directory.is_absolute() and directory.is_dir() and not directory.is_symlink()
            and directory.stat().st_uid == os.getuid() and not directory.stat().st_mode & 0o077,
            "result_directory_requires_owner_only_access")
    run_id = str(uuid.uuid4())
    result_path = directory / (run_id + ".json")
    env.update(LOCAL_RUN_ID=run_id, LOCAL_RESULT_PATH=str(result_path))
    # Refresh after network reads; this does not claim protection from malicious
    # processes running as the same user or imports omitted from review.
    for path, sha in files.items():
        verify_file(path, sha)
    try:
        result = subprocess.run(task["argv"], cwd=task["cwd"], env=env,
                                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL, close_fds=True, timeout=task.get("timeout_seconds", 120))
    except (OSError, subprocess.TimeoutExpired):
        raise Blocked("task_unavailable_or_timeout") from None
    require(result.returncode == 0, "task_preflight_failed_inspect_sanitized_task_report")
    require(result_path.is_file() and not result_path.is_symlink(), "fresh_task_evidence_missing")
    evidence = json.loads(result_path.read_text())
    require(set(evidence) == {"run_id", "target", "checks"} and evidence["run_id"] == run_id
            and evidence["target"] == contract["target"], "task_evidence_identity_mismatch")
    require(set(evidence["checks"]) == set(contract["checks"]) and
            all(value is True for value in evidence["checks"].values()), "task_evidence_incomplete")
    return {"operation": "task", "task": name, "status": "passed", "code": "reviewed_task_completed",
            "source_revision": task["source_revision"], "reviewed_files": files,
            "evidence_sha256": digest(result_path), "run_id": run_id, "checks": contract["checks"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", required=True)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--bootstrap", action="store_true")
    group.add_argument("--task")
    parser.add_argument("--service-input", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    os.umask(0o077)
    try:
        cfg = load_profile(args.profile)
        if args.bootstrap:
            require(not args.service_input, "bootstrap_input_invalid")
            report = bootstrap(cfg)
        else:
            require(args.service_input, "use_compiled_keychain_launcher")
            token = sys.stdin.buffer.read(32769).decode()
            report = execute(cfg, args.task, token)
        code = 0
    except Blocked as exc:
        report = {"status": "blocked", "code": str(exc)}
        code = 1
    except (Exception, KeyboardInterrupt):
        report = {"status": "blocked", "code": "invalid_configuration_or_unexpected_failure"}
        code = 1
    report["checked_at"] = datetime.now(timezone.utc).isoformat()
    print(json.dumps(report, sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main())
