# Recipe collection

A public, buildless recipe collection at https://mtb39.github.io/recipe-collection/. Plain HTML, CSS and JavaScript; no accounts, backend, analytics or remote assets.

## Menus

- **Seven Fishes / Christmas Eve:** four supplied recipes spanning seven seafood varieties. Original recipe objects and shopping item strings are preserved. Amounts and servings remain unspecified except the source’s reserved pasta water.
- **Thanksgiving:** a sourced whole deep-fried turkey guide for the Creole Feast TFS3010, including equipment, prominent risk/emergency panels, prep sequence and linked primary sources. This is a sourced guide, not a tested family recipe. No turkey weight, oil gallons, servings, fixed duration or automatic scaling is assumed.

The menu chooser scopes search, counts, checklist state, text downloads, prep notes and printing. Printing includes the selected menu’s complete instructions and sources, even if a tab or search has hidden them. It restores the prior search and disclosure state afterward. The Seven Fishes browser-storage key and item strings remain compatible with existing checks. Each menu has its own clear/check/export actions.

## Edit and generate

Edit `content.py` for recipes, menu metadata, equipment/shopping groups, source links, warnings and prep notes. `site/template.html`, `site/styles.css` and `site/app.js` define presentation and browser behavior. Run:

```sh
python3 build.py
node tests/check-site.mjs
```

Commit both generated outputs, `docs/index.html` and `docs/recipes.json`, with source changes. The JSON is a readable export; the page embeds its data and does not fetch it at runtime. The build needs no network or third-party dependencies. `SOURCE.md` distinguishes supplied recipes from sourced guide material.

Keep public content free of email headers, sender addresses, secrets and private notes. Use linked primary sources for new safety guidance and check the actual equipment manual before importing generic cooking advice.

## Local preview and QA

From the repository root, run `python3 -m http.server 8000` and open `http://localhost:8000/docs/`. Test below a subpath, as Pages uses `/recipe-collection/`.

CI regenerates outputs and requires no diff, then runs dependency-free checks for original-recipe preservation, menu/storage isolation, search, keyboard tabs, exports, malformed/unavailable storage and print state restoration. These script checks do not verify mobile rendering, actual touch behavior or paginated print output. Before approving content changes, inspect both menus in a browser, including a narrow window, repeated menu switches, reload persistence, downloaded lists and print preview.

## Publication

GitHub Pages is already configured from `main:/docs`, with HTTPS. All content changes go through feature branches/worktrees and PRs. The owner merges; an agent must not merge or enable auto-merge without explicit authorization. Merging a content PR triggers the existing Pages publication. Do not add a new hosting account, credentials, custom domain or deployment workflow. Roll back through a revert PR.
