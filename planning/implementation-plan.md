# Recipe collection implementation

## Scope and requirements
Create a public, buildless recipe collection for GitHub Pages. The first menu contains four recipes spanning seven seafood species. Preserve the verified source instructions; mark missing quantities and servings as unspecified. No accounts, backend, analytics, external assets, credentials, or automated scaling.

## Implementation
1. Receive the verified HTML/CSS/JS and recipe source from the parent; inspect for private metadata and correctness.
2. Place the static site in `docs/`, using relative URLs so it works below `/recipe-collection/`. Provide search, menu grouping, ingredient checklists, readable cooking steps, mobile layout, and a print view.
3. Add a README with recipe editing guidance, source limitations, local preview, and exact post-merge publishing instructions. Add `.nojekyll` for branch-based Pages.
4. Validate source data, links, JavaScript, search/checklist/print behavior, and desktop/mobile layouts. Use a lightweight read-only CI check only if warranted, without deployment credentials or OIDC grants.
5. Commit all files on `feat/seven-fishes-recipe-site`, create a draft PR, obtain final engineering/QA/release/security review, and verify checks against the exact PR head.

## Release and security boundaries
`main` contains exactly one empty bootstrap commit until user merge. Do not enable publishing before user merge. After merge, configure Pages from `main:/docs` using existing access, then verify the published project URL. No custom domains or paid services. Public content excludes sender addresses, message IDs, and personal email details. Rollback is a revert PR; disable Pages if needed only when authorized.

## Acceptance evidence
- Four complete source-faithful recipes, seven seafood species, explicit unspecified amounts/servings.
- Search works for titles and ingredients; no-results state is understandable.
- Ingredient checklist state and reset operate; mobile page has no horizontal overflow.
- Print stylesheet produces readable recipes and hides interactive chrome.
- No absolute root asset URLs, secrets, email metadata, or deployment token workflow.
- Draft PR links exact head and verification results; publishing remains pending merge.
