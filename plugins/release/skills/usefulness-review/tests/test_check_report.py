#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_report import check_report, main  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures"
SHA = "a" * 40


class CheckReportTests(unittest.TestCase):
    def test_pass_fixture_is_clean(self):
        text = (FIXTURES / "pass.md").read_text(encoding="utf-8")
        self.assertEqual(check_report(text, expect_sha=SHA), [])

    def test_fail_with_named_gap_is_clean(self):
        text = (FIXTURES / "fail-gap.md").read_text(encoding="utf-8")
        self.assertEqual(check_report(text, expect_sha=SHA), [])

    def test_pass_cannot_carry_a_gap(self):
        text = (FIXTURES / "bad-pass.md").read_text(encoding="utf-8")
        errors = check_report(text)
        self.assertTrue(any("PASS requires" in item for item in errors), errors)

    def test_short_sha_is_rejected(self):
        text = (FIXTURES / "short-sha.md").read_text(encoding="utf-8")
        errors = check_report(text)
        self.assertTrue(any("40-character" in item for item in errors), errors)

    def test_cli_pass(self):
        self.assertEqual(main([str(FIXTURES / "pass.md"), "--commit", SHA]), 0)

    def test_cli_rejects_mismatch(self):
        self.assertEqual(main([str(FIXTURES / "pass.md"), "--commit", "b" * 40]), 1)


if __name__ == "__main__":
    unittest.main()
