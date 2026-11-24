"""Validate discoverability and local reference integrity, without dependencies."""
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

PIN_RE = re.compile(r'^[0-9a-f]{40}$')
SHA256_RE = re.compile(r'^[0-9a-f]{64}$')
PUBLIC_SKILLS = 'public-skills'


def _markdown_targets(text):
    """Yield Markdown link targets that are not inside fences or inline code."""
    without_fences = re.sub(r'```.*?```', '', text, flags=re.S)
    without_fences = re.sub(r'~~~.*?~~~', '', without_fences, flags=re.S)
    without_code = re.sub(r'`[^`]*`', '', without_fences)
    return re.findall(r'\]\(([^)]+)\)', without_code)


def _strip_cell(value):
    return value.strip().strip('`').strip()


def parse_pin_records(text):
    """Parse the Pin records table from a public-skills PROVENANCE.md."""
    marker = '## Pin records'
    start = text.find(marker)
    assert start != -1, 'PROVENANCE.md is missing a Pin records section'
    section = text[start:]
    nxt = section.find('\n## ', 1)
    if nxt != -1:
        section = section[:nxt]
    rows = {}
    for line in section.splitlines():
        if not line.startswith('|'):
            continue
        cells = [part.strip() for part in line.strip().strip('|').split('|')]
        if len(cells) != 4:
            continue
        header = [cell.lower().strip('`') for cell in cells]
        if header == ['skill', 'commit', 'skill_md_sha256', 'license']:
            continue
        if all(set(cell) <= set('-: ') for cell in cells):
            continue
        skill, commit, digest, license_path = (_strip_cell(cell) for cell in cells)
        assert skill not in rows, f'duplicate pin record: {skill}'
        rows[skill] = {
            'commit': commit,
            'sha256': digest,
            'license': license_path,
        }
    assert rows, 'PROVENANCE.md Pin records table is empty'
    return rows


def license_file(skill_dir):
    for name in ('LICENSE', 'LICENSE.txt', 'LICENSE.md'):
        path = skill_dir / name
        if path.is_file():
            return path
    return None


def validate_public_skills_provenance(package):
    """Enforce pins, license files and SKILL.md hashes for public-skills."""
    package = Path(package)
    provenance = package / 'PROVENANCE.md'
    assert provenance.is_file(), f'missing {provenance}'
    records = parse_pin_records(provenance.read_text())
    skill_dirs = {
        path.parent.name: path.parent
        for path in (package / 'skills').glob('*/SKILL.md')
    }
    missing_records = sorted(set(skill_dirs) - set(records))
    extra_records = sorted(set(records) - set(skill_dirs))
    assert not missing_records, f'PROVENANCE missing pin records: {missing_records}'
    assert not extra_records, f'PROVENANCE pin records without skill folders: {extra_records}'
    for name, record in records.items():
        assert PIN_RE.fullmatch(record['commit']), (
            f'{name} pin must be a 40-character lowercase hex commit, '
            f'not {record["commit"]!r}'
        )
        assert SHA256_RE.fullmatch(record['sha256']), (
            f'{name} SKILL.md sha256 must be 64 lowercase hex, '
            f'not {record["sha256"]!r}'
        )
        skill_dir = skill_dirs[name]
        present = license_file(skill_dir)
        assert present is not None, f'{name} is missing a LICENSE file'
        recorded = (package / record['license']).resolve()
        assert recorded.is_relative_to(package.resolve()), (
            f'{name} license path escapes the plugin: {record["license"]}'
        )
        assert recorded.is_file(), f'{name} recorded license is missing: {record["license"]}'
        actual = hashlib.sha256((skill_dir / 'SKILL.md').read_bytes()).hexdigest()
        assert actual == record['sha256'], (
            f'{name} SKILL.md sha256 does not match PROVENANCE '
            f'(recorded {record["sha256"]}, actual {actual})'
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
            text = skill.read_text()
            front = text.split('---', 2)
            assert len(front) == 3 and not front[0].strip(), str(skill)
            assert re.search(
                rf'^name:\s*["\']?{re.escape(skill.parent.name)}["\']?\s*$',
                front[1],
                re.M,
            ), str(skill)
            assert re.search(r'^description: .+', front[1], re.M), str(skill)
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
