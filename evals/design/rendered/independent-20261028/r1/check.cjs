const fs = require('fs');
const path = require('path');
const http = require('http');
const crypto = require('crypto');
const { chromium } = require('/PLAYWRIGHT_PACKAGE');

const packet = path.resolve(__dirname, '../r1');
const fixtureDir = path.join(packet, 'fixtures');
const record = { label: 'Independent agent evaluation', observedAt: new Date().toISOString(), model: 'Exact model identifier unknown; Codex agent based on GPT-6 per environment', node: process.version, playwright: require('/PLAYWRIGHT_PACKAGE/package.json').version, viewports: [], errors: [], inputHashes: {} };
for (const name of ['r1.html','fixture.js','style.css']) record.inputHashes[name] = crypto.createHash('sha256').update(fs.readFileSync(path.join(fixtureDir,name))).digest('hex');
const server = http.createServer((req, res) => {
  const filename = req.url.split('?')[0].replace(/^\//, '');
  if (!['r1.html','fixture.js','style.css'].includes(filename)) { res.writeHead(404); res.end(); return; }
  res.setHeader('Content-Type', filename.endsWith('.html') ? 'text/html' : filename.endsWith('.js') ? 'text/javascript' : 'text/css');
  res.end(fs.readFileSync(path.join(fixtureDir, filename)));
});
const snapshot = async (page, action) => ({ action, ...(await page.evaluate(() => ({
  artifact: document.querySelector('#app').dataset.artifact,
  status: document.querySelector('#status').textContent,
  beds: [...document.querySelectorAll('.garden span')].map(el=>el.textContent),
  focus: document.activeElement.id || document.activeElement.tagName,
  documentWidth: document.documentElement.scrollWidth,
  viewportWidth: innerWidth,
  buttons: [...document.querySelectorAll('button')].map(el=>({ id:el.id, text:el.textContent, hidden:el.hidden, disabled:el.disabled, ariaDisabled:el.getAttribute('aria-disabled'), tabIndex:el.tabIndex, rect:{x:el.getBoundingClientRect().x,y:el.getBoundingClientRect().y,width:el.getBoundingClientRect().width,height:el.getBoundingClientRect().height}, focusVisible:el.matches(':focus-visible') }))
}))) });
(async () => {
  await new Promise(resolve => server.listen(0, '127.0.0.1', resolve));
  const url = `http://127.0.0.1:${server.address().port}/r1.html`;
  record.url = url;
  let browser;
  try {
    browser = await chromium.launch({executablePath:'/CHROMIUM_EXECUTABLE',headless:true,args:['--disable-background-networking','--disable-component-update','--no-first-run']});
    record.browser = await browser.version();
    for (const width of [1280,390]) {
      const context = await browser.newContext({ viewport:{width,height:900} });
      await context.route('**/*',route=>route.request().url().startsWith(`http://127.0.0.1:${server.address().port}/`) ? route.continue() : route.abort());
      const page = await context.newPage();
      page.on('pageerror',error=>record.errors.push({width,error:error.message}));
      await page.goto(url);
      const lane = {width,height:900,input:'Browser mouse click',events:[]};
      record.viewports.push(lane);
      lane.events.push(await snapshot(page,'Direct entry'));
      await page.screenshot({path:path.join(__dirname,`start-${width}.png`),fullPage:true});
      for (const id of ['water','overview','undo','restart']) { await page.locator('#'+id).click(); lane.events.push(await snapshot(page,'Starting: click '+id)); }
      await page.locator('#start').click(); lane.events.push(await snapshot(page,'Click Start'));
      await page.locator('#undo').click(); lane.events.push(await snapshot(page,'Active with empty history: click Undo'));
      await page.locator('#water').click(); lane.events.push(await snapshot(page,'Active: click Water once'));
      await page.screenshot({path:path.join(__dirname,`active-${width}.png`),fullPage:true});
      await page.locator('#water').click(); lane.events.push(await snapshot(page,'Active: repeat Water'));
      await page.locator('#overview').click(); lane.events.push(await snapshot(page,'Click Overview'));
      await page.screenshot({path:path.join(__dirname,`overview-${width}.png`),fullPage:true});
      await page.locator('#water').click(); lane.events.push(await snapshot(page,'Overview: click Water'));
      await page.locator('#undo').click(); lane.events.push(await snapshot(page,'Overview: click Undo'));
      await page.screenshot({path:path.join(__dirname,`overview-undo-${width}.png`),fullPage:true});
      await page.locator('#restart').click(); lane.events.push(await snapshot(page,'Overview: click Restart'));
      await page.locator('#undo').click(); lane.events.push(await snapshot(page,'Overview: Undo Restart'));
      await page.locator('#overview').click(); lane.events.push(await snapshot(page,'Click Resume'));
      await page.locator('#water').click(); lane.events.push(await snapshot(page,'Active: Water after resume'));
      await page.locator('#undo').click(); lane.events.push(await snapshot(page,'Recovery: Undo Water'));
      await page.screenshot({path:path.join(__dirname,`recovery-${width}.png`),fullPage:true});
      await page.locator('#restart').click(); lane.events.push(await snapshot(page,'Active: Restart'));
      await page.locator('#undo').click(); lane.events.push(await snapshot(page,'Active: Undo Restart'));
      for (let n=0;n<3;n++) { await page.locator('#water').click(); lane.events.push(await snapshot(page,`Active: water toward/at cap, click ${n+1}`)); }
      await page.screenshot({path:path.join(__dirname,`cap-${width}.png`),fullPage:true});
      await page.reload(); lane.events.push(await snapshot(page,'Reload after play'));
      const keyboard = {width,height:900,input:'Browser keyboard Tab, Enter, Space',events:[]};
      record.viewports.push(keyboard);
      for(let n=0;n<5;n++) {await page.keyboard.press('Tab'); keyboard.events.push(await snapshot(page,`Starting Tab ${n+1}`));}
      await page.reload(); await page.keyboard.press('Tab'); await page.keyboard.press('Enter');
      keyboard.events.push(await snapshot(page,'Tab to Start, Enter'));
      await page.keyboard.press('Tab'); keyboard.events.push(await snapshot(page,'Tab after Start'));
      await page.screenshot({path:path.join(__dirname,`keyboard-focus-${width}.png`),fullPage:true});
      await page.keyboard.press('Space'); keyboard.events.push(await snapshot(page,'Space on Water'));
      await page.keyboard.press('Enter'); keyboard.events.push(await snapshot(page,'Enter on Water'));
      await page.keyboard.press('Tab'); await page.keyboard.press('Enter'); keyboard.events.push(await snapshot(page,'Tab to Overview, Enter'));
      await page.keyboard.press('Shift+Tab'); await page.keyboard.press('Space'); keyboard.events.push(await snapshot(page,'Overview: Shift+Tab to Water, Space'));
      await page.keyboard.press('Tab'); await page.keyboard.press('Tab'); await page.keyboard.press('Enter'); keyboard.events.push(await snapshot(page,'Overview: Tab to Undo, Enter'));
      await page.keyboard.press('Shift+Tab'); await page.keyboard.press('Space'); keyboard.events.push(await snapshot(page,'Shift+Tab to Resume, Space'));
      await page.keyboard.press('Tab'); await page.keyboard.press('Tab'); await page.keyboard.press('Enter'); keyboard.events.push(await snapshot(page,'Tab to Restart, Enter'));
      await page.keyboard.press('Shift+Tab'); await page.keyboard.press('Space'); keyboard.events.push(await snapshot(page,'Shift+Tab to Undo, Space'));
      await context.close();
    }
    const context = await browser.newContext({viewport:{width:390,height:900},hasTouch:true,isMobile:true,deviceScaleFactor:1});
    await context.route('**/*',route=>route.request().url().startsWith(`http://127.0.0.1:${server.address().port}/`) ? route.continue() : route.abort());
    const page=await context.newPage(); await page.goto(url);
    const touch={width:390,height:900,input:'Browser-emulated touchscreen tap; no physical device',events:[await snapshot(page,'Direct entry')]}; record.viewports.push(touch);
    for (const id of ['water','start','water','water','overview','water','undo','overview','restart','undo']) {await page.locator('#'+id).tap(); touch.events.push(await snapshot(page,'Tap '+id));}
    await context.close();
    record.finishedAt=new Date().toISOString();
  } catch(error) {record.fatalError=error.stack; process.exitCode=1;}
  finally {if(browser) await browser.close(); server.close(); fs.writeFileSync(path.join(__dirname,'action-receipts.json'),JSON.stringify(record,null,2));}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
