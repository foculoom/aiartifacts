#!/usr/bin/env node
// Optional JS module graph guard. Inventory and product tests remain separate gates.
import { readFileSync, lstatSync } from 'node:fs';
import { resolve, extname, posix, sep } from 'node:path';
import { fileURLToPath } from 'node:url';
import { parse } from 'acorn';

const JS = new Set(['.js', '.mjs', '.cjs']);

function safeFile(root, name) {
  if (typeof name !== 'string' || !name || name.includes('\\') ||
      name.startsWith('/') || name.split('/').some(part => !part || part === '.' || part === '..')) {
    throw new Error(`invalid repository-relative path: ${name}`);
  }
  const file = resolve(root, name);
  if (file !== root && !file.startsWith(root + sep)) throw new Error(`path escapes root: ${name}`);
  let cursor = root;
  for (const part of name.split('/')) {
    cursor = resolve(cursor, part);
    if (lstatSync(cursor).isSymbolicLink()) throw new Error(`symlink unsupported: ${name}`);
  }
  return file;
}

function walk(node, visit) {
  if (!node || typeof node !== 'object') return;
  if (typeof node.type === 'string') visit(node);
  for (const value of Object.values(node)) {
    if (Array.isArray(value)) value.forEach(child => walk(child, visit));
    else if (value && typeof value === 'object') walk(value, visit);
  }
}

function imports(source, file) {
  const commonJs = extname(file) === '.cjs';
  const ast = parse(source, { ecmaVersion: 'latest', sourceType: commonJs ? 'script' : 'module',
    allowHashBang: true, allowReturnOutsideFunction: commonJs });
  const found = [];
  walk(ast, node => {
    if ((node.type === 'ImportDeclaration' || node.type === 'ExportNamedDeclaration' ||
         node.type === 'ExportAllDeclaration') && node.source) {
      found.push({ value: node.source.value, at: node.start });
    } else if (node.type === 'ImportExpression') {
      found.push({ value: node.source.type === 'Literal' ? node.source.value : null, at: node.start });
    } else if (node.type === 'CallExpression' && node.callee.type === 'Identifier' &&
               node.callee.name === 'require') {
      found.push({ value: node.arguments.length === 1 && node.arguments[0].type === 'Literal'
        ? node.arguments[0].value : null, at: node.start });
    } else if (node.type === 'CallExpression' && node.callee.type === 'MemberExpression' &&
               node.callee.object.type === 'MetaProperty' && node.callee.object.meta.name === 'import') {
      found.push({ value: null, at: node.start }); // import.meta.glob and similar loaders need review.
    }
  });
  return found;
}

function nonemptyStrings(value, field) {
  if (!Array.isArray(value) || !value.length || value.some(v => typeof v !== 'string' || !v.trim())) {
    throw new Error(`${field} must be a nonempty string list`);
  }
  return value;
}

function cycle(graph) {
  const active = new Set();
  const done = new Set();
  const stack = [];
  const cycles = new Set();
  function visit(file) {
    if (done.has(file)) return;
    active.add(file); stack.push(file);
    for (const next of graph.get(file) || []) {
      if (active.has(next)) {
        const start = stack.indexOf(next);
        cycles.add([...stack.slice(start), next].join(' -> '));
      } else visit(next);
    }
    stack.pop(); active.delete(file); done.add(file);
  }
  for (const file of graph.keys()) visit(file);
  return [...cycles].sort();
}

export function check(rootPath, inventoryName = 'architecture-inventory.json', policyName = 'architecture-imports.json') {
  const root = resolve(rootPath);
  const inventory = JSON.parse(readFileSync(safeFile(root, inventoryName), 'utf8'));
  const policy = JSON.parse(readFileSync(safeFile(root, policyName), 'utf8'));
  if (inventory.version !== 1 || policy.version !== 1) throw new Error('expected version 1 profiles');
  nonemptyStrings(policy.review_gaps, 'review_gaps');
  if (!Array.isArray(inventory.areas) || !inventory.areas.length) throw new Error('inventory areas required');
  if (!Array.isArray(policy.forbidden) || !policy.forbidden.length) {
    throw new Error('at least one forbidden rule required');
  }
  if (!Array.isArray(policy.forbid_external_in) || !policy.forbid_external_in.length) {
    throw new Error('at least one forbid_external_in area required');
  }
  if (!Array.isArray(policy.excluded_extensions) ||
      policy.excluded_extensions.some(x => typeof x !== 'string' || !x.startsWith('.'))) {
    throw new Error('explicit excluded_extensions required');
  }
  const owner = new Map();
  const areas = new Set();
  for (const area of inventory.areas) {
    if (!area.id || areas.has(area.id) || !Array.isArray(area.files)) throw new Error('invalid area');
    areas.add(area.id);
    for (const file of area.files) {
      safeFile(root, file);
      if (owner.has(file)) throw new Error(`duplicate ownership: ${file}`);
      owner.set(file, area.id);
    }
  }
  for (const rule of policy.forbidden) {
    if (!areas.has(rule.from) || !areas.has(rule.to)) throw new Error('forbidden rule references unknown area');
  }
  for (const area of policy.forbid_external_in) {
    if (!areas.has(area)) throw new Error('external rule references unknown area');
  }
  const findings = [];
  const graph = new Map();
  const excepted = (inventory.exceptions || []).map(item => item.file).sort();
  let checked = 0;
  const excluded = new Set();
  for (const [file, area] of owner) {
    if (!JS.has(extname(file))) {
      if (!policy.excluded_extensions.includes(extname(file))) {
        throw new Error(`unclassified source extension: ${file}`);
      }
      excluded.add(file);
      continue;
    }
    checked++;
    const dependencies = new Set();
    graph.set(file, dependencies);
    let found;
    try { found = imports(readFileSync(safeFile(root, file), 'utf8'), file); }
    catch (error) { findings.push(`${file}: unsupported or invalid JavaScript: ${error.message}`); continue; }
    for (const item of found) {
      const specifier = item.value;
      if (typeof specifier !== 'string' || !specifier) {
        findings.push(`${file}:${item.at}: dynamic or unsupported import`); continue;
      }
      if (specifier.startsWith('/') || specifier.includes('://')) {
        findings.push(`${file}: unsupported import: ${specifier}`); continue;
      }
      if (!specifier.startsWith('.')) {
        if (policy.forbid_external_in.includes(area)) findings.push(`${file}: external import ${specifier} in ${area}`);
        continue;
      }
      const target = posix.normalize(posix.join(posix.dirname(file), specifier));
      if (target.startsWith('../') || target === '..' || target.startsWith('/')) {
        findings.push(`${file}: import escapes repository: ${specifier}`); continue;
      }
      const candidates = [target, ...['.js', '.mjs', '.cjs', '.json'].map(ext => target + ext),
        ...['.js', '.mjs', '.cjs'].map(ext => target + '/index' + ext)];
      const matches = [...new Set(candidates.filter(name => owner.has(name)))];
      if (matches.length !== 1) {
        findings.push(`${file}: ${specifier} resolves to ${matches.length} owned files`); continue;
      }
      const imported = matches[0];
      if (policy.forbidden.some(rule => rule.from === area && rule.to === owner.get(imported))) {
        findings.push(`${file}: forbidden ${area} -> ${owner.get(imported)} import: ${imported}`);
      }
      if (JS.has(extname(imported))) dependencies.add(imported);
    }
  }
  for (const path of cycle(graph)) findings.push(`cycle: ${path}`);
  if (!checked) throw new Error('inventory has no JavaScript files');
  return { status: findings.length ? 'findings' : 'graph_passed', checked,
    excluded: [...excluded].sort(), excepted, findings,
    review_gaps: policy.review_gaps };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2);
  const value = key => {
    const index = args.indexOf(key);
    return index < 0 ? undefined : args[index + 1];
  };
  try {
    if (!args.includes('--root')) throw new Error('--root required');
    const result = check(value('--root'), value('--inventory') || undefined, value('--policy') || undefined);
    console.log(JSON.stringify(result, null, 2));
    process.exitCode = result.findings.length ? 1 : 0;
  } catch (error) {
    console.error(JSON.stringify({ status: 'invalid_profile', error: error.message }));
    process.exitCode = 2;
  }
}
