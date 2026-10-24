import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/runner.py'
spec = importlib.util.spec_from_file_location('runner', SCRIPT)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
VAULT = 'a' * 26
ITEM = 'b' * 26
USER = 'c' * 26
SECRET = 'synthetic-only-provider-secret'
TOKEN = 'synthetic-only-service-token'
# The hosted CI toolcache interpreter is group-writable and must be rejected by
# production guards. Use the system interpreter for these stdlib-only fixtures.
TEST_PYTHON = Path('/usr/bin/python3').resolve()


def cfg():
    return {'op': {'path': '/synthetic/op'}, 'service_account_id': USER, 'vault_ids': [VAULT]}


def identity(*args):
    if args[1][:2] == ['user', 'get']:
        return {'id': USER, 'type': 'SERVICE_ACCOUNT', 'state': 'ACTIVE'}
    return [{'id': VAULT}]


class RunnerTests(unittest.TestCase):
    def test_identity_and_vault_allowlist(self):
        with patch.object(runner, 'op_json', side_effect=identity):
            runner.verify_identity(cfg(), TOKEN)

    def test_broader_vault_scope_fails(self):
        with patch.object(runner, 'op_json', side_effect=[
            {'id': USER, 'type': 'SERVICE_ACCOUNT', 'state': 'ACTIVE'},
            [{'id': VAULT}, {'id': 'd' * 26}]]):
            with self.assertRaisesRegex(runner.Blocked, 'scope_mismatch'):
                runner.verify_identity(cfg(), TOKEN)

    def test_wrong_identity_or_suspended_account(self):
        for who in ({'id': 'd' * 26, 'type': 'SERVICE_ACCOUNT', 'state': 'ACTIVE'},
                    {'id': USER, 'type': 'SERVICE_ACCOUNT', 'state': 'SUSPENDED'},
                    {'id': USER, 'type': 'HUMAN', 'state': 'ACTIVE'}):
            with patch.object(runner, 'op_json', return_value=who):
                with self.assertRaisesRegex(runner.Blocked, 'identity_or_state'):
                    runner.verify_identity(cfg(), TOKEN)

    def test_missing_malformed_token_no_network(self):
        for token in ('', None, 'tiny', TOKEN + '\n', TOKEN + ' space'):
            with patch.object(runner, 'op_json') as remote:
                with self.assertRaisesRegex(runner.Blocked, 'malformed'):
                    runner.verify_identity(cfg(), token)
                remote.assert_not_called()

    def test_expired_revoked_inaccessible_are_sanitized(self):
        for returncode in (1, 2, 77):
            with patch.object(runner, 'run', return_value=subprocess.CompletedProcess([], returncode, b'', SECRET.encode())):
                with self.assertRaisesRegex(runner.Blocked, '^vault_access_failed_check_expiry_revocation_or_scope$'):
                    runner.op_json(cfg(), ['user', 'get', '--me'], TOKEN)

    def test_op_env_excludes_connect_and_inherited_secrets(self):
        with patch.dict(os.environ, {'OP_CONNECT_TOKEN': SECRET, 'OTHER_SECRET': SECRET}), \
             patch.object(runner, 'run', return_value=subprocess.CompletedProcess([], 0, b'{}', b'')) as call:
            runner.op_json(cfg(), ['user', 'get', '--me'], TOKEN)
            env = call.call_args.kwargs['env']
            self.assertEqual(env['OP_SERVICE_ACCOUNT_TOKEN'], TOKEN)
            self.assertEqual(env['OP_BIOMETRIC_UNLOCK_ENABLED'], 'false')
            self.assertNotIn('OP_CONNECT_TOKEN', env)
            self.assertNotIn('OTHER_SECRET', env)

    def test_exact_concealed_field_only(self):
        ref = {'vault_id': VAULT, 'item_id': ITEM, 'field_id': 'password', 'pattern': r'[a-z-]+'}
        good = {'id': ITEM, 'vault': {'id': VAULT}, 'fields': [{'id': 'password', 'type': 'CONCEALED', 'value': SECRET}]}
        with patch.object(runner, 'op_json', return_value=good):
            self.assertEqual(runner.resolve_field(cfg(), ref, TOKEN), SECRET)
        for fields in ([], good['fields'] * 2, [{'id': 'password', 'type': 'STRING', 'value': SECRET}],
                       [{'id': 'password', 'type': 'CONCEALED', 'value': SECRET + '\n'}],
                       [{'id': 'password', 'type': 'CONCEALED', 'value': '123'}]):
            with patch.object(runner, 'op_json', return_value={**good, 'fields': fields}):
                with self.assertRaises(runner.Blocked):
                    runner.resolve_field(cfg(), ref, TOKEN)

    def test_wrong_item_and_vault(self):
        ref = {'vault_id': VAULT, 'item_id': ITEM, 'field_id': 'password', 'pattern': '.+'}
        for item in ({'id': 'd' * 26, 'vault': {'id': VAULT}}, {'id': ITEM, 'vault': {'id': 'd' * 26}}):
            with patch.object(runner, 'op_json', return_value=item):
                with self.assertRaisesRegex(runner.Blocked, 'item_mismatch'):
                    runner.resolve_field(cfg(), ref, TOKEN)

    def test_profile_requires_private_permissions(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'profile.json'; p.write_text('{}'); p.chmod(0o644)
            with self.assertRaisesRegex(runner.Blocked, '0600'):
                runner.load_profile(str(p))

    def test_changed_reviewed_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'script'; p.write_text('original')
            sha = runner.digest(p); p.write_text('changed')
            with self.assertRaisesRegex(runner.Blocked, 'changed'):
                runner.verify_file(str(p), sha)

    def test_group_writable_reviewed_file_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'script'; p.write_text('original'); p.chmod(0o660)
            with self.assertRaisesRegex(runner.Blocked, 'reviewed_file_writable_by_others'):
                runner.verify_file(str(p), runner.digest(p))

    def test_unreviewed_task_fails_before_keychain(self):
        with patch.object(runner, 'run') as read:
            with self.assertRaisesRegex(runner.Blocked, 'not_reviewed'):
                runner.execute({'tasks': {}}, 'arbitrary', TOKEN)
            read.assert_not_called()

    def test_child_never_receives_service_token_or_emits_secrets(self):
        with tempfile.TemporaryDirectory() as tmp:
            child = Path(tmp) / 'child.py'
            child.write_text('import os,sys,json\nassert "OP_SERVICE_ACCOUNT_TOKEN" not in os.environ\nassert "OTHER_SECRET" not in os.environ\nassert os.environ["PROVIDER_KEY"] == "' + SECRET + '"\nprint(os.environ["PROVIDER_KEY"])\nprint(os.environ["PROVIDER_KEY"],file=sys.stderr)\nopen(os.environ["LOCAL_RESULT_PATH"],"w").write(json.dumps({"run_id":os.environ["LOCAL_RUN_ID"],"target":"fixture","checks":{"scope":True}}))\n')
            config = {**cfg(), 'keychain_helper': {'path': '/synthetic/keychain'}, 'keychain_service': 'fixture', 'keychain_account': 'fixture', 'tasks': {'probe': {
                'authorization': 'Synthetic read-only test', 'source_revision': 'fixture-v1', 'argv': [str(TEST_PYTHON), '-I', str(child)],
                'cwd': tmp, 'reviewed_files': {str(TEST_PYTHON): runner.digest(str(TEST_PYTHON)), str(child): runner.digest(child)},
                'result_contract': {'directory': tmp, 'target':'fixture', 'checks':['scope']}, 'credentials': {'PROVIDER_KEY': {}}}}}
            with patch.dict(os.environ, {'OTHER_SECRET': SECRET}), \
                 patch.object(runner, 'run', return_value=subprocess.CompletedProcess([], 0, TOKEN.encode(), b'')), \
                 patch.object(runner, 'verify_identity'), patch.object(runner, 'resolve_field', return_value=SECRET):
                result = runner.execute(config, 'probe', TOKEN)
                self.assertEqual(result['status'], 'passed')
                self.assertNotIn(SECRET, json.dumps(result))
                self.assertNotIn(TOKEN, json.dumps(result))

    def test_no_keychain_export_operation(self):
        swift = SCRIPT.with_name('keychain.swift').read_text()
        self.assertNotIn('operation == "read"', swift)
        self.assertIn('kSecUseAuthenticationUIFail', swift)
        self.assertIn('LaunchConfig.files', swift)
        self.assertIn('LaunchConfig.tasks.contains', swift)

    def test_unpinned_script_argument_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            script = Path(tmp) / 'unreviewed.py'; script.write_text('pass')
            config = {'tasks': {'probe': {'authorization': 'test', 'source_revision': 'fixture',
                'argv': [str(TEST_PYTHON), '-I', str(script)], 'cwd': tmp,
                'reviewed_files': {str(TEST_PYTHON): runner.digest(str(TEST_PYTHON))}}}}
            with self.assertRaisesRegex(runner.Blocked, 'file_argument_not_pinned'):
                runner.execute(config, 'probe', TOKEN)

    def test_compiler_rejects_relative_python_script_and_inline_code(self):
        spec = importlib.util.spec_from_file_location('compiler', SCRIPT.with_name('compile_launcher.py'))
        compiler = importlib.util.module_from_spec(spec); spec.loader.exec_module(compiler)
        with tempfile.TemporaryDirectory() as tmp:
            child = Path(tmp) / 'child.py'; child.write_text('pass')
            executable = str(TEST_PYTHON)
            for argv in ([executable, '-I', 'child.py'], [executable, '-c', 'pass'], [executable, str(child)]):
                with self.assertRaises(ValueError):
                    compiler.validate_tasks({'tasks': {'x': {'argv':argv,'cwd':tmp,'reviewed_files':{executable:'pin'}}}})
            compiler.validate_tasks({'tasks': {'x': {'argv':[executable,'-I',str(child)],'cwd':tmp,
                'reviewed_files':{executable:'pin',str(child):'pin'}}}})

    def test_success_exit_without_fresh_evidence_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            child = Path(tmp) / 'empty.py'; child.write_text('pass')
            executable = str(TEST_PYTHON)
            config = {**cfg(), 'tasks': {'probe': {'authorization':'test','source_revision':'fixture',
                'argv':[executable,'-I',str(child)],'cwd':tmp,
                'reviewed_files':{executable:runner.digest(executable),str(child):runner.digest(child)},
                'result_contract':{'directory':tmp,'target':'fixture','checks':['scope']}}}}
            with patch.object(runner,'verify_identity'):
                with self.assertRaisesRegex(runner.Blocked,'fresh_task_evidence_missing'):
                    runner.execute(config,'probe',TOKEN)


if __name__ == '__main__':
    unittest.main()
