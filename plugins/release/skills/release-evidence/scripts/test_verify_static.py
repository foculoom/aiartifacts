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

if __name__=='__main__':unittest.main()
