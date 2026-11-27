#!/usr/bin/env python3
from __future__ import annotations

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_owner_yes import same_sha, main  # noqa: E402

SHA = "c" * 40
OTHER = "d" * 40


class CheckOwnerYesTests(unittest.TestCase):
    def test_matching_full_shas(self):
        self.assertEqual(same_sha(SHA, SHA), [])
        self.assertEqual(same_sha(SHA.upper(), SHA), [])

    def test_mismatch(self):
        errors = same_sha(SHA, OTHER)
        self.assertTrue(any("does not match" in item for item in errors), errors)

    def test_short_sha(self):
        errors = same_sha("abc", SHA)
        self.assertTrue(any("40-character" in item for item in errors), errors)

    def test_cli(self):
        self.assertEqual(main(["--commit", SHA, "--owner-yes-sha", SHA]), 0)
        self.assertEqual(main(["--commit", SHA, "--owner-yes-sha", OTHER]), 1)


if __name__ == "__main__":
    unittest.main()
