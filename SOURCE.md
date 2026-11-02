# Source and editorial record

The Seven Fishes recipe content was supplied by the owner on October 31, 2026, under the title “Christmas Eve Feast of the Seven Fishes - Recipe Instructions.” No sender address, email identifier, routing header or signature is included.

## Source facts
- Crab-stuffed mushrooms: mushrooms, cream cheese, garlic, Parmesan, lemon juice, Old Bay, parsley, lump crab and panko. Bake at 375°F for 18–20 minutes.
- Fried calamari: rings and tentacles soaked in buttermilk about 30 minutes; flour, cornstarch, salt, pepper, garlic powder and paprika coating; fry at 375°F in batches about 1.5–2 minutes; sea salt, lemon, marinara or garlic aioli.
- Seafood pasta: linguine, olive oil, butter, garlic, pepper flakes, clams, mussels, white wine, shrimp, scallops, cherry tomatoes and parsley. Reserve 1 cup pasta water. Original shellfish steaming guidance is 3–5 minutes; discard unopened shells. Original email says to sear shrimp/scallops “in the same pan” for 1–2 minutes per side, then toss pasta and tomatoes in pan juices and recombine seafood.
- Flounder: flour, beaten egg, seasoned breadcrumb breading; salt, pepper, olive oil and butter. Pan-fry 3–4 minutes then 2–3 minutes; serve with lemon.
- Wine: Pinot Grigio, Vermentino or Falanghina with calamari; lightly chilled Etna Rosso or Frappato with pasta/fish.

No guest count, serving count, ingredient quantities beyond the reserved pasta water, dinner time or exact total preparation time was supplied. Do not scale or generate purchase quantities until the owner provides a base recipe or approves explicitly labeled estimates.

## Added notes, not source instructions
- Keep the calamari refrigerated during its soak.
- Pat scallops dry and use a separate hot pan for a browned sear instead of trying to sear in wine broth.
- The proposed prep order is organizational advice, not the source's schedule.
- Food-safety summary comes from FDA guidance: https://www.fda.gov/food/buy-store-serve-safe-food/selecting-and-serving-fresh-and-frozen-seafood-safely

## Thanksgiving sourced guide

The owner identified the Creole Feast TFS3010 product and requested a Thanksgiving whole deep-fried turkey guide with equipment. This is newly compiled cooking guidance, not a tested family recipe. No bird weight, oil volume, servings or fixed cooking duration was supplied.

The matching manufacturer manual is https://m.media-amazon.com/images/I/C1lB2VFWj2L.pdf (cover TFP1030/TFS3010/TFK3001, Serial 10091). The actual unit label/manual governs; conflicting listing/manual pot-size wording is not converted into an oil capacity or turkey-weight limit. No larger replacement pot, guessed gas control settings, improvised lifting rig or automated oil/time calculator is recommended.

The guide distinguishes equipment rules from general food/fire guidance. NTF’s general 350°F oil/~3 minutes per pound is only planning guidance; the manual’s 400°F warning is overheating, not a target. Cold actual-bird-plus-holder fit/fill verification, fill marks and at least 3-inch headspace must coexist; otherwise choose a smaller bird or different cooking method. All three food locations must measure 165°F.

Primary sources and claim scope are stored with the Thanksgiving menu in `content.py` and rendered in Source & notes and beside relevant steps: Creole Feast, NPS, USFA, CPSC, CDC, National Turkey Federation, U.S. Air Force Safety Center, Seattle Fire Department, USDA FSIS and FoodSafety.gov. Manufacturer and agency sources were checked October 31, 2026. Generic source suggestions that conflict with the equipment manual (gallons, replacement pot, soft ground, DIY lifting) are excluded.

Independent cooking-safety review specifically checked displacement, fill/headspace compatibility, burner-off lowering/lifting, three-site doneness, underdone retry handling and emergency/cooling behavior. The resulting guide requires a clean/sanitized or replacement tray and utensils after contact with undercooked turkey.

## Verification

`tests/fixtures/seven-fishes.json` preserves the first menu’s original export for structural comparison. Tests verify unchanged recipe objects and shopping strings, separate storage keys, per-menu interaction behavior and selected-menu printing. Generated output is reproducible without network access. Browser verification is reported separately in the PR; script tests are not visual or real-print QA.
