"""Synthetic fixtures only; no product assets, private paths or provider calls."""
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/check_export.py'
spec = importlib.util.spec_from_file_location('check_export', SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class ExportCheckTests(unittest.TestCase):
    def fixture(self, root):
        payload = root / 'website-preview'
        payload.mkdir()
        files = {'index.html': b'<p>Synthetic preview</p>', 'mark.svg': b'<svg/>'}
        for name, data in files.items():
            (payload / name).write_bytes(data)
        return payload, {'version': 1, 'files': {name: hashlib.sha256(data).hexdigest() for name, data in files.items()}}

    def test_explicit_roots_and_new_output_without_creation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            output = root / 'fresh-kit'
            result = checker.preflight(root, output)
            self.assertEqual(result['status'], 'passed')
            self.assertFalse(output.exists())
            with self.assertRaisesRegex(ValueError, 'absolute'):
                checker.preflight(Path('.'), output)
            output.mkdir()
            with self.assertRaisesRegex(ValueError, 'preserved'):
                checker.preflight(root, output)
            self.assertTrue(output.is_dir())

    def test_existing_dangling_output_link_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            output = root / 'linked-kit'
            output.symlink_to(root / 'missing-target')
            with self.assertRaisesRegex(ValueError, 'preserved'):
                checker.preflight(root, output)
            self.assertTrue(output.is_symlink())
            self.assertFalse((root / 'missing-target').exists())

    def test_exact_payload_pass_is_not_release_or_physical_proof(self):
        with tempfile.TemporaryDirectory() as temporary:
            payload, record = self.fixture(Path(temporary))
            result = checker.verify_payload(payload, record)
            self.assertEqual(result['file_count'], 2)
            self.assertEqual(result['public_availability'], 'unverified')
            self.assertEqual(result['physical_proof'], 'unperformed')

    def test_same_count_substitution_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            payload, record = self.fixture(Path(temporary))
            (payload / 'mark.svg').rename(payload / 'private-notes.txt')
            with self.assertRaisesRegex(ValueError, 'inventory'):
                checker.verify_payload(payload, record)

    def test_extra_guide_and_changed_asset_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            payload, record = self.fixture(Path(temporary))
            guide = payload / 'README.md'
            guide.write_text('Review-only instructions')
            with self.assertRaisesRegex(ValueError, 'inventory'):
                checker.verify_payload(payload, record)
            guide.unlink()
            (payload / 'mark.svg').write_text('<svg>changed</svg>')
            with self.assertRaisesRegex(ValueError, 'bytes'):
                checker.verify_payload(payload, record)

    def test_linked_payload_file_and_directory_rejected(self):
        for kind in ('file', 'directory'):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                payload, record = self.fixture(root)
                if kind == 'file':
                    (payload / 'mark.svg').unlink()
                    target = root / 'outside.svg'; target.write_text('<svg/>')
                    (payload / 'mark.svg').symlink_to(target)
                else:
                    target = root / 'private'; target.mkdir()
                    (payload / 'extra').symlink_to(target, target_is_directory=True)
                with self.assertRaisesRegex(ValueError, 'Linked'):
                    checker.verify_payload(payload, record)

    def test_unsafe_manifest_paths_and_hashes_rejected(self):
        with self.assertRaisesRegex(ValueError, 'object'):
            checker.checked_files([])
        for name in ('../secret', '/absolute', './index.html', 'dir//index.html', 'dir\\index.html'):
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'Unsafe'):
                checker.checked_files({'version': 1, 'files': {name: 'a' * 64}})
        with self.assertRaisesRegex(ValueError, 'SHA-256'):
            checker.checked_files({'version': 1, 'files': {'index.html': 'not-a-hash'}})


if __name__ == '__main__':
    unittest.main()
