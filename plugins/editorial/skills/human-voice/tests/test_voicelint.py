#!/usr/bin/env python3
"""Behavioral checks for the bundled voicelint script."""
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
SCRIPT = SKILL / "scripts" / "voicelint.mjs"
FIXTURES = Path(__file__).resolve().parent / "fixtures"
NODE = shutil.which("node")


def run_in(work: Path, allow=None, extra_exclude=None) -> subprocess.CompletedProcess:
    cfg = {
        "include": ["."],
        "exclude": extra_exclude or [],
        "allow": allow or [],
    }
    path = work / "voicelint.config.json"
    path.write_text(json.dumps(cfg), encoding="utf-8")
    return subprocess.run(
        [NODE, str(SCRIPT), "--json", "--config", str(path)],
        cwd=str(work),
        capture_output=True,
        text=True,
    )


@unittest.skipUnless(NODE, "node is required to run voicelint")
class VoiceLintTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.work = Path(self._tmp.name) / "site"
        self.work.mkdir()

    def tearDown(self):
        self._tmp.cleanup()

    def place(self, name: str) -> None:
        shutil.copy(FIXTURES / name, self.work / name)

    def lint(self, *names: str, allow=None) -> tuple[subprocess.CompletedProcess, dict]:
        for name in names:
            self.place(name)
        proc = run_in(self.work, allow=allow)
        self.assertTrue(proc.stdout.strip(), proc.stderr or "empty stdout")
        return proc, json.loads(proc.stdout)

    def test_clean_copy_exits_zero(self):
        proc, data = self.lint("clean.html")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertEqual(data["flags"], [])

    def test_stock_words_are_flagged(self):
        proc, data = self.lint("stock.html")
        self.assertEqual(proc.returncode, 1, proc.stdout)
        joined = " ".join(item["rule"] for item in data["flags"])
        self.assertIn("unlock", joined)
        self.assertIn("seamless", joined)
        self.assertIn("elevate", joined)

    def test_not_just_formula_is_flagged(self):
        proc, data = self.lint("formula.html")
        self.assertEqual(proc.returncode, 1, proc.stdout)
        rules = {item["rule"] for item in data["flags"]}
        self.assertIn("formula:not-just", rules)

    def test_concrete_triple_is_not_flagged(self):
        proc, data = self.lint("concrete-triple.html")
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertEqual(data["flags"], [])

    def test_vague_triple_is_flagged(self):
        proc, data = self.lint("vague-triple.html")
        self.assertEqual(proc.returncode, 1, proc.stdout)
        rules = {item["rule"] for item in data["flags"]}
        self.assertIn("formula:rule-of-three", rules)

    def test_title_case_heading_is_flagged(self):
        proc, data = self.lint("title-case.html")
        rules = {item["rule"] for item in data["flags"]}
        self.assertIn("formula:title-case-slogan", rules)

    def test_allowlist_with_reason_suppresses_a_flag(self):
        proc, data = self.lint("stock.html", allow=[{
            "file": "stock.html",
            "contains": "Unlock a seamless way",
            "reason": "synthetic allowlist coverage",
        }])
        self.assertEqual(proc.returncode, 0, proc.stdout)
        self.assertEqual(data["flags"], [])
        self.assertGreaterEqual(data["allowed"], 1)


if __name__ == "__main__":
    unittest.main()
