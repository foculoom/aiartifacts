#!/usr/bin/env python3
"""Check that a usefulness REPORT.md has the required unique gate lines.

This is a format check, not a judgment of usefulness and not a deploy.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
VALUE_RE = re.compile(r"^VALUE_GATE\s*:\s*(PASS|FAIL)\s*$", re.I | re.M)
GAP_RE = re.compile(r"^Hero-vs-data gap\s*:\s*(.+?)\s*$", re.I | re.M)
COMMIT_RE = re.compile(r"^Commit\s*:\s*`?([0-9a-f]+)`?\s*$", re.I | re.M)
AUDIENCE_RE = re.compile(r"^(?:Target audience|Audience|Minimum bar)\s*:\s*(.+)$", re.I | re.M)


def check_report(text: str, expect_sha: str | None = None) -> list[str]:
    errors: list[str] = []
    values = list(VALUE_RE.finditer(text))
    gaps = list(GAP_RE.finditer(text))
    commits = list(COMMIT_RE.finditer(text))
    audiences = list(AUDIENCE_RE.finditer(text))
    if len(values) != 1:
        errors.append(f"need exactly one VALUE_GATE line, found {len(values)}")
    if len(gaps) != 1:
        errors.append(f"need exactly one Hero-vs-data gap line, found {len(gaps)}")
    if len(commits) != 1:
        errors.append(f"need exactly one Commit line, found {len(commits)}")
    if len(audiences) != 1:
        errors.append(f"need exactly one Target audience line, found {len(audiences)}")
    sha = commits[0].group(1).lower() if commits else ""
    if commits and not SHA_RE.fullmatch(sha):
        errors.append("Commit must be a 40-character lowercase hex SHA")
    if expect_sha:
        want = expect_sha.lower()
        if not SHA_RE.fullmatch(want):
            errors.append("expected SHA must be a 40-character hex SHA")
        elif sha and sha != want:
            errors.append("Commit line does not match the expected SHA")
    if values and gaps:
        verdict = values[0].group(1).upper()
        gap = gaps[0].group(1).strip()
        if verdict == "PASS" and gap.lower() != "none":
            errors.append("VALUE_GATE PASS requires 'Hero-vs-data gap: none'")
        if verdict == "FAIL" and gap.lower() == "none":
            errors.append("VALUE_GATE FAIL must name a hero-vs-data gap")
    if re.search(r"VALUE_GATE\s*:\s*FAIL", text, re.I) and values and values[0].group(1).upper() == "PASS":
        errors.append("report also contains VALUE_GATE: FAIL")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="path to REPORT.md")
    parser.add_argument("--commit", help="expected 40-character SHA")
    args = parser.parse_args(argv)
    try:
        text = args.report.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"check_report: cannot read {args.report}: {exc}", file=sys.stderr)
        return 2
    errors = check_report(text, expect_sha=args.commit)
    if errors:
        for item in errors:
            print(item, file=sys.stderr)
        return 1
    print("REPORT format OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
