"""Repository integration checks; require this checkout, never a model or installer."""
import importlib.util
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile


REPO = Path(__file__).resolve().parents[2]
TOOL = REPO / 'scripts/skill-delivery'
SPEC = importlib.util.spec_from_file_location('export_skill', TOOL / 'export_skill.py')
exporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(exporter)


class PilotPackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()

    def test_real_editorial_skill_exports_with_its_references_tests_and_license(self):
        skill = REPO / 'plugins/editorial/skills/editorial-writing'
        self.assertTrue(skill.is_dir(), REPO)
        files = {
            p.relative_to(skill).as_posix(): p.relative_to(REPO).as_posix()
            for p in skill.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        files['LICENSE'] = 'LICENSE'
        config = self.base / 'config.json'
        config.write_text(json.dumps({
            'version': 1, 'name': 'editorial-writing', 'kind': 'skill',
            'source_commit': 'a' * 40, 'files': files}), encoding='utf-8')
        output = self.base / 'output'
        exporter.export(REPO, config, output)
        with zipfile.ZipFile(output / 'skill.zip') as archive:
            self.assertIn('scripts/prose_lint.py', archive.namelist())
            self.assertIn('tests/test_prose_lint.py', archive.namelist())
            self.assertEqual(archive.read('LICENSE'), (REPO / 'LICENSE').read_bytes())
            self.assertFalse(any(p.startswith('plugins/') for p in archive.namelist()))
        exporter.verify(output / 'manifest.json', installed_root=output / 'payload')

    def test_checked_in_pilot_contracts_preserve_same_skill_and_license_boundaries(self):
        for kind in ('skill', 'plugin'):
            config = REPO / 'evals/skill-delivery/pilot' / ('editorial-' + kind + '.json')
            exporter.export(REPO, config, self.base / kind)
        skill = self.base / 'skill/payload'
        plugin = self.base / 'plugin/payload'
        nested = plugin / 'skills/editorial-writing'

        def inventory(root):
            return {path.relative_to(root).as_posix(): path.read_bytes()
                    for path in root.rglob('*') if path.is_file()}

        self.assertEqual(inventory(skill), inventory(nested))
        self.assertEqual((skill / 'LICENSE').read_bytes(), (REPO / 'LICENSE').read_bytes())
        self.assertEqual((plugin / 'LICENSE').read_bytes(), (REPO / 'LICENSE').read_bytes())
        self.assertEqual(json.loads((plugin / 'plugin.json').read_text())['name'], 'editorial')
        self.assertEqual({p.name for p in (plugin / 'skills').iterdir()}, {'editorial-writing'})

    def test_tool_suite_needs_no_other_repository_files(self):
        isolated = self.base / 'tools/skill-delivery'
        shutil.copytree(TOOL, isolated, ignore=shutil.ignore_patterns('__pycache__'))
        completed = subprocess.run(
            [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests',
             '-p', 'test_*.py', '-q'],
            cwd=isolated, text=True, capture_output=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertRegex(completed.stderr, r'Ran [1-9][0-9]* tests')

    def test_deferred_candidate_is_not_an_active_plugin_skill(self):
        catalog = json.loads((REPO / '.agents/plugins/marketplace.json').read_text())
        for plugin in catalog['plugins']:
            root = REPO / plugin['source']['path']
            for entry in root.rglob('SKILL.md'):
                self.assertNotEqual(entry.parent.name, 'skill-delivery')
                self.assertIsNone(re.search(r'^name:\s*skill-delivery\s*$',
                                            entry.read_text(), re.MULTILINE))
        candidate = REPO / 'evals/skill-delivery/candidate'
        self.assertEqual(list(candidate.rglob('SKILL.md')), [])
        self.assertEqual(
            hashlib.sha256((candidate / 'SKILL.md.txt').read_bytes()).hexdigest(),
            'fd0e23926156028f9446b43c275eb9fb667b8af9aa3cc5dbf3282a02fb464733')
        manifest = json.loads((REPO / 'plugins/engineering/plugin.json').read_text())
        self.assertIsNone(re.search(r'\bskill[ -]delivery\b', json.dumps(manifest).lower()))


if __name__ == '__main__':
    unittest.main()
