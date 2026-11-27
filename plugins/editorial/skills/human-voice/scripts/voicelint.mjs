#!/usr/bin/env node
// voicelint: flags stock AI wording and stiff formulas in user-facing copy.
// Dependency-free. Usage: node scripts/voicelint.mjs [--json] [--config path] [--no-allow]
// Config (voicelint.config.json at repo root): { include: [paths], exclude: [substrings], allow: [{file, contains, rule?, reason}] }
// This is a style lint, not an authorship test. See ../references/sources.md.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, relative, extname } from 'node:path';

const args = process.argv.slice(2);
const flag = (n) => args.includes(n);
const opt = (n, d) => (args.includes(n) ? args[args.indexOf(n) + 1] : d);
const root = process.cwd();
const configPath = opt('--config', join(root, 'voicelint.config.json'));
const config = existsSync(configPath) ? JSON.parse(readFileSync(configPath, 'utf8')) : { include: ['.'] };
const allow = flag('--no-allow') ? [] : config.allow || [];
const NAMES = [...(config.properNames || [])];
for (const src of config.properNamesFrom || []) { const f = join(root, src.file); if (existsSync(f)) for (const row of JSON.parse(readFileSync(f, 'utf8'))) for (const k of src.keys) if (typeof row[k] === 'string') NAMES.push(row[k]); }
NAMES.sort((a, b) => b.length - a.length);
const SKIP = ['node_modules', '/.git/', '/proof/', '/docs/', '/test/', '/tests/', '/pagefind/', ...(config.exclude || [])];
const EXT = new Set(['.html', '.mjs', '.js', '.json', '.md', '.txt', '.xml', '.webmanifest']);

const WORDS = [
  ['delve', /\bdelv(e|es|ed|ing)\b/i], ['elevate', /\belevat(e|es|ed|ing)\b/i], ['seamless', /\bseamless(ly)?\b/i],
  ['unlock', /\bunlock(s|ed|ing)?\b/i], ['unleash', /\bunleash(es|ed|ing)?\b/i], ['empower', /\bempower(s|ed|ing|ment)?\b/i],
  ['curated', /\bcurat(ed|es|ing|ion)\b/i], ['tailored', /\btailor(ed|s|ing)?\b/i], ['robust', /\brobust(ly|ness)?\b/i],
  ['leverage', /\bleverag(e|es|ed|ing)\b/i], ['journey', /\bjourney(s)?\b/i], ['realm', /\brealm(s)?\b/i],
  ['embark', /\bembark(s|ed|ing)?\b/i], ['navigate the', /\bnavigat(e|es|ing) the\b/i], ["in today's", /\bin today[’']s\b/i],
  ['ever-evolving', /\bever[- ]evolving\b/i], ['game-changer', /\bgame[- ]chang(er|ers|ing)\b/i],
  ['effortless(ly)', /\beffortless(ly)?\b/i], ['dive in', /\bdiv(e|ing) (in|into|deep)\b/i], ['look no further', /\blook no further\b/i],
  ["whether you're", /\bwhether you[’']?re\b/i], ['crafted', /\bcrafted\b/i], ['meticulous', /\bmeticulous(ly)?\b/i],
  ['testament', /\btestament\b/i], ['tapestry', /\btapestry\b/i], ['supercharge', /\bsupercharg(e|es|ed|ing)\b/i],
  ['transform your', /\btransform(s|ing)? your\b/i],
  // small extras of the same family
  ['harness', /\bharness(es|ed|ing)?\b/i], ['streamline', /\bstreamlin(e|es|ed|ing)\b/i], ['cutting-edge', /\bcutting[- ]edge\b/i],
  ['revolutionize', /\brevolutioniz(e|es|ed|ing)\b/i], ['plethora/myriad', /\b(plethora|myriad)\b/i],
  ['more than just', /\bmore than (just|simply|only)\b/i], ['next level', /\bto the next level\b/i],
  ['say goodbye', /\bsay goodbye to\b/i], ['perfect blend', /\b(perfect|seamless) (blend|mix|fusion)\b/i],
  ['genuinely', /\bgenuinely\b/i], ['comprehensive', /\bcomprehensive(ly)?\b/i], ['utilize', /\butili[sz](e|es|ed|ing)\b/i],
  ['perfect/ideal for', /\b(perfect|ideal) for\b/i], ['feel free', /\bfeel free\b/i], ['stay informed', /\bstay (informed|ahead)\b/i],
  ['all-in-one', /\ball-in-one\b|\bone-stop\b/i], ['peace of mind', /\bpeace of mind\b/i], ['hassle-free', /\b(hassle|stress)-free\b/i],
  ['brings together', /\bbrings\b[^.]{0,60}\btogether\b/i], ['convene', /\bconvenes?\b/i], ['gathers', /\bgathers\b/i],
  ['at the end of the day', /\bat the end of the day\b/i], ['stand out', /\bstand(s)? out from the crowd\b/i],
];
const NOT_JUST = /\b(?:not|isn[’']t|aren[’']t|wasn[’']t|doesn[’']t|don[’']t|never)\s+(?:just|only|merely|simply)\b[^.!?]{1,80}?(?:[,;:–—-]|\.\.\.)\s*(?:but\s+|it[’']?s\b|it is\b|they[’']?re\b|this is\b|that[’']?s\b)/i;
const NOT_ABOUT = /\bit[’']?s not about\b[^.!?]{1,80}[,;–—-]\s*it[’']?s about\b/i;
const SMALL = new Set('a an the of and or for to in on with at by from as vs via into your our is it no not'.split(' '));
const THREE = /\b([a-z]{3,14}), ([a-z]{3,14}),? (?:and|or) ([a-z]{3,14})\b/gi;
// Rule-of-three padding = a triple where at least two items are vague quality words. Concrete lists (coffee, tea and cocoa) are fine.
const VAGUE = new Set(('fast quick simple easy effortless reliable powerful flexible intuitive modern clean smart thoughtful meaningful personal practical playful beautiful stylish innovative engaging exciting fresh bold unique special memorable cozy comfortable helpful useful fun creative inspiring effective efficient secure safe trusted accurate clear honest transparent sleek lasting premium quality value convenience comfort style joy connection speed ease clarity confidence focus control growth creativity productivity innovation performance flexibility simplicity reliability security privacy trust warmth charm character personality heart soul meaning magic wonder delight beauty').split(' '));

const BLOCK = new Set('span p div li ul ol h1 h2 h3 h4 h5 h6 td th tr table section article main nav header footer aside title button summary details dt dd blockquote figcaption label option select form body head html br hr noscript'.split(' '));
const HEAD = new Set(['title', 'h1', 'h2', 'h3', 'button']);
const ATTRS = ['alt', 'aria-label', 'title', 'placeholder', 'content', 'value'];

function* walk(p) {
  const full = join(root, p);
  if (!existsSync(full)) return;
  const st = statSync(full);
  const rel = '/' + relative(root, full) + (st.isDirectory() ? '/' : '');
  if (SKIP.some((s) => rel.includes(s))) return;
  if (st.isDirectory()) { for (const n of readdirSync(full).sort()) yield* walk(join(p, n)); return; }
  if (EXT.has(extname(full)) && !/package(-lock)?\.json$|voicelint\.config\.json$|wrangler|site-standards|architecture|\.generated\./.test(full)) yield relative(root, full);
}

const decode = (s) => s.replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&quot;/g, '"').replace(/&#0?39;|&apos;|&rsquo;|&lsquo;/g, "'").replace(/&mdash;/g, '—').replace(/&ndash;/g, '–').replace(/&nbsp;|&middot;/g, ' ').replace(/&#(\d+);/g, (_, n) => String.fromCharCode(+n));
const lineAt = (src, idx) => src.slice(0, idx).split('\n').length;

// Returns [{text, line, kind}] copy segments for a file.
function segments(file, src) {
  const out = [];
  const ext = extname(file);
  if (ext === '.html' || ext === '.xml') {
    let i = 0; let cur = ''; let curLine = 0; let kind = 'text'; const stack = [];
    const flush = () => { const t = decode(cur.replace(/\s+/g, ' ').trim()); if (t) out.push({ text: t, line: curLine, kind }); cur = ''; curLine = 0; kind = 'text'; };
    const re = /<!--[\s\S]*?-->|<(script|style)\b([^>]*)>([\s\S]*?)<\/\1>|<(\/?)([a-zA-Z][\w:-]*)([^>]*)>|([^<]+)/g;
    let m;
    while ((m = re.exec(src))) {
      if (m[1]) {
        if (/ld\+json/.test(m[2])) for (const s of m[3].matchAll(/"(?:name|description|headline|text|title)"\s*:\s*"((?:\\.|[^"\\])+)"/g)) out.push({ text: decode(s[1]), line: lineAt(src, m.index + m[0].indexOf(s[0])), kind: 'text' });
        continue;
      }
      if (m[5]) {
        const closing = m[4] === '/'; const tag = m[5].toLowerCase();
        if (!closing) for (const a of m[6].matchAll(/\s([\w:-]+)\s*=\s*("([^"]*)"|'([^']*)')/g)) {
          const name = a[1].toLowerCase(); const v = decode(a[3] ?? a[4]);
          const isMeta = tag === 'meta' && name === 'content' && /name=["'](description|twitter:(title|description))|property=["']og:(title|description)/.test(m[6]);
          if ((ATTRS.includes(name) && name !== 'content' && name !== 'value' && /[a-z]{3,}\s+[a-z]/i.test(v)) || isMeta) out.push({ text: v, line: lineAt(src, m.index), kind: isMeta && /title/.test(m[6]) ? 'head' : 'text' });
        }
        if (BLOCK.has(tag)) { flush(); }
        if (!closing && HEAD.has(tag)) { stack.push(tag); }
        if (closing && stack.length && stack[stack.length - 1] === tag) stack.pop();
        continue;
      }
      if (m[7]) {
        if (!cur.trim() && m[7].trim()) { curLine = lineAt(src, m.index + m[7].search(/\S/)); kind = stack.length ? 'head' : 'text'; }
        cur += m[7];
      }
    }
    flush();
    return out;
  }
  // js/json/md/txt: per-line string literals (js, json) or whole lines (md, txt)
  const lines = src.split('\n');
  lines.forEach((ln, idx) => {
    if (ext === '.md' || ext === '.txt') { if (ln.trim()) out.push({ text: ln.trim(), line: idx + 1, kind: /^#/.test(ln) ? 'head' : 'text' }); return; }
    if (/^\s*(import|export \{|\/\/)/.test(ln)) return;
    for (const m of ln.matchAll(/(["'`])((?:\\.|(?!\1).)*)\1/g)) {
      const raw = m[2].replace(/\\(["'`])/g, '$1');
      for (const h of raw.matchAll(/<(h[1-3]|title|button)\b[^>]*>([^<]+)</g)) { const ht = decode(h[2]).replace(/\$\{[^}]*\}/g, ' ').replace(/\s+/g, ' ').trim(); if (ht.length > 5) out.push({ text: ht, line: idx + 1, kind: 'head' }); }
      let t = raw.replace(/<[^>]+>/g, ' ');
      t = decode(t).replace(/\$\{[^}]*\}/g, ' ').replace(/\s+/g, ' ').trim();
      if (t.length < 8 || !/[A-Za-z]{3,} [A-Za-z]{2,}|[A-Za-z]{5,}/.test(t)) continue;
      if (/^(https?:|\/|\.|#|[\w-]+\/[\w./-]+$|[a-z-]+$)/.test(t) && !/\s/.test(t)) continue;
      const keyed = /(title|headline|heading|tagline|slogan|cta|button|h1)["']?\s*:\s*$/i.test(ln.slice(0, m.index));
      out.push({ text: t, line: idx + 1, kind: keyed ? 'head' : 'text' });
    }
  });
  return out;
}

function check(seg) {
  const flags = [];
  const { text, kind } = seg;
  for (const [name, re] of WORDS) if (re.test(text)) flags.push({ rule: 'word:' + name, why: `stock AI word/phrase "${name}"` });
  if (NOT_JUST.test(text) || NOT_ABOUT.test(text)) flags.push({ rule: 'formula:not-just', why: '"not just X, it\'s Y" formula' });
  if (kind === 'head') for (const rawPiece of text.split(/\s[|·—]\s|\s[-–]\s/)) {
    let piece = rawPiece; for (const n of NAMES) piece = piece.split(n).join(' ');
    piece = piece.replace(/\s+/g, ' ').trim();
    const words = piece.split(/\s+/).filter(Boolean);
    if (words.length < 3 || words.length > 9 || /[.!?:]$/.test(piece)) continue;
    const sig = words.filter((w) => !SMALL.has(w.toLowerCase().replace(/[^a-z]/g, '')) && /[A-Za-z]/.test(w));
    const names = false;
    if (!names && sig.length >= 3 && sig.every((w) => /^[A-Z$"“(]/.test(w))) flags.push({ rule: 'formula:title-case-slogan', why: 'Title Case Slogan (every word capitalised)' });
  }
  for (const m of text.matchAll(THREE)) {
    const t = [m[1], m[2], m[3]].map((w) => w.toLowerCase());
    if (t.filter((w) => VAGUE.has(w)).length >= 2) flags.push({ rule: 'formula:rule-of-three', why: `rule-of-three list "${m[0]}"` });
  }
  if (/!{2,}|!\s*[^!\n]{0,120}!/.test(text) && (text.match(/!/g) || []).length >= 2) flags.push({ rule: 'formula:exclamation-stack', why: 'two or more exclamation marks close together' });
  const dashes = (text.match(/—/g) || []).length;
  if (dashes >= 2) flags.push({ rule: 'formula:em-dash', why: `${dashes} em dashes in one ${kind === 'head' ? 'heading/title' : 'passage'}` });
  return flags;
}

const results = []; let files = 0; const totals = { all: 0, allowed: 0 };
const fileDash = [];
for (const inc of config.include || ['.']) for (const f of walk(inc)) {
  files++;
  const src = readFileSync(join(root, f), 'utf8');
  const segs = segments(f, src);
  if (flag('--dump')) { for (const g of segs) console.log(`${f}:${g.line}\t${g.kind}\t${g.text}`); continue; }
  let chars = 0; let dashes = 0;
  for (const seg of segs) {
    chars += seg.text.length; dashes += (seg.text.match(/—/g) || []).length;
    for (const fl of check(seg)) {
      const a = allow.find((x) => x.file === f && seg.text.includes(x.contains) && (!x.rule || fl.rule.startsWith(x.rule)));
      totals.all++;
      if (a) { totals.allowed++; continue; }
      results.push({ file: f, line: seg.line, rule: fl.rule, why: fl.why, text: seg.text.length > 220 ? seg.text.slice(0, 217) + '...' : seg.text });
    }
  }
  if (dashes >= 4 && dashes / Math.max(chars, 1) > 1 / 700) {
    const a = allow.find((x) => x.file === f && x.rule === 'formula:em-dash-density');
    totals.all++;
    if (a) totals.allowed++; else results.push({ file: f, line: 1, rule: 'formula:em-dash-density', why: `${dashes} em dashes in ${chars} chars of copy`, text: '(file level)' });
  }
}
if (flag('--json')) console.log(JSON.stringify({ files, flags: results, allowed: totals.allowed }, null, 2));
else {
  for (const r of results) console.log(`${r.file}:${r.line}  [${r.rule}]  ${r.why}\n    ${r.text}`);
  console.log(`voicelint: ${files} files, ${results.length} flag(s)${totals.allowed ? `, ${totals.allowed} allowlisted (with reasons in voicelint.config.json)` : ''}`);
}
process.exit(results.length ? 1 : 0);
