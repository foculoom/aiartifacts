// Optional local render/interaction verification. Uses an already installed Playwright.
import {createServer} from 'node:http';
import {createHash} from 'node:crypto';
import {readFile,mkdir,writeFile,readdir} from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createRequire} from 'node:module';
import assert from 'node:assert/strict';
const require=createRequire(import.meta.url);
const dependency=process.env.PLAYWRIGHT_MODULE||'playwright';
const {chromium}=require(dependency);
const root=path.dirname(fileURLToPath(import.meta.url)),fixtures=path.join(root,'fixtures');
if(process.argv.length!==4||process.argv[2]!=='--output')throw Error('Usage: node run.mjs --output NEW_DIRECTORY');
const output=path.resolve(process.argv[3]);
await mkdir(output,{recursive:false}); // Refuse to reuse evidence from an earlier run.
const names=await readdir(fixtures),payload={};
for(const name of names)payload[name]=await readFile(path.join(fixtures,name));
const hash=b=>createHash('sha256').update(b).digest('hex');
const inputManifest=Object.fromEntries(Object.entries(payload).map(([name,b])=>[name,hash(b)]));
const mime={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8'};
const server=createServer((req,res)=>{
  const name=req.url?.slice(1);
  if(req.method!=='GET'||!Object.hasOwn(payload,name)){res.writeHead(404);res.end();return;}
  res.writeHead(200,{'Content-Type':mime[path.extname(name)],'Content-Security-Policy':"default-src 'self'; connect-src 'none'; object-src 'none'; base-uri 'none'"});res.end(payload[name]);
});
await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve);});
const origin=`http://127.0.0.1:${server.address().port}`;
const checks=[],captures=[],errors=[];
let browser;
try{
  browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_EXECUTABLE?{executablePath:process.env.CHROMIUM_EXECUTABLE}:{})});
  const context=await browser.newContext({reducedMotion:'reduce',serviceWorkers:'block'});
  await context.route('**/*',route=>new URL(route.request().url()).origin===origin?route.continue():route.abort());
  const page=await context.newPage();
  page.on('pageerror',e=>errors.push(e.message));
  const check=(name,condition)=>{assert.ok(condition,name);checks.push(name);};
  const capture=async(name,width)=>{
    const file=`${name}-${width}.png`;
    await page.screenshot({path:path.join(output,file),fullPage:false,animations:'disabled'});
    captures.push({file,sha256:hash(await readFile(path.join(output,file))),width,height:900,
      ...await page.evaluate(()=>({artifact:document.querySelector('main').dataset.artifact,
        documentWidth:document.documentElement.scrollWidth,status:document.querySelector('#status')?.textContent||'',
        focus:document.activeElement?.id||'',dialogOpen:!!document.querySelector('dialog[open]')}))});
  };
  for(const width of [1280,390]){
    await page.setViewportSize({width,height:900});
    await page.goto(`${origin}/r1.html`);
    check(`R1 starting Water appears enabled ${width}`,await page.locator('#water').isEnabled());
    await page.locator('#water').click();
    check(`R1 starting Water no-op ${width}`,(await page.locator('#status').textContent()).includes('0 beds'));
    await capture('r1-start',width);
    await page.locator('#start').click();await page.locator('#water').click();
    check(`R1 active Water advances ${width}`,(await page.locator('#status').textContent()).includes('1 beds'));
    await capture('r1-active',width);
    await page.locator('#overview').click();await page.locator('#water').click();
    check(`R1 overview Water no-op ${width}`,(await page.locator('#status').textContent()).includes('1 beds'));
    await capture('r1-overview',width);
    await page.locator('#undo').click();
    check(`R1 overview Undo recovers ${width}`,(await page.locator('#status').textContent()).includes('0 beds'));
    await page.locator('#overview').click();await page.locator('#water').click();await page.locator('#restart').click();await page.locator('#undo').click();
    check(`R1 restart can be undone ${width}`,(await page.locator('#status').textContent()).includes('1 beds'));
    await capture('r1-recovery',width);
    await page.goto(`${origin}/r2.html`);await capture('r2-ready',width);
    await page.locator('#deliver').click();
    check(`R2 delivery works ${width}`,await page.locator('#status').textContent()==='1 parcel delivered.');
    await capture('r2-delivered',width);await page.locator('#reset').click();
    check(`R2 reset works ${width}`,await page.locator('#status').textContent()==='1 parcel ready.');
    await page.goto(`${origin}/r3.html`);
    check(`R3 selection required ${width}`,await page.locator('#reserve').isDisabled());
    await capture('r3-start',width);await page.locator('#room').selectOption({label:'Window room'});
    check(`R3 selection enables review ${width}`,await page.locator('#reserve').isEnabled());
    await page.locator('#reserve').click();
    check(`R3 dialog opens ${width}`,await page.locator('dialog').isVisible());await capture('r3-dialog',width);
    await page.locator('#cancel').click();
    check(`R3 return preserves selection ${width}`,await page.locator('#room').inputValue()==='Window room');
    check(`R3 return restores focus ${width}`,await page.locator('#reserve').evaluate(el=>el===document.activeElement));
    await capture('r3-return',width);
    for(const version of ['a','b']){
      await page.goto(`${origin}/r4-${version}.html`);await capture(`r4-${version}`,width);
      const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
      check(`R4 ${version} expected layout ${width}`,overflow===(version==='b'&&width===390));
      await page.locator('a[href="#woods"]').click();
      check(`R4 ${version} navigation works ${width}`,new URL(page.url()).hash==='#woods');
    }
  }
  check('No browser page errors',errors.length===0);
  let playwrightVersion='unknown';try{playwrightVersion=require(`${dependency}/package.json`).version;}catch{}
  const receipt={createdAt:new Date().toISOString(),node:process.version,playwright:playwrightVersion,browser:browser.version(),
    scope:'Local synthetic Chromium fixtures; no device, live service, human usability, aesthetic approval or release claim.',
    inputs:inputManifest,checks,captures};
  await writeFile(path.join(output,'manifest.json'),JSON.stringify(receipt,null,2)+'\n');
  console.log(`PASS ${checks.length} fixture assertions; ${captures.length} captures; ${path.join(output,'manifest.json')}`);
}finally{
  if(browser)await browser.close();
  await new Promise(resolve=>server.close(resolve));
}
