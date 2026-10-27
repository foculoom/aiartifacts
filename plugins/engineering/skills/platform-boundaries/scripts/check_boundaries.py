"""Bounded lexical architecture guard. No network, commands, or target imports."""
import argparse
import json
from pathlib import Path
import re

CHECKS = {
    'store-sdk': r'\b(?:StoreKit|SKPaymentQueue|Steamworks|steamworks|steamDlcAppId|appleProductId)\b|@capacitor/',
    'browser-effects': r'\b(?:document|localStorage|sessionStorage|XMLHttpRequest)\s*[.(]|\bfetch\s*\(',
}


def inside(root, relative):
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('paths must stay inside the product repository')
    resolved = (root / path).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError('symlink escapes product repository')
    return resolved


def check(root, profile):
    root = Path(root).resolve()
    config = json.loads(inside(root, profile).read_text())
    if config.get('version') != 1 or not isinstance(config.get('rules'), list):
        raise ValueError('expected version 1 and rules list')
    gaps = config.get('review_gaps')
    if not isinstance(gaps, list) or not gaps or not all(isinstance(x, str) and x.strip() for x in gaps):
        raise ValueError('declare nonempty review_gaps; lexical checks are incomplete')
    findings, scanned, ids = [], set(), set()
    for rule in config['rules']:
        identifier = rule.get('id')
        if not isinstance(identifier, str) or not identifier.strip() or identifier in ids:
            raise ValueError('rule IDs must be nonempty and unique')
        ids.add(identifier)
        files, checks = rule.get('files'), rule.get('checks')
        if not isinstance(files, list) or not files or not all(isinstance(x, str) and x for x in files):
            raise ValueError('each rule needs file patterns')
        if not isinstance(checks, list) or not checks or any(x not in CHECKS for x in checks):
            raise ValueError('unknown or empty checks')
        selected = set()
        for pattern in files:
            inside(root, pattern)
            matches = [p for p in root.glob(pattern) if p.is_file()]
            if not matches:
                raise ValueError('file pattern matched nothing: ' + pattern)
            for path in matches:
                inside(root, str(path.relative_to(root)))
                selected.add(path)
        for path in sorted(selected):
            relative = str(path.relative_to(root))
            scanned.add(relative)
            for line, text in enumerate(path.read_text().splitlines(), 1):
                for name in checks:
                    if re.search(CHECKS[name], text):
                        findings.append({'file': relative, 'line': line, 'rule': identifier, 'check': name})
    return {'status': 'findings' if findings else ('lexical_checks_passed' if scanned else 'review_only'),
            'scanned_files': sorted(scanned), 'findings': findings, 'review_gaps': gaps}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--profile', default='architecture.json')
    args = parser.parse_args()
    try:
        result = check(args.root, args.profile)
    except (ValueError, OSError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({'status': 'invalid_profile', 'error': str(error)}))
        return 2
    print(json.dumps(result, indent=2))
    return 1 if result['findings'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
