"""Validate discoverability and local reference integrity, without dependencies."""
import hashlib
import json
from pathlib import Path
import re
import stat

ROOT = Path(__file__).resolve().parents[1]

PIN_RE = re.compile(r'^[0-9a-f]{40}$')
SHA256_RE = re.compile(r'^[0-9a-f]{64}$')
PUBLIC_SKILLS = 'public-skills'
COMMIT_LINE = re.compile(r'^- Commit:\s*`([^`]+)`', re.M)
VENDORED_LIST = re.compile(r'Skills vendored \(\d+\):\s*(.+)')
SKILL_SHA_LINE = re.compile(r'^- SKILL.md sha256:\s*`([^`]+)`', re.M)
LICENSES_MANIFEST_LINE = re.compile(
    r'^- licenses/ manifest sha256:\s*`([^`]+)`', re.M)


def _markdown_targets(text):
    """Yield Markdown link targets that are not inside fences or inline code."""
    without_fences = re.sub(r'```.*?```', '', text, flags=re.S)
    without_fences = re.sub(r'~~~.*?~~~', '', without_fences, flags=re.S)
    without_code = re.sub(r'`[^`]*`', '', without_fences)
    return re.findall(r'\]\(([^)]+)\)', without_code)


def _strip_cell(value):
    return value.strip().strip('`').strip()


def _before_pin_records(text):
    marker = '## Pin records'
    start = text.find(marker)
    assert start != -1, 'PROVENANCE.md is missing a Pin records section'
    return text[:start], text[start:]


def parse_pin_records(text):
    """Parse the Pin records table from a public-skills PROVENANCE.md."""
    _, section = _before_pin_records(text)
    nxt = section.find('\n## ', 1)
    if nxt != -1:
        section = section[:nxt]
    rows = {}
    for line in section.splitlines():
        if not line.startswith('|'):
            continue
        cells = [part.strip() for part in line.strip().strip('|').split('|')]
        if len(cells) != 5:
            continue
        header = [cell.lower().strip('`') for cell in cells]
        if header == ['skill', 'commit', 'manifest_sha256', 'license', 'notice']:
            continue
        if all(set(cell) <= set('-: ') for cell in cells):
            continue
        skill, commit, digest, license_path, notice = (
            _strip_cell(cell) for cell in cells)
        assert skill not in rows, f'duplicate pin record: {skill}'
        notice_paths = []
        if notice and notice not in {'-', '—'}:
            notice_paths = [_strip_cell(part) for part in notice.split(',') if _strip_cell(part)]
        rows[skill] = {
            'commit': commit,
            'manifest': digest,
            'license': license_path,
            'notice': notice_paths,
        }
    assert rows, 'PROVENANCE.md Pin records table is empty'
    return rows


def license_file(skill_dir):
    for name in ('LICENSE', 'LICENSE.txt', 'LICENSE.md'):
        path = skill_dir / name
        if path.is_file():
            return path
    return None


def file_manifest_hash(skill_dir):
    """Hash every regular file in a skill folder.

    The digest is SHA-256 of sorted lines ``path\\0file-sha256\\0mode\\n``,
    where mode is ``0755`` if any execute bit is set and ``0644`` otherwise.
    """
    skill_dir = Path(skill_dir)
    lines = []
    for path in sorted(skill_dir.rglob('*')):
        if not path.is_file() or path.is_symlink():
            continue
        if any(part in {'.git', '__pycache__'} for part in path.parts):
            continue
        relative = path.relative_to(skill_dir).as_posix()
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        mode = '0755' if stat.S_IMODE(path.stat().st_mode) & 0o111 else '0644'
        lines.append(f'{relative}\0{digest}\0{mode}\n')
    return hashlib.sha256(''.join(lines).encode('utf-8')).hexdigest()


def parse_narrative_commits(text, record_names):
    """Map each narrative ``- Commit:`` line to one or more pin-record skills."""
    prefix, _ = _before_pin_records(text)
    sections = re.split(r'^## ', prefix, flags=re.M)
    mapped = {}
    for block in sections[1:]:
        heading, _, body = block.partition('\n')
        heading = heading.strip()
        commits = COMMIT_LINE.findall(body)
        if not commits:
            continue
        assert len(commits) == 1, (
            f'section {heading!r} has {len(commits)} Commit lines; expected one'
        )
        names = _skills_for_section(heading, body, record_names)
        assert names, (
            f'section {heading!r} has a Commit line but no mapped skills'
        )
        for name in names:
            assert name not in mapped, (
                f'{name} has more than one narrative Commit line'
            )
            mapped[name] = commits[0]
    return mapped


def _skills_for_section(heading, body, record_names):
    for name in sorted(record_names, key=len, reverse=True):
        if heading == name or heading.startswith(name + ' ') or heading.startswith(name + '('):
            return [name]
    listed = VENDORED_LIST.search(body)
    if not listed:
        return []
    names = []
    for part in listed.group(1).split(','):
        item = part.strip().strip('`').strip()
        if item:
            names.append(item)
    return names


def parse_narrative_skill_sha256(text, record_names):
    """Map each narrative ``- SKILL.md sha256:`` line to one pin-record skill."""
    prefix, _ = _before_pin_records(text)
    sections = re.split(r'^## ', prefix, flags=re.M)
    mapped = {}
    for block in sections[1:]:
        heading, _, body = block.partition('\n')
        heading = heading.strip()
        digests = SKILL_SHA_LINE.findall(body)
        if not digests:
            continue
        assert len(digests) == 1, (
            f'section {heading!r} has {len(digests)} SKILL.md sha256 lines; '
            'expected one'
        )
        names = _skills_for_section(heading, body, record_names)
        assert names, (
            f'section {heading!r} has a SKILL.md sha256 line but no mapped skills'
        )
        assert len(names) == 1, (
            f'section {heading!r} SKILL.md sha256 line maps to {len(names)} '
            'skills; expected one'
        )
        name = names[0]
        assert name not in mapped, (
            f'{name} has more than one narrative SKILL.md sha256 line'
        )
        mapped[name] = digests[0]
    return mapped


def parse_license_copies(text):
    """Parse the License copies section from a public-skills PROVENANCE.md."""
    marker = '## License copies'
    start = text.find(marker)
    assert start != -1, 'PROVENANCE.md is missing a License copies section'
    section = text[start:]
    nxt = section.find('\n## ', 1)
    if nxt != -1:
        section = section[:nxt]
    matches = LICENSES_MANIFEST_LINE.findall(section)
    assert len(matches) == 1, (
        'PROVENANCE.md must record exactly one licenses/ manifest sha256'
    )
    digest = matches[0]
    assert SHA256_RE.fullmatch(digest), (
        f'licenses/ manifest sha256 must be 64 lowercase hex, not {digest!r}'
    )
    paths = []
    for line in section.splitlines():
        if not line.startswith('|'):
            continue
        cells = [part.strip() for part in line.strip().strip('|').split('|')]
        if len(cells) != 1:
            continue
        header = cells[0].lower().strip('`')
        if header == 'path':
            continue
        if set(cells[0]) <= set('-: '):
            continue
        path = _strip_cell(cells[0])
        assert path not in paths, f'duplicate license copy path: {path}'
        paths.append(path)
    assert paths, 'PROVENANCE.md License copies table is empty'
    return digest, paths


def assert_skill_frontmatter(skill):
    """Require a matching, consistently quoted name: field."""
    skill = Path(skill)
    text = skill.read_text()
    front = text.split('---', 2)
    assert len(front) == 3 and not front[0].strip(), str(skill)
    name = re.escape(skill.parent.name)
    assert re.search(
        rf'^name:\s*(?:{name}|"{name}"|\'{name}\')\s*$',
        front[1],
        re.M,
    ), f'{skill} has a missing or mismatched name: field'
    assert re.search(r'^description: .+', front[1], re.M), str(skill)


def validate_public_skills_provenance(package):
    """Enforce pins, licenses, notices, license copies and per-skill file manifests."""
    package = Path(package)
    provenance = package / 'PROVENANCE.md'
    assert provenance.is_file(), f'missing {provenance}'
    text = provenance.read_text()
    records = parse_pin_records(text)
    skill_dirs = {
        path.parent.name: path.parent
        for path in (package / 'skills').glob('*/SKILL.md')
    }
    missing_records = sorted(set(skill_dirs) - set(records))
    extra_records = sorted(set(records) - set(skill_dirs))
    assert not missing_records, f'PROVENANCE missing pin records: {missing_records}'
    assert not extra_records, f'PROVENANCE pin records without skill folders: {extra_records}'
    narrative = parse_narrative_commits(text, records)
    skill_shas = parse_narrative_skill_sha256(text, records)
    missing_narrative = sorted(set(records) - set(narrative))
    extra_narrative = sorted(set(narrative) - set(records))
    assert not missing_narrative, (
        f'PROVENANCE Commit lines missing for: {missing_narrative}'
    )
    assert not extra_narrative, (
        f'PROVENANCE Commit lines for unknown skills: {extra_narrative}'
    )
    for name, record in records.items():
        assert PIN_RE.fullmatch(record['commit']), (
            f'{name} pin must be a 40-character lowercase hex commit, '
            f'not {record["commit"]!r}'
        )
        if narrative[name] != record['commit']:
            raise AssertionError(
                f'{name} narrative Commit line {narrative[name]!r} does not '
                f'match the pin table {record["commit"]!r}'
            )
        assert SHA256_RE.fullmatch(record['manifest']), (
            f'{name} manifest sha256 must be 64 lowercase hex, '
            f'not {record["manifest"]!r}'
        )
        skill_dir = skill_dirs[name]
        present = license_file(skill_dir)
        assert present is not None, f'{name} is missing a LICENSE file'
        recorded = (package / record['license']).resolve()
        assert recorded.is_relative_to(package.resolve()), (
            f'{name} license path escapes the plugin: {record["license"]}'
        )
        assert recorded.is_file(), f'{name} recorded license is missing: {record["license"]}'
        undeclared = skill_dir / 'NOTICE'
        if undeclared.is_file():
            relative = undeclared.relative_to(package).as_posix()
            assert relative in record['notice'], (
                f'{name} has {relative} but it is not listed in the notice column'
            )
        for notice_path in record['notice']:
            notice = (package / notice_path).resolve()
            assert notice.is_relative_to(package.resolve()), (
                f'{name} notice path escapes the plugin: {notice_path}'
            )
            assert notice.is_file(), f'{name} recorded NOTICE is missing: {notice_path}'
        actual = file_manifest_hash(skill_dir)
        assert actual == record['manifest'], (
            f'{name} file manifest sha256 does not match PROVENANCE '
            f'(recorded {record["manifest"]}, actual {actual})'
        )
        if name in skill_shas:
            recorded_skill = skill_shas[name]
            assert SHA256_RE.fullmatch(recorded_skill), (
                f'{name} SKILL.md sha256 must be 64 lowercase hex, '
                f'not {recorded_skill!r}'
            )
            actual_skill = hashlib.sha256(
                (skill_dir / 'SKILL.md').read_bytes()).hexdigest()
            assert actual_skill == recorded_skill, (
                f'{name} narrative SKILL.md sha256 does not match the file '
                f'(recorded {recorded_skill}, actual {actual_skill})'
            )
    validate_license_copies(package, text)


def validate_license_copies(package, text):
    """Enforce top-level licenses/ copies: listed paths exist and the manifest matches."""
    package = Path(package)
    recorded_manifest, license_copy_paths = parse_license_copies(text)
    licenses_dir = package / 'licenses'
    assert licenses_dir.is_dir(), 'missing licenses/ directory'
    licenses_root = licenses_dir.resolve()
    for rel in license_copy_paths:
        path = (package / rel).resolve()
        assert path.is_relative_to(licenses_root), (
            f'license copy path escapes licenses/: {rel}'
        )
        assert path.is_file(), f'recorded license copy is missing: {rel}'
    present = []
    for path in licenses_dir.rglob('*'):
        if not path.is_file() or path.is_symlink():
            continue
        if any(part in {'.git', '__pycache__'} for part in path.parts):
            continue
        present.append(path.relative_to(package).as_posix())
    missing = sorted(set(license_copy_paths) - set(present))
    extra = sorted(set(present) - set(license_copy_paths))
    assert not missing, f'recorded license copies are missing: {missing}'
    assert not extra, f'unrecorded files under licenses/: {extra}'
    actual = file_manifest_hash(licenses_dir)
    assert actual == recorded_manifest, (
        f'licenses/ file manifest sha256 does not match PROVENANCE '
        f'(recorded {recorded_manifest}, actual {actual})'
    )


def validate(root=None):
    root = Path(root) if root is not None else ROOT
    catalog = json.loads((root / '.agents/plugins/marketplace.json').read_text())
    names = set()
    count = 0
    for entry in catalog['plugins']:
        name = entry['name']
        assert name not in names, f'duplicate plugin: {name}'
        names.add(name)
        package = (root / entry['source']['path']).resolve()
        assert package.is_relative_to(root.resolve()), 'package escapes repository'
        manifest = json.loads((package / 'plugin.json').read_text())
        assert manifest['name'] == name, f'name mismatch: {name}'
        assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
        skills = list((package / 'skills').glob('*/SKILL.md'))
        assert skills, f'no discoverable skills: {name}'
        for skill in skills:
            assert_skill_frontmatter(skill)
            count += 1
        if name == PUBLIC_SKILLS:
            validate_public_skills_provenance(package)
    for path in root.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in _markdown_targets(path.read_text()):
            if '://' in target or target.startswith('#') or target.startswith('mailto:'):
                continue
            destination = (path.parent / target.split('#')[0]).resolve()
            assert destination.is_relative_to(root.resolve()) and destination.exists(), (
                f'{path}: broken link {target}'
            )
    print(f'PASS {len(names)} plugins, {count} skills; local Markdown references resolve')


if __name__ == '__main__':
    validate()
