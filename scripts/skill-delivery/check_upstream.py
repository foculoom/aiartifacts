#!/usr/bin/env python3
"""Compare explicit upstream and local instruction bundles without installing them.

This is a discovery aid, not an update manager. The caller supplies exact,
already-retrieved directories and records the source revisions separately.
"""

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import sys


MAX_FILES = 2048
MAX_BYTES = 16 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024
GENERATED_PARTS = {'.git', '__pycache__', 'node_modules', '.pytest_cache',
                   '.mypy_cache', '.ruff_cache', '.tox'}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def identity(files):
    lines = ''.join(f'{name}\0{files[name]["sha256"]}\0{files[name]["mode"]}\n'
                    for name in sorted(files))
    return digest(lines.encode('utf-8'))


def relative_file(value):
    if (not value or '\\' in value or ':' in value or
            any(ord(char) < 32 for char in value)):
        raise ValueError('Required file must be a safe relative path')
    path = PurePosixPath(value)
    if path.is_absolute() or path.as_posix() != value or any(
            part in {'', '.', '..'} for part in value.split('/')):
        raise ValueError('Required file must be a safe relative path')
    return value


def inventory(root):
    root = Path(root)
    if not root.is_dir() or root.is_symlink():
        raise FileNotFoundError(f'Bundle directory unavailable: {root}')
    files = {}
    total_bytes = 0
    for path in root.rglob('*'):
        relative = path.relative_to(root)
        if (any(part in GENERATED_PARTS for part in relative.parts) or
                path.name.endswith(('.pyc', '.pyo')) or path.name == '.DS_Store'):
            raise ValueError(f'Generated material requires a clean reviewed snapshot: {relative}')
        if path.is_symlink():
            raise ValueError(f'Symlink requires manual review: {relative}')
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError(f'Non-regular file requires manual review: {relative}')
        name = relative.as_posix()
        details = path.stat()
        total_bytes += details.st_size
        if (len(files) >= MAX_FILES or details.st_size > MAX_BYTES or
                total_bytes > MAX_TOTAL_BYTES):
            raise ValueError('Bundle exceeds bounded review limits')
        files[name] = {'sha256': digest(path.read_bytes()),
                       'mode': '0755' if stat.S_IMODE(details.st_mode) & 0o111 else '0644'}
    return files


def compare(accepted, candidate, local, required=('SKILL.md',)):
    """Return content evidence only; never copy, execute, or adopt a candidate."""
    required = tuple(relative_file(name) for name in required)
    try:
        baseline = inventory(accepted)
        current = inventory(local)
    except OSError as error:
        return {'status': 'accepted_or_local_unavailable', 'reason': str(error)}
    try:
        upstream = inventory(candidate)
    except OSError as error:
        return {'status': 'upstream_unavailable', 'reason': str(error),
                'accepted_identity': identity(baseline), 'local_identity': identity(current)}

    missing = {label: [name for name in required if name not in files]
               for label, files in [('accepted', baseline), ('candidate', upstream),
                                    ('local', current)]}
    missing = {label: names for label, names in missing.items() if names}
    all_names = sorted(set(baseline) | set(upstream) | set(current))
    upstream_changes = []
    local_modifications = []
    conflicts = []
    for name in all_names:
        before, after, adapted = baseline.get(name), upstream.get(name), current.get(name)
        if adapted != before:
            local_modifications.append(name)
        if after != before:
            upstream_changes.append({'path': name, 'accepted': before,
                                     'candidate': after, 'local': adapted})
            if adapted != before and adapted != after:
                conflicts.append(name)

    status = ('required_dependency_missing' if missing else
              'change_for_assessment' if upstream_changes else 'upstream_content_identical')
    return {'status': status, 'accepted_identity': identity(baseline),
            'candidate_identity': identity(upstream), 'local_identity': identity(current),
            'entrypoint_changed': baseline.get('SKILL.md') != upstream.get('SKILL.md'),
            'required_missing': missing, 'upstream_changes': upstream_changes,
            'local_modifications': local_modifications, 'conflicts': conflicts,
            'limits': 'Content comparison only; no relevance, license, behavior, or runtime-loading decision.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--accepted', required=True, help='Accepted upstream bundle directory')
    parser.add_argument('--candidate', required=True, help='Candidate upstream bundle directory')
    parser.add_argument('--local', required=True, help='Accepted local bundle directory')
    parser.add_argument('--required', action='append', default=['SKILL.md'],
                        help='Required relative file, repeat for scripts, references, and notices')
    args = parser.parse_args(argv)
    try:
        result = compare(args.accepted, args.candidate, args.local, args.required)
    except ValueError as error:
        result = {'status': 'manual_review_required', 'reason': str(error)}
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write('\n')
    return 2 if result['status'] in {
        'accepted_or_local_unavailable', 'upstream_unavailable',
        'required_dependency_missing', 'manual_review_required'} else 0


if __name__ == '__main__':
    sys.exit(main())
