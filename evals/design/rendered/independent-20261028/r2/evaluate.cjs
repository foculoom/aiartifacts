const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const crypto = require('node:crypto');
const { chromium } = require('/PLAYWRIGHT_PACKAGE');
const root = '/EVALUATOR_PACKETS/r2';
const out = __dirname;
const results = { evaluator: 'Codex agent evaluation', model: 'unknown: exact runtime model identifier not exposed', startedAt: new Date().toISOString(), node: process.version, playwright: require('/PLAYWRIGHT_PACKAGE/package.json').version, checks: [], errors: [], blockedRequests: [] };
const prov = JSON.parse(fs.readFileSync(path.join(root, 'provenance.json'), 'utf8'));
results.sourceCommit = prov.sourceCommit;
results.identity = {};
for (const file of ['fixtures/r2.html', 'fixtures/fixture.js', 'fixtures/style.css', 'skills/product-identity/SKILL.md', 'skills/experience-review/SKILL.md', 'skills/experience-review/references/interactive-experiences.md', 'skills/experience-review/references/production-acceptance.md']) {
  const sha256 = crypto.createHash('sha256').update(fs.readFileSync(path.join(root, file))).digest('hex');
  results.identity[file] = { sha256, matchesProvenance: sha256 === prov.inputHashes[file] };
}
const server = http.createServer((req, res) => {
  const name = new URL(req.url, 'http://localhost').pathname.slice(1);
  if (!['r2.html','style.css','fixture.js'].includes(name)) { res.writeHead(404); res.end(); return; }
  res.setHeader('Content-Type', name.endsWith('.html') ? 'text/html' : name.endsWith('.css') ? 'text/css' : 'text/javascript');
  res.end(fs.readFileSync(path.join(root,'fixtures',name)));
});
const state = async (page) => page.evaluate(() => {
  const bounds = selector => { const e=document.querySelector(selector); const b=e.getBoundingClientRect(), c=getComputedStyle(e); return { x:b.x,y:b.y,width:b.width,height:b.height,color:c.color,background:c.backgroundColor,fontSize:c.fontSize,opacity:c.opacity,outline:c.outline,transition:c.transition,transform:c.transform }; };
  return { artifact:document.querySelector('#app').dataset.artifact, documentWidth:document.documentElement.scrollWidth, viewportWidth:innerWidth, status:document.querySelector('#status').textContent, focus:document.activeElement.id, courierClass:document.querySelector('.courier').className, components:Object.fromEntries(['.promotion','.courier','.dock','.parcel-world','.parcel-world small','#deliver','#reset','#status','header'].map(s=>[s,bounds(s)])) };
});
(async () => {
  await new Promise(resolve => server.listen(0,'127.0.0.1',resolve));
  const base = `http://127.0.0.1:${server.address().port}`;
  results.url = `${base}/r2.html`;
  const browser = await chromium.launch({ executablePath:'/CHROMIUM_EXECUTABLE', headless:true });
  results.browser = await browser.version();
  try {
    for (const width of [1280,390]) {
      const context = await browser.newContext({ viewport:{width,height:900}, hasTouch:width===390 });
      await context.route('**/*', route => { if (route.request().url().startsWith(base + '/')) return route.continue(); results.blockedRequests.push(route.request().url()); return route.abort(); });
      const page = await context.newPage();
      page.on('pageerror', error => results.errors.push(String(error)));
      await page.goto(results.url);
      const check={ viewport:{width,height:900}, input:width===1280?'keyboard: Tab, Enter, Tab, Space':'browser-emulated touchscreen taps', states:[] };
      check.states.push({ action:'direct-entry', value:await state(page) });
      await page.screenshot({ path:path.join(out,`actual-ready-${width}.png`) });
      if(width===1280){ await page.keyboard.press('Tab'); check.states.push({action:'Tab from initial document',value:await state(page)}); await page.screenshot({path:path.join(out,'actual-focus-1280.png')}); await page.keyboard.press('Enter'); }
      else await page.locator('#deliver').tap();
      await page.waitForTimeout(70);
      check.states.push({action:'Deliver during transition (approximately 70ms after action)',value:await state(page)});
      await page.screenshot({path:path.join(out,`actual-transition-${width}.png`)});
      await page.waitForTimeout(250);
      check.states.push({ action:'Deliver settled',value:await state(page) });
      await page.screenshot({path:path.join(out,`actual-delivered-${width}.png`)});
      if(width===1280) await page.keyboard.press('Enter'); else await page.locator('#deliver').tap();
      check.states.push({action:'Repeat Deliver',value:await state(page)});
      if(width===1280){ await page.keyboard.press('Tab'); check.states.push({action:'Tab to Reset',value:await state(page)}); await page.keyboard.press('Space'); }
      else await page.locator('#reset').tap();
      await page.waitForTimeout(250);
      check.states.push({action:'Reset settled',value:await state(page)});
      await page.screenshot({path:path.join(out,`actual-reset-${width}.png`)});
      await page.reload();
      check.states.push({action:'Reload after reset',value:await state(page)});
      results.checks.push(check);
      await context.close();
    }
    const reduced = await browser.newContext({viewport:{width:390,height:900},reducedMotion:'reduce'});
    await reduced.route('**/*',route=>route.request().url().startsWith(base+'/')?route.continue():route.abort());
    const page=await reduced.newPage(); await page.goto(results.url); await page.locator('#deliver').click();
    results.reducedMotion={input:'pointer click in emulated reduced-motion context',state:await state(page)};
    await reduced.close();
  } finally { await browser.close(); server.close(); results.completedAt = new Date().toISOString(); fs.writeFileSync(path.join(out,'action-receipts.json'),JSON.stringify(results,null,2)); }
  console.log(JSON.stringify({completedAt:results.completedAt,browser:results.browser,errors:results.errors,output:out},null,2));
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
