#!/usr/bin/env python3
"""Confirm two SHA arguments are the same full 40-character commit.

This does not prove that an owner approved the revision.
"""
from __future__ import annotations

import argparse
import re
import sys

SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def same_sha(commit: str, owner_yes_sha: str) -> list[str]:
    errors = []
    for label, value in (("commit", commit), ("owner-yes-sha", owner_yes_sha)):
        if not SHA_RE.fullmatch((value or "").lower()) or value != value.lower() and not SHA_RE.fullmatch(value.lower()):
            if not SHA_RE.fullmatch((value or "").lower()):
                errors.append(f"{label} must be a 40-character hex SHA")
    if SHA_RE.fullmatch((commit or "").lower()) and SHA_RE.fullmatch((owner_yes_sha or "").lower()):
        if commit.lower() != owner_yes_sha.lower():
            errors.append("owner-yes-sha does not match commit")
    return errors


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--owner-yes-sha", required=True)
    args = parser.parse_args(argv)
    errors = same_sha(args.commit, args.owner_yes_sha)
    if errors:
        for item in errors:
            print(item, file=sys.stderr)
        return 1
    print("SHA match OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
