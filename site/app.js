// Build output is static. Browser state and interactions are scoped to one menu.
const byId = id => document.getElementById(id);
const states = new Map();
let currentMenu = data.menus[0].id;
let printSnapshot = null;

function loadChecks(key) {
  try {
    const value = JSON.parse(localStorage.getItem(key) || '{}');
    return value && typeof value === 'object' && !Array.isArray(value) ? value : {};
  } catch { return {}; }
}

function saveChecks(state) {
  try {
    localStorage.setItem(state.menu.storageKey, JSON.stringify(state.saved));
    byId(`${state.menu.id}-storage-status`).textContent = 'Saved in this browser for this menu.';
  } catch {
    byId(`${state.menu.id}-storage-status`).textContent = 'Browser storage is unavailable. Checks work for this visit only.';
  }
}

function filterRecipes(state) {
  const query = byId(`${state.menu.id}-search`).value.trim().toLowerCase();
  let visible = 0;
  state.cards.forEach(card => {
    card.hidden = !card.dataset.search.includes(query);
    if (!card.hidden) visible++;
  });
  byId(`${state.menu.id}-count`).textContent = `${visible} recipe${visible === 1 ? '' : 's'} ${query ? 'found' : 'in this menu'}`;
  byId(`${state.menu.id}-empty`).hidden = visible > 0;
}

function showTab(state, id) {
  state.tabs.forEach(button => {
    const active = button.dataset.tab === id;
    button.setAttribute('aria-selected', String(active));
    button.tabIndex = active ? 0 : -1;
    byId(`${state.menu.id}-${button.dataset.tab}`).hidden = !active;
  });
}

function selectMenu(id) {
  if (!states.has(id)) return;
  currentMenu = id;
  states.forEach(state => { state.element.hidden = state.menu.id !== id; });
  const state = states.get(id);
  byId(`${id}-search`).value = '';
  filterRecipes(state);
  showTab(state, 'recipes');
  byId('menu-select').value = id;
  byId('menu-status').textContent = `${state.menu.title} selected · ${state.menu.recipes.length} recipe${state.menu.recipes.length === 1 ? '' : 's'}`;
  document.title = `The Recipe Book · ${state.menu.title}`;
}

function downloadChecklist(state) {
  const menu = state.menu;
  const text = `${menu.title.toUpperCase()}\n${menu.exportNote}\n\n` +
    Object.entries(menu.shoppingGroups).map(([name, items]) =>
      name + '\n' + items.map(item => `${state.saved[item] === true ? '[x]' : '[ ]'} ${item}`).join('\n')
    ).join('\n\n');
  const url = URL.createObjectURL(new Blob([text], {type: 'text/plain;charset=utf-8'}));
  const link = document.createElement('a');
  link.href = url;
  link.download = menu.exportName;
  link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

data.menus.forEach(menu => {
  const element = byId(`menu-${menu.id}`);
  const state = {menu, element, saved: loadChecks(menu.storageKey), checks: [],
    cards: [...element.querySelectorAll('.card')], tabs: [...element.querySelectorAll('[data-tab]')]};
  states.set(menu.id, state);
  state.tabs.forEach((button, index) => {
    button.addEventListener('click', () => showTab(state, button.dataset.tab));
    button.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % state.tabs.length;
      else if (event.key === 'ArrowLeft') next = (index + state.tabs.length - 1) % state.tabs.length;
      else if (event.key === 'Home') next = 0;
      else if (event.key === 'End') next = state.tabs.length - 1;
      else return;
      event.preventDefault();
      showTab(state, state.tabs[next].dataset.tab);
      state.tabs[next].focus();
    });
  });
  byId(`${menu.id}-search`).addEventListener('input', () => filterRecipes(state));
  Object.entries(menu.shoppingGroups).forEach(([name, items]) => {
    const group = document.createElement('div'); group.className = 'shopping-group';
    const heading = document.createElement('h3'); heading.textContent = name; group.append(heading);
    items.forEach(item => {
      const label = document.createElement('label'); label.className = 'check';
      const check = document.createElement('input'); check.type = 'checkbox'; check.checked = state.saved[item] === true;
      check.addEventListener('change', () => { state.saved[item] = check.checked; saveChecks(state); });
      const text = document.createElement('span'); text.textContent = item;
      label.append(check, text); group.append(label); state.checks.push(check);
    });
    byId(`${menu.id}-shopping-groups`).append(group);
  });
  byId(`${menu.id}-clear`).addEventListener('click', () => {
    state.saved = {};
    state.checks.forEach(check => {check.checked = false;});
    saveChecks(state);
  });
  byId(`${menu.id}-download`).addEventListener('click', () => downloadChecklist(state));
  byId(`${menu.id}-print`).addEventListener('click', () => window.print());
  showTab(state, 'recipes');
});
byId('menu-select').addEventListener('change', event => selectMenu(event.target.value));
selectMenu(currentMenu);

// Works for the button and browser Print/Ctrl-P. Restore search and disclosures afterward.
window.addEventListener('beforeprint', () => {
  if (printSnapshot) return;
  const state = states.get(currentMenu);
  const details = [...state.element.querySelectorAll('details')];
  printSnapshot = {state, query: byId(`${currentMenu}-search`).value, details: details.map(node => [node, node.open])};
  byId(`${currentMenu}-search`).value = '';
  filterRecipes(state);
  details.forEach(node => { node.open = true; });
});
window.addEventListener('afterprint', () => {
  if (!printSnapshot) return;
  const {state, query, details} = printSnapshot;
  byId(`${state.menu.id}-search`).value = query;
  filterRecipes(state);
  details.forEach(([node, wasOpen]) => {node.open = wasOpen;});
  printSnapshot = null;
});
