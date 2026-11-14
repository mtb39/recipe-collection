import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const html = fs.readFileSync(new URL('../docs/index.html', import.meta.url), 'utf8');
const data = JSON.parse(fs.readFileSync(new URL('../docs/recipes.json', import.meta.url)));
const original = JSON.parse(fs.readFileSync(new URL('fixtures/seven-fishes.json', import.meta.url)));
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
assert.equal(data.menus.length, 3);
const [seafood, thanksgiving, ziti] = data.menus;
assert.deepEqual(seafood.recipes, original.recipes);
assert.deepEqual(seafood.shoppingGroups, original.shoppingGroups);
assert.equal(seafood.storageKey, 'recipebook-sevenfishes-shopping-v1');
assert.equal(new Set(seafood.recipes.flatMap(r => r.seafood)).size, 7);
assert.equal(thanksgiving.recipes.length, 1);
assert.equal(thanksgiving.recipes[0].seafood.length, 0);
assert.notEqual(seafood.storageKey, thanksgiving.storageKey);
assert.ok([seafood, thanksgiving].every(m => m.servings === null && !m.quantitiesComplete));
assert.ok(!/[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}/.test(html));
assert.ok(!/\b(?:fetch|XMLHttpRequest)\s*\(/.test(script));
assert.ok(!/innerHTML/.test(fs.readFileSync(new URL('../site/app.js', import.meta.url), 'utf8')));
assert.match(html, /\.menu\[hidden\]\{display:none!important\}/);
assert.match(html, /\.menu:not\(\[hidden\]\) \.panel\[hidden\]/);
const idsInHTML = [...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]);
assert.equal(new Set(idsInHTML).size, idsInHTML.length, 'IDs must be unique across menus');
for (const m of data.menus) {
  for (const id of ['search','count','empty','storage-status','shopping-groups','clear','download','print','recipes','shopping','prep','notes'])
    assert.ok(idsInHTML.includes(`${m.id}-${id}`));
  for(const r of m.recipes) assert.ok(idsInHTML.includes(r.id));
  for(const source of m.sources) assert.ok(source.url.startsWith('https://'));
}
const guide = thanksgiving.recipes[0].steps.map(s=>s.text).join(' ');
for(const term of ['40°F','4–5 pounds','1–2 days','10 feet','24 inches','3 inches','minimum/maximum','no oil or ignition','mark the remaining water level','Do not rinse','400°F','350°F','3 minutes per pound','burner-OFF','165°F','breast','thigh','wing','completely cool','within 2 hours','Never pour it into drains','Wash and sanitize or replace the landing tray','For marked pots too']) assert.ok(guide.includes(term), `missing guide safeguard: ${term}`);
assert.match(thanksgiving.warning.text,/NFPA discourages/);
assert.match(thanksgiving.emergency.text,/Never put water/);
assert.ok(!/\d+\s*gallons/i.test(guide));

// Exercise the actual delivered script with a minimal DOM, using its generated markup.
// This checks interaction logic; browser rendering/print pagination are separate QA.
class Element {
  constructor(tag='div') {this.tag=tag;this.children=[];this.dataset={};this.listeners={};this.hidden=false;this.value='';this.attrs={};this.queries={};}
  append(...nodes) {this.children.push(...nodes);}
  addEventListener(name,fn) {this.listeners[name]=fn;}
  setAttribute(name,value) {this.attrs[name]=value;}
  dispatchEvent(event) {this.listeners[event.type]?.({target:this,...event});}
  click() {this.dispatchEvent({type:'click'});}
  focus() {this.focused=true;}
  querySelectorAll(selector) {return this.queries[selector]||[];}
}
function run(initial={}, blocked=false) {
  const ids=Object.fromEntries(idsInHTML.map(id=>[id,new Element()]));
  const store={...initial}, events={}, blobs=[], links=[];
  let printed=0;
  data.menus.forEach(menu=>{
    const element=ids[`menu-${menu.id}`];
    const chunk=html.split(`id="menu-${menu.id}"`)[1].split('<div class="menu"')[0];
    element.queries['.card']=[...chunk.matchAll(/<article class="card" data-search="([^"]*)"/g)].map(m=>Object.assign(new Element('article'),{dataset:{search:m[1]}}));
    element.queries['[data-tab]']=[...chunk.matchAll(/data-tab="([^"]+)"/g)].map(m=>Object.assign(new Element('button'),{dataset:{tab:m[1]}}));
    element.queries.details=menu.recipes.map(r=>ids[r.id]);
  });
  const document={title:'',getElementById:id=>ids[id],createElement:tag=>{const node=new Element(tag);if(tag==='a')links.push(node);return node;}};
  const window={addEventListener:(name,fn)=>{events[name]=fn;},print(){printed++;events.beforeprint?.();}};
  const context=vm.createContext({document,window,localStorage:{getItem(key){if(blocked)throw Error();return store[key]||null;},setItem(key,value){if(blocked)throw Error();store[key]=value;}},Blob,URL:{createObjectURL(blob){blobs.push(blob);return 'blob:test';},revokeObjectURL(){}},setTimeout(fn){fn();}});
  vm.runInContext(script,context);
  const all=node=>[node,...node.children.flatMap(all)];
  return {ids,store,events,blobs,links,context,printed:()=>printed,checks:id=>all(ids[`${id}-shopping-groups`]).filter(n=>n.tag==='input'),menu:id=>ids[`menu-${id}`],select(id){ids['menu-select'].value=id;ids['menu-select'].dispatchEvent({type:'change'});},search(id,text){ids[`${id}-search`].value=text;ids[`${id}-search`].dispatchEvent({type:'input'});}};
}
const app=run({[seafood.storageKey]:JSON.stringify({'Lump crab meat':true})});
assert.equal(app.menu('thanksgiving').hidden,true);
assert.equal(app.menu('seven-fishes').hidden,false);
assert.ok(app.checks('seven-fishes').some(c=>c.checked),'old persisted seafood checks survive');
app.search('seven-fishes','scallops');
assert.equal(app.menu('seven-fishes').queries['.card'].filter(c=>!c.hidden).length,1);
app.search('seven-fishes','turkey');assert.equal(app.ids['seven-fishes-empty'].hidden,false);
app.select('thanksgiving');assert.equal(app.menu('seven-fishes').hidden,true);assert.equal(app.menu('thanksgiving').hidden,false);
assert.equal(app.ids['thanksgiving-count'].textContent,'1 recipe in this menu');
app.search('thanksgiving','scallops');assert.equal(app.ids['thanksgiving-empty'].hidden,false);
app.search('thanksgiving','heat shield');assert.equal(app.ids['thanksgiving-empty'].hidden,true);
const tabs=app.menu('thanksgiving').queries['[data-tab]'];tabs[1].click();assert.equal(app.ids['thanksgiving-shopping'].hidden,false);
tabs[1].dispatchEvent({type:'keydown',key:'End',preventDefault(){}});assert.equal(tabs[3].focused,true);assert.equal(app.ids['thanksgiving-notes'].hidden,false);
const check=app.checks('thanksgiving')[0];check.checked=true;check.dispatchEvent({type:'change'});
assert.ok(Object.values(JSON.parse(app.store[thanksgiving.storageKey])).includes(true));
assert.deepEqual(JSON.parse(app.store[seafood.storageKey]),{'Lump crab meat':true});
const restored=run(app.store);assert.equal(restored.checks('thanksgiving')[0].checked,true);
app.ids['thanksgiving-download'].click();
assert.equal(app.links.at(-1).download,'thanksgiving-turkey-checklist.txt');
const exportText=await app.blobs.at(-1).text();assert.match(exportText,/THANKSGIVING TURKEY/);assert.match(exportText,/\[x\] Whole turkey/);assert.ok(!exportText.includes('Lump crab'));
app.ids['thanksgiving-clear'].click();assert.equal(app.checks('thanksgiving')[0].checked,false);assert.deepEqual(JSON.parse(app.store[seafood.storageKey]),{'Lump crab meat':true});
app.select('seven-fishes');assert.equal(app.ids['seven-fishes-search'].value,'');app.ids['seven-fishes-download'].click();assert.match(await app.blobs.at(-1).text(),/FEAST OF THE SEVEN FISHES/);assert.ok(!(await app.blobs.at(-1).text()).includes('Whole turkey'));
for(let i=0;i<3;i++){app.select('thanksgiving');app.select('seven-fishes');}assert.equal(app.checks('seven-fishes').filter(c=>c.checked).length,1);
app.select('thanksgiving');app.search('thanksgiving','no match');app.ids['thanksgiving-turkey'].open=false;
app.ids['thanksgiving-print'].click();assert.equal(app.printed(),1);assert.equal(app.ids['thanksgiving-turkey'].open,true);assert.equal(app.ids['thanksgiving-empty'].hidden,true);assert.equal(app.menu('seven-fishes').hidden,true);
app.events.afterprint();assert.equal(app.ids['thanksgiving-search'].value,'no match');assert.equal(app.ids['thanksgiving-turkey'].open,false);
app.events.beforeprint();assert.equal(app.ids['thanksgiving-turkey'].open,true);app.events.afterprint();
for(const bad of ['bad json','null','[]']){const broken=run({[thanksgiving.storageKey]:bad});broken.select('thanksgiving');assert.equal(broken.ids['thanksgiving-count'].textContent,'1 recipe in this menu');}
const blocked=run({},true);const bcheck=blocked.checks('thanksgiving')[0];bcheck.checked=true;bcheck.dispatchEvent({type:'change'});assert.match(blocked.ids['thanksgiving-storage-status'].textContent,/unavailable/);blocked.select('seven-fishes');blocked.select('thanksgiving');assert.equal(bcheck.checked,true);
console.log('PASS: menu/data isolation, source safeguards, original seafood preservation, search, keyboard tabs, legacy storage, per-menu checks/reset/export, repeated switching, unavailable storage, selected-menu print and state restoration');

// The quantified recipe must remain usable through the same menu interactions.
assert.equal(ziti.servings, '6–8');
assert.equal(ziti.quantitiesComplete, true);
assert.equal(new Set(data.menus.map(m => m.storageKey)).size, 3);
app.select('baked-ziti');
app.search('baked-ziti', 'ricotta');
assert.equal(app.ids['baked-ziti-count'].textContent, '1 recipe found');
assert.equal(app.menu('thanksgiving').hidden, true);
const zcheck = app.checks('baked-ziti')[0];
zcheck.checked = true; zcheck.dispatchEvent({type:'change'});
assert.equal(run(app.store).checks('baked-ziti')[0].checked, true);
app.ids['baked-ziti-download'].click();
assert.equal(app.links.at(-1).download, 'baked-ziti-checklist.txt');
assert.match(await app.blobs.at(-1).text(), /1 lb dry ziti/);
assert.ok(!(await app.blobs.at(-1).text()).includes('Whole turkey'));
app.search('baked-ziti', 'no match');
app.ids['baked-ziti'].open = false;
app.ids['baked-ziti-print'].click();
assert.equal(app.ids['baked-ziti'].open, true);
app.events.afterprint();
assert.equal(app.ids['baked-ziti-search'].value, 'no match');
assert.equal(app.ids['baked-ziti'].open, false);
console.log('PASS: quantified ziti menu search, checklist persistence, isolated export and print restoration');

app.search('baked-ziti', 'flat-leaf parsley');
assert.equal(app.ids['baked-ziti-count'].textContent, '1 recipe found');
assert.equal(ziti.recipes.length, 2);

// Grocery exports must represent one two-meat batch, without also buying prepared sauce.
app.select('baked-ziti');
app.ids['baked-ziti-download'].click();
const meatList = await app.blobs.at(-1).text();
for (const required of ['1 lb dry ziti', '1 lb mild Italian pork sausage, casings removed', '1 lb 93/7 ground beef', '15 oz whole-milk ricotta', '12 oz low-moisture mozzarella', '½ cup grated Parmesan', '3 (28 oz) cans whole peeled tomatoes', '1½ medium onions', '6 garlic cloves', '6 tbsp chopped fresh Italian flat-leaf parsley', '6 tbsp loosely packed fresh basil']) {
  assert.ok(meatList.includes(required), `missing two-meat grocery requirement: ${required}`);
}
const groceryItems = Object.values(ziti.shoppingGroups).flat();
assert.equal(groceryItems.filter(i => i.includes('whole peeled tomatoes')).length, 1);
assert.ok(!groceryItems.some(i => /cups.*(?:sauce|marinara)/.test(i)), 'homemade list must not also buy prepared sauce');
assert.match(ziti.recipes[0].note, /Meatless alternative:/);
assert.match(ziti.recipes[0].note, /omit both meats/i);
assert.match(ziti.recipes[0].note, /4½–5 cups/);
assert.notEqual(ziti.storageKey, 'recipebook-baked-ziti-shopping-v1', 'changed quantities start a fresh checklist');
const stale = run({'recipebook-baked-ziti-shopping-v1': JSON.stringify({'1 lb dry ziti': true})});
assert.equal(stale.checks('baked-ziti').filter(c => c.checked).length, 0);
console.log('PASS: two-meat grocery quantities, no duplicate prepared sauce, meatless adjustment and fresh checklist');
