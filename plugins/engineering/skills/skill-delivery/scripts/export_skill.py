#!/usr/bin/env python3
"""Prepare an explicit, local skill payload; never install, submit or publish.

Python 3.9+ standard library only. Checks are deliberately bounded: basic
frontmatter, ordinary local Markdown links, a narrow secret/path screen and
exact bytes. They do not certify rights, privacy, dependency or agent behavior.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
import stat
from urllib.parse import unquote, urlsplit
import zipfile


MAX_FILE = 16 * 1024 * 1024
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
DENIED = {'.git', '.aws', '.ssh', '.codex', '.agents', 'private', 'secrets',
          'credentials', 'customer-data', '__pycache__', 'node_modules'}
PRIVATE_FILES = {'agents.md', 'handoff.md', 'session_context.md'}
SECRET = re.compile(
    rb'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|'
    rb'(?:gh[pousr]_|github_pat_)[A-Za-z0-9_]{20,}|'
    rb'sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|'
    rb'PRIVATE_CONTEXT_TEST_' rb'SENTINEL|EXPORT_SECRET_TEST_' rb'SENTINEL')
PROVENANCE_LIMIT = 'Caller-supplied commit label; input hashes identify working-tree bytes.'
LIMITS = [
    'Basic metadata and local Markdown checks, not full format validation.',
    'Narrow secret/path screening, not privacy or licensing clearance.',
    'Executable bits normalize to 0755 or 0644; no ownership, ACL or xattr preservation.',
    'No dependency installation, runtime compatibility or behavior evaluation.',
    'No publication, submission or consumer update.']


def digest(data):
    return hashlib.sha256(data).hexdigest()


def strict_json(data):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON member')
            result[key] = value
        return result
    return json.loads(data, object_pairs_hook=unique)


def relative(value):
    if (not isinstance(value, str) or not value or '\\' in value or ':' in value
            or any(ord(c) < 32 for c in value)):
        raise ValueError('Unsafe relative path')
    path = PurePosixPath(value)
    if (path.is_absolute() or path.as_posix() != value
            or any(p in {'', '.', '..'} for p in value.split('/'))):
        raise ValueError('Unsafe relative path')
    return path


def public_path(value):
    path = relative(value)
    if any(p.lower() in DENIED or p.lower().startswith('.env') for p in path.parts):
        raise ValueError('Private or generated path is not exportable')
    if path.name.lower() in PRIVATE_FILES:
        raise ValueError('Repository instructions/handoffs are not exportable')
    return path


def root_directory(value):
    path = Path(value)
    if not path.is_absolute() or path.is_symlink() or not path.is_dir():
        raise ValueError('An explicit ordinary absolute directory is required')
    return path.resolve()


def source_bytes(root, name):
    path = root
    for part in relative(name).parts:
        path = path / part
        if path.is_symlink():
            raise ValueError('Symlinks are not exportable')
    if not path.is_file() or not path.resolve().is_relative_to(root):
        raise ValueError('Missing or non-regular source file')
    if path.stat().st_size > MAX_FILE:
        raise ValueError('File exceeds the 16 MiB review limit')
    data = path.read_bytes()
    if len(data) > MAX_FILE:
        raise ValueError('File exceeds the 16 MiB review limit')
    return data


def metadata(record):
    if (type(record.get('version')) is not int or record['version'] != 1
            or not isinstance(record.get('name'), str)
            or not NAME.fullmatch(record['name']) or len(record['name']) > 64
            or record.get('kind') not in {'skill', 'plugin'}
            or not isinstance(record.get('source_commit'), str)
            or not re.fullmatch(r'[0-9a-f]{40}', record['source_commit'])):
        raise ValueError('Invalid version, name, kind or source commit')


def config_record(raw):
    record = strict_json(raw)
    if not isinstance(record, dict) or set(record) != {
            'version', 'name', 'kind', 'source_commit', 'files'}:
        raise ValueError('Unexpected export configuration fields')
    metadata(record)
    if not isinstance(record['files'], dict) or not record['files']:
        raise ValueError('Explicit nonempty file mapping required')
    destinations = set()
    for target, source in record['files'].items():
        public_path(target)
        public_path(source)
        if target.casefold() in destinations:
            raise ValueError('Case-colliding destinations')
        destinations.add(target.casefold())
    for target in destinations:
        if any(parent.as_posix() in destinations
               for parent in PurePosixPath(target).parents if parent.as_posix() != '.'):
            raise ValueError('A destination cannot be both file and directory')
    return record


def skill_structure(data):
    text = data.decode('utf-8')
    parts = re.fullmatch(r'---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n(.*))?', text, re.S)
    if parts is None or not parts[1].strip() or not (parts[2] or '').strip():
        raise ValueError('SKILL.md needs frontmatter delimiters and nonempty instructions')
    # Deliberately no partial YAML parser: target tooling checks keys and semantics.


def inline_targets(text):
    """Read ordinary balanced inline destinations; not a full Markdown parser."""
    for match in re.finditer(r'\]\(', text):
        start, depth, escaped, angle = match.end(), 1, False, False
        for index in range(start, len(text)):
            char = text[index]
            if char == '\n':
                break
            if escaped:
                escaped = False
                continue
            if char == '\\':
                escaped = True
            elif char == '<':
                angle = True
            elif char == '>':
                angle = False
            elif not angle and char in '()':
                depth += 1 if char == '(' else -1
                if depth == 0:
                    yield text[start:index]
                    break


def check_links(payload):
    for name, data in payload.items():
        if not name.lower().endswith('.md'):
            continue
        text = data.decode('utf-8')
        targets = list(inline_targets(text))
        targets += re.findall(r'^\s{0,3}\[[^\]]+\]:\s*(\S+)', text, re.M)
        for target in targets:
            target = target.strip()
            if not target:
                continue  # An empty destination refers to the current document.
            if target.startswith('<'):
                target = target[1:].split('>', 1)[0]
            else:
                target = target.split()[0]
            parsed = urlsplit(target)
            if parsed.scheme in {'https', 'http', 'mailto'}:
                continue
            if parsed.scheme or parsed.netloc:
                raise ValueError('Unsupported Markdown reference scheme')
            route = unquote(parsed.path)
            if not route:
                continue
            if route.startswith('/') or '\\' in route:
                raise ValueError('Absolute Markdown reference')
            destination = posixpath.normpath(posixpath.join(posixpath.dirname(name), route))
            if destination == '.':
                continue  # A contained link to the package's own root directory.
            relative(destination)
            if destination not in payload and not any(
                    p.startswith(destination.rstrip('/') + '/') for p in payload):
                raise ValueError('Local Markdown reference is outside the payload')


def check_payload(record, payload):
    if 'LICENSE' not in payload or not payload['LICENSE'].decode('utf-8').strip():
        raise ValueError('Nonempty LICENSE at the payload root required')
    if record['kind'] == 'skill':
        if 'SKILL.md' not in payload:
            raise ValueError('Root SKILL.md required')
        skill_structure(payload['SKILL.md'])
    else:
        if 'plugin.json' not in payload:
            raise ValueError('Root plugin.json required')
        plugin = strict_json(payload['plugin.json'])
        if not isinstance(plugin, dict) or plugin.get('name') != record['name']:
            raise ValueError('Plugin name mismatch')
        skills = [p for p in payload if re.fullmatch(r'skills/[^/]+/SKILL\.md', p)]
        if not skills:
            raise ValueError('Plugin requires at least one contained skill')
        for path in skills:
            skill_structure(payload[path])
    for data in payload.values():
        if SECRET.search(data):
            raise ValueError('Potential secret/private marker; human review required')
    check_links(payload)


def export(source_root, config, output):
    root = root_directory(source_root)
    raw = Path(config).read_bytes()
    record = config_record(raw)
    output = Path(output)
    if not output.is_absolute() or output.exists() or output.is_symlink():
        raise ValueError('Output must be a new absolute path')
    if not output.parent.is_dir() or output.parent.is_symlink():
        raise ValueError('Output parent must be an existing ordinary directory')
    selected = [root / source for source in record['files'].values()] + [Path(config)]
    if any(path.resolve().is_relative_to(output.resolve()) for path in selected):
        raise ValueError('Output cannot contain selected inputs or its configuration')
    payload = {target: source_bytes(root, source)
               for target, source in record['files'].items()}
    modes = {target: '0755' if (root / source).stat().st_mode & 0o111 else '0644'
             for target, source in record['files'].items()}
    check_payload(record, payload)
    manifest = {key: record[key] for key in ('version', 'name', 'kind', 'source_commit')}
    manifest.update(source_commit_verification=PROVENANCE_LIMIT, config_sha256=digest(raw),
                    limitations=LIMITS, files={
                        name: {'source': record['files'][name], 'sha256': digest(payload[name]),
                               'mode': modes[name]}
                        for name in sorted(payload)})
    # Validation finishes before claiming a fresh output directory. Never overwrite.
    output.mkdir(mode=0o700)
    stage = output / 'payload'
    stage.mkdir()
    with zipfile.ZipFile(output / 'skill.zip', 'x', compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(payload):
            destination = stage / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            with destination.open('xb') as handle:
                handle.write(payload[name])
            destination.chmod(int(modes[name], 8))
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = (stat.S_IFREG | int(modes[name], 8)) << 16
            archive.writestr(entry, payload[name])
    with (output / 'manifest.json').open('x', encoding='utf-8') as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
        handle.write('\n')
    verify(output / 'manifest.json', archive=output / 'skill.zip')
    return {'status': 'prepared', 'file_count': len(payload), 'limitations': LIMITS}


def manifest_files(path):
    record = strict_json(Path(path).read_bytes())
    if not isinstance(record, dict) or set(record) != {
            'version', 'name', 'kind', 'source_commit', 'source_commit_verification',
            'config_sha256', 'limitations', 'files'}:
        raise ValueError('Unexpected manifest fields')
    metadata(record)
    if (record['source_commit_verification'] != PROVENANCE_LIMIT
            or record['limitations'] != LIMITS
            or not isinstance(record['config_sha256'], str)
            or not re.fullmatch(r'[0-9a-f]{64}', record['config_sha256'])
            or not isinstance(record['files'], dict) or not record['files']):
        raise ValueError('Invalid manifest provenance')
    files = {}
    for name, entry in record['files'].items():
        public_path(name)
        if (not isinstance(entry, dict) or set(entry) != {'source', 'sha256', 'mode'}
                or not isinstance(entry['sha256'], str)
                or not re.fullmatch(r'[0-9a-f]{64}', entry['sha256'])
                or entry['mode'] not in {'0644', '0755'}):
            raise ValueError('Invalid file evidence')
        public_path(entry['source'])
        files[name] = {'sha256': entry['sha256'], 'mode': entry['mode']}
    return files


def verify(manifest, archive=None, installed_root=None):
    expected = manifest_files(manifest)
    actual = {}
    if (archive is None) == (installed_root is None):
        raise ValueError('Choose one archive or installed directory')
    if archive is not None:
        with zipfile.ZipFile(archive) as handle:
            for entry in handle.infolist():
                public_path(entry.filename)
                mode = entry.external_attr >> 16
                if (entry.filename in actual or entry.is_dir()
                        or stat.S_IFMT(mode) not in {0, stat.S_IFREG}
                        or entry.file_size > MAX_FILE):
                    raise ValueError('Duplicate, oversized or non-regular ZIP entry')
                if entry.filename not in expected:
                    raise ValueError('Unexpected ZIP entry')
                actual[entry.filename] = {'sha256': digest(handle.read(entry)),
                                          'mode': format(stat.S_IMODE(mode), '04o')}
    else:
        root = root_directory(installed_root)
        for path in root.rglob('*'):
            if path.is_symlink():
                raise ValueError('Installed links are not exact file evidence')
            if path.is_dir():
                continue
            name = path.relative_to(root).as_posix()
            public_path(name)
            actual[name] = {'sha256': digest(source_bytes(root, name)),
                            'mode': format(stat.S_IMODE(path.stat().st_mode), '04o')}
    if actual != expected:
        raise ValueError('Inventory, bytes or file modes differ from reviewed manifest')
    return {'status': 'verified', 'file_count': len(actual),
            'scope': 'Exact local bytes and normalized modes only; no runtime or publication claim.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest='mode', required=True)
    prepare = modes.add_parser('export')
    prepare.add_argument('--source-root', type=Path, required=True)
    prepare.add_argument('--config', type=Path, required=True)
    prepare.add_argument('--output', type=Path, required=True)
    check = modes.add_parser('verify')
    check.add_argument('--manifest', type=Path, required=True)
    target = check.add_mutually_exclusive_group(required=True)
    target.add_argument('--archive', type=Path)
    target.add_argument('--installed-root', type=Path)
    args = parser.parse_args()
    try:
        result = (export(args.source_root, args.config, args.output) if args.mode == 'export'
                  else verify(args.manifest, args.archive, args.installed_root))
    except (ValueError, OSError, UnicodeError, TypeError, zipfile.BadZipFile) as error:
        # Do not echo input content, paths or credential values in diagnostic output.
        parser.exit(2, 'Blocked: ' + (str(error) if type(error) is ValueError else
                                    type(error).__name__) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
