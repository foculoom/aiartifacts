"""Synthetic subprocess tests: no provider, real login or agent inference."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

RUNNER = Path(__file__).with_name("run_codex_case.py")


class RuntimeGuardTests(unittest.TestCase):
    def run_case(self, login_message, login_exit=0):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            project = root / "project"
            project.mkdir()
            prompt = root / "prompt.txt"
            prompt.write_text("Return 437 only.\n")
            marker = root / "exec-called"
            fake = root / "fake-codex"
            fake.write_text(
                "#!" + sys.executable + "\nimport sys\nfrom pathlib import Path\n"
                "if sys.argv[1:3] == ['login', 'status']:\n"
                " print(" + repr(login_message) + ")\n sys.exit(" + str(login_exit) + ")\n"
                "if '--version' in sys.argv:\n print('codex-cli synthetic')\n sys.exit(0)\n"
                "Path(" + repr(str(marker)) + ").write_text('called')\n"
                "print('{}')\n"
            )
            fake.chmod(0o755)
            result = subprocess.run([
                sys.executable, str(RUNNER), "--project", str(project),
                "--prompt", str(prompt), "--output", str(root / "receipt"),
                "--codex", str(fake),
            ], capture_output=True, text=True)
            return result, marker.exists()

    def test_api_key_login_refuses_inference(self):
        result, called = self.run_case("Logged in using an API key")
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(called)

    def test_unavailable_auth_refuses_inference(self):
        result, called = self.run_case("Authentication unavailable", 1)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(called)

    def test_chatgpt_status_allows_stub(self):
        result, called = self.run_case("Logged in using ChatGPT")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(called)


if __name__ == "__main__":
    unittest.main()
