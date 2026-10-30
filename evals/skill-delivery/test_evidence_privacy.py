"""Bounded host-path regression for tracked public evidence, not a privacy audit."""
import io
from pathlib import Path
import re
import subprocess
import unittest
import zipfile


REPO = Path(__file__).resolve().parents[2]
EVIDENCE = ('evals/skill-delivery/results',
            'evals/skill-delivery/agent-supply-chain/results-*')
MAX_FILE_BYTES = 16 * 1024 * 1024
MAX_MEMBER_BYTES = 4 * 1024 * 1024
MAX_ARCHIVE_BYTES = 32 * 1024 * 1024
HOST_PATH = re.compile(
    rb'/(?:private/)?var/folders/(?!<)[A-Za-z0-9_.-]+/'
    rb'|/(?:Users|home)/(?!<)[A-Za-z0-9_.-]+(?:/|(?=[\s"\x27]|$))'
    rb'|[A-Za-z]:[\\/]+Users[\\/]+(?!<)[A-Za-z0-9_.-]+[\\/]'
    rb'|~[\\/](?:Documents|Desktop|Downloads)[\\/](?!<)[A-Za-z0-9_.-]+')


def zip_issues(data, member_limit=MAX_MEMBER_BYTES):
    """Read capped members; report categories without echoing matched paths."""
    issues = set()
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        members = archive.infolist()
        if sum(member.file_size for member in members) > MAX_ARCHIVE_BYTES:
            return {'archive exceeds scan limit'}
        for member in members:
            if member.file_size > member_limit:
                issues.add('ZIP member exceeds scan limit')
                continue
            with archive.open(member) as stream:
                content = stream.read(member_limit + 1)
            if len(content) > member_limit:
                issues.add('ZIP member exceeds scan limit')
            elif HOST_PATH.search(content):
                issues.add('host-local path in ZIP member')
    return issues


class EvidencePrivacyTests(unittest.TestCase):
    def test_detects_common_host_local_prefixes(self):
        for value in [b'/var/folders/zz/synthetic-machine/T/checker-file',
                      b'/private/var/folders/zz/synthetic-machine/T/checker-file',
                      b'/Users/synthetic-user/work/file',
                      b'/home/synthetic-user/work/file',
                      rb'C:\Users\synthetic-user\work\file',
                      b'| ~/Documents/synthetic-workspace/project |\n| /build/output |']:
            with self.subTest(prefix_case=value.split(b'synthetic')[0]):
                self.assertIsNotNone(HOST_PATH.search(value))

    def test_allows_redaction_placeholders_and_generic_system_paths(self):
        for value in [b'<USER_HOME>/work/file', b'<SYSTEM_TMP>/checker-file',
                      b'/Users/<REDACTED>/file', b'/home/<REDACTED>/file',
                      b'/var/folders/<REDACTED>/file',
                      b'/private/var/folders/<REDACTED>/file',
                      rb'C:\Users\<REDACTED>\file', b'/private/tmp',
                      b'/usr/bin/python3', b'~/Documents/<REDACTED>/file']:
            self.assertIsNone(HOST_PATH.search(value))

    def test_compressed_zip_members_are_scanned_and_size_bounded(self):
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr('report.txt', b'/var/folders/zz/synthetic/T/file')
        self.assertEqual(zip_issues(data.getvalue()), {'host-local path in ZIP member'})
        self.assertEqual(zip_issues(data.getvalue(), member_limit=8),
                         {'ZIP member exceeds scan limit'})

    def test_tracked_public_evidence_contains_no_common_host_paths(self):
        # Only tracked evidence is selected; ignored/raw local captures are excluded.
        # CI checks the committed checkout; locally this checks its current file bytes.
        output = subprocess.check_output(
            ['git', 'ls-files', '-z', '--', *EVIDENCE], cwd=REPO)
        names = [name.decode('utf-8') for name in output.split(b'\0') if name]
        self.assertTrue(names, 'No tracked public evidence found')
        for name in names:
            with self.subTest(evidence=name):
                path = REPO / name
                self.assertFalse(path.is_symlink(), 'Evidence symlink is not scanned')
                self.assertLessEqual(path.stat().st_size, MAX_FILE_BYTES,
                                     'Evidence file exceeds scan limit')
                data = path.read_bytes()
                self.assertIsNone(HOST_PATH.search(data), 'Host-local path in evidence')
                if path.suffix == '.zip':
                    self.assertEqual(zip_issues(data), set())


if __name__ == '__main__':
    unittest.main()
