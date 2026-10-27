import json
from pathlib import Path
import tempfile
import unittest
from check_boundaries import check


class Boundaries(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'core.js').write_text('export const score = n => n * 2;')
        self.profile = {'version': 1, 'review_gaps': ['Imports and new files require review.'],
                        'rules': [{'id': 'core', 'files': ['core.js'], 'checks': ['store-sdk', 'browser-effects']}]}

    def run_check(self):
        (self.root / 'architecture.json').write_text(json.dumps(self.profile))
        return check(self.root, 'architecture.json')

    def test_pure_core_and_adapter(self):
        (self.root / 'adapter.js').write_text('fetch("/api"); StoreKit.purchase();')
        self.assertEqual(self.run_check()['status'], 'lexical_checks_passed')

    def test_store_sdk_is_caught(self):
        (self.root / 'core.js').write_text('import StoreKit\nsteamDlcAppId = 123;')
        self.assertEqual(len(self.run_check()['findings']), 2)

    def test_core_effects_are_caught(self):
        (self.root / 'core.js').write_text('fetch("/api");\nlocalStorage.setItem("a", 1);')
        self.assertEqual(len(self.run_check()['findings']), 2)

    def test_missing_files_fail(self):
        self.profile['rules'][0]['files'] = ['missing/*.js']
        with self.assertRaises(ValueError): self.run_check()

    def test_unknown_check_fails(self):
        self.profile['rules'][0]['checks'] = ['imaginary']
        with self.assertRaises(ValueError): self.run_check()

    def test_escape_fails(self):
        self.profile['rules'][0]['files'] = ['../*.js']
        with self.assertRaises(ValueError): self.run_check()

    def test_symlink_escape_fails(self):
        (self.root / 'core.js').unlink()
        (self.root / 'core.js').symlink_to(Path(__file__).resolve())
        with self.assertRaises(ValueError): self.run_check()

    def test_review_only_is_not_code_pass(self):
        self.profile['rules'] = []
        self.assertEqual(self.run_check()['status'], 'review_only')

    def test_gaps_required(self):
        self.profile['review_gaps'] = []
        with self.assertRaises(ValueError): self.run_check()

    def test_duplicate_ids_fail(self):
        self.profile['rules'].append(self.profile['rules'][0])
        with self.assertRaises(ValueError): self.run_check()

    def test_empty_checks_fail(self):
        self.profile['rules'][0]['checks'] = []
        with self.assertRaises(ValueError): self.run_check()

    def test_absolute_profile_rejected(self):
        with self.assertRaises(ValueError): check(self.root, '/tmp/profile.json')


if __name__ == '__main__': unittest.main()
