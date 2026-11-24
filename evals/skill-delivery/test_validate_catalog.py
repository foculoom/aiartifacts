"""Mutation tests for public-skills pin, license and hash checks."""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_catalog import validate_public_skills_provenance  # noqa: E402

PLUGIN = ROOT / 'plugins' / 'public-skills'
PLAYWRIGHT_PIN = '99d4c415db3794d1c989be16ac4987f4529e3220'


class PublicSkillsProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = Path(tempfile.mkdtemp())
        self.package = self.temp / 'public-skills'
        shutil.copytree(PLUGIN, self.package)

    def tearDown(self):
        shutil.rmtree(self.temp, ignore_errors=True)

    def test_current_snapshot_passes(self):
        validate_public_skills_provenance(self.package)

    def test_tampered_skill_md_fails(self):
        path = self.package / 'skills' / 'frontend-design' / 'SKILL.md'
        path.write_text(path.read_text() + 'tampered\n')
        with self.assertRaisesRegex(AssertionError, 'frontend-design SKILL.md sha256'):
            validate_public_skills_provenance(self.package)

    def test_deleted_license_fails(self):
        (self.package / 'skills' / 'playwright-cli' / 'LICENSE').unlink()
        (self.package / 'skills' / 'playwright-cli' / 'NOTICE').unlink()
        with self.assertRaisesRegex(AssertionError, 'playwright-cli is missing a LICENSE file'):
            validate_public_skills_provenance(self.package)

    def test_pin_set_to_main_fails(self):
        provenance = self.package / 'PROVENANCE.md'
        text = provenance.read_text()
        self.assertIn(PLAYWRIGHT_PIN, text)
        provenance.write_text(text.replace(PLAYWRIGHT_PIN, 'main'))
        with self.assertRaisesRegex(AssertionError, 'playwright-cli pin must be a 40-character'):
            validate_public_skills_provenance(self.package)


if __name__ == '__main__':
    unittest.main()
