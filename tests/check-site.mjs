import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const html = fs.readFileSync(new URL('../docs/index.html', import.meta.url), 'utf8');
const data = JSON.parse(fs.readFileSync(new URL('../docs/recipes.json', import.meta.url)));
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
assert.equal(data.recipes.length, 4);
assert.equal(new Set(data.recipes.flatMap(r => r.seafood)).size, 7);
assert.equal(data.servings, null);
assert.equal(data.quantitiesComplete, false);
assert.ok(!/[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}/.test(html));
assert.ok(!/\b(?:fetch|XMLHttpRequest)\s*\(/.test(script));
assert.match(html, /section\[hidden\],article\[hidden\]\{display:block!important\}/);

// Exercise the delivered script with a minimal DOM; browser visual QA is separate.
class Element {
  constructor(tag = 'div') { this.tag = tag; this.children = []; this.dataset = {}; this.listeners = {}; this.hidden = false; this.value = ''; this.attrs = {}; }
  append(...items) { this.children.push(...items); }
  addEventListener(name, fn) { this.listeners[name] = fn; }
  setAttribute(name, value) { this.attrs[name] = value; }
  dispatchEvent(e) { this.listeners[e.type]?.({ target: this, ...e }); }
  click() { this.dispatchEvent({ type: 'click' }); }
  focus() { this.focused = true; }
}
function run(storageValue = '{}', blocked = false) {
  const ids = Object.fromEntries(['cards','search','count','empty','storage-status','shopping-groups','clear','download','print','recipes','shopping','prep','notes'].map(id => [id, new Element()]));
  const tabs = ['recipes','shopping','prep','notes'].map(id => Object.assign(new Element('button'), { dataset: {tab:id} }));
  const details = Array.from({length: 4}, () => new Element('details'));
  const all = () => Object.values(ids).flatMap(function walk(e) { return [e, ...e.children.flatMap(walk)]; });
  let stored = storageValue, printed = 0, downloads = 0;
  const document = {
    querySelector: s => ids[s.slice(1)],
    getElementById: id => ids[id],
    querySelectorAll: s => s === '[data-tab]' ? tabs : s === 'details' ? details : all().filter(e => e.tag === 'input'),
    createElement: tag => new Element(tag),
  };
  const context = vm.createContext({document, localStorage: {getItem() {if(blocked) throw Error(); return stored;}, setItem(k,v) {if(blocked) throw Error(); stored=v;}}, window:{print(){printed++;}}, Event:class {constructor(type){this.type=type;}}, Blob, URL:{createObjectURL(){downloads++;return 'blob:test';},revokeObjectURL(){}},setTimeout(fn){fn();}});
  vm.runInContext(script,context);
  return {ids,tabs,details,all,context,stored:()=>stored,printed:()=>printed,downloads:()=>downloads};
}
const app = run();
assert.equal(app.ids.cards.children.length, 4);
app.ids.search.value = 'scallops'; app.ids.search.dispatchEvent({type:'input'});
assert.equal(app.ids.cards.children.filter(c=>!c.hidden).length, 1);
assert.match(app.ids.count.textContent, /^1 recipe found$/);
app.ids.search.value = 'no such recipe'; app.ids.search.dispatchEvent({type:'input'});
assert.equal(app.ids.empty.hidden, false);
app.tabs[1].click(); assert.equal(app.ids.shopping.hidden, false); assert.equal(app.ids.recipes.hidden, true);
app.tabs[1].dispatchEvent({type:'keydown',key:'End',preventDefault(){}});
assert.equal(app.tabs[3].focused, true); assert.equal(app.ids.notes.hidden, false);
const check=app.all().find(e=>e.tag==='input'); check.checked=true;check.dispatchEvent({type:'change'});
assert.ok(Object.values(JSON.parse(app.stored())).includes(true));
const restored=run(app.stored());assert.equal(restored.all().find(e=>e.tag==='input').checked,true);
app.ids.clear.click();assert.equal(check.checked,false);assert.equal(app.stored(),'{}');
app.ids.download.click();assert.equal(app.downloads(),1);
app.ids.print.click();assert.equal(app.printed(),1);assert.ok(app.details.every(d=>d.open));assert.ok(app.ids.cards.children.every(c=>!c.hidden));
for(const initial of ['bad json','null','[]']) assert.equal(run(initial).ids.cards.children.length,4);
const blocked=run('{}',true);const bcheck=blocked.all().find(e=>e.tag==='input');bcheck.checked=true;bcheck.dispatchEvent({type:'change'});assert.match(blocked.ids['storage-status'].textContent,/unavailable/);
assert.equal(vm.runInContext('escapeHTML(`<b>"&`) ',app.context),'&lt;b&gt;&quot;&amp;');
console.log('PASS: recipe data, privacy, search/no-results, tabs/keyboard, checklist/persistence/reset, storage failure, download, print reset, HTML escaping');
