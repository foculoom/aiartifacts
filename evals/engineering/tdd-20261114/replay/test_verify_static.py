import tempfile
import unittest
from unittest.mock import patch, MagicMock
from urllib.error import HTTPError
from pathlib import Path
from verify_static import manifest, verify, digest

class Checks(unittest.TestCase):
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

import io
import json
from contextlib import redirect_stdout, redirect_stderr
from verify_static import main

class ContractChecks(unittest.TestCase):
    def test_record_shape_rejected_before_network(self):
        invalid_records = [
            None, [], 'record', 1, True,
            {}, {'version': 1}, {'version': 1, 'files': {}},
            {'version': 1, 'files': []},
            *({'version': version, 'files': {'a.txt': 'a' * 64}}
              for version in [True, 1.0, '1', 0, 2, None]),
        ]
        for record in invalid_records:
            with self.subTest(record=record):
                with patch('verify_static.build_opener') as network:
                    with self.assertRaises(ValueError):
                        verify(record, 'https://example.com')
                    network.assert_not_called()

    def test_all_paths_validated_before_network(self):
        bad_paths = ['', '.', '..', './a', 'a/.', 'a/../b', '/a',
                     'a//b', 'a/', 'a\\b', 1, None]
        for name in bad_paths:
            for late in [False, True]:
                with self.subTest(name=name, invalid_after_valid=late):
                    files = {'valid.txt': 'a' * 64} if late else {}
                    files[name] = 'a' * 64
                    with patch('verify_static.build_opener') as network:
                        with self.assertRaises(ValueError):
                            verify({'version': 1, 'files': files}, 'https://example.com')
                        network.assert_not_called()

    def test_all_digests_validated_before_network(self):
        for bad_digest in [None, True, 64, [], '', 'a' * 63, 'a' * 65,
                           'A' * 64, 'g' * 64, 'a' * 63 + '\n']:
            for late in [False, True]:
                with self.subTest(digest=bad_digest, invalid_after_valid=late):
                    files = {'valid.txt': 'a' * 64} if late else {}
                    files['invalid.txt'] = bad_digest
                    with patch('verify_static.build_opener') as network:
                        with self.assertRaises(ValueError):
                            verify({'version': 1, 'files': files}, 'https://example.com')
                        network.assert_not_called()

    def test_cli_rejects_duplicate_json_members_without_output(self):
        entry = '"a.txt":"' + 'a' * 64 + '"'
        inventories = [
            '{"version":1,"version":1,"files":{' + entry + '}}',
            '{"version":1,"files":{' + entry + '},"files":{' + entry + '}}',
            '{"version":1,"files":{' + entry + ',' + entry + '}}',
            '{"version":1,"files":{' + entry + ',"a.txt":"' + 'b' * 64 + '"}}',
            '{"version":1,"files":{' + entry + ',"a\\u002etxt":"' + 'a' * 64 + '"}}',
            '{"version":1,"files":{' + entry + '},"extra":{"x":1,"x":2}}',
        ]
        for text in inventories:
            with self.subTest(text=text), tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
                source, output = Path(d) / 'manifest.json', Path(d) / 'report.json'
                source.write_text(text)
                argv = ['verify_static', '--manifest', str(source), '--origin',
                        'https://example.com', '--output', str(output)]
                with patch('sys.argv', argv), patch('verify_static.build_opener') as network:
                    network.return_value.open.side_effect = OSError('offline test transport')
                    with redirect_stdout(io.StringIO()), self.assertRaises(ValueError):
                        main()
                    network.assert_not_called()
                self.assertFalse(output.exists())

    def test_valid_distinct_cli_entries_survive_with_exact_outputs(self):
        empty_sha = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        abc_sha = 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
        files = {'index.html': empty_sha, 'docs/index.html': abc_sha,
                 'a b#?.txt': empty_sha, 'café.txt': abc_sha}
        opener = MagicMock()
        responses = []
        for body in [b'', b'abc', b'', b'abc']:
            context = MagicMock()
            context.__enter__.return_value.status = 200
            context.__enter__.return_value.read.return_value = body
            responses.append(context)
        opener.open.side_effect = responses
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
            source, output = Path(d) / 'manifest.json', Path(d) / 'report.json'
            source.write_text(json.dumps({'version': 1, 'files': files}))
            argv = ['verify_static', '--manifest', str(source), '--origin',
                    'https://example.com', '--output', str(output)]
            stdout = io.StringIO()
            with patch('sys.argv', argv), patch('verify_static.build_opener', return_value=opener):
                with redirect_stdout(stdout):
                    self.assertEqual(main(), 0)
            self.assertEqual(stdout.getvalue(), 'PASS\n')
            self.assertEqual(json.loads(output.read_text()), {
                'status': 'passed', 'origin': 'https://example.com', 'files': [
                    {'path': 'index.html', 'result': 'exact', 'http_status': 200},
                    {'path': 'docs/index.html', 'result': 'exact', 'http_status': 200},
                    {'path': 'a b#?.txt', 'result': 'exact', 'http_status': 200},
                    {'path': 'café.txt', 'result': 'exact', 'http_status': 200},
                ]})
            self.assertEqual([call.args[0].full_url for call in opener.open.call_args_list], [
                'https://example.com/', 'https://example.com/docs/',
                'https://example.com/a%20b%23%3F.txt', 'https://example.com/caf%C3%A9.txt'])

    def test_invalid_cli_records_create_no_output(self):
        records = [None, [], {}, {'version': True, 'files': {'a': 'a' * 64}},
                   {'version': 1.0, 'files': {'a': 'a' * 64}},
                   {'version': 1, 'files': {}}]
        records += [{'version': 1, 'files': {'valid': 'a' * 64, name: value}}
                    for name, value in [('', 'a' * 64), ('.', 'a' * 64),
                                        ('../secret', 'a' * 64), ('a\\b', 'a' * 64),
                                        ('bad', 'A' * 64), ('bad', None)]]
        for record in records:
            with self.subTest(record=record), tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
                source, output = Path(d) / 'manifest.json', Path(d) / 'report.json'
                source.write_text(json.dumps(record))
                argv = ['verify_static', '--manifest', str(source), '--origin',
                        'https://example.com', '--output', str(output)]
                with patch('sys.argv', argv), patch('verify_static.build_opener') as network:
                    with self.assertRaises(ValueError):
                        main()
                    network.assert_not_called()
                self.assertFalse(output.exists())

    def test_cli_preserves_existing_output_and_payload_boundary(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
            root = Path(d) / 'payload'
            root.mkdir()
            (root / 'index.html').write_bytes(b'abc')
            existing = Path(d) / 'existing.json'
            existing.write_bytes(b'preserve me')
            for output in [existing, root / 'new.json']:
                argv = ['verify_static', '--root', str(root), '--output', str(output)]
                with patch('sys.argv', argv), redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit) as error:
                        main()
                self.assertEqual(error.exception.code, 2)
            self.assertEqual(existing.read_bytes(), b'preserve me')
            self.assertFalse((root / 'new.json').exists())

    def test_manifest_cli_preserves_valid_output(self):
        with tempfile.TemporaryDirectory(dir=Path(__file__).parent) as d:
            root, output = Path(d) / 'payload', Path(d) / 'manifest.json'
            root.mkdir()
            (root / 'index.html').write_bytes(b'abc')
            argv = ['verify_static', '--root', str(root), '--output', str(output)]
            with patch('sys.argv', argv), redirect_stdout(io.StringIO()) as stdout:
                self.assertEqual(main(), 0)
            self.assertEqual(stdout.getvalue(), 'PASS\n')
            self.assertEqual(json.loads(output.read_text()), {'version': 1, 'files': {
                'index.html': 'ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'}})

if __name__=='__main__':unittest.main()
