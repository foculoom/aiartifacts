import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, mkdirSync, writeFileSync, rmSync, symlinkSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { check } from './check.mjs';

function fixture(body = {}) {
  const root = mkdtempSync(join(tmpdir(), 'import-graph-'));
  const files = {
    'core/rules.mjs': 'export const answer = 42;\n',
    'adapter/index.mjs': "import { answer } from '../core/rules.mjs'; export { answer };\n",
    ...body,
  };
  for (const [name, source] of Object.entries(files)) {
    mkdirSync(dirname(join(root, name)), { recursive: true });
    writeFileSync(join(root, name), source);
  }
  const inventory = { version: 1, areas: [
    { id: 'core', files: Object.keys(files).filter(x => x.startsWith('core/')) },
    { id: 'adapter', files: Object.keys(files).filter(x => x.startsWith('adapter/')) },
  ] };
  const policy = { version: 1, review_gaps: ['Native imports require separate review.'],
    forbidden: [{ from: 'core', to: 'adapter' }], forbid_external_in: ['core'],
    excluded_extensions: [] };
  const save = () => {
    writeFileSync(join(root, 'architecture-inventory.json'), JSON.stringify(inventory));
    writeFileSync(join(root, 'architecture-imports.json'), JSON.stringify(policy));
  };
  save();
  return { root, files, inventory, policy, save, close: () => rmSync(root, { recursive: true, force: true }) };
}

function withFixture(body, run) {
  const f = fixture(body);
  try { run(f); } finally { f.close(); }
}

test('accepts an adapter importing pure rules', () => withFixture({}, f => {
  assert.equal(check(f.root).status, 'graph_passed');
}));

test('rejects inward boundary violation and cycle', () => withFixture({
  'core/rules.mjs': "import '../adapter/index.mjs'; export const answer = 42;\n",
}, f => {
  const found = check(f.root).findings.join('\n');
  assert.match(found, /forbidden core -> adapter/);
  assert.match(found, /cycle:/);
}));

test('reports literal and variable dynamic imports', () => withFixture({
  'core/rules.mjs': "export async function read(name) { return import(name); }\n",
  'adapter/dynamic.mjs': "export const read = () => import('../core/rules.mjs');\n",
}, f => {
  const found = check(f.root).findings.join('\n');
  assert.match(found, /dynamic or unsupported import/);
  assert.doesNotMatch(found, /adapter\/dynamic/);
}));

test('rejects variable require and unsupported import meta loader', () => withFixture({
  'core/rules.mjs': "const x = require(name); export const y = import.meta.glob('./*');\n",
}, f => {
  assert.equal(check(f.root).findings.filter(x => /dynamic or unsupported import/.test(x)).length, 2);
}));

test('reports invalid syntax instead of silently accepting it', () => withFixture({
  'core/rules.mjs': 'export const = 1;\n',
}, f => assert.match(check(f.root).findings.join('\n'), /invalid JavaScript/)));

test('rejects missing, ambiguous and external core imports', () => withFixture({
  'core/rules.mjs': "import './missing.mjs'; import './thing'; import 'node:crypto';\n",
  'core/thing.js': 'export const a=1;\n',
  'core/thing.mjs': 'export const b=2;\n',
}, f => {
  const found = check(f.root).findings.join('\n');
  assert.match(found, /missing.mjs resolves to 0 owned files/);
  assert.match(found, /thing resolves to 2 owned files/);
  assert.match(found, /external import node:crypto/);
}));

test('rejects an unowned imported file, not just a missing file', () => withFixture({
  'core/rules.mjs': "import './extra.mjs';\n",
  'core/extra.mjs': 'export const x=1;\n',
}, f => {
  f.inventory.areas[0].files = ['core/rules.mjs']; f.save();
  assert.match(check(f.root).findings.join('\n'), /extra.mjs resolves to 0 owned files/);
}));

test('rejects invalid profile references and symlink source', () => withFixture({}, f => {
  f.policy.forbidden = [{ from: 'missing', to: 'adapter' }]; f.save();
  assert.throws(() => check(f.root), /unknown area/);
  f.policy.forbidden = [{ from: 'core', to: 'adapter' }]; f.save();
  rmSync(join(f.root, 'core/rules.mjs'));
  symlinkSync(join(f.root, 'adapter/index.mjs'), join(f.root, 'core/rules.mjs'));
  assert.throws(() => check(f.root), /symlink unsupported/);
}));

test('requires newly classified source extensions to be explicit', () => withFixture({
  'core/settings.json': '{}',
}, f => {
  assert.throws(() => check(f.root), /unclassified source extension/);
  f.policy.excluded_extensions = ['.json']; f.save();
  assert.deepEqual(check(f.root).excluded, ['core/settings.json']);
}));

test('parses CommonJS and returns useful CLI exit codes', () => withFixture({
  'adapter/runtime.cjs': "return; const rules = require('../core/rules.mjs'); module.exports = rules;\n",
}, f => {
  assert.equal(check(f.root).status, 'graph_passed');
  const script = fileURLToPath(new URL('./check.mjs', import.meta.url));
  const passed = spawnSync(process.execPath, [script, '--root', f.root], { encoding: 'utf8' });
  assert.equal(passed.status, 0, passed.stderr || passed.stdout);
  f.files['core/rules.mjs'] = "import '../adapter/index.mjs';\n";
  writeFileSync(join(f.root, 'core/rules.mjs'), f.files['core/rules.mjs']);
  const failed = spawnSync(process.execPath, [script, '--root', f.root], { encoding: 'utf8' });
  assert.equal(failed.status, 1);
  assert.match(failed.stdout, /forbidden core -> adapter/);
}));
