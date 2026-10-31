"""Meaningful state and receipt checks for the fictional chat simulator."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "chatctl.py"


class ChatCtlTests(unittest.TestCase):
    def setUp(self):
        self.sandbox = tempfile.TemporaryDirectory()
        self.addCleanup(self.sandbox.cleanup)
        self.project = Path(self.sandbox.name) / "case"

    def call(self, *args, expected=0):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), "--project", str(self.project), *args],
            capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, expected, result.stderr + result.stdout)
        return json.loads(result.stdout)

    def initialize(self, case):
        self.call("init", "--fixture", str(ROOT / "fixtures" / f"{case}.json"))

    def test_c3_reconcile_then_rearchive(self):
        self.initialize("c3")
        self.assertFalse(self.call("move", "--id", "c-201", "--project-id", "p-workshop")["changed"])
        self.assertTrue(self.call("move", "--id", "c-202", "--project-id", "p-workshop")["changed"])
        for chat_id in ("c-201", "c-202"):
            self.call("set-archive", "--id", chat_id, "--value", "true")
            chat = self.call("show", "--id", chat_id)["chat"]
            self.assertEqual(chat["project_id"], "p-workshop")
            self.assertTrue(chat["archived"])
        self.assertEqual(len(self.call("receipts")["receipts"]), 3)
        self.assertEqual(self.call("move", "--id", "c-202", "--project-id", "p-archive", expected=2)["code"], "ARCHIVED_MOVE_UNSUPPORTED")

    def test_c4_reject_unsafe_destinations_and_move_safe_chat(self):
        self.initialize("c4")
        self.assertEqual(self.call("move", "--id", "c-301", "--project-id", "p-community", expected=2)["code"], "SHARED_BOUNDARY")
        self.assertEqual(self.call("move", "--id", "c-302", "--project-id", "p-vault", expected=2)["code"], "MEMORY_INCOMPATIBLE")
        self.call("move", "--id", "c-303", "--project-id", "p-kitchen")
        self.assertEqual(self.call("show", "--id", "c-303")["chat"]["project_id"], "p-kitchen")
        self.assertEqual(len(self.call("receipts")["receipts"]), 1)

    def test_c6_repeat_is_noop_and_preserves_automations(self):
        self.initialize("c6")
        before = self.call("overview")
        self.assertFalse(self.call("ensure-section", "--name", "Garden")["changed"])
        self.assertFalse(self.call("ensure-section", "--name", "Home")["changed"])
        self.assertFalse(self.call("rename", "--id", "c-501", "--title", "Garden — Seed inventory")["changed"])
        self.assertFalse(self.call("set-pin", "--id", "c-502", "--value", "true")["changed"])
        self.assertEqual(self.call("receipts")["receipts"], [])
        after = self.call("overview")
        self.assertEqual(before, after)

    def test_init_does_not_replace_existing_case(self):
        self.initialize("c3")
        self.assertEqual(self.call("init", "--fixture", str(ROOT / "fixtures" / "c4.json"), expected=2)["code"], "PROJECT_NOT_EMPTY")
        self.assertEqual(self.call("overview")["case"], "C3")


if __name__ == "__main__":
    unittest.main()
