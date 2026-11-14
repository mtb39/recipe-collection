# Baked ziti verification · 2026-11-14

## Scope and release boundary

Medium tier under installed home-lab-agent-flow. Isolated branch `feat/baked-ziti-20261114` from current public `main` at `d2e8c3f3073d6baa858b32ac97f632b3ace9f0f4`. Existing historical checkout and worktrees were read only. No calendar terminal or unrelated repository changed.

Read-only GitHub Pages API confirmed legacy branch publication from `main:/docs`. The repository workflow only validates on push/PR. No push or PR was performed: the user's initial instruction was to research and develop the addition, and publishing/PR authorization was not explicit. No merge or automatic merge. Owner merge remains the publication gate.

## Results

- `python3 build.py`: pass.
- `node tests/check-site.mjs`: pass, including both existing menus, quantified ziti search, companion sauce search, checklist persistence, isolated export and selected-menu printing/state restoration.
- Rebuild SHA-256 comparison: generated HTML/JSON reproducible.
- Original two exported menu objects equal `origin/main` exactly.
- `git diff --check`: pass.
- Independent engineering/QA/release review by `review_ziti`: approved after correcting sausage measurement. Measure the full 4½–5 cups tomato sauce separately, then add cooked sausage during the pasta toss.

## Remaining visual QA

Not performed. Opening the generated local file in Chrome via browser tooling was denied before navigation by browser URL security policy (file: protocol disallowed). No alternate browser route was attempted. The local-only Python preview server also failed to bind with sandbox `PermissionError: Operation not permitted`. Neither action remained pending, and no live-site changes occurred. Mobile layout, actual browser rendering and real paginated print preview must be checked before publication; script print-state checks are not real print QA.

## Next step

Owner review of the recipe and visual preview, then explicit authorization to push this feature branch and create a review PR. Push only the feature branch; never push main. Owner merges after review, which triggers existing Pages publication. No deployment, CI, hosting or inventory behavior was changed.
