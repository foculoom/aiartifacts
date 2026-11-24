"""Mutation tests for public-skills pin, license, notice and manifest checks."""
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_catalog import (  # noqa: E402
    assert_skill_frontmatter,
    validate_public_skills_provenance,
)

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
        with self.assertRaisesRegex(
                AssertionError, 'frontend-design file manifest sha256'):
            validate_public_skills_provenance(self.package)

    def test_deleted_license_fails(self):
        (self.package / 'skills' / 'playwright-cli' / 'LICENSE').unlink()
        (self.package / 'skills' / 'playwright-cli' / 'NOTICE').unlink()
        with self.assertRaisesRegex(
                AssertionError, 'playwright-cli is missing a LICENSE file'):
            validate_public_skills_provenance(self.package)

    def test_pin_set_to_main_fails(self):
        provenance = self.package / 'PROVENANCE.md'
        text = provenance.read_text()
        self.assertIn(PLAYWRIGHT_PIN, text)
        provenance.write_text(text.replace(PLAYWRIGHT_PIN, 'main'))
        with self.assertRaisesRegex(
                AssertionError, 'playwright-cli pin must be a 40-character'):
            validate_public_skills_provenance(self.package)

    def test_deleted_notice_fails(self):
        # Delete only the listed licenses/ NOTICE; leave the in-skill NOTICE
        # so the file-manifest check does not also fire.
        (self.package / 'licenses' / 'playwright' / 'NOTICE').unlink()
        with self.assertRaisesRegex(
                AssertionError, 'playwright-cli recorded NOTICE is missing'):
            validate_public_skills_provenance(self.package)

    def test_commit_line_disagrees_with_table_fails(self):
        provenance = self.package / 'PROVENANCE.md'
        text = provenance.read_text()
        # Change only the narrative playwright-cli Commit line, not the table.
        needle = f'- Commit: `{PLAYWRIGHT_PIN}` (November 20, 2026, 11:10 AM PT)'
        self.assertIn(needle, text)
        self.assertEqual(text.count(needle), 1)
        provenance.write_text(text.replace(
            needle, '- Commit: `main` (November 20, 2026, 11:10 AM PT)', 1))
        with self.assertRaisesRegex(
                AssertionError,
                'playwright-cli narrative Commit line .main. does not match'):
            validate_public_skills_provenance(self.package)

    def test_non_skill_md_file_change_fails(self):
        path = (self.package / 'skills' / 'cloudflare' / 'references'
                / 'bindings' / 'api.md')
        path.write_text(path.read_text() + 'tampered\n')
        with self.assertRaisesRegex(
                AssertionError, 'cloudflare file manifest sha256'):
            validate_public_skills_provenance(self.package)

    def test_mismatched_name_quotes_fails(self):
        skill_dir = self.temp / 'editorial-writing'
        skill_dir.mkdir()
        (skill_dir / 'SKILL.md').write_text(
            '---\nname: "editorial-writing\'\ndescription: fixture\n---\n')
        with self.assertRaisesRegex(
                AssertionError, 'mismatched name: field'):
            assert_skill_frontmatter(skill_dir / 'SKILL.md')


if __name__ == '__main__':
    unittest.main()
