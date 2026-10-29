/* Original synthetic evaluation interfaces. No external requests or real transactions. */
'use strict';
const app=document.querySelector('#app'), fixture=document.body.dataset.fixture;
const revision={r1:'G1',r2:'P2',r3:'L3','r4-a':'N4','r4-b':'N5'}[fixture];
app.dataset.artifact=revision;
const header=(name,description)=>`<header><small>LOCAL FIXTURE · ${revision}</small><h1>${name}</h1><p>${description}</p></header>`;
if(fixture==='r1'){
  app.innerHTML=header('Signal Garden','A small planning game. Water the next bed; Undo recalls one action.')+
    '<div class="garden" aria-label="Three garden beds"><span>1<br>Seed</span><span>2<br>Seed</span><span>3<br>Seed</span></div>'+
    '<p id="status" role="status"></p><div class="actions"><button id="start">Start</button><button id="water">Water next bed</button><button id="overview">Overview</button><button id="undo">Undo</button><button id="restart">Restart</button></div>';
  let mode='starting',count=0,history=[];
  const show=()=>{document.querySelector('#status').textContent=`${mode==='starting'?'Ready to start':mode==='overview'?'Overview — planning paused':'Playing'} · ${count} beds watered`;document.querySelector('#overview').textContent=mode==='overview'?'Resume':'Overview';document.querySelector('#start').hidden=mode!=='starting';document.querySelectorAll('.garden span').forEach((el,i)=>{el.textContent=`${i+1} · ${i<count?'Watered':'Seed'}`;el.classList.toggle('watered',i<count);});};
  document.querySelector('#start').onclick=()=>{mode='active';show();};
  document.querySelector('#water').onclick=()=>{if(mode!=='active'||count===3)return;history.push(count);count++;show();};
  document.querySelector('#overview').onclick=()=>{if(mode==='starting')return;mode=mode==='active'?'overview':'active';show();};
  document.querySelector('#undo').onclick=()=>{if(history.length)count=history.pop();show();};
  document.querySelector('#restart').onclick=()=>{if(mode==='starting')return;history.push(count);count=0;show();};
  show();
}else if(fixture==='r2'){
  app.innerHTML=header('Parcel Path','Guide the courier to the marked delivery dock.')+
    '<section class="promotion"><b>24 / 24</b><span>COLLECTION INDEX</span></section>'+
    '<div class="parcel-world" aria-label="Courier and delivery dock"><span class="prop">●<small>crate</small></span><span class="courier">●<small>courier</small></span><span class="prop">●<small>parcel</small></span><span class="dock">●<small>dock</small></span></div>'+
    '<div class="parcel-actions"><button id="deliver">Deliver</button><button id="reset">Reset</button></div><p id="status" role="status">1 parcel ready.</p>';
  document.querySelector('#deliver').onclick=()=>{document.querySelector('#status').textContent='1 parcel delivered.';document.querySelector('.courier').classList.add('delivered');};
  document.querySelector('#reset').onclick=()=>{document.querySelector('#status').textContent='1 parcel ready.';document.querySelector('.courier').classList.remove('delivered');};
}else if(fixture==='r3'){
  app.innerHTML=header('Cedar Library','Choose a reading room. This local example creates no booking.')+
    '<form><label for="room">Reading room</label><select id="room"><option value="">Choose a room</option><option>Window room</option><option>Courtyard room</option></select><button id="reserve" disabled>Review reservation</button></form><p><button id="help">Help</button></p><p id="status" role="status"></p>'+
    '<dialog aria-labelledby="dialog-title"><h2 id="dialog-title">Review your selection</h2><p id="selection"></p><p>This is a local preview. No reservation will be sent.</p><button id="cancel">Back to selection</button></dialog>';
  const room=document.querySelector('#room'),reserve=document.querySelector('#reserve'),dialog=document.querySelector('dialog');
  room.onchange=()=>{reserve.disabled=!room.value;};
  document.querySelector('form').onsubmit=e=>{e.preventDefault();document.querySelector('#selection').textContent=room.value;dialog.showModal();};
  document.querySelector('#cancel').onclick=()=>{dialog.close();reserve.focus();};
  document.querySelector('#help').onclick=()=>{document.querySelector('#status').textContent='Choose a room, then review it. You can return without losing your choice.';};
}else{
  app.innerHTML=header('Field Notes','Browse three saved trail notes.')+
    '<nav aria-label="Notes"><a href="#coast">Coast</a><a href="#woods">Woods</a><a href="#ridge">Ridge</a></nav>'+
    '<section class="notes"><article id="coast"><h2>Coast</h2><p>Salt air, pale stones and a clear horizon.</p></article><article id="woods"><h2>Woods</h2><p>A shaded path through the trees.</p></article><article id="ridge"><h2>Ridge</h2><p>The narrow path opens onto a long view.</p></article></section>';
}
