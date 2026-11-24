"""Validate discoverability and local reference integrity, without dependencies."""
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

def _markdown_targets(text):
    """Yield Markdown link targets that are not inside fences or inline code."""
    without_fences = re.sub(r'```.*?```', '', text, flags=re.S)
    without_code = re.sub(r'`[^`]*`', '', without_fences)
    return re.findall(r'\]\(([^)]+)\)', without_code)


def validate():
    catalog = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
    names = set()
    count = 0
    for entry in catalog['plugins']:
        name = entry['name']
        assert name not in names, f'duplicate plugin: {name}'
        names.add(name)
        package = (ROOT / entry['source']['path']).resolve()
        assert package.is_relative_to(ROOT), 'package escapes repository'
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
    for path in ROOT.rglob('*.md'):
        if '.git' in path.parts:
            continue
        for target in _markdown_targets(path.read_text()):
            if '://' in target or target.startswith('#') or target.startswith('mailto:'):
                continue
            destination = (path.parent / target.split('#')[0]).resolve()
            assert destination.is_relative_to(ROOT) and destination.exists(), f'{path}: broken link {target}'
    print(f'PASS {len(names)} plugins, {count} skills; local Markdown references resolve')


if __name__ == '__main__':
    validate()
