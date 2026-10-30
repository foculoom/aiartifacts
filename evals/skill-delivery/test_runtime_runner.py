"""Synthetic subprocess tests: no provider, real login or agent inference."""
from pathlib import Path
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time
import unittest

RUNNER = Path(__file__).with_name("run_codex_case.py")
SPEC = importlib.util.spec_from_file_location("runtime_runner", RUNNER)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class RuntimeGuardTests(unittest.TestCase):
    def run_case(self, login_message="Logged in using ChatGPT", login_exit=0,
                 extra=(), model="gpt-6.1-sol", effort="medium", emit_capture=False,
                 exec_exit=0, delay=0, mismatch_cwd=False):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            project = root / "project"
            project.mkdir()
            prompt = root / "prompt.txt"
            prompt.write_text("Return 437 only.\n")
            marker = root / "exec-called"
            fake = root / "fake-codex"
            fake.write_text(
                "#!" + sys.executable + "\nimport sys, os, json, time\nfrom pathlib import Path\n"
                "if sys.argv[1:3] == ['login', 'status']:\n"
                " print(" + repr(login_message) + ")\n sys.exit(" + str(login_exit) + ")\n"
                "if '--version' in sys.argv:\n print('codex-cli synthetic')\n sys.exit(0)\n"
                "Path(" + repr(str(marker)) + ").write_text('called')\n"
                "assert 'OPENAI_API_KEY' not in os.environ\n"
                "assert 'CODEX_HOME' not in os.environ\n"
                "thread_id='00000000-0000-4000-8000-000000000001'\n"
                "print(json.dumps({'type':'thread.started','thread_id':thread_id}), flush=True)\n"
                "if " + repr(emit_capture) + ":\n"
                " p=Path(os.environ['HOME'])/'.codex/sessions/2026/10/30'/('rollout-test-'+thread_id+'.jsonl')\n"
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
                "--codex", str(fake), *extra,
            ], capture_output=True, text=True, env={**os.environ, "HOME":str(root),
                "OPENAI_API_KEY":"synthetic-must-not-enter-child", "CODEX_HOME":"synthetic-override"})
            receipt = root / "receipt/run.json"
            data = json.loads(receipt.read_text()) if receipt.exists() else None
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
