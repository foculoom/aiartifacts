"""Portable, synthetic packaging checks; no installer or model is invoked."""
import importlib.util
import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
import warnings
import zipfile


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/export_skill.py'
SPEC = importlib.util.spec_from_file_location('export_skill', SCRIPT)
exporter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(exporter)
REPO = SCRIPT.parents[5]


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.source = self.base / 'source'
        self.source.mkdir()
        self.config = self.base / 'config.json'
        self.output = self.base / 'output'
        self.record = {
            'version': 1, 'name': 'sample', 'kind': 'skill',
            'source_commit': 'a' * 40,
            'files': {'SKILL.md': 'skill/SKILL.md', 'LICENSE': 'LICENSE',
                      'references/usage.md': 'skill/references/usage.md'}}
        self.write('skill/SKILL.md', '---\nname: sample\ndescription: Review a sample.\n---\n'
                   '[Usage](references/usage.md)\n')
        self.write('skill/references/usage.md', 'Synthetic, original instructions.\n')
        self.write('LICENSE', 'Synthetic license fixture; not a rights assertion.\n')
        self.save()

    def write(self, name, value):
        path = self.source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding='utf-8')
        return path

    def save(self):
        self.config.write_text(json.dumps(self.record), encoding='utf-8')

    def run_export(self):
        return exporter.export(self.source, self.config, self.output)

    def cli(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *map(str, args)],
                              text=True, capture_output=True, check=False)

    def rejected(self):
        with self.assertRaises((ValueError, OSError)):
            self.run_export()
        self.assertFalse(self.output.exists())

    def test_end_to_end_exact_files_deterministic_archive_and_candidate_provenance(self):
        # An unlisted file is never swept into the public payload.
        self.write('notes.md', 'Private source not requested for export.')
        original = (self.source / 'skill/SKILL.md').read_bytes()
        result = self.cli('export', '--source-root', self.source,
                          '--config', self.config, '--output', self.output)
        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = self.output / 'manifest.json'
        evidence = json.loads(manifest.read_text())
        self.assertEqual(set(evidence['files']), set(self.record['files']))
        self.assertEqual(evidence['source_commit'], 'a' * 40)
        self.assertIn('Caller-supplied', evidence['source_commit_verification'])
        self.assertEqual(evidence['files']['SKILL.md']['sha256'], exporter.digest(original))
        self.assertEqual((self.source / 'skill/SKILL.md').read_bytes(), original)
        for option, target in [('--archive', self.output / 'skill.zip'),
                               ('--installed-root', self.output / 'payload')]:
            checked = self.cli('verify', '--manifest', manifest, option, target)
            self.assertEqual(checked.returncode, 0, checked.stderr)
        second = self.base / 'second'
        exporter.export(self.source, self.config, second)
        self.assertEqual((self.output / 'skill.zip').read_bytes(),
                         (second / 'skill.zip').read_bytes())
        self.assertEqual(manifest.read_bytes(), (second / 'manifest.json').read_bytes())

    def test_real_editorial_skill_exports_with_its_references_tests_and_license(self):
        skill = REPO / 'plugins/editorial/skills/editorial-writing'
        self.assertTrue(skill.is_dir(), REPO)
        self.record.update(name='editorial-writing')
        self.record['files'] = {
            p.relative_to(skill).as_posix(): p.relative_to(REPO).as_posix()
            for p in skill.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
        self.record['files']['LICENSE'] = 'LICENSE'
        self.save()
        exporter.export(REPO, self.config, self.output)
        with zipfile.ZipFile(self.output / 'skill.zip') as archive:
            self.assertIn('scripts/prose_lint.py', archive.namelist())
            self.assertIn('tests/test_prose_lint.py', archive.namelist())
            self.assertEqual(archive.read('LICENSE'), (REPO / 'LICENSE').read_bytes())
            self.assertFalse(any(p.startswith('plugins/') for p in archive.namelist()))
        exporter.verify(self.output / 'manifest.json', installed_root=self.output / 'payload')

    def test_checked_in_pilot_contracts_preserve_same_skill_and_license_boundaries(self):
        for kind in ('skill', 'plugin'):
            config = REPO / 'evals/skill-delivery/pilot' / ('editorial-' + kind + '.json')
            exporter.export(REPO, config, self.base / kind)
        skill = self.base / 'skill/payload'
        plugin = self.base / 'plugin/payload'
        nested = plugin / 'skills/editorial-writing'
        def inventory(root):
            return {path.relative_to(root).as_posix(): path.read_bytes()
                    for path in root.rglob('*') if path.is_file()}
        self.assertEqual(inventory(skill), inventory(nested))
        self.assertEqual((skill / 'LICENSE').read_bytes(), (REPO / 'LICENSE').read_bytes())
        self.assertEqual((plugin / 'LICENSE').read_bytes(), (REPO / 'LICENSE').read_bytes())
        self.assertEqual(json.loads((plugin / 'plugin.json').read_text())['name'], 'editorial')
        self.assertEqual({p.name for p in (plugin / 'skills').iterdir()}, {'editorial-writing'})

    def test_skill_delivery_can_export_its_own_runtime_files(self):
        skill = SCRIPT.parents[1]
        self.record.update(name='skill-delivery')
        self.record['files'] = {
            path.relative_to(skill).as_posix(): path.relative_to(REPO).as_posix()
            for path in skill.rglob('*') if path.is_file()
            and not {'tests', '__pycache__'}.intersection(path.relative_to(skill).parts)}
        self.save()
        exporter.export(REPO, self.config, self.output)
        exporter.verify(self.output / 'manifest.json', installed_root=self.output / 'payload')
        self.assertEqual((self.output / 'payload/scripts/export_skill.py').read_bytes(),
                         SCRIPT.read_bytes())

    def test_executable_helper_retains_behavior_and_mode_tampering_fails(self):
        helper = self.write('skill/scripts/helper.py',
                            '#!/usr/bin/env python3\nprint("synthetic helper works")\n')
        helper.chmod(0o711)
        self.record['files']['scripts/helper.py'] = 'skill/scripts/helper.py'
        self.save()
        self.run_export()
        installed = self.output / 'payload'
        manifest = self.output / 'manifest.json'
        evidence = json.loads(manifest.read_text())
        self.assertEqual(evidence['files']['scripts/helper.py']['mode'], '0755')
        self.assertEqual(evidence['files']['SKILL.md']['mode'], '0644')
        staged = installed / 'scripts/helper.py'
        self.assertEqual(stat.S_IMODE(staged.stat().st_mode), 0o755)
        completed = subprocess.run([str(staged)], text=True, capture_output=True, check=False)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertEqual(completed.stdout, 'synthetic helper works\n')
        exporter.verify(manifest, installed_root=installed)
        original = self.output / 'skill.zip'
        changed = self.base / 'changed-mode.zip'
        with zipfile.ZipFile(original) as source, zipfile.ZipFile(changed, 'w') as target:
            for entry in source.infolist():
                if entry.filename == 'scripts/helper.py':
                    self.assertEqual(stat.S_IMODE(entry.external_attr >> 16), 0o755)
                    entry.external_attr = (stat.S_IFREG | 0o644) << 16
                target.writestr(entry, source.read(entry.filename))
        with self.assertRaises(ValueError):
            exporter.verify(manifest, archive=changed)
        staged.chmod(0o644)
        with self.assertRaises(ValueError):
            exporter.verify(manifest, installed_root=installed)

    def test_existing_directory_and_archive_are_preserved(self):
        self.output.mkdir()
        sentinel = self.output / 'skill.zip'
        sentinel.write_bytes(b'previous evidence')
        with self.assertRaises(ValueError):
            self.run_export()
        self.assertEqual(sentinel.read_bytes(), b'previous evidence')
        self.assertEqual(list(self.output.iterdir()), [sentinel])

    def test_source_and_destination_traversal_and_absolute_paths_fail_before_writing(self):
        for bad in ['../outside', '/absolute', 'a/../b', 'a//b', 'a\\b', 'C:drive', './a']:
            for position in ('source', 'target'):
                with self.subTest(path=bad, position=position):
                    self.record['files'] = {'SKILL.md': bad} if position == 'source' else {
                        bad: 'skill/SKILL.md'}
                    self.save()
                    self.rejected()

    def test_source_links_and_linked_ancestors_are_rejected(self):
        outside = self.base / 'outside.md'
        outside.write_text('not selected', encoding='utf-8')
        for name, target in [('linked.md', outside), ('linked-dir', self.source / 'skill')]:
            path = self.source / name
            try:
                path.symlink_to(target, target_is_directory=target.is_dir())
            except (OSError, NotImplementedError):
                self.skipTest('Symlinks unavailable')
            self.record['files']['references/usage.md'] = (
                name + '/references/usage.md' if target.is_dir() else name)
            self.save()
            self.rejected()

    def test_source_root_and_output_links_are_rejected(self):
        linked = self.base / 'linked'
        try:
            linked.symlink_to(self.source, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest('Symlinks unavailable')
        with self.assertRaises(ValueError):
            exporter.export(linked, self.config, self.output)
        self.output.symlink_to(self.base / 'missing')
        with self.assertRaises(ValueError):
            self.run_export()
        self.assertTrue(self.output.is_symlink())

    def test_new_output_inside_source_is_safe_with_explicit_allowlist(self):
        build = self.source / 'build'
        build.mkdir()
        output = build / 'skill-delivery'
        before = {p: (self.source / p).read_bytes() for p in self.record['files'].values()}
        exporter.export(self.source, self.config, output)
        exporter.verify(output / 'manifest.json', installed_root=output / 'payload')
        self.assertEqual(before, {p: (self.source / p).read_bytes() for p in before})
        self.assertEqual(set(json.loads((output / 'manifest.json').read_text())['files']),
                         set(self.record['files']))
        # A later export from the same source never discovers old build outputs.
        exporter.export(self.source, self.config, build / 'second')
        self.assertEqual((output / 'skill.zip').read_bytes(),
                         (build / 'second/skill.zip').read_bytes())

    def test_missing_file_and_missing_license_are_rejected(self):
        (self.source / 'LICENSE').unlink()
        self.rejected()
        self.record['files'].pop('LICENSE')
        self.save()
        self.rejected()

    def test_private_paths_rejected_even_when_explicitly_allowlisted(self):
        for name in ['.env', '.env.production', '.git/config', 'private/brief.md',
                     'AGENTS.md', 'HANDOFF.md', 'credentials/token']:
            with self.subTest(name=name):
                self.record['files']['references/usage.md'] = name
                self.save()
                self.rejected()

    def test_secret_screen_does_not_echo_secret_or_create_payload(self):
        tokens = ['ghp_' + 'Z' * 32, 'sk-' + 'Z' * 32,
                  'PRIVATE_CONTEXT_TEST_' + 'SENTINEL',
                  '-----BEGIN PRIVATE KEY-----']
        for token in tokens:
            with self.subTest(token_type=token[:4]):
                self.write('skill/references/usage.md', token)
                result = self.cli('export', '--source-root', self.source,
                                  '--config', self.config, '--output', self.output)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn(token, result.stdout + result.stderr)
                self.assertFalse(self.output.exists())

    def test_missing_escaping_encoded_and_reference_style_links_rejected(self):
        for text in ['[private](../../outside.md)', '[missing](missing.md)',
                     '[encoded](%2E%2E/%2E%2E/outside.md)',
                     '[ref][hidden]\n\n[hidden]: ../../outside.md',
                     '[local](file:///etc/passwd)']:
            with self.subTest(link=text):
                self.write('skill/references/usage.md', text)
                self.rejected()

    def test_external_anchor_and_contained_parent_links_work(self):
        self.write('skill/references/usage.md',
                   '[Back](../SKILL.md#purpose) [Official](https://example.com/a) '
                   '[Mail](mailto:contact@example.com) [Anchor](#here)')
        self.run_export()

    def test_package_root_and_balanced_parentheses_links_work(self):
        guide = 'references/guide(v2).md'
        self.write('skill/' + guide, '[Root](../) [Current](./)\n')
        self.record['files'][guide] = 'skill/' + guide
        self.save()
        self.write('skill/SKILL.md', '---\nname: sample\ndescription: Example\n---\n'
                   '[Root](./) [Guide](references/guide(v2).md)\n')
        self.run_export()
        with zipfile.ZipFile(self.output / 'skill.zip') as archive:
            self.assertIn(guide, archive.namelist())

    def test_empty_inline_destination_refers_to_current_document(self):
        self.write('skill/references/usage.md', '[Self]() and [Whitespace](   )\n')
        self.run_export()
        exporter.verify(self.output / 'manifest.json', archive=self.output / 'skill.zip')

    def test_config_duplicate_members_unknown_fields_versions_and_collisions_rejected(self):
        self.config.write_text('{"version":1,"version":1}', encoding='utf-8')
        self.rejected()
        for version in [True, 1.0, 2]:
            self.record['version'] = version
            self.save()
            self.rejected()
        self.record['version'] = 1
        self.record['unexpected'] = 'field'
        self.save()
        self.rejected()
        self.record.pop('unexpected')
        self.record['files']['license'] = 'LICENSE'
        self.save()
        self.rejected()

    def test_file_directory_destination_conflict_fails_before_output(self):
        self.record['files']['references'] = 'LICENSE'
        self.save()
        self.rejected()

    def test_missing_frontmatter_or_empty_instructions_rejected(self):
        for text in ['', 'No frontmatter.', '---\n\n---\nBody',
                     '---\nname: sample\n---\n']:
            self.write('skill/SKILL.md', text)
            self.rejected()

    def test_block_description_is_preserved_for_target_yaml_validation(self):
        original = ('---\nname: sample\ndescription: |\n'
                    '  Review this sample and its output.\n  Preserve the brief.\n'
                    '---\nUseful instructions.\n')
        self.write('skill/SKILL.md', original)
        self.run_export()
        self.assertEqual((self.output / 'payload/SKILL.md').read_text(), original)

    def test_one_plugin_with_nested_skill_and_root_license(self):
        self.record.update(kind='plugin', name='sample-plugin')
        self.write('plugin.json', '{"name":"sample-plugin","version":"0.1.0"}')
        self.record['files'] = {
            'plugin.json': 'plugin.json', 'LICENSE': 'LICENSE',
            'skills/sample/SKILL.md': 'skill/SKILL.md',
            'skills/sample/references/usage.md': 'skill/references/usage.md'}
        self.save()
        self.run_export()
        exporter.verify(self.output / 'manifest.json', archive=self.output / 'skill.zip')

    def test_installed_missing_changed_extra_and_symlinked_files_fail(self):
        self.run_export()
        root = self.output / 'payload'
        manifest = self.output / 'manifest.json'
        original = (root / 'SKILL.md').read_bytes()
        (root / 'SKILL.md').write_bytes(b'changed')
        with self.assertRaises(ValueError):
            exporter.verify(manifest, installed_root=root)
        (root / 'SKILL.md').unlink()
        with self.assertRaises(ValueError):
            exporter.verify(manifest, installed_root=root)
        (root / 'SKILL.md').write_bytes(original)
        (root / 'extra.txt').write_text('unexpected')
        with self.assertRaises(ValueError):
            exporter.verify(manifest, installed_root=root)
        (root / 'extra.txt').unlink()
        (root / 'SKILL.md').unlink()
        try:
            (root / 'SKILL.md').symlink_to(self.source / 'skill/SKILL.md')
        except (OSError, NotImplementedError):
            self.skipTest('Symlinks unavailable')
        with self.assertRaises(ValueError):
            exporter.verify(manifest, installed_root=root)

    def test_zip_duplicate_unexpected_traversal_symlink_and_changed_bytes_fail(self):
        self.run_export()
        manifest = self.output / 'manifest.json'
        original = self.output / 'skill.zip'
        for case in ['duplicate', 'unexpected', 'traversal', 'symlink', 'changed', 'missing']:
            archive = self.base / (case + '.zip')
            with zipfile.ZipFile(original) as source, zipfile.ZipFile(archive, 'w') as target:
                for entry in source.infolist():
                    if case == 'missing' and entry.filename == 'SKILL.md':
                        continue
                    value = source.read(entry)
                    if entry.filename == 'SKILL.md' and case == 'changed':
                        value = b'changed'
                    if entry.filename == 'SKILL.md' and case == 'symlink':
                        entry.external_attr = (stat.S_IFLNK | 0o777) << 16
                    target.writestr(entry, value)
                if case == 'duplicate':
                    with warnings.catch_warnings():
                        warnings.simplefilter('ignore', UserWarning)
                        target.writestr('LICENSE', source.read('LICENSE'))
                elif case in {'unexpected', 'traversal'}:
                    target.writestr('extra.txt' if case == 'unexpected' else '../escape', b'bad')
            with self.subTest(case=case), self.assertRaises(ValueError):
                exporter.verify(manifest, archive=archive)

    def test_duplicate_manifest_members_and_invalid_digest_fail(self):
        self.run_export()
        manifest = self.output / 'manifest.json'
        original = manifest.read_text()
        manifest.write_text(original.replace('"version": 1', '"version": 1, "version": 1'))
        with self.assertRaises(ValueError):
            exporter.verify(manifest, archive=self.output / 'skill.zip')
        data = json.loads(original)
        data['files']['SKILL.md']['sha256'] = 'not a hash'
        manifest.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            exporter.verify(manifest, archive=self.output / 'skill.zip')


if __name__ == '__main__':
    unittest.main()
