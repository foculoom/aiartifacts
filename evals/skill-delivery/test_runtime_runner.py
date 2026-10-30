"""Synthetic subprocess tests: no provider, real login or agent inference."""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch

RUNNER = Path(__file__).with_name("run_codex_case.py")
SPEC = importlib.util.spec_from_file_location("runtime_runner", RUNNER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RuntimeGuardTests(unittest.TestCase):
    def run_case(self, login_message="Logged in using ChatGPT", login_exit=0,
                 extra=(), model="gpt-6.1-sol", effort="medium", emit_capture=False,
                 exec_exit=0, delay=0, mismatch_cwd=False, explicit_home=False,
                 initialize_profile_skill=False, capture_in_default=False, inventory=None):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            project = root / "project"
            project.mkdir()
            prompt = root / "prompt.txt"
            prompt.write_text("Return 437 only.\n")
            inventory_path = (project if inventory == "legacy" else root) / "input-inventory.json"
            inventory_bytes = b'{"files":{},"measurement_only":"not an evaluator input"}\n'
            if inventory is not None:
                inventory_path.write_bytes(inventory_bytes)
            marker = root / "exec-called"
            calls = root / "calls.jsonl"
            profile = root / "separate-profile"
            if explicit_home:
                profile.mkdir()
                (profile / "auth.json").write_text("synthetic-auth-sentinel")
                (profile / "requirements.toml").write_text("synthetic-policy-sentinel")
            fake = root / "fake-codex"
            fake.write_text(
                "#!" + sys.executable + "\nimport sys, os, json, time\nfrom pathlib import Path\n"
                "assert os.environ.get('CODEX_HOME') == "
                + repr(str(profile) if explicit_home else None) + "\n"
                "assert os.environ.get('HOME') == " + repr(str(root)) + "\n"
                "assert not any(k in os.environ for k in ['OPENAI_API_KEY', 'ANTHROPIC_API_KEY', 'OPENAI_BASE_URL', 'CODEX_API_KEY', 'CODEX_ACCESS_TOKEN', 'CODEX_THREAD_ID'])\n"
                "state=Path(os.environ['CODEX_HOME']) if 'CODEX_HOME' in os.environ else Path(os.environ['HOME'])/'.codex'\n"
                "stage='auth' if sys.argv[1:3] == ['login','status'] else 'version' if '--version' in sys.argv else 'exec'\n"
                "model_input=sys.stdin.read() if stage=='exec' else None\n"
                "with Path(" + repr(str(calls)) + ").open('a') as log:\n"
                " log.write(json.dumps({'stage':stage,'home':os.environ['HOME'],'codex_home':os.environ.get('CODEX_HOME'),'args':sys.argv[1:],'input':model_input})+'\\n')\n"
                "if " + repr(inventory == "external") + ":\n"
                " assert " + repr(str(inventory_path)) + " not in json.dumps([sys.argv,dict(os.environ),model_input])\n"
                " assert 'measurement_only' not in (model_input or '')\n"
                " assert not list(Path(" + repr(str(project)) + ").iterdir())\n"
                "if sys.argv[1:3] == ['login', 'status']:\n"
                " print(" + repr(login_message) + ")\n sys.exit(" + str(login_exit) + ")\n"
                "if '--version' in sys.argv:\n"
                " if " + repr(initialize_profile_skill) + ":\n"
                "  skill=state/'skills/.system/initialized/SKILL.md'\n"
                "  skill.parent.mkdir(parents=True)\n  skill.write_text('synthetic initialized skill')\n"
                " print('codex-cli synthetic')\n sys.exit(0)\n"
                "Path(" + repr(str(marker)) + ").write_text('called')\n"
                "thread_id='00000000-0000-4000-8000-000000000001'\n"
                "print(json.dumps({'type':'thread.started','thread_id':thread_id}), flush=True)\n"
                "if " + repr(emit_capture) + ":\n"
                " capture_state=Path(os.environ['HOME'])/'.codex' if " + repr(capture_in_default) + " else state\n"
                " p=capture_state/'sessions/2026/10/30'/('rollout-test-'+thread_id+'.jsonl')\n"
                " p.parent.mkdir(parents=True)\n"
                " records=[{'type':'session_meta','payload':{'id':thread_id,'cwd':"
                + repr(str(root if mismatch_cwd else project)) + ",'cli_version':'synthetic'}},\n"
                " {'type':'turn_context','payload':{'model':" + repr(model)
                + ",'effort':" + repr(effort) + "}}]\n"
                " p.write_text(''.join(json.dumps(r)+'\\n' for r in records))\n"
                "time.sleep(" + str(delay) + ")\n"
                "sys.exit(" + str(exec_exit) + ")\n"
            )
            fake.chmod(0o755)
            result = subprocess.run([
                sys.executable, str(RUNNER), "--project", str(project),
                "--prompt", str(prompt), "--output", str(root / "receipt"),
                *(["--input-inventory", str(inventory_path)] if inventory == "external" else []),
                "--codex", str(fake), *(["--codex-home", str(profile)] if explicit_home else []), *extra,
            ], capture_output=True, text=True, env={**os.environ, "HOME":str(root),
                "OPENAI_API_KEY":"synthetic-must-not-enter-child", "CODEX_HOME":"synthetic-override",
                "ANTHROPIC_API_KEY":"synthetic", "OPENAI_BASE_URL":"https://invalid.example",
                "CODEX_API_KEY":"synthetic", "CODEX_ACCESS_TOKEN":"synthetic", "CODEX_THREAD_ID":"synthetic"})
            receipt = root / "receipt/run.json"
            data = json.loads(receipt.read_text()) if receipt.exists() else None
            if data is not None:
                data["observed_calls"] = [json.loads(line) for line in calls.read_text().splitlines()]
            if inventory is not None:
                self.assertEqual(inventory_path.read_bytes(), inventory_bytes)
                self.assertFalse((root / "receipt/input-inventory.json").exists())
            if inventory == "external":
                self.assertEqual(list(project.iterdir()), [])
            if explicit_home:
                self.assertEqual((profile / "auth.json").read_text(), "synthetic-auth-sentinel")
                self.assertEqual((profile / "requirements.toml").read_text(), "synthetic-policy-sentinel")
                self.assertFalse(any(project.rglob("auth.json")))
            return result, marker.exists(), data

    def test_api_key_login_refuses_inference(self):
        result, called, _ = self.run_case("Logged in using an API key")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(called)

    def test_unavailable_auth_refuses_inference(self):
        result, called, _ = self.run_case("Authentication unavailable", 1)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(called)

    def test_chatgpt_status_allows_stub(self):
        result, called, data = self.run_case()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(called)
        self.assertEqual(data["model_identity"], "unknown")
        self.assertIn("--ephemeral", data["command"])
        self.assertEqual(data["codex_home_source"], "default_home")
        self.assertTrue(data["parent_codex_home_override_present"])
        self.assertEqual([call["codex_home"] for call in data["observed_calls"]], [None, None, None])
        self.assertEqual(data["input_inventory_source"], "not_provided")
        self.assertIsNone(data["input_inventory_sha256"])
        self.assertIsNone(data["input_inventory_path"])

    def test_external_inventory_is_hashed_but_not_exposed_or_copied(self):
        result, called, data = self.run_case(inventory="external")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(called)
        self.assertEqual(data["input_inventory_source"], "explicit_external")
        expected = b'{"files":{},"measurement_only":"not an evaluator input"}\n'
        self.assertEqual(data["input_inventory_sha256"], hashlib.sha256(expected).hexdigest())
        self.assertNotIn(data["input_inventory_path"], data["command"])
        self.assertNotIn("--input-inventory", data["command"])
        self.assertEqual(data["observed_calls"][-1]["input"], "Return 437 only.\n")

    def test_legacy_project_inventory_remains_explicitly_labelled(self):
        result, called, data = self.run_case(inventory="legacy")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(called)
        self.assertEqual(data["input_inventory_source"], "legacy_project_path")
        self.assertEqual(data["input_inventory_sha256"], hashlib.sha256(
            b'{"files":{},"measurement_only":"not an evaluator input"}\n').hexdigest())
        self.assertEqual(Path(data["input_inventory_path"]).parent.name, "project")

    def test_explicit_profile_forwarded_to_all_phases_and_capture(self):
        result, called, data = self.run_case(explicit_home=True, emit_capture=True,
            initialize_profile_skill=True, extra=("--model", "gpt-6.1-sol",
                "--reasoning-effort", "medium", "--capture-session"))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(called)
        self.assertEqual(data["codex_home_source"], "explicit_argument")
        self.assertEqual([call["stage"] for call in data["observed_calls"]], ["auth", "version", "exec"])
        self.assertEqual({call["codex_home"] for call in data["observed_calls"]}, {data["codex_home"]})
        self.assertNotEqual(data["observed_calls"][0]["home"], data["codex_home"])
        initialized = str(Path(data["codex_home"]) / "skills/.system/initialized/SKILL.md")
        self.assertIn(initialized, data["disabled_host_skills"])
        self.assertTrue(any(initialized in arg and "enabled=false" in arg for arg in data["command"]))
        self.assertEqual(data["session_capture"]["status"], "captured")
        self.assertEqual(data["model_identity"], "matches_runtime_record")
        self.assertIn("--ignore-user-config", data["command"])
        self.assertNotIn("--ignore-rules", data["command"])
        self.assertEqual(data["command"][data["command"].index("--sandbox") + 1], "workspace-write")
        self.assertEqual(data["command"][data["command"].index("-a") + 1], "never")

    def test_explicit_profile_does_not_capture_default_home_session(self):
        result, _, data = self.run_case(explicit_home=True, emit_capture=True,
            capture_in_default=True, extra=("--capture-session",))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(data["session_capture"]["status"], "unavailable")
        self.assertEqual(data["model_identity"], "unknown")

    def test_explicit_profile_still_requires_chatgpt_authentication(self):
        result, called, data = self.run_case("Logged in using an API key", explicit_home=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(called)
        self.assertIsNone(data)

    def test_explicit_identity_and_capture(self):
        result, _, data = self.run_case(extra=("--model", "gpt-6.1-sol",
            "--reasoning-effort", "medium", "--capture-session"), emit_capture=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        command = data["command"]
        self.assertEqual(command[command.index("--model")+1], "gpt-6.1-sol")
        self.assertIn('model_reasoning_effort="medium"', command)
        self.assertNotIn("--ephemeral", command)
        self.assertNotIn("--ignore-rules", command)
        self.assertEqual(data["model_identity"], "matches_runtime_record")
        self.assertEqual(data["session_capture"]["status"], "captured")
        self.assertIsNone(data["session_capture"]["backend_model"])
        self.assertIn("independent", data["session_capture"]["isolation"])

    def test_mismatched_model_or_effort_never_passes(self):
        for model, effort in (("another-model", "medium"), ("gpt-6.1-sol", "low")):
            with self.subTest(model=model, effort=effort):
                _, _, data = self.run_case(extra=("--model", "gpt-6.1-sol",
                    "--reasoning-effort", "medium", "--capture-session"),
                    emit_capture=True, model=model, effort=effort)
                self.assertEqual(data["model_identity"], "mismatch")

    def test_missing_capture_stays_unknown(self):
        _, _, data = self.run_case(extra=("--capture-session",))
        self.assertEqual(data["session_capture"]["status"], "unavailable")
        self.assertEqual(data["model_identity"], "unknown")

    def test_wrong_session_directory_is_not_captured(self):
        _, _, data = self.run_case(extra=("--capture-session",), emit_capture=True, mismatch_cwd=True)
        self.assertEqual(data["session_capture"]["status"], "unavailable")

    def test_nonzero_exit_is_preserved(self):
        result, _, data = self.run_case(exec_exit=7)
        self.assertEqual(result.returncode, 7)
        self.assertEqual(data["exit"], 7)

    def test_timeout_preserves_receipt(self):
        result, _, data = self.run_case(extra=("--timeout", "1"), delay=20)
        self.assertEqual(result.returncode, 124)
        self.assertTrue(data["timeout"])


class DiscoveryAndCaptureTests(unittest.TestCase):
    def test_invalid_external_inventories_are_refused_before_auth(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            project = root / "project"
            project.mkdir()
            prompt = root / "prompt.txt"
            prompt.write_text("synthetic")
            inventory = root / "inventory.json"
            inventory.write_text("{}")
            inside = project / "inventory.json"
            inside.write_text("{}")
            linked = root / "linked"
            linked.symlink_to(inventory)
            parent_alias = root / "alias"
            parent_alias.symlink_to(root, target_is_directory=True)
            for selected, error in (
                (root / "missing", "existing physical regular file"),
                (root, "existing physical regular file"),
                (project, "outside the evaluator"),
                (inside, "outside the evaluator"),
                (linked, "symlink aliases"),
                (parent_alias / "inventory.json", "symlink aliases"),
                (project / ".." / "inventory.json", "parent-directory"),
            ):
                with self.subTest(inventory=selected):
                    with patch.object(MODULE.subprocess, "run") as child:
                        with patch.object(sys, "argv", [str(RUNNER),
                            "--project", str(project), "--prompt", str(prompt),
                            "--output", str(root / "receipt"), "--input-inventory", str(selected)]):
                            with patch("sys.stderr") as stderr:
                                with self.assertRaises(SystemExit) as stopped:
                                    MODULE.main()
                        self.assertEqual(stopped.exception.code, 2)
                        self.assertIn(error, "".join(call.args[0] for call in stderr.write.call_args_list))
                        child.assert_not_called()
                    self.assertFalse((root / "receipt").exists())

    def test_invalid_explicit_profiles_are_refused_before_auth(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            project = root / "project"
            project.mkdir()
            prompt = root / "prompt.txt"
            prompt.write_text("synthetic")
            profile = root / "profile"
            profile.mkdir()
            inside = project / "profile"
            inside.mkdir()
            file = root / "file"
            file.write_text("synthetic")
            linked = root / "linked"
            linked.symlink_to(profile, target_is_directory=True)
            parent_alias = root / "alias"
            parent_alias.symlink_to(root, target_is_directory=True)
            cases = [
                (root / "missing", "existing directory"),
                (file, "existing directory"),
                (project, "outside the evaluator"),
                (inside, "outside the evaluator"),
                (linked, "symlink aliases"),
                (parent_alias / "profile", "symlink aliases"),
                (profile / ".." / "profile", "parent-directory"),
            ]
            for selected, error in cases:
                with self.subTest(profile=selected):
                    result = subprocess.run([sys.executable, str(RUNNER),
                        "--project", str(project), "--prompt", str(prompt),
                        "--output", str(root / "receipt"), "--codex-home", str(selected),
                        "--codex", "nonexistent-synthetic-executable"], capture_output=True, text=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn("invalid explicit Codex profile", result.stderr)
                    self.assertIn(error, result.stderr)
                    self.assertFalse((root / "receipt").exists())
            self.assertFalse((root / "missing").exists())

    def test_profile_requires_usable_directory_without_changing_permissions(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            profile = root / "profile"
            profile.mkdir(mode=0o700)
            original_mode = profile.stat().st_mode
            with patch.object(MODULE.os, "access", return_value=False) as access:
                with self.assertRaisesRegex(ValueError, "readable, writable and searchable"):
                    MODULE.validate_codex_home(profile, root / "project")
                access.assert_called_once_with(profile, os.R_OK | os.W_OK | os.X_OK)
            self.assertEqual(profile.stat().st_mode, original_mode)

    def test_linked_entry_retains_alias_and_canonical_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            actual = root / "actual"
            actual.mkdir()
            (actual / "SKILL.md").write_text("synthetic")
            skills = root / "skills"
            skills.mkdir()
            (skills / "linked").symlink_to(actual, target_is_directory=True)
            found = MODULE.discover_host_skills([skills])
            self.assertEqual(set(found), {str(actual / "SKILL.md"), str(skills / "linked/SKILL.md")})

    def test_cycle_dangling_link_and_budget_fail_closed(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "cycle").symlink_to(root, target_is_directory=True)
            with self.assertRaises(ValueError):
                MODULE.discover_host_skills([root])
            (root / "cycle").unlink()
            (root / "broken").symlink_to(root / "missing")
            with self.assertRaises(OSError):
                MODULE.discover_host_skills([root])
            (root / "broken").unlink()
            with self.assertRaises(ValueError):
                MODULE.discover_host_skills([root], limit=0)

    def test_invalid_or_multiple_thread_ids_are_not_read(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for ids in (("../../other",), ("00000000-0000-4000-8000-000000000001",
                                          "00000000-0000-4000-8000-000000000002")):
                stdout = "\n".join(json.dumps({"type":"thread.started", "thread_id":i}) for i in ids)
                capture = MODULE.capture_session(stdout, root, root, "synthetic", root, 0)
                self.assertEqual(capture["status"], "unavailable")

    def test_linked_duplicate_and_malformed_rollouts_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            tid = "00000000-0000-4000-8000-000000000001"
            stdout = json.dumps({"type":"thread.started", "thread_id":tid})
            source = root / "sessions/2026/10/30" / ("rollout-one-" + tid + ".jsonl")
            source.parent.mkdir(parents=True)
            other = root / "unrelated.jsonl"
            other.write_text("private sentinel; not a rollout")
            source.symlink_to(other)
            captured = MODULE.capture_session(stdout, root, root, "synthetic", root, time.time())
            self.assertIn("linked", captured["error"])
            self.assertFalse((root / "session.jsonl").exists())
            source.unlink()
            source.write_text("[]\n")
            captured = MODULE.capture_session(stdout, root, root, "synthetic", root, time.time())
            self.assertEqual(captured["status"], "unavailable")
            self.assertIn("invalid rollout", captured["error"])
            duplicate = source.with_name("rollout-two-" + tid + ".jsonl")
            duplicate.write_text("{}\n")
            captured = MODULE.capture_session(stdout, root, root, "synthetic", root, time.time())
            self.assertIn("one matching", captured["error"])

    def test_output_inside_project_is_refused_before_auth(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            prompt = root / "prompt.txt"
            prompt.write_text("synthetic")
            result = subprocess.run([sys.executable, str(RUNNER), "--project", str(root),
                "--prompt", str(prompt), "--output", str(root / "receipt"),
                "--codex", "nonexistent-synthetic-executable"], capture_output=True, text=True)
            self.assertIn("outside the evaluator", result.stderr)
            self.assertFalse((root / "receipt").exists())


if __name__ == "__main__":
    unittest.main()
