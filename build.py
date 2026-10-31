"""Build the dependency-free site; content.py is the single recipe-editing source."""
import html
import json
from pathlib import Path

from content import menus

ROOT = Path(__file__).parent
OUT = ROOT / 'docs'
OUT.mkdir(exist_ok=True)


def esc(value):
    return html.escape(str(value), quote=True)


def source_links(menu, ids):
    sources = {s['id']: s for s in menu['sources']}
    return ' '.join(
        f'<a href="{esc(sources[key]["url"])}" target="_blank" rel="noopener noreferrer">'
        f'{esc(sources[key]["label"].split(" · ")[0])}</a>' for key in ids
    )


def paragraphs(blocks):
    return ''.join(f'<h3>{esc(b["title"])}</h3><p>{esc(b["text"])}</p>' for b in blocks)


def recipe_card(menu, recipe):
    tags = recipe.get('tags', recipe['seafood'])
    searchable = ' '.join([recipe['title'], recipe['course'], *tags, *recipe['ingredients'],
                           *recipe.get('equipment', [])]).lower()
    gear = ''
    if recipe.get('equipment'):
        gear = '<h4>Equipment before you begin</h4><ul class="gear-list">' + ''.join(
            f'<li>{esc(item)}</li>' for item in recipe['equipment']) + '</ul>'
    steps = ''
    for step in recipe['steps']:
        if isinstance(step, str):
            steps += f'<li>{esc(step)}</li>'
        else:
            steps += (f'<li><strong>{esc(step["title"])}</strong><p>{esc(step["text"])}</p>'
                      f'<span class="step-sources">Sources: {source_links(menu, step["sources"])}</span></li>')
    return f'''<article class="card" data-search="{esc(searchable)}">
      <div class="card-top"><div class="course">{esc(recipe['course'])}</div><h3>{esc(recipe['title'])}</h3>
      <p>{esc(recipe['intro'])}</p><div class="pills">{''.join(f'<span class="pill">{esc(t)}</span>' for t in tags)}</div>
      <div class="time">{esc(recipe['time'])} · {esc(recipe['method'])}</div></div>
      <details id="{esc(recipe['id'])}"><summary>Open recipe</summary><div class="recipe-body">
      <h4>Ingredients · amounts to confirm</h4><ul>{''.join(f'<li>{esc(i)}</li>' for i in recipe['ingredients'])}</ul>
      {gear}<h4>Method</h4><ol>{steps}</ol><div class="note">{esc(recipe['note'])}</div>
      </div></details></article>'''


def warning(menu, name):
    block = menu.get(name)
    if not block:
        return ''
    return (f'<aside class="risk {name}" aria-label="{esc(block["title"])}"><h2>{esc(block["title"])}</h2>'
            f'<p>{esc(block["text"])}</p><p class="step-sources">Sources: '
            f'{source_links(menu, block["sources"])}</p></aside>')


def render_menu(menu):
    mid = menu['id']
    recipe_count = len(menu['recipes'])
    tabs = [('recipes', 'Recipes'), ('shopping', menu['shoppingTab']), ('prep', 'Prep order'), ('notes', 'Source & notes')]
    tab_html = ''.join(
        f'<button id="{mid}-tab-{key}" role="tab" aria-controls="{mid}-{key}" '
        f'aria-selected="{str(key == "recipes").lower()}" data-tab="{key}">{esc(label)}</button>'
        for key, label in tabs)
    pairings = ''
    if menu['pairings']:
        pairings = '<div class="wine"><h3>At the table</h3>' + ''.join(
            f'<p><strong>{esc(b["title"])}:</strong> {esc(b["text"])}</p>' for b in menu['pairings']) + '</div>'
    sources = ''.join(
        f'<li><a href="{esc(s["url"])}" target="_blank" rel="noopener noreferrer">{esc(s["label"])}</a>'
        f'<p>{esc(s["detail"])}</p></li>' for s in menu['sources'])
    prep = ''.join(f'<div class="stage"><h3>{esc(b["title"])}</h3><p>{esc(b["text"])}</p></div>' for b in menu['prep'])
    return f'''<div class="menu" id="menu-{mid}" data-menu="{mid}">
      <div class="hero"><div><div class="eyebrow">{esc(menu['eyebrow'])}</div><h1>{esc(menu['title'])}</h1>
      <p class="lead">{esc(menu['intro'])}</p><div class="meta"><div><strong>{recipe_count}</strong>{'recipe' if recipe_count == 1 else 'recipes'}</div>
      <div><strong>{esc(menu['statValue'])}</strong>{esc(menu['statLabel'])}</div><div><strong>To confirm</strong>servings & quantities</div></div></div>
      <div class="hero-art" aria-hidden="true"><span class="plate-number">{esc(menu['statValue'])}<small>{esc(menu['statLabel'])}</small></span></div></div>
      {warning(menu, 'warning')}{warning(menu, 'emergency')}
      <div class="note"><strong>{esc(menu['noticeTitle'])}</strong> {esc(menu['notice'])}</div>
      <nav class="tabs" aria-label="{esc(menu['title'])} sections" role="tablist">{tab_html}</nav>
      <section class="panel" id="{mid}-recipes" role="tabpanel" aria-labelledby="{mid}-tab-recipes">
      <div class="tools"><input id="{mid}-search" class="search" type="search" placeholder="Find a recipe, ingredient or tool…"
      aria-label="Search {esc(menu['title'])} recipes and ingredients"><span id="{mid}-count" class="count" aria-live="polite">{recipe_count} {'recipe' if recipe_count == 1 else 'recipes'} in this menu</span></div>
      <div class="grid{' guide-grid' if menu.get('warning') else ''}">{''.join(recipe_card(menu, r) for r in menu['recipes'])}</div>
      <p id="{mid}-empty" class="empty" hidden>No recipes match in this menu. Clear the search or choose another menu.</p>{pairings}</section>
      <section class="panel" id="{mid}-shopping" role="tabpanel" aria-labelledby="{mid}-tab-shopping">
      <h2>{esc(menu['shoppingTitle'])}</h2><p class="section-intro">{esc(menu['shoppingIntro'])}</p>
      <div class="actions"><button class="button" id="{mid}-download">Download this checklist</button><button class="button secondary" id="{mid}-clear">Clear this menu’s checks</button></div>
      <p id="{mid}-storage-status" class="count" aria-live="polite"></p><div id="{mid}-shopping-groups" class="shopping-grid"></div>
      <noscript><ul>{''.join(f'<li>{esc(i)}</li>' for items in menu['shoppingGroups'].values() for i in items)}</ul></noscript></section>
      <section class="panel" id="{mid}-prep" role="tabpanel" aria-labelledby="{mid}-tab-prep"><h2>Plan the order.</h2>
      <p class="section-intro">{esc(menu['prepIntro'])}</p><div class="timeline">{prep}</div></section>
      <section class="panel" id="{mid}-notes" role="tabpanel" aria-labelledby="{mid}-tab-notes"><h2>Source & notes</h2>
      <div class="source">{paragraphs(menu['notes'])}<h3>Read the sources</h3><ul class="source-list">{sources}</ul></div></section>
      <aside class="safety">{esc(menu['safety'])}</aside>
      <div class="actions"><button class="button secondary" id="{mid}-print">Print this menu</button></div>
      </div>'''


payload = {'menus': menus}
output = (ROOT / 'site/template.html').read_text()
replacements = {
    '__COUNTS__': f'{len(menus)} menus · {sum(len(m["recipes"]) for m in menus)} recipes',
    '__STYLE__': (ROOT / 'site/styles.css').read_text(),
    '__OPTIONS__': ''.join(f'<option value="{esc(m["id"])}">{esc(m["shortTitle"])}</option>' for m in menus),
    '__MENUS__': '\n'.join(render_menu(m) for m in menus),
    '__DATA__': json.dumps(payload, ensure_ascii=False).replace('<', '\\u003c'),
    '__SCRIPT__': (ROOT / 'site/app.js').read_text(),
}
# One pass avoids treating marker-like recipe text as a template directive.
import re
output = re.sub('|'.join(map(re.escape, replacements)), lambda match: replacements[match[0]], output)
output = '\n'.join(line.rstrip() for line in output.splitlines()) + '\n'
(OUT / 'index.html').write_text(output)
(OUT / 'recipes.json').write_text(json.dumps(payload, indent=2, ensure_ascii=False) + '\n')
