// IndexedDB is on the Streamlit page origin; no application data is sent to another endpoint.
const stateKey = Symbol.for('dsafe.v364113.device-storage');
const state = globalThis[stateKey] ||= {operations:new Map(), db:null};
async function openDatabase(){
 if(state.db)return state.db;
 state.db=await new Promise((resolve,reject)=>{
  const req=indexedDB.open('dsafe-v364113-device',1);
  req.onupgradeneeded=()=>req.result.createObjectStore('storage');
  req.onsuccess=()=>{req.result.onversionchange=()=>{req.result.close();state.db=null;};resolve(req.result);};
  req.onerror=()=>reject(req.error);req.onblocked=()=>reject(new Error('Penyimpanan sedang digunakan oleh tab lain.'));
 });return state.db;
}
async function execute(request){
 const db=await openDatabase();
 return new Promise((resolve,reject)=>{
  const tx=db.transaction('storage',request.operation==='write'?'readwrite':'readonly');
  const store=tx.objectStore('storage');let response;let conflict=false;
  const read=store.get('files');
  read.onsuccess=()=>{
   const current=read.result||{revision:0,files:{}};
   if(request.operation==='write'){
    if(request.expectedRevision!==current.revision){conflict=true;tx.abort();return;}
    const next={revision:current.revision+1,files:request.files};
    store.put(next,'files');response={id:request.id,ok:true,revision:next.revision};
   }else response={id:request.id,ok:true,revision:current.revision,files:current.files};
  };
  tx.oncomplete=()=>resolve(response);
  tx.onabort=()=>reject(new Error(conflict?'Data pada perangkat telah berubah di tab lain. Muat ulang aplikasi sebelum menyimpan.':tx.error?.message||'Penyimpanan dibatalkan.'));
  tx.onerror=()=>reject(tx.error||new Error('Tidak dapat menyimpan data di perangkat.'));
 });
}

// DSAFE_NAVIGATION_BRIDGE_V1
// Streamlit Community Cloud: force the existing HTML navigation
// controls to navigate on the top-level application page.
function installDsafeNavigationBridge(){
  const stateKey = Symbol.for('dsafe.v364113.navigation-bridge');

  if(globalThis[stateKey]) return;
  globalThis[stateKey] = true;

  const selector = [
    'a.home-card-shell',
    'a.settings-float',
    'a.bk-hist-action-btn',
    'a.dk70-week-arrow'
  ].join(',');

  const handleNavigation = (event) => {
    let anchor = null;

    if(typeof event.composedPath === 'function'){
      for(const node of event.composedPath()){
        if(
          node &&
          typeof node.matches === 'function' &&
          node.matches(selector)
        ){
          anchor = node;
          break;
        }
      }
    }

    if(
      !anchor &&
      event.target &&
      typeof event.target.closest === 'function'
    ){
      anchor = event.target.closest(selector);
    }

    if(!anchor) return;

    const href = anchor.getAttribute('href');

    if(!href || !href.includes('nav=')) return;

    event.preventDefault();
    event.stopPropagation();

    if(typeof event.stopImmediatePropagation === 'function'){
      event.stopImmediatePropagation();
    }

    const destination = new URL(href, globalThis.location.href);

    globalThis.location.assign(destination.href);
  };

  document.addEventListener('click', handleNavigation, true);
}

installDsafeNavigationBridge();

export default function({data,parentElement,setStateValue}){
 // Hide only the storage bridge's wrapper, leaving the original application layout intact.
 parentElement.closest('[data-testid="stElementContainer"]')?.style.setProperty('display','none');
 if(!data?.id||state.operations.has(data.id))return;
 const operation=execute(data).then(result=>setStateValue('result',result)).catch(e=>setStateValue('result',{id:data.id,ok:false,error:e.message}));
 state.operations.set(data.id,operation);
 // Avoid retaining personal payloads in this operation registry: it holds promises only.
 if(state.operations.size>100){for(const key of state.operations.keys()){if(key!==data.id)state.operations.delete(key);if(state.operations.size<=50)break;}}
}
