const fs=require('fs');
const path=require('path');
const crypto=require('crypto');
const http=require('http');
const {chromium}=require('/PLAYWRIGHT_PACKAGE');
const packet='/EVALUATOR_PACKETS/r4';
const output=__dirname;
const files=['r4-a.html','r4-b.html','style.css','fixture.js'];
const provenance=JSON.parse(fs.readFileSync(path.join(packet,'provenance.json'),'utf8'));
const testedFiles=['INSTRUCTIONS.md','provenance.json','skills/experience-review/SKILL.md','skills/experience-review/references/production-acceptance.md','skills/experience-review/references/interactive-experiences.md',...files.map(f=>'fixtures/'+f),...provenance.captures.map(f=>'evidence/'+f.file)];
const hashes=Object.fromEntries(testedFiles.map(f=>[f,crypto.createHash('sha256').update(fs.readFileSync(path.join(packet,f))).digest('hex')]));
const server=http.createServer((req,res)=>{const name=(req.url||'').split('?')[0].slice(1);if(!files.includes(name)){res.writeHead(404);res.end();return;}res.setHeader('Content-Type',name.endsWith('.html')?'text/html':name.endsWith('.css')?'text/css':'application/javascript');res.end(fs.readFileSync(path.join(packet,'fixtures',name)));});
const receipt={agentEvaluation:true,reviewer:'Codex agent /root/quality_eval_r4',model:'unknown (exact model identifier not exposed)',startedAt:new Date().toISOString(),sourceCommitReported:provenance.sourceCommit,provenanceCreatedAt:provenance.createdAt,hashes,provenanceHashMatches:Object.fromEntries(Object.entries(hashes).filter(([f])=>f in provenance.inputHashes).map(([f,h])=>[f,h===provenance.inputHashes[f]])),node:process.version,playwright:require('/PLAYWRIGHT_PACKAGE/package.json').version,results:[],blockedRequests:[]};
let browser;
const snapshot=async page=>page.evaluate(()=>({url:location.href,artifact:document.querySelector('#app').dataset.artifact,viewport:{width:innerWidth,height:innerHeight},documentWidth:document.documentElement.scrollWidth,documentHeight:document.documentElement.scrollHeight,scroll:{x:scrollX,y:scrollY},focus:{tag:document.activeElement.tagName,text:document.activeElement.textContent,href:document.activeElement.getAttribute('href'),outline:getComputedStyle(document.activeElement).outline,outlineOffset:getComputedStyle(document.activeElement).outlineOffset},heading:{font:getComputedStyle(document.querySelector('h1')).font,color:getComputedStyle(document.querySelector('h1')).color},bodyFont:getComputedStyle(document.body).font,cards:[...document.querySelectorAll('.notes article')].map(el=>{const r=el.getBoundingClientRect();return{id:el.id,text:el.textContent,rect:{x:r.x,y:r.y,width:r.width,height:r.height,right:r.right,bottom:r.bottom},fullyWithinViewport:r.x>=0&&r.right<=innerWidth&&r.y>=0&&r.bottom<=innerHeight};})}));
(async()=>{
 await new Promise((resolve,reject)=>{server.once('error',reject);server.listen(0,'127.0.0.1',resolve);});
 const base='http://127.0.0.1:'+server.address().port;
 browser=await chromium.launch({headless:true,executablePath:'/CHROMIUM_EXECUTABLE'});
 receipt.browser=browser.version();
 for(const variant of ['a','b'])for(const width of [1280,390]){
  const context=await browser.newContext({viewport:{width,height:900},deviceScaleFactor:1});
  await context.route('**/*',route=>{if(new URL(route.request().url()).origin===base)return route.continue();receipt.blockedRequests.push(route.request().url());return route.abort();});
  const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  const url=base+'/r4-'+variant+'.html';const result={variant,artifact:variant==='a'?'N4':'N5',viewport:{width,height:900},input:'browser automation mouse and keyboard, no physical device',errors,actions:[]};
  await page.goto(url,{waitUntil:'networkidle'});result.initial=await snapshot(page);
  await page.screenshot({path:path.join(output,`r4-${variant}-${width}-initial.png`)});
  for(const name of ['Coast','Woods','Ridge']){
   await page.goto(url,{waitUntil:'networkidle'});await page.getByRole('link',{name,exact:true}).click();
   result.actions.push({type:'mouse click',target:name,state:await snapshot(page)});
   if(name==='Ridge'&&width===390)await page.screenshot({path:path.join(output,`r4-${variant}-${width}-ridge-click.png`)});
  }
  await page.goto(url,{waitUntil:'networkidle'});
  for(const [index,name] of ['Coast','Woods','Ridge'].entries()){await page.goto(url,{waitUntil:'networkidle'});for(let i=0;i<=index;i++)await page.keyboard.press('Tab');const before=await snapshot(page);await page.keyboard.press('Enter');result.actions.push({type:'keyboard from fresh page: '+(index+1)+' Tab(s) then Enter',target:name,before,state:await snapshot(page)});}
  await page.goto(url,{waitUntil:'networkidle'});await page.keyboard.press('Tab');await page.screenshot({path:path.join(output,`r4-${variant}-${width}-keyboard-focus.png`)});
  for(const name of ['coast','woods','ridge']){await page.goto(url+'#'+name,{waitUntil:'networkidle'});result.actions.push({type:'direct fragment entry',target:name,state:await snapshot(page)});}
  receipt.results.push(result);await context.close();
 }
 receipt.completedAt=new Date().toISOString();
 fs.writeFileSync(path.join(output,'action-receipts.json'),JSON.stringify(receipt,null,2)+'\n');
 console.log(JSON.stringify({startedAt:receipt.startedAt,completedAt:receipt.completedAt,browser:receipt.browser,hashesMatch:Object.values(receipt.provenanceHashMatches).every(Boolean),results:receipt.results.map(r=>({artifact:r.artifact,viewport:r.viewport,documentWidth:r.initial.documentWidth,errors:r.errors,actions:r.actions.map(a=>({type:a.type,target:a.target,hash:new URL(a.state.url).hash,scroll:a.state.scroll,focusedBefore:a.before?.focus.text}))})),blockedRequests:receipt.blockedRequests},null,2));
})().catch(e=>{receipt.error=String(e.stack||e);fs.writeFileSync(path.join(output,'action-receipts.json'),JSON.stringify(receipt,null,2)+'\n');console.error(e);process.exitCode=1;}).finally(async()=>{if(browser)await browser.close();server.close();});
