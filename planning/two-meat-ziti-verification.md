# Two-meat ziti verification · 2026-11-14

Medium tier, isolated feature worktree from main b91b6ca (merged PR #3). Owner explicitly authorized the recipe update and a new draft PR, never merge/auto-merge.

- Build and dependency-free site tests pass, including original menu preservation/interactions and quantified ziti checks.
- New grocery/export checks verify both 1 lb meats, unchanged pasta/cheeses, three tomato cans and scaled aromatics/herbs, no duplicate prepared sauce purchase, and a fresh checklist after quantity changes.
- Generated HTML/JSON are reproducible, JSON matches content.py, and Seven Fishes/Thanksgiving exported objects equal main.
- Sauce allocation: ½ cup bottom + 4½ cups with both cooked meats + 1 cup top = 6 cups plain tomato sauce measured before meat. Meatless alternative retains 4½–5 cups and unchanged pasta/cheeses/egg.
- Independent recipe/grocery/release review found one wording ambiguity: explicitly season plain sauce for the meatless path. Corrected in the meatless note; no other findings.
- Whitespace diff check passes. No presentation code, workflow or hosting changes.

Pages API confirms legacy publication from main:/docs; validate.yml only runs read-only validation on push/PR. A feature-only push and draft PR do not publish. Owner merge remains the gate.

Browser/mobile layout and actual print preview remain unverified. Prior local-file browser policy denial and preview-server sandbox denial were not retried or routed around. Script print-state restoration checks pass; they are not real print QA. Verify visual/print output before owner merge and production availability after Pages deploys.
