"""Repository integration checks; require this checkout, never a model or installer."""
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile


REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / 'plugins/engineering/skills/skill-delivery'
SPEC = importlib.util.spec_from_file_location('export_skill', SKILL / 'scripts/export_skill.py')
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

    def test_standalone_skill_suite_needs_no_other_repository_files(self):
        # Exercise the real installed layout that exposed repository assumptions.
        isolated = self.base / '.agents/skills/skill-delivery'
        shutil.copytree(SKILL, isolated, ignore=shutil.ignore_patterns('__pycache__'))
        completed = subprocess.run(
            [sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests',
             '-p', 'test_*.py', '-q'],
            cwd=isolated, text=True, capture_output=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertRegex(completed.stderr, r'Ran [1-9][0-9]* tests')


if __name__ == '__main__':
    unittest.main()
