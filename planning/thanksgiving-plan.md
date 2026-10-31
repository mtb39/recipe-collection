# Thanksgiving turkey guide

## Scope
Add a separate Thanksgiving menu containing a sourced whole deep-fried turkey guide for the verified Creole Feast TFS3010. Preserve the four Seven Fishes recipes exactly. No purchases, accounts, backend, hosting changes, automatic scaling, assumed turkey weight, oil gallons, or serving count. Existing main:/docs Pages publication happens only after the owner merges the new PR.

## Data and UI
Use an explicit menus data structure so recipes, counts, source notes, safety guidance, prep stages, shopping groups, exports, and browser storage belong to their menu. Keep the existing Seven Fishes storage key so prior checks survive. Provide a labeled menu chooser; search applies only to the selected menu and says so. Print/export only the selected menu. The Thanksgiving checklist includes equipment to inventory, not an instruction to buy everything.

Keep the visual language and buildless output. Split the existing generator into readable data/template/script files only as needed to maintain the menu behavior. HTML escape text and use static rendering where practical; no untrusted HTML execution. Generate docs/index.html and docs/recipes.json consistently.

## Guide and safety
Use the matching manufacturer manual (cover TFP1030/TFS3010/TFK3001, Serial 10091), supplemented by CPSC, USFA/NPS, CDC/USDA, and National Turkey Federation. Distinguish general 350°F/~3 min/lb guidance from device limits; 400°F is an overheating warning, not a target. The actual unit label/manual controls if different.

Make the severe burn/fire warning and safer alternatives prominent before opening the recipe. Cover compatible assembled equipment/heat shield/inspection/leak test, weather/site clearances, complete fridge thaw/drying, cold bird-plus-holder displacement with at least 3-inch headspace and fill marks, burner-off lowering/lifting, constant supervision/oil thermometer, separate 165°F food checks in three locations, cooling/disposal/leftovers, and retreat/911/no-water emergency behavior. Provide equipment and source links near the instructions. No improvised lifting rigs or guessed gas-control settings.

## Validation and gates
1. Engineering/adversarial/release/security plan review plus Astra advice before implementation.
2. Independent source/cooking-safety review and independent UI/code review after implementation; resolve actual defects.
3. Generator reproducibility, unchanged original four recipes, source links and safety invariants, search/menu isolation, per-menu checklist persistence/reset/export, keyboard tabs, and selected-menu print checks.
4. Browser desktop/narrow QA if a surface is available. No unlock or installation workaround. If unavailable, provide an exact committed source archive for parent cloud QA and state remaining print/touch limits.
5. Draft PR on feat/thanksgiving-turkey-guide only; verify exact-head CI and leave merge/publication to the owner.
