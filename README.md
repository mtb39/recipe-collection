# Recipe collection

A small, public recipe collection, starting with a Seven Fishes dinner. Built with plain HTML, CSS, and JavaScript; no installation or build is required.

## Content

The first menu contains four recipes covering seven seafood species. The original recipe notes do not specify quantities or servings. Those values stay explicitly unspecified; the site does not invent amounts or offer automatic scaling.

Recipe content is public. Do not add email headers, sender addresses, private notes, credentials, or material you do not have permission to publish.

## Local preview

From the repository root:

```sh
python3 -m http.server 8000
```

Open `http://localhost:8000/docs/`. This also checks that relative assets work below a subpath. Search and ingredient checklists run in the browser. There is no backend or account system.

## Publishing after the first PR is merged

The initial pull request contains all website content. The default branch starts with one empty bootstrap commit. Publishing is deliberately pending the owner's merge.

After that merge:

1. Open **Settings → Pages** in this repository.
2. Select **Deploy from a branch**, branch **main**, folder **/docs**, and save.
3. Wait for GitHub's Pages deployment to complete.
4. Verify `https://mtb39.github.io/recipe-collection/` on desktop and mobile, including search, ingredient checks, and print preview.

No custom domain, external hosting account, deployment token, or custom deployment workflow is needed. The site URL above is the expected address, not confirmation that publishing has completed.

Future changes go through a feature branch and pull request. Merging updates to the publishing branch lets GitHub Pages publish them automatically. Revert a problematic change through a pull request.

## Editing recipes

Edit `recipes` and `groups` in `build.py`, then run `python3 build.py` to regenerate `docs/index.html` and `docs/recipes.json`. Commit both outputs with the generator. `recipes.json` is a readable export; this version embeds its data in the HTML rather than fetching the export at runtime. `SOURCE.md` records the supplied instructions and identifies editorial additions.

## Verification

Run `python3 build.py`, then `git diff --exit-code -- docs/` and `node tests/check-site.mjs`. CI runs these same dependency-free checks with read-only repository access. The script tests delivered JavaScript against a minimal DOM: search, tabs and keyboard navigation, checklist persistence/reset, unavailable storage, download creation, and print reset. It also checks recipe counts and privacy constraints. This is not a substitute for browser rendering, mobile layout, or print-preview QA.
