"""Synthetic comparison cases; no real upstream event is claimed here."""

import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / 'check_upstream.py'
SPEC = importlib.util.spec_from_file_location('check_upstream', SCRIPT)
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class UpstreamComparisonTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name in ('accepted', 'candidate', 'local'):
            (self.root / name).mkdir()
            self.put(name, 'SKILL.md', '---\nname: example\ndescription: fixture\n---\nUse the reference.\n')
            self.put(name, 'references/procedure.md', 'Check the record.\n')
            self.put(name, 'scripts/check.py', 'print("accepted")\n')

    def put(self, bundle, name, content):
        path = self.root / bundle / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')

    def compare(self):
        return checker.compare(*(self.root / name for name in
                                 ('accepted', 'candidate', 'local')),
                               required=('SKILL.md', 'references/procedure.md',
                                         'scripts/check.py'))

    def test_dependency_change_is_seen_when_wrapper_unchanged(self):
        self.put('candidate', 'scripts/check.py', 'print("candidate")\n')
        result = self.compare()
        self.assertEqual(result['status'], 'change_for_assessment')
        self.assertFalse(result['entrypoint_changed'])
        self.assertEqual([change['path'] for change in result['upstream_changes']],
                         ['scripts/check.py'])
        self.assertEqual(result['conflicts'], [])
        self.assertEqual((self.root / 'local' / 'scripts/check.py').read_text(),
                         'print("accepted")\n')

    def test_local_adaptation_conflict_is_explicit(self):
        self.put('candidate', 'references/procedure.md', 'Check the new upstream record.\n')
        self.put('local', 'references/procedure.md', 'Check the product record.\n')
        result = self.compare()
        self.assertEqual(result['status'], 'change_for_assessment')
        self.assertEqual(result['conflicts'], ['references/procedure.md'])
        self.assertEqual(result['local_modifications'], ['references/procedure.md'])

    def test_unavailable_upstream_and_missing_required_file_block(self):
        unavailable = checker.compare(self.root / 'accepted', self.root / 'offline',
                                      self.root / 'local')
        self.assertEqual(unavailable['status'], 'upstream_unavailable')
        (self.root / 'candidate' / 'scripts/check.py').unlink()
        missing = self.compare()
        self.assertEqual(missing['status'], 'required_dependency_missing')
        self.assertEqual(missing['required_missing'],
                         {'candidate': ['scripts/check.py']})

    def test_local_content_identity_is_separate_from_upstream(self):
        self.put('candidate', 'SKILL.md', '---\nname: example\ndescription: fixture\n---\nNew upstream.\n')
        result = self.compare()
        self.assertEqual(result['status'], 'change_for_assessment')
        self.assertEqual(result['accepted_identity'], result['local_identity'])
        self.assertNotEqual(result['candidate_identity'], result['local_identity'])
        self.assertIn('Use the reference.', (self.root / 'local' / 'SKILL.md').read_text())

    def test_identical_upstream_does_not_hide_local_adaptation(self):
        self.put('local', 'references/procedure.md', 'Check the product record.\n')
        result = self.compare()
        self.assertEqual(result['status'], 'upstream_content_identical')
        self.assertEqual(result['upstream_changes'], [])
        self.assertEqual(result['local_modifications'], ['references/procedure.md'])
        self.assertNotEqual(result['accepted_identity'], result['local_identity'])

    def test_generated_cache_blocks_comparison(self):
        self.put('candidate', 'scripts/__pycache__/check.cpython-312.pyc', 'cache')
        with self.assertRaisesRegex(ValueError, 'clean reviewed snapshot'):
            self.compare()

    def test_permission_change_is_seen_and_total_read_is_bounded(self):
        (self.root / 'candidate' / 'scripts/check.py').chmod(0o755)
        result = self.compare()
        self.assertEqual(result['status'], 'change_for_assessment')
        self.assertEqual([change['path'] for change in result['upstream_changes']],
                         ['scripts/check.py'])
        self.assertEqual(result['upstream_changes'][0]['accepted']['sha256'],
                         result['upstream_changes'][0]['candidate']['sha256'])
        with patch.object(checker, 'MAX_TOTAL_BYTES', 8):
            with self.assertRaisesRegex(ValueError, 'bounded review limits'):
                checker.inventory(self.root / 'candidate')


if __name__ == '__main__':
    unittest.main()
