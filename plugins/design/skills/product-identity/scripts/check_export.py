"""Read-only design-export path preflight and exact static payload verification."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re


def preflight(source_root, output_root):
    source_root, output_root = Path(source_root), Path(output_root)
    if not source_root.is_absolute() or not output_root.is_absolute():
        raise ValueError('Explicit absolute source and output roots are required')
    if source_root.is_symlink() or not source_root.is_dir():
        raise ValueError('Source root must be an existing ordinary directory')
    if output_root.exists() or output_root.is_symlink():
        raise ValueError('Output root must be new; existing entries are preserved')
    return {'status': 'passed', 'scope': 'path preflight only; create output exclusively at export time',
            'source_root': str(source_root.resolve()), 'output_root': str(output_root.resolve())}


def checked_files(record):
    if not isinstance(record, dict):
        raise ValueError('Manifest must be an object')
    files = record.get('files')
    if record.get('version') != 1 or not isinstance(files, dict) or not files:
        raise ValueError('A nonempty version 1 reviewed public-file manifest is required')
    for name, expected in files.items():
        if not isinstance(name, str):
            raise ValueError('Manifest paths must be strings')
        path = PurePosixPath(name)
        if (not name or path.is_absolute() or '\\' in name or
                any(part in {'', '.', '..'} for part in name.split('/')) or str(path) != name):
            raise ValueError('Unsafe manifest path')
        if not isinstance(expected, str) or not re.fullmatch(r'[0-9a-f]{64}', expected):
            raise ValueError('Invalid SHA-256 digest')
    return files


def verify_payload(payload_root, record):
    root = Path(payload_root)
    if root.is_symlink() or not root.is_dir():
        raise ValueError('Payload root must be an existing ordinary directory')
    expected = checked_files(record)
    actual = {}
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Linked entries are not allowed in the payload')
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError('Payload entries must be ordinary files or directories')
        actual[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    if set(actual) != set(expected):
        raise ValueError('Payload inventory differs from the reviewed public-file allowlist')
    if actual != expected:
        raise ValueError('Payload bytes differ from the reviewed hashes')
    return {'status': 'passed', 'scope': 'exact local payload only', 'file_count': len(actual),
            'public_availability': 'unverified', 'physical_proof': 'unperformed'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest='mode', required=True)
    paths = modes.add_parser('preflight')
    paths.add_argument('--source-root', type=Path, required=True)
    paths.add_argument('--output-root', type=Path, required=True)
    payload = modes.add_parser('payload')
    payload.add_argument('--payload-root', type=Path, required=True)
    payload.add_argument('--manifest', type=Path, required=True)
    args = parser.parse_args()
    try:
        result = (preflight(args.source_root, args.output_root) if args.mode == 'preflight'
                  else verify_payload(args.payload_root, json.loads(args.manifest.read_text())))
    except (ValueError, OSError, TypeError) as error:
        parser.exit(2, f'Blocked: {error}\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
