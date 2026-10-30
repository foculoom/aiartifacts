import tempfile
import json
import sys
import unittest
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError
from pathlib import Path
from verify_static import manifest, verify, digest, main

class Checks(unittest.TestCase):
    def run_manifest_cli(self, source):
        with tempfile.TemporaryDirectory() as directory:
            record = Path(directory) / 'manifest.json'
            output = Path(directory) / 'report.json'
            record.write_text(source)
            argv = ['verify_static.py', '--manifest', str(record), '--origin',
                    'https://example.com', '--output', str(output)]
            with patch.object(sys, 'argv', argv):
                result = main()
            return result, json.loads(output.read_text())

    def test_duplicate_members_rejected_before_network_or_report(self):
        good = digest(b'expected')
        cases = [
            '{"version":1,"files":{"missing.css":"' + good + '"},"files":{"index.html":"' + good + '"}}',
            '{"version":1,"files":{"index.html":"' + 'a'*64 + '","index.html":"' + good + '"}}',
            '{"version":2,"version":1,"files":{"index.html":"' + good + '"}}',
        ]
        for source in cases:
            with self.subTest(source=source), tempfile.TemporaryDirectory() as directory:
                record = Path(directory) / 'manifest.json'
                output = Path(directory) / 'report.json'
                record.write_text(source)
                argv = ['verify_static.py', '--manifest', str(record), '--origin',
                        'https://example.com', '--output', str(output)]
                with patch.object(sys, 'argv', argv), patch('verify_static.build_opener') as opener:
                    response = opener.return_value.open.return_value.__enter__.return_value
                    response.status = 200
                    response.read.return_value = b'expected'
                    with self.assertRaisesRegex(ValueError, 'Duplicate manifest member'):
                        main()
                    opener.assert_not_called()
                    self.assertFalse(output.exists())

    def test_only_integer_version_one_is_accepted(self):
        for version in [True, 1.0, '1', 2, None]:
            with self.subTest(version=version), patch('verify_static.build_opener') as opener:
                with self.assertRaisesRegex(ValueError, 'Invalid manifest'):
                    verify({'version': version, 'files': {'index.html': digest(b'expected')}},
                           'https://example.com')
                opener.assert_not_called()

    def test_entire_inventory_validated_before_network(self):
        for name, value in [('../secret', 'a'*64), ('later.css', 'invalid'), ('.', 'a'*64)]:
            with self.subTest(name=name), patch('verify_static.build_opener') as opener:
                with self.assertRaises(ValueError):
                    verify({'version': 1, 'files': {'index.html': 'a'*64, name: value}},
                           'https://example.com')
                opener.assert_not_called()

    def test_generated_manifest_round_trip_preserves_all_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'index.html').write_bytes(b'expected')
            (root / 'nested').mkdir()
            (root / 'nested' / 'index.html').write_bytes(b'expected')
            (root / 'style.css').write_bytes(b'expected')
            source = json.dumps(manifest(root))
        with patch('verify_static.build_opener') as opener:
            response = opener.return_value.open.return_value.__enter__.return_value
            response.status = 200
            response.read.return_value = b'expected'
            code, report = self.run_manifest_cli(source)
        self.assertEqual(code, 0)
        self.assertEqual(report['status'], 'passed')
        self.assertEqual([row['path'] for row in report['files']],
                         ['index.html', 'nested/index.html', 'style.css'])
        self.assertEqual([call.args[0].full_url for call in opener.return_value.open.call_args_list],
                         ['https://example.com/', 'https://example.com/nested/', 'https://example.com/style.css'])

    def test_empty_manifest_remains_rejected(self):
        with patch('verify_static.build_opener') as opener:
            with self.assertRaises(ValueError):
                verify({'version': 1, 'files': {}}, 'https://example.com')
            opener.assert_not_called()

    def test_readback_and_index_routes(self):
        opener = MagicMock()
        response = opener.open.return_value.__enter__.return_value
        response.status = 200
        response.read.return_value = b'expected'
        with patch('verify_static.build_opener', return_value=opener):
            report = verify({'version':1,'files':{'index.html':digest(b'expected'),'myindex.html':digest(b'other')}}, 'https://example.com')
        self.assertEqual(report['status'], 'incomplete')
        self.assertEqual([r['result'] for r in report['files']], ['exact','mismatch'])
        self.assertEqual([c.args[0].full_url for c in opener.open.call_args_list], ['https://example.com/','https://example.com/myindex.html'])
    def test_http_failure_is_not_success(self):
        opener = MagicMock()
        opener.open.side_effect = HTTPError('https://example.com',403,'Forbidden',{},None)
        with patch('verify_static.build_opener', return_value=opener):
            report = verify({'version':1,'files':{'index.html':'a'*64}}, 'https://example.com')
        self.assertEqual(report['status'],'incomplete')
        self.assertEqual(report['files'][0]['http_status'],403)
    def test_manifest_detects_changes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'index.html';p.write_text('a');a=manifest(d);p.write_text('b')
            self.assertNotEqual(a,manifest(d))
    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'real';p.write_text('a');(Path(d)/'link').symlink_to(p)
            with self.assertRaises(ValueError):manifest(d)
    def test_unsafe_inputs_rejected_before_network(self):
        for origin in ['http://example.com','https://user:secret@example.com','https://example.com/?key=x']:
            with self.assertRaises(ValueError):verify({'version':1,'files':{'index.html':'a'*64}},origin)
        with self.assertRaises(ValueError):verify({'version':1,'files':{'../secret':'a'*64}},'https://example.com')

if __name__=='__main__':unittest.main()
