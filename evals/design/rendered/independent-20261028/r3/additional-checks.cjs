const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const { chromium } = require('/PLAYWRIGHT_PACKAGE');
const root = '/EVALUATOR_PACKETS/r3/fixtures';
const output = { evaluation: 'agent evaluation', date: new Date().toISOString(), viewport: {width:390,height:900}, environment:'Headless Chrome with touch/mobile emulation; not a physical device', actions:[], errors:[] };
const server = http.createServer((req,res)=>{ const f=new URL(req.url,'http://127.0.0.1').pathname.slice(1); if(!['r3.html','style.css','fixture.js'].includes(f)){res.writeHead(404).end();return;}res.end(fs.readFileSync(path.join(root,f))); });
const luminance = hex => { const [r,g,b]=hex.match(/\w\w/g).map(x=>parseInt(x,16)/255).map(x=>x<=.04045?x/12.92:((x+.055)/1.055)**2.4);return .2126*r+.7152*g+.0722*b; };
output.contrast = [['body text','#203832','#f3f0e8'],['enabled control text','#203832','#ffffff'],['dialog text','#000000','#ffffff'],['focus outline on page','#a05012','#f3f0e8'],['focus outline on dialog','#a05012','#ffffff']].map(([component,fg,bg])=>{ const a=luminance(fg.slice(1)),b=luminance(bg.slice(1)); return {component,foreground:fg,background:bg,ratio:(Math.max(a,b)+.05)/(Math.min(a,b)+.05),method:'sRGB relative luminance from inspected CSS/computed colors; not pixel sampling'}; });
(async()=>{
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 let browser;
 try {
  const base=`http://127.0.0.1:${server.address().port}`;
  browser=await chromium.launch({executablePath:'/CHROMIUM_EXECUTABLE',headless:true,args:['--no-sandbox']});
  const context=await browser.newContext({viewport:output.viewport,isMobile:true,hasTouch:true});
  await context.route('**/*',route=>new URL(route.request().url()).origin===base?route.continue():route.abort());
  const page=await context.newPage();
  const record=async action=>output.actions.push({action,...await page.evaluate(()=>({selection:document.querySelector('#room').value,dialogOpen:document.querySelector('dialog').open,dialogSelection:document.querySelector('#selection').textContent,focus:document.activeElement.id,status:document.querySelector('#status').textContent,documentWidth:document.documentElement.scrollWidth,viewport:innerWidth,targets:[...document.querySelectorAll('button,select')].map(el=>{const r=el.getBoundingClientRect();return{id:el.id,width:r.width,height:r.height};})}))});
  await page.goto(`${base}/r3.html`);
  await page.locator('#help').tap(); await record('Emulated touch tap Help');
  await page.locator('#room').selectOption({label:'Courtyard room'}); await record('Playwright native-select selection; does not verify touch select popup');
  await page.locator('#reserve').tap(); await record('Emulated touch tap Review reservation');
  await page.waitForTimeout(500);
  await page.screenshot({path:path.join(__dirname,'touch-dialog-390.png'),fullPage:true});
  await page.locator('#cancel').tap(); await record('Emulated touch tap Back to selection');
  await page.waitForTimeout(500);
  await page.screenshot({path:path.join(__dirname,'touch-return-390.png'),fullPage:true});
  await context.close();
 }catch(error){output.errors.push(String(error.stack||error));throw error;}
 finally{fs.writeFileSync(path.join(__dirname,'additional-checks.json'),JSON.stringify(output,null,2));if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}
})().catch(error=>{console.error(error);process.exitCode=1;});
