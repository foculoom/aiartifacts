'use strict';
const fs = require('node:fs');
const path = require('node:path');
const os = require('node:os');
const http = require('node:http');
const {execFileSync} = require('node:child_process');
const git = (root, ...args) => execFileSync('git', ['-C', root, ...args], {encoding:'utf8'}).trim();
const toolkitRoot = path.resolve(__dirname, '../../../../..');
const nextPaint = page => page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
async function measure(page, action) {
  const start = await page.evaluate(() => performance.now());
  await action();
  await nextPaint(page);
  return await page.evaluate(() => performance.now()) - start;
}
async function frames(page) {
  return page.evaluate(() => new Promise(resolve => {
    const values=[]; let last;
    function tick(now) { if(last!==undefined) values.push(now-last); last=now;
      if(values.length===60) resolve(Math.max(...values)); else requestAnimationFrame(tick); }
    requestAnimationFrame(tick);
  }));
}
async function run({root, serveRoot=root, scenario, fixture, exercise}) {
  if(!process.env.PERF_OUTPUT) throw Error('PERF_OUTPUT must name a new JSON file');
  if(fs.existsSync(process.env.PERF_OUTPUT)) throw Error('refusing to overwrite a measurement');
  const pin=JSON.parse(fs.readFileSync(path.join(root,'tests/performance-toolkit.json')));
  const toolkitRevision=git(toolkitRoot,'rev-parse','HEAD');
  if(toolkitRevision!==pin.revision || git(toolkitRoot,'status','--porcelain')) throw Error('toolkit differs from clean pinned revision');
  if(git(root,'status','--porcelain')) throw Error('commit source before measurement');
  const {chromium}=require(process.env.PLAYWRIGHT_MODULE || 'playwright');
  const pkg=require((process.env.PLAYWRIGHT_MODULE || 'playwright') + '/package.json');
  const mime={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.css':'text/css','.json':'application/json','.svg':'image/svg+xml','.woff2':'font/woff2'};
  const server=http.createServer((req,res)=>{
    try {const url=new URL(req.url,'http://localhost'); const decoded=decodeURIComponent(url.pathname);
      let file=path.resolve(serveRoot,'.'+decoded); if(file!==path.resolve(serveRoot)&&!file.startsWith(path.resolve(serveRoot)+path.sep)) throw Error('path');
      if(fs.statSync(file).isDirectory()) file=path.join(file,'index.html');
      if(!fs.realpathSync(file).startsWith(fs.realpathSync(serveRoot)+path.sep)) throw Error('symlink');
      res.setHeader('Content-Type',mime[path.extname(file)]||'application/octet-stream');
      res.setHeader('Cache-Control','no-store');res.end(fs.readFileSync(file));
    }catch{res.writeHead(404);res.end();}
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  let browser;
  try {
    browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_EXECUTABLE?{executablePath:process.env.CHROMIUM_EXECUTABLE}:{})});
    const base=`http://127.0.0.1:${server.address().port}`;
    const report={schema_version:1,source_revision:git(root,'rev-parse','HEAD'),source_dirty:false,
      toolkit_revision:toolkitRevision,scenario,fixture,captured_at:new Date().toISOString(),
      environment:{os:os.platform()+' '+os.release(),arch:os.arch(),cpu:os.cpus()[0].model,memory_bytes:os.totalmem(),node:process.version,browser:browser.version(),playwright:pkg.version,viewport:{width:1280,height:900},headless:true},
      conditions:{protocol:'browser-action-settle-v1',warmups:1,samples:5,cache:'new context per sample; HTTP no-store',network:'loopback only; external blocked',power:process.env.PERF_POWER||'unrecorded'},
      experiment:{injected_input_delay_ms:Number(process.env.PERF_INJECT_DELAY_MS||0)},metrics:{}};
    const delay=report.experiment.injected_input_delay_ms;
    if(!Number.isFinite(delay)||delay<0||delay>1000) throw Error('invalid delay');
    for(let i=-1;i<5;i++) {
      const context=await browser.newContext({viewport:report.environment.viewport,acceptDownloads:true,serviceWorkers:'block'});
      const errors=[];
      try {
        await context.route('**/*',route=>new URL(route.request().url()).origin===base?route.continue():route.abort());
        if(delay) await context.addInitScript(ms=>document.addEventListener('click',()=>{const until=performance.now()+ms;while(performance.now()<until){}},true),delay);
        const page=await context.newPage();page.on('pageerror',e=>errors.push(e.message));
        const values=await exercise({page,context,base,measure,nextPaint,frames});
        if(errors.length) throw Error(errors.join('\n'));
        if(i>=0) for(const [name,value] of Object.entries(values)) {
          if(!Number.isFinite(value)||value<0) throw Error('invalid measurement '+name);
          (report.metrics[name]??={unit:name.endsWith('_bytes')?'bytes':'ms',direction:'lower',samples:[]}).samples.push(value);
        }
      } finally {await context.close();}
    }
    if(!Object.keys(report.metrics).length || Object.values(report.metrics).some(m=>m.samples.length!==5)) throw Error('incomplete metrics');
    fs.mkdirSync(path.dirname(path.resolve(process.env.PERF_OUTPUT)),{recursive:true});
    fs.writeFileSync(process.env.PERF_OUTPUT,JSON.stringify(report,null,2)+'\n',{flag:'wx'});
    console.log('Measured '+scenario+' (advisory; no release decision)');
  }finally{if(browser)await browser.close();await new Promise(resolve=>server.close(resolve));}
}
module.exports={run};
