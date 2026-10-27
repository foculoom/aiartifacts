"""Read-only source ownership guard, not an import-graph or design proof."""
import argparse
from datetime import date
import json
from pathlib import Path


def inside(root, value):
    if not isinstance(value, str) or not value or '\\' in value:
        raise ValueError('expected nonempty POSIX relative path')
    p = Path(value)
    if p.is_absolute() or '..' in p.parts or str(p) != value:
        raise ValueError('expected normalized repository-relative path: ' + value)
    cursor = root
    for part in p.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError("symlink path component unsupported: " + value)
    target = root / p
    if not target.resolve().is_relative_to(root):
        raise ValueError('path escapes repository: ' + value)
    return target


def text(value, field):
    if not isinstance(value, str) or not value.strip():
        raise ValueError('nonempty ' + field + ' required')
    return value


def check(root, profile='architecture-inventory.json', today=None):
    root = Path(root).resolve()
    config = json.loads(inside(root, profile).read_text())
    if config.get('version') != 1:
        raise ValueError('expected inventory version 1')
    gaps = config.get('review_gaps')
    if not isinstance(gaps, list) or not gaps:
        raise ValueError('explicit review_gaps required')
    for gap in gaps:
        text(gap, 'review gap')
    scopes = config.get('scopes')
    if not isinstance(scopes, list) or not scopes:
        raise ValueError('nonempty scopes required')
    found = set()
    for scope in scopes:
        directory = inside(root, scope['root'])
        extensions = scope['extensions']
        if not directory.is_dir() or not isinstance(extensions, list) or not extensions:
            raise ValueError('each scope needs an existing directory and extensions')
        if any(not isinstance(x, str) or not x.startswith('.') or '/' in x for x in extensions):
            raise ValueError('invalid extensions')
        # No symlink traversal: a symlink directory could hide new source files.
        for path in directory.rglob('*'):
            if path.is_symlink():
                raise ValueError('symlinks unsupported in source scope: ' + str(path.relative_to(root)))
            if path.is_file() and path.suffix in extensions:
                relative = path.relative_to(root).as_posix()
                if relative in found:
                    raise ValueError('overlapping scopes: ' + relative)
                found.add(relative)
    if not found:
        raise ValueError('source scopes matched no files')
    areas = config.get('areas')
    if not isinstance(areas, list) or not areas:
        raise ValueError('nonempty areas required')
    assigned, ids = {}, set()
    for area in areas:
        identifier = text(area.get('id'), 'area id')
        if identifier in ids:
            raise ValueError('duplicate area: ' + identifier)
        ids.add(identifier)
        text(area.get('responsibility'), 'responsibility')
        files = area.get('files')
        if not isinstance(files, list) or not files:
            raise ValueError('area needs explicit files')
        for file in files:
            inside(root, file)
            if file in assigned:
                raise ValueError('duplicate ownership: ' + file)
            if file not in found:
                raise ValueError('declared file missing or outside source scopes: ' + file)
            assigned[file] = identifier
    exceptions = config.get('exceptions', [])
    if not isinstance(exceptions, list):
        raise ValueError('exceptions must be a list')
    excepted = set()
    for exception in exceptions:
        file = exception['file']
        inside(root, file)
        for field in ('reason', 'owner', 'review_condition'):
            text(exception.get(field), field)
        expires = date.fromisoformat(exception['review_by'])
        if expires <= (today or date.today()):
            raise ValueError('expired exception: ' + file)
        if file not in found or file in assigned or file in excepted:
            raise ValueError('unused or duplicate exception: ' + file)
        excepted.add(file)
    unowned = sorted(found - assigned.keys() - excepted)
    return {'status': 'findings' if unowned else 'inventory_passed',
            'files': len(found), 'owned': len(assigned), 'excepted': len(excepted),
            'unowned': unowned, 'review_gaps': gaps}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', required=True)
    parser.add_argument('--profile', default='architecture-inventory.json')
    args = parser.parse_args()
    try:
        result = check(args.root, args.profile)
    except (ValueError, OSError, TypeError, KeyError, AttributeError) as error:
        print(json.dumps({'status': 'invalid_profile', 'error': str(error)}))
        return 2
    print(json.dumps(result, indent=2))
    return 1 if result['unowned'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
