const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const crypto = require('node:crypto');
const { chromium } = require('/PLAYWRIGHT_PACKAGE');

const packet = '/EVALUATOR_PACKETS/r3';
const out = __dirname;
const receipts = { evaluation: 'agent evaluation', startedAt: new Date().toISOString(), model: 'Exact model identifier not exposed', tools: ['functions.exec', 'exec_command', 'Playwright', 'headless Chrome'], node: process.version, playwright: require('/PLAYWRIGHT_PACKAGE/package.json').version, runs: [], errors: [] };
const provenance = JSON.parse(fs.readFileSync(path.join(packet, 'provenance.json'), 'utf8'));
receipts.sourceCommit = provenance.sourceCommit;
receipts.artifact = 'L3';
receipts.verifiedHashes = {};
for (const file of ['fixtures/r3.html', 'fixtures/style.css', 'fixtures/fixture.js', 'skills/experience-review/SKILL.md', 'skills/experience-review/references/interactive-experiences.md']) {
  const sha256 = crypto.createHash('sha256').update(fs.readFileSync(path.join(packet, file))).digest('hex');
  receipts.verifiedHashes[file] = { sha256, matchesProvenance: sha256 === provenance.inputHashes[file] };
}
const allowed = new Set(['r3.html', 'style.css', 'fixture.js']);
const server = http.createServer((req, res) => {
  const file = new URL(req.url, 'http://127.0.0.1').pathname.slice(1);
  if (!allowed.has(file)) { res.writeHead(404); res.end(); return; }
  res.setHeader('Content-Type', file.endsWith('.html') ? 'text/html' : file.endsWith('.css') ? 'text/css' : 'text/javascript');
  res.end(fs.readFileSync(path.join(packet, 'fixtures', file)));
});
async function snapshot(page) {
  return page.evaluate(() => {
    const room = document.querySelector('#room'), dialog = document.querySelector('dialog');
    const box = el => { const r = el.getBoundingClientRect(); const c = getComputedStyle(el); return { x: r.x, y: r.y, width: r.width, height: r.height, color: c.color, background: c.backgroundColor, font: c.font, outline: c.outline, outlineOffset: c.outlineOffset }; };
    return { artifact: document.querySelector('#app').dataset.artifact, viewport: { width: innerWidth, height: innerHeight }, documentWidth: document.documentElement.scrollWidth, selection: room.value, reserveDisabled: document.querySelector('#reserve').disabled, dialogOpen: dialog.open, dialogSelection: document.querySelector('#selection').textContent, focus: document.activeElement.id || document.activeElement.tagName, status: document.querySelector('#status').textContent, body: box(document.body), room: box(room), reserve: box(document.querySelector('#reserve')), help: box(document.querySelector('#help')), cancel: box(document.querySelector('#cancel')), dialog: box(dialog), dialogName: dialog.getAttribute('aria-labelledby'), roomLabel: room.labels[0]?.textContent, motion: getComputedStyle(document.querySelector('#app')).animationName };
  });
}
async function main() {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  receipts.url = `${base}/r3.html`;
  let browser;
  try {
    browser = await chromium.launch({ executablePath: '/CHROMIUM_EXECUTABLE', headless: true, args: ['--no-sandbox'] });
    receipts.browser = browser.version();
    for (const width of [1280, 390]) {
      const context = await browser.newContext({ viewport: { width, height: 900 }, reducedMotion: 'reduce' });
      await context.route('**/*', route => new URL(route.request().url()).origin === base ? route.continue() : route.abort());
      const page = await context.newPage();
      const run = { viewport: { width, height: 900 }, inputEnvironment: 'Headless desktop browser with viewport emulation; not a physical device', actions: [], consoleErrors: [], requests: [] };
      receipts.runs.push(run);
      page.on('pageerror', error => run.consoleErrors.push(String(error)));
      page.on('request', request => run.requests.push({ method: request.method(), url: request.url() }));
      const record = async action => { const state = await snapshot(page); run.actions.push({ action, state }); return state; };
      await page.goto(`${base}/r3.html`, { waitUntil: 'networkidle' });
      await record('Direct entry with no selection');
      await page.screenshot({ path: path.join(out, `start-${width}.png`), fullPage: true });
      await page.getByRole('button', { name: 'Help', exact: true }).click();
      await record('Pointer click Help');
      await page.screenshot({ path: path.join(out, `help-${width}.png`), fullPage: true });
      await page.reload({ waitUntil: 'networkidle' });
      await page.keyboard.press('Tab');
      await record('Keyboard Tab from fresh entry reaches room selector');
      await page.keyboard.press('ArrowDown');
      await page.keyboard.press('Enter');
      const keyboardSelection = await record('Keyboard ArrowDown and Enter attempt to commit Window room');
      if (keyboardSelection.selection !== 'Window room') {
        run.keyboardSelectionLimit = 'ArrowDown then Enter did not commit Window room in this headless run; native select popup keyboard selection remains unverified.';
        await page.locator('#room').selectOption({ label: 'Window room' });
        await record('Playwright native-select selection of Window room');
      }
      await page.keyboard.press('Tab');
      await record('Keyboard Tab reaches enabled review button');
      await page.screenshot({ path: path.join(out, `selection-${width}.png`), fullPage: true });
      await page.keyboard.press('Enter');
      await record('Keyboard Enter on review opens dialog');
      await page.screenshot({ path: path.join(out, `dialog-${width}.png`), fullPage: true });
      await page.keyboard.press('Tab');
      await record('Tab while dialog is open');
      await page.keyboard.press('Tab');
      await record('Second Tab while dialog is open');
      await page.keyboard.press('Shift+Tab');
      await record('Shift+Tab while dialog is open');
      await page.locator('#cancel').click();
      await record('Pointer click Back to selection');
      await page.screenshot({ path: path.join(out, `return-${width}.png`), fullPage: true });
      await page.locator('#reserve').click();
      await record('Pointer click review again');
      await page.keyboard.press('Escape');
      await record('Escape closes dialog and preserves selection');
      await page.locator('#room').selectOption({ label: 'Courtyard room' });
      await record('Playwright native-select selection of Courtyard room');
      await page.locator('#reserve').click();
      await record('Pointer review of second room');
      await page.locator('#cancel').press('Enter');
      await record('Keyboard Enter on Back to selection');
      await page.locator('#room').selectOption('');
      await record('Playwright native-select reset to placeholder');
      run.accessibilitySnapshot = await page.locator('body').ariaSnapshot();
      await context.close();
    }
  } catch (error) { receipts.errors.push(String(error.stack || error)); throw error; }
  finally {
    receipts.finishedAt = new Date().toISOString();
    fs.writeFileSync(path.join(out, 'action-receipts.json'), JSON.stringify(receipts, null, 2));
    if (browser) await browser.close();
    await new Promise(resolve => server.close(resolve));
  }
}
main().catch(error => { console.error(error); process.exitCode = 1; });
