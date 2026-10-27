import json
from datetime import date
from pathlib import Path
import tempfile
import unittest
from check_inventory import check


class Inventory(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'src').mkdir()
        (self.root / 'src/core.js').write_text('export const score = 1;')
        self.profile = {'version': 1, 'scopes': [{'root': 'src', 'extensions': ['.js']}],
                        'areas': [{'id': 'core', 'responsibility': 'Rules', 'files': ['src/core.js']}],
                        'exceptions': [], 'review_gaps': ['No import graph.']}

    def run_check(self):
        (self.root / 'architecture-inventory.json').write_text(json.dumps(self.profile))
        return check(self.root, today=date(2026, 1, 1))

    def exception(self):
        self.profile['exceptions'] = [{'file': 'src/legacy.js', 'reason': 'Pending extraction',
            'owner': 'Product maintainer', 'review_condition': 'Next adapter change',
            'review_by': '2026-02-01'}]
        (self.root / 'src/legacy.js').write_text('')

    def test_owned(self):
        self.assertEqual(self.run_check()['status'], 'inventory_passed')

    def test_new_nested_file_fails(self):
        (self.root / 'src/new').mkdir()
        (self.root / 'src/new/adapter.js').write_text('')
        self.assertEqual(self.run_check()['unowned'], ['src/new/adapter.js'])

    def test_missing_file(self):
        (self.root / 'src/core.js').rename(self.root / 'src/renamed.js')
        with self.assertRaises(ValueError): self.run_check()

    def test_duplicate_owner(self):
        self.profile['areas'].append({'id': 'adapter', 'responsibility': 'UI', 'files': ['src/core.js']})
        with self.assertRaises(ValueError): self.run_check()

    def test_overlapping_scope(self):
        self.profile['scopes'] *= 2
        with self.assertRaises(ValueError): self.run_check()

    def test_escaping_path(self):
        self.profile['areas'][0]['files'] = ['../core.js']
        with self.assertRaises(ValueError): self.run_check()

    def test_directory_symlink(self):
        (self.root / 'src/linked').symlink_to(self.root / 'src', target_is_directory=True)
        with self.assertRaises(ValueError): self.run_check()

    def test_exception(self):
        self.exception()
        self.assertEqual(self.run_check()['excepted'], 1)

    def test_expired_exception(self):
        self.exception(); self.profile['exceptions'][0]['review_by'] = '2026-01-01'
        with self.assertRaises(ValueError): self.run_check()

    def test_stale_exception(self):
        self.exception(); (self.root / 'src/legacy.js').unlink()
        with self.assertRaises(ValueError): self.run_check()

    def test_exception_requires_owner(self):
        self.exception(); self.profile['exceptions'][0]['owner'] = ''
        with self.assertRaises(ValueError): self.run_check()

    def test_gap_required(self):
        self.profile['review_gaps'] = []
        with self.assertRaises(ValueError): self.run_check()

    def test_empty_scope(self):
        self.profile['scopes'][0]['extensions'] = ['.swift']
        with self.assertRaises(ValueError): self.run_check()

    def test_not_a_dependency_checker(self):
        (self.root / 'src/core.js').write_text('import adapter from "./missing.js";')
        self.assertEqual(self.run_check()['status'], 'inventory_passed')


if __name__ == '__main__': unittest.main()
