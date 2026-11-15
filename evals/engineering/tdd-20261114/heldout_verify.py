"""Independent acceptance probes; withheld from the replay implementer."""
import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import MagicMock, patch

sys.path.insert(0, sys.argv.pop(1))
import verify_static as subject

HASH = 'a' * 64

class Acceptance(unittest.TestCase):
    def cli(self, raw):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / 'manifest.json'
            target = Path(tmp) / 'report.json'
            source.write_text(raw)
            args = ['verify_static', '--manifest', str(source), '--origin', 'https://example.com', '--output', str(target)]
            with patch.object(sys, 'argv', args), patch.object(subject, 'build_opener') as network:
                with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
                    with self.assertRaises((ValueError, SystemExit)):
                        subject.main()
                network.assert_not_called()
                self.assertFalse(target.exists())

    def test_duplicate_members_at_both_levels(self):
        for raw in [
            '{"version":1,"version":1,"files":{"a":"'+HASH+'"}}',
            '{"version":1,"files":{"a":"'+HASH+'","a":"'+HASH+'"}}',
            '{"version":1,"files":{"a":"'+HASH+'"},"files":{"b":"'+HASH+'"}}',
        ]:
            with self.subTest(raw=raw): self.cli(raw)

    def test_versions_and_shapes(self):
        for version in [True, False, 1.0, '1', None, 0, 2]:
            with self.subTest(version=version):
                self.cli(json.dumps({'version':version,'files':{'a':HASH}}))
        for record in [None, [], {}, {'version':1,'files':{}}, {'version':1,'files':[]}]:
            with self.subTest(record=record): self.cli(json.dumps(record))

    def test_invalid_later_paths_and_digests(self):
        for path in ['', '.', '/a', '../a', 'a/../b', 'a/./b', 'a//b', 'a/', 'a\\b']:
            with self.subTest(path=path):
                self.cli(json.dumps({'version':1,'files':{'valid.txt':HASH,path:HASH}}))
        for value in [None, 4, 'A'*64, 'g'*64, 'a'*63, 'a'*65]:
            with self.subTest(value=value):
                self.cli(json.dumps({'version':1,'files':{'valid.txt':HASH,'later.txt':value}}))

    def test_direct_verify_rejects_before_network(self):
        for record in [{'version':True,'files':{'a':HASH}}, {'version':1,'files':{'a':HASH, 7:HASH}}, {'version':1,'files':{'a':HASH,'bad/':HASH}}]:
            with self.subTest(record=record), patch.object(subject,'build_opener') as network:
                with self.assertRaises(ValueError): subject.verify(record,'https://example.com')
                network.assert_not_called()

    def test_valid_inventory_cli_preserved(self):
        # Known SHA-256 of empty bytes, independent of the subject's digest helper.
        empty='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        record={'version':1,'files':{'index.html':empty,'nested/index.html':empty,'space name.txt':empty}}
        with tempfile.TemporaryDirectory() as tmp:
            source=Path(tmp)/'in.json'; source.write_text(json.dumps(record)); target=Path(tmp)/'out.json'
            client=MagicMock(); response=client.open.return_value.__enter__.return_value
            response.status=200; response.read.return_value=b''
            args=['verify_static','--manifest',str(source),'--origin','https://example.com','--output',str(target)]
            with patch.object(sys,'argv',args),patch.object(subject,'build_opener',return_value=client),contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(subject.main(),0)
            report=json.loads(target.read_text())
            self.assertEqual(report['status'],'passed')
            self.assertEqual([x['path'] for x in report['files']],['index.html','nested/index.html','space name.txt'])
            self.assertEqual([x['result'] for x in report['files']],['exact','exact','exact'])
            self.assertEqual([x.args[0].full_url for x in client.open.call_args_list],['https://example.com/','https://example.com/nested/','https://example.com/space%20name.txt'])

if __name__ == '__main__': unittest.main(verbosity=2)
