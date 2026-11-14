"""Curated recipe content. Generate public output with python3 build.py."""

seven_fishes_recipes = [{'id': 'crab-mushrooms',
  'title': 'Crab-Stuffed Mushrooms',
  'course': 'Appetizer',
  'seafood': ['Crab'],
  'time': '18–20 min bake',
  'method': 'Oven · 375°F',
  'intro': 'Golden mushroom caps with a creamy lump-crab filling and a little panko crunch.',
  'ingredients': ['Mushroom caps',
                  'Softened cream cheese',
                  'Minced garlic',
                  'Grated Parmesan',
                  'Lemon juice',
                  'Old Bay seasoning',
                  'Chopped parsley',
                  'Lump crab meat',
                  'Panko breadcrumbs'],
  'steps': ['Wipe the mushrooms clean, remove the stems, and gently scoop out a little of the inside to make '
            'room. Arrange on a parchment-lined baking sheet.',
            'Mix cream cheese, garlic, Parmesan, lemon juice, Old Bay and parsley until smooth. Gently fold '
            'in the crab, keeping the lumps intact.',
            'Fill each mushroom cap generously and sprinkle with panko.',
            'Bake at 375°F for 18–20 minutes, until the mushrooms are tender and the tops golden. Serve '
            'warm.'],
  'note': 'The email gives a method but no ingredient amounts or yield. Confirm quantities before cooking.'},
 {'id': 'calamari',
  'title': 'Fried Calamari',
  'course': 'Antipasto',
  'seafood': ['Calamari'],
  'time': '30 min soak + batch frying',
  'method': 'Fry · 375°F oil',
  'intro': 'Light, crisp rings and tentacles, finished with sea salt and fresh lemon.',
  'ingredients': ['Calamari rings and tentacles',
                  'Buttermilk',
                  'All-purpose flour',
                  'Cornstarch',
                  'Salt and pepper',
                  'Garlic powder',
                  'Paprika',
                  'Frying oil',
                  'Sea salt',
                  'Lemon wedges',
                  'Marinara or garlic aioli'],
  'steps': ['Soak the calamari in buttermilk for about 30 minutes. Keep it refrigerated during the soak.',
            'Whisk flour, cornstarch, salt, pepper, garlic powder and paprika together.',
            'Heat frying oil in a deep skillet or Dutch oven to 375°F.',
            'Dredge the calamari in the flour mixture, shaking off excess. Fry in small batches for about '
            '1½–2 minutes, until lightly golden and crisp. Do not crowd the pan.',
            'Drain, season immediately with sea salt, and serve hot with lemon and marinara or garlic '
            'aioli.'],
  'note': 'Keep the soak refrigerated is an added handling note. Frying time is guidance from the email, not '
          'a substitute for checking doneness.'},
 {'id': 'seafood-pasta',
  'title': 'Seafood Linguine',
  'course': 'Main course',
  'seafood': ['Shrimp', 'Scallops', 'Clams', 'Mussels'],
  'time': 'Cook just before serving',
  'method': 'Stovetop',
  'intro': 'Four kinds of seafood, white wine, cherry tomatoes and parsley in a glossy pan sauce.',
  'ingredients': ['Linguine',
                  'Salt',
                  'Olive oil',
                  'Butter',
                  'Minced garlic',
                  'Red pepper flakes',
                  'Clams',
                  'Mussels',
                  'White wine',
                  'Shrimp',
                  'Sea scallops',
                  'Cherry tomatoes, halved',
                  'Fresh parsley',
                  'Reserved pasta water — 1 cup'],
  'steps': ['Cook linguine in salted water until just shy of al dente. Reserve 1 cup of pasta water before '
            'draining.',
            'Warm olive oil and butter in a deep pan. Sauté garlic and red pepper flakes until fragrant, '
            'about 1 minute.',
            'Add clams, mussels and white wine; cover for 3–5 minutes, until the shells open. Discard any '
            'that stay closed. Set the cooked shellfish aside.',
            'The original email says to sear shrimp and scallops in the same pan for 1–2 minutes per side, '
            'then set them aside. See the practical adjustment below if you want a browned sear.',
            'Toss cherry tomatoes and pasta in the pan juices. Add a little reserved pasta water until the '
            'sauce coats the noodles.',
            'Gently fold in all the seafood. Finish with parsley and olive oil, and serve promptly.'],
  'note': 'Practical adjustment: a wine-filled pan will simmer rather than sear. For browning, pat the '
          'scallops dry and sear them separately in a hot pan, then combine with the sauce. This is a '
          'suggested adjustment, not an instruction from the original email.'},
 {'id': 'flounder',
  'title': 'Breaded Flounder',
  'course': 'Main course',
  'seafood': ['Flounder'],
  'time': 'About 5–7 min per batch',
  'method': 'Pan-fry',
  'intro': 'Delicate fillets in a crisp breadcrumb coating, served simply with lemon.',
  'ingredients': ['Flounder fillets',
                  'All-purpose flour',
                  'Eggs, beaten',
                  'Seasoned breadcrumbs',
                  'Salt and pepper',
                  'Olive oil',
                  'Butter',
                  'Lemon wedges'],
  'steps': ['Set out three shallow dishes: flour, beaten eggs and seasoned breadcrumbs.',
            'Pat the fillets dry and season lightly with salt and pepper. Coat in flour, dip in egg, then '
            'press into the breadcrumbs.',
            'Heat olive oil and butter in a large skillet over medium-high heat.',
            'Cook until golden, about 3–4 minutes on the first side, then carefully flip and cook for '
            'another 2–3 minutes. Check doneness; timing varies with thickness.',
            'Drain on a wire rack or paper towel-lined plate. Serve immediately with lemon.'],
  'note': 'The cooking times come from the email. Check the thickest part for doneness rather than relying '
          'on time alone.'}]

seven_fishes_groups = {'Seafood': ['Lump crab meat',
             'Calamari rings and tentacles',
             'Shrimp',
             'Sea scallops',
             'Clams',
             'Mussels',
             'Flounder fillets'],
 'Produce': ['Mushrooms', 'Garlic', 'Lemons', 'Fresh parsley', 'Cherry tomatoes'],
 'Dairy & eggs': ['Cream cheese', 'Parmesan', 'Buttermilk', 'Butter', 'Eggs'],
 'Pantry': ['Panko breadcrumbs',
            'All-purpose flour',
            'Cornstarch',
            'Seasoned breadcrumbs',
            'Linguine',
            'Olive oil',
            'Frying oil',
            'Old Bay seasoning',
            'Salt and pepper',
            'Sea salt',
            'Garlic powder',
            'Paprika',
            'Red pepper flakes',
            'White wine'],
 'To serve': ['Marinara or garlic aioli',
              'Optional pairing: Pinot Grigio, Vermentino or Falanghina',
              'Optional pairing: Etna Rosso or Frappato']}

seafood_sources = [
    {'id': 'fda', 'label': 'FDA — selecting and serving seafood safely',
     'url': 'https://www.fda.gov/food/buy-store-serve-safe-food/selecting-and-serving-fresh-and-frozen-seafood-safely',
     'detail': 'Seafood handling, doneness and holding temperatures.'},
]

turkey_sources = [
    {'id': 'manual', 'label': '1 · Creole Feast owner’s manual — TFS3010 included',
     'url': 'https://m.media-amazon.com/images/I/C1lB2VFWj2L.pdf',
     'detail': 'Cover: TFP1030/TFS3010/TFK3001, Serial 10091. Printed pp. 2–4: setup, heat shield, clearances and fill limits; pp. 5–8: propane, leak test, thermometer and lighting. Use the actual unit’s label/manual if stricter or different; contact the manufacturer about conflicts.'},
    {'id': 'nps', 'label': '2 · National Park Service — deep-fryer hazards',
     'url': 'https://www.nps.gov/articles/p52-deep-fried-turkey-fire-safety.htm',
     'detail': 'NFPA discourages open-flame turkey fryers; safer alternatives, protective gear, weather and supervision.'},
    {'id': 'usfa', 'label': '3 · U.S. Fire Administration — turkey fryer safety',
     'url': 'https://www.usfa.fema.gov/downloads/pdf/publications/turkey-fryer-fire-safety-infographic.pdf',
     'detail': 'Stable placement, clearance, full thawing, oil thermometer and exclusion zone.'},
    {'id': 'cpsc', 'label': '4 · CPSC — turkey fryer safety',
     'url': 'https://www.cpsc.gov/Newsroom/News-Releases/2004/CPSC-Issues-Safety-Tips-for-Turkey-Fryers',
     'detail': 'Dry thawed food, slow lowering, exposed-skin protection, smoke shutdown and no water on fires.'},
    {'id': 'cdc', 'label': '5 · CDC — holiday turkey handling',
     'url': 'https://www.cdc.gov/food-safety/foods/holiday-turkey.html',
     'detail': 'Refrigerator thawing, no rinsing, cross-contamination prevention, three-location 165°F checks and leftovers.'},
    {'id': 'ntf', 'label': '6 · National Turkey Federation — general frying guidance',
     'url': 'https://www.eatturkey.org/how-to-deep-fry-turkey/',
     'detail': '350°F oil and roughly 3 minutes per pound are general guidance, not TFS3010 limits or proof of doneness. Its generic oil amounts, pot choices and ground-surface advice are not used here.'},
    {'id': 'airforce', 'label': '7 · U.S. Air Force Safety Center — holiday cooking',
     'url': 'https://www.safety.af.mil/News/Article-Display/Article/3247358/holiday-cooking-stay-safe-in-the-kitchen/',
     'detail': 'Turn the burner off before lowering; relight only after the bird is lowered and splattering has settled.'},
    {'id': 'seattle', 'label': '8 · Seattle Fire Department — turkey frying',
     'url': 'https://fireline.seattle.gov/2022/11/22/holiday-cooking-safety-frying-a-turkey/',
     'detail': 'Burner-off lowering and lifting. Improvised lifting methods from general guidance are not used here.'},
    {'id': 'extinguisher', 'label': '9 · U.S. Fire Administration — extinguisher selection and use',
     'url': 'https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/fire-extinguishers/index.html',
     'detail': 'Correct fire rating, training, small contained fires and a clear escape route; otherwise retreat and call 911.'},
    {'id': 'oil', 'label': '10 · USDA FSIS — used oil and disposal',
     'url': 'https://ask.fsis.usda.gov/article/Can-oil-be-reused-safely',
     'detail': 'Sealed containers and local recycling/disposal; never pour cooking oil into drains.'},
    {'id': 'temps', 'label': '11 · FoodSafety.gov — poultry temperatures and thawing',
     'url': 'https://www.foodsafety.gov/food-safety-charts/meat-poultry-charts',
     'detail': '40°F-or-below refrigerator thawing and 165°F checks in breast, thigh and wing.'},
]

turkey_gear = [
    'Matching turkey pot and stable TFS3010 burner/stand, fully assembled with its required heat shield; inventory the kit before buying extras.',
    'Manufacturer-approved turkey rack/stand and lifting hook that fit this pot and bird — no ladders, broomsticks or DIY lifting rigs.',
    'Compatible propane cylinder plus the supplied or manufacturer-approved hose and regulator; inspect them and follow the manual’s connection and leak-test procedure.',
    'Working manufacturer-approved clip-on oil thermometer, plus a separate instant-read food thermometer; a meat thermometer does not replace the oil thermometer.',
    'Dry heat-protective gloves/mitts, eye protection, covered skin and closed shoes.',
    'Raw-poultry tray, a separate clean cooked-turkey tray and carving board, paper towels, timer and carving utensils.',
    'Appropriate extinguisher labeled for cooking-oil/grease fires (Class K is intended for cooking oils); follow the manual and extinguisher label. Keep it reachable away from the burner, with a phone and clear retreat route.',
    'Sealable containers for completely cooled oil and shallow food-storage containers for leftovers.',
]

turkey_recipe = {
    'id': 'thanksgiving-turkey', 'title': 'Whole Deep-Fried Turkey', 'course': 'Thanksgiving main · sourced guide',
    'seafood': [], 'tags': ['Turkey', 'Creole Feast TFS3010'],
    'time': 'Plan by weight; verify 165°F in three places', 'method': 'Outdoor propane immersion frying',
    'intro': 'A practical setup-to-cleanup guide for the Creole Feast TFS3010. Compiled from the matching manual and primary safety sources; not a tested family recipe.',
    'ingredients': [
        'Whole turkey — weight, fit, servings and portions to confirm before shopping',
        'High-smoke-point frying oil, such as refined canola or peanut oil — choose for guests’ allergies; determine volume by the cold fit/fill procedure, never a fixed gallon amount',
        'Basic dry seasoning, such as salt, pepper and a dry Creole blend — amount to taste, checking the turkey and blend labels for added salt',
    ],
    'equipment': turkey_gear,
    'steps': [
        {'title': 'Read the manual and decide whether to fry',
         'text': 'Propane immersion frying can cause severe burns and fire even with care. Oven roasting or a professionally fried turkey is a safer alternative. Read the matching manual before setup; the actual unit label/manual controls equipment use. The listing’s 30-quart pot size is not an oil capacity or turkey-weight limit. If your equipment, markings or instructions conflict, stop and contact the manufacturer rather than fitting a larger pot.',
         'sources': ['manual', 'nps']},
        {'title': 'Thaw completely in the refrigerator',
         'text': 'Keep the wrapped bird on a tray in a refrigerator at 40°F or below. Allow about 24 hours per 4–5 pounds; cook within 1–2 days after refrigerator thawing. Check that the cavity is fully thawed, with no ice or frost. Never counter-thaw or lower a frozen, partly frozen or wet bird into oil.',
         'sources': ['cdc', 'temps', 'cpsc']},
        {'title': 'Choose the outdoor site and check the kit',
         'text': 'Use a bare, hard, level, noncombustible surface outdoors, never a tabletop, deck, garage, carport or covered patio. Keep at least 10 feet from combustibles and at least 24 inches between appliance and cylinder, with no combustible overhead surface. Follow any stricter unit requirements. Do not fry in rain, snow or high wind. Keep children and pets outside an exclusion zone at least 3 feet away, and keep traffic clear. Fully assemble the stand and heat shield; inspect the supplied/approved hose, regulator and burner. With cookware removed and before oil or ignition, leak-test exactly as the manual directs, never with a flame. Do not operate with gas odor, leaks or damaged parts.',
         'sources': ['manual', 'usfa', 'cpsc', 'nps']},
        {'title': 'Remove packaging and measure the cold fit/fill level',
         'text': 'With everything cold and no oil or ignition, remove packaging and giblets, then fit the actual thawed bird on its intended approved holder in the matching pot. For marked pots too, verify the cold actual bird-plus-holder fit using the unit’s marked-fill procedure; never override any minimum/maximum fill marking. For a pot without a maximum fill line, add water only until the bird is fully submerged with its holder in place, leaving at least 3 inches from water to rim; remove the bird and holder and mark the remaining water level. That remaining level is the oil-fill reference, not the water level with the bird still inside. If safe submersion, headspace and applicable fill marks cannot coexist, use a smaller bird or another cooking method. Never solve the problem with a bigger replacement pot.',
         'sources': ['manual']},
        {'title': 'Empty the water, then dry and season',
         'text': 'Empty all test water and thoroughly dry the pot, rack/holder and turkey inside and out, especially the cavity. Do not rinse raw poultry. Keep raw juices away from ready-to-eat food; wash hands and clean raw-contact tools/surfaces. Use basic dry seasoning only for this guide; no stuffing, wet brine or injection. Keep the prepared bird refrigerated until needed and check/dry it again before frying. Never add water to hot oil.',
         'sources': ['manual', 'cdc', 'cpsc']},
        {'title': 'Set out protection, thermometers and the landing tray',
         'text': 'Use the equipment checklist before starting. Check the oil thermometer as the manufacturer directs and have a separate instant-read food thermometer. Wear dry heat gloves/mitts, eye protection, covered skin and closed shoes. Set a clean, stable cooked-turkey tray nearby, separate from the raw tray. Keep the proper extinguisher accessible away from the burner and a clear exit. Checklist ticks track items; they do not certify that the setup is safe.',
         'sources': ['manual', 'nps', 'extinguisher']},
        {'title': 'Add the measured oil and heat under constant watch',
         'text': 'Center the dry pot on the stand and add oil only to the cold, verified fill level, obeying every minimum/maximum mark. Light and operate the burner using the unit manual, not guessed control settings. Watch the clip-on oil thermometer continuously. National Turkey Federation guidance uses 350°F oil; this is general cooking guidance, not a manufacturer limit. The manual’s 400°F warning is an overheating ceiling, never a target. If oil smokes or overheats, shut off the burner/gas if safe and do not add the bird. Never leave the fryer unattended or move a hot pot.',
         'sources': ['manual', 'ntf', 'cpsc']},
        {'title': 'Turn the burner OFF, then lower slowly',
         'text': 'Follow the manual’s shutdown procedure and confirm the burner flame is out before lowering. Using the approved rack and hook and wearing protection, slowly lower the completely thawed, dry bird into the oil in a controlled motion. Keep your face and body clear of splatter; do not drop it. If you cannot control the lift safely with the approved equipment, use another cooking method. Relight only by the manual’s procedure after the bird is fully lowered and splattering has settled.',
         'sources': ['airforce', 'seattle', 'manual']},
        {'title': 'Monitor the oil; use time only for planning',
         'text': 'Stay with the fryer and monitor the oil temperature throughout cooking. Roughly 3 minutes per pound is National Turkey Federation planning guidance only, not a guaranteed duration or evidence that the turkey is done. Bird weight and total time remain unspecified here. Maintain the cooking temperature with the unit’s controls as directed; never chase a time estimate by overheating the oil.',
         'sources': ['ntf', 'manual']},
        {'title': 'Turn the burner OFF, lift slowly and check 165°F',
         'text': 'Before lifting, shut down by the manual and confirm the flame is out. Use the proper hook/rack and protection to lift slowly and let oil drain over the pot without swinging or moving it, then transfer to the clean stable tray. With the separate food thermometer, verify at least 165°F in the thickest breast and the innermost thigh and wing, avoiding bone. Color, elapsed time and hoped-for carryover are not proof. If any spot is below 165°F, do not serve: return the bird using the same burner-OFF slow-lowering procedure, relight only after settling per the manual, cook further and repeat all three temperature checks with a clean thermometer. Wash and sanitize or replace the landing tray and utensils touched by undercooked turkey before the final cooked transfer.',
         'sources': ['seattle', 'cdc', 'temps', 'airforce']},
        {'title': 'Shut down and let everything cool undisturbed',
         'text': 'Shut off the burner, regulator and cylinder using the manual’s shutdown instructions. Leave the pot and oil in place until completely cool; this takes hours. Keep supervising the area and exclude children and pets throughout cooling. Do not move the hot pot, transfer hot oil or speed cooling with water.',
         'sources': ['manual', 'nps', 'ntf']},
        {'title': 'Carve, refrigerate and dispose of cooled oil',
         'text': 'Use a clean carving board and utensils. Carve leftovers into smaller portions and refrigerate in shallow containers within 2 hours of cooking, or within 1 hour if exposed to temperatures above 90°F. Only after oil is completely cool, transfer it into sealable containers for locally accepted cooking-oil recycling or disposal. Never pour it into drains; follow local collection rules.',
         'sources': ['cdc', 'oil']},
    ],
    'note': 'No turkey weight, servings, oil gallons or fixed cooking duration has been assumed. Check the actual bird’s fit and all equipment limits first. Sources are linked at each step and in Source & notes.',
}

menus = [
    {
        'id': 'seven-fishes', 'title': 'Feast of the Seven Fishes', 'shortTitle': 'Seven Fishes · Christmas Eve',
        'eyebrow': 'Christmas Eve · A menu to keep',
        'intro': 'Four dishes. Seven kinds of seafood. A little family tradition, gathered in one place for the next time around.',
        'statValue': '7', 'statLabel': 'seafood varieties', 'servings': None, 'quantitiesComplete': False,
        'noticeTitle': 'A recipe draft, ready to organize.',
        'notice': 'The supplied email includes cooking methods, but no serving count and almost no ingredient quantities. Those are marked as missing rather than guessed. The shopping list is an ingredient checklist, not a purchase-quantity plan.',
        'recipes': seven_fishes_recipes, 'shoppingGroups': seven_fishes_groups,
        'storageKey': 'recipebook-sevenfishes-shopping-v1',
        'exportName': 'seven-fishes-ingredient-checklist.txt', 'shoppingTab': 'Shopping list',
        'shoppingTitle': 'One list, all four dishes.',
        'shoppingIntro': 'Check your pantry first. Ingredient amounts and guest count still need to be added. Checks are saved only in this browser, not synced between devices.',
        'exportNote': 'Ingredient checklist — quantities and servings not yet supplied.',
        'prepIntro': 'Suggested order, not a timed schedule from the email. Set the guest count, quantities and serving time before turning this into a minute-by-minute plan.',
        'prep': [
            {'title': 'Before shopping', 'text': 'Confirm guests, portions and ingredient quantities. Check equipment: oven and baking tray, pasta pot, deep frying pan and a separate pan for flounder. Plan who handles the last-minute frying.'},
            {'title': 'Before cooking', 'text': 'Thaw frozen seafood in the refrigerator. Gather and measure the ingredients once quantities are settled. Keep raw seafood chilled and use separate clean equipment for ready-to-eat foods.'},
            {'title': 'Prepare the components', 'text': 'Clean mushrooms, make the crab filling and prepare aromatics. Set up the flounder breading station and calamari coating. Keep perishable components refrigerated until needed.'},
            {'title': 'Appetizers first', 'text': 'Bake the mushrooms. Give the calamari its refrigerated 30-minute soak, then fry in small batches close to serving. The crisp coating is best served right away.'},
            {'title': 'Finish the main courses', 'text': 'Cook the pasta and shellfish close to serving. For browned scallops, use a separate hot pan rather than the wine sauce. Pan-fry the flounder near the end; coordinate the two mains so neither sits waiting.'},
        ],
        'notes': [
            {'title': 'Source', 'text': 'Organized from the supplied “Christmas Eve Feast of the Seven Fishes — Recipe Instructions” email. Sender details and headers are excluded. Crab, calamari, shrimp, scallops, clams, mussels and flounder span four dishes, not seven separate recipes.'},
            {'title': 'Still to fill in', 'text': 'Servings, portion size and ingredient amounts, except the supplied 1 cup of reserved pasta water. Guest count and serving time are needed for a detailed shopping/cooking plan.'},
            {'title': 'Editorial notes', 'text': 'Instructions are organized and lightly edited. The refrigerated calamari soak, separate-pan scallop suggestion and prep sequence are added practical notes. They do not replace the source recipe.'},
        ],
        'pairings': [
            {'title': 'With calamari', 'text': 'Pinot Grigio, Vermentino or Falanghina.'},
            {'title': 'With pasta and flounder', 'text': 'A lightly chilled Etna Rosso or Frappato. These pairings come from the original email.'},
        ],
        'sources': seafood_sources,
        'safety': 'Seafood safety: FDA guidance calls for most seafood to reach 145°F; discard clams and mussels that do not open during cooking. Keep perishable food out for no more than 2 hours, or 1 hour above 90°F. Recipe times are approximate.',
    },
    {
        'id': 'thanksgiving', 'title': 'Thanksgiving Turkey', 'shortTitle': 'Thanksgiving · Turkey',
        'eyebrow': 'Thanksgiving · Equipment & cooking guide',
        'intro': 'Whole deep-fried turkey for the Creole Feast TFS3010, with the tools, setup and safety checks gathered in one place.',
        'statValue': '165°F', 'statLabel': 'breast, thigh & wing', 'servings': None, 'quantitiesComplete': False,
        'noticeTitle': 'Sourced guide · read before you start.',
        'notice': 'Compiled from the matching equipment manual and primary safety sources, not a tested family recipe. Weight, fit, oil volume and servings must be confirmed. The actual unit label/manual controls setup; if it differs or conflicts, stop and ask the manufacturer.',
        'warning': {
            'title': 'Severe burn and fire risk',
            'text': 'Propane immersion frying can cause severe burns and fire. NFPA discourages outdoor gas-fueled turkey fryers; oven roasting or buying a professionally fried turkey is a safer alternative. Never fry a frozen, partly frozen or wet turkey. Use the matching manual and all its setup limits.',
            'sources': ['nps', 'manual'],
        },
        'emergency': {
            'title': 'If oil ignites: retreat and call 911',
            'text': 'Never put water on an oil fire or move a burning pot. Get people away and call 911. Use an appropriate cooking-oil/grease-rated extinguisher only if trained, the fire is small and contained, and you have a clear escape route; otherwise retreat. Do not approach flames to reach a shutoff.',
            'sources': ['cpsc', 'extinguisher'],
        },
        'recipes': [turkey_recipe],
        'shoppingGroups': {
            'Ingredients — confirm fit and amount': turkey_recipe['ingredients'],
            'Equipment — inventory the existing kit first': turkey_gear[:4],
            'Protection, food handling & cleanup': turkey_gear[4:],
        },
        'storageKey': 'recipebook-thanksgiving-shopping-v1', 'exportName': 'thanksgiving-turkey-checklist.txt',
        'shoppingTab': 'Ingredients & gear', 'shoppingTitle': 'Ingredients and the tools alongside the fryer.',
        'shoppingIntro': 'Inventory included accessories before buying extras. No purchase quantities or bird weight are assumed. Checks only track items; they do not certify a safe setup. Read the guide and matching manual. Checks stay in this browser and are separate from Seven Fishes.',
        'exportNote': 'Ingredient and equipment inventory — no assumed bird weight, servings or oil gallons. Checklist ticks do not certify safety. Read the full guide and manufacturer manual.',
        'prepIntro': 'A sequence for planning, not a fixed dinner-time schedule. Read the full guide and manual before setting up or lighting the fryer.',
        'prep': [
            {'title': 'Several days ahead', 'text': 'Confirm the exact unit/manual and approved accessories. Plan refrigerator thawing at about 24 hours per 4–5 pounds; cook 1–2 days after thawing. Choose another method if the site or equipment cannot meet every requirement.'},
            {'title': 'Before any oil or ignition', 'text': 'Choose the outdoor hard, level site and check weather/clearances. Assemble and inspect the kit, then leak-test per the manual with cookware removed. Cold-test the actual bird and holder, obey fill marks and headspace, then empty all water and dry everything completely.'},
            {'title': 'Before heating', 'text': 'Dry and season the fully thawed bird. Separate raw and cooked trays, check both thermometers and protective gear, and prepare the exclusion zone, extinguisher and exit. Add only the measured oil.'},
            {'title': 'Cooking and food checks', 'text': 'Supervise constantly. Turn the burner OFF before every lowering or lifting. Relight per the manual only after full lowering and settled splatter. Verify at least 165°F in breast, innermost thigh and wing; a time estimate is not doneness.'},
            {'title': 'After cooking', 'text': 'Shut down per the manual. Leave oil and equipment undisturbed until completely cool, keeping children/pets away. Refrigerate carved leftovers promptly. Transfer only completely cooled oil for local recycling/disposal, never into drains.'},
        ],
        'notes': [
            {'title': 'Equipment match and limits', 'text': 'The supplied product listing identifies TFS3010. The linked manual cover includes TFP1030/TFS3010/TFK3001, Serial 10091. Its pot-size wording differs from the listing; 30 quarts is not an oil amount or a proven turkey-weight limit. Use the actual matching pot and labels/manual; ask Creole Feast about conflicts, never enlarge the pot to fit a bird.'},
            {'title': 'What the numbers mean', 'text': '350°F oil and roughly 3 minutes per pound are general National Turkey Federation guidance only. 400°F is the manual’s overheating warning, not a cooking target. 165°F must be measured in all three food locations. No turkey weight, oil gallons, total cooking time or servings were supplied.'},
            {'title': 'Source hierarchy', 'text': 'The equipment manual controls setup, fill marks, propane connections, inspection and lighting. General sources add food handling and fire precautions; generic pot sizes, oil volumes and surface suggestions that conflict with the manual are excluded. The steps below are a sourced guide, not proof of safety or a family-tested recipe.'},
        ],
        'pairings': [], 'sources': turkey_sources,
        'safety': 'Read the severe-risk and emergency panels above, the complete guide and the actual unit manual. Do not begin if safe fit, fill, drying, equipment or outdoor conditions cannot all be achieved. Choose another cooking method instead.',
    },
]

ziti_recipe = {'id': 'baked-ziti',
 'title': 'Sausage & Beef Baked Ziti',
 'course': 'Main course',
 'seafood': [],
 'tags': ['Pasta', 'Ricotta', 'Italian sausage', '93/7 ground beef', 'Meatless alternative'],
 'time': 'Freshly assembled: about 35 min prep + 35–45 min bake + 10 min rest (sauce separately); make-ahead '
         'options below',
 'method': 'Oven · 375°F',
 'intro': 'A hearty baked ziti with 1 lb mild Italian sausage, 1 lb lean ground beef and pockets of ricotta. '
          'Keep the pasta and cheeses at the original amounts; use a deep 9×13-inch dish or divide between '
          'two dishes.',
 'ingredients': ['1 lb dry ziti',
                 '6 cups tomato sauce, measured before adding meat',
                 '1 lb mild Italian pork sausage, casings removed',
                 '1 lb 93/7 ground beef',
                 '15 oz whole-milk ricotta',
                 '12 oz low-moisture mozzarella, shredded and divided',
                 '½ cup grated Parmesan, divided',
                 '1 large egg',
                 'Salt and black pepper, to taste after adding sausage',
                 'Butter or oil, enough to lightly grease the baking dishes',
                 'Reserve 1 cup pasta water; use only as needed',
                 'Optional: chopped basil or parsley, to finish'],
 'equipment': ['Deep 9×13-inch baking dish or two smaller oven-safe dishes with room for the full batch',
               'Foil',
               'Large pasta pot and colander',
               'Mixing bowl',
               'Measuring jug',
               'Food thermometer',
               'Large skillet and saucepan'],
 'steps': ['Make the three-can Homemade Red Sauce below first. Heat the oven to 375°F. Grease a deep '
           '9×13-inch dish, or divide the batch between two smaller dishes. Leave space below the rims for '
           'bubbling; do not force the full batch into a shallow dish.',
           'Remove sausage casings. Brown the crumbled sausage and the ground beef in separate batches so '
           'each browns rather than steams, breaking up large pieces. Check each ground meat reaches 160°F, '
           'then drain excess fat. Keep the cooked meats aside while measuring the plain tomato sauce.',
           'Measure 6 cups tomato sauce before adding any meat: reserve ½ cup for the bottom and 1 cup for '
           'the top. Combine the remaining 4½ cups tomato sauce with all the cooked sausage and beef. Simmer '
           'gently 5–10 minutes. Taste and adjust salt only after the sausage is in the sauce. Keep it loose '
           'and spoonable; add a little water if it becomes too thick.',
           'Boil the ziti in salted water about 2 minutes less than the package al dente time. It should '
           'bend but still have a firm center. Reserve 1 cup pasta water, then drain without rinsing. Mix '
           'ricotta, egg, ¼ cup Parmesan and a little pepper; salt lightly, remembering the sausage and '
           'cheeses.',
           'Spread the reserved ½ cup plain sauce across the bottom of the dish (split evenly if using two). '
           'Toss all the pasta with all the meat sauce made from the 4½ cups tomato sauce. Loosen with '
           'reserved pasta water a little at a time if needed: every piece should be generously coated.',
           'Layer half the sauced pasta, half the ricotta in small dollops and half the mozzarella; repeat '
           'with the rest. Spoon the reserved 1 cup plain tomato sauce over exposed pasta and finish with '
           'the remaining ¼ cup Parmesan. When using two dishes, divide every component evenly between them '
           'and make the same two layers in each.',
           'Cover with foil, tented above the cheese. Bake at 375°F for 20 minutes, then uncover for 15–25 '
           'minutes, until the pasta is tender, sauce bubbles into the center and the cheese is browned in '
           'spots. Check the center of each dish reaches 165°F; allow more time if needed. Timing assumes '
           'freshly cooked pasta and warm sauce, not a chilled pan.',
           'Rest 10 minutes before serving. Finish with optional basil or parsley.',
           {'title': 'Same-day option 1: assemble, refrigerate, bake at dinner',
            'text': 'Works for the two-meat recipe or the meatless alternative using its own sauce amounts. '
                    'Cook the meats fully if using, then assemble through the layering step without baking. '
                    'For chilling a freshly assembled warm batch, divide between two shallow dishes rather '
                    'than holding a large deep hot casserole; cover and refrigerate promptly at 40°F or '
                    'below. Do not leave it on the counter to cool. Keep total time out of refrigeration '
                    'within 2 hours, or 1 hour above 90°F. Metal bakeware is the simplest choice: follow the '
                    'manufacturer’s directions for refrigerator-to-hot-oven use, especially glass or '
                    'ceramic, to avoid thermal shock. Do not assume a cold glass dish can go straight into a '
                    'hot oven. At dinner, remove any non-oven-safe wrapping, cover with foil and bake from '
                    'refrigerator-cold at 375°F for about 30–35 minutes covered, then 15–25 minutes '
                    'uncovered. These are starting estimates; dish depth and temperature vary. Check the '
                    'center of each dish reaches 165°F, with tender pasta and hot sauce throughout; continue '
                    'baking as needed and rest 10 minutes. Do not partially bake before chilling.',
            'sources': ['leftovers-storage', 'temps']},
           {'title': 'Same-day option 2: bake early, refrigerate, reheat portions',
            'text': 'Fully bake either version as directed until the center reaches 165°F. Promptly divide '
                    'into shallow portions or shallow containers for faster cooling and refrigerate at 40°F '
                    'or below. Refrigerate within 2 hours of cooking, or within 1 hour if exposed to '
                    'temperatures above 90°F; do not wait for a whole deep pan to cool on the counter. Cover '
                    'stored portions. At dinner, transfer chilled portions to suitable oven-safe dishes, add '
                    'a spoonful of reserved sauce or a splash of water and cover with foil. Reheat at 350°F: '
                    'allow roughly 20–30 minutes for small shallow portions as an initial estimate, with '
                    'more time for thicker or larger portions. Check several places with a food thermometer '
                    'until 165°F throughout; elapsed time and bubbling edges alone do not prove the center '
                    'is hot. Keep covered longer if needed to prevent drying, and follow the bakeware '
                    'manufacturer’s refrigerator-to-oven directions. These portion timings do not apply to '
                    'reheating a whole deep casserole.',
            'sources': ['leftovers-storage', 'leftovers-reheat']}],
 'note': 'Meatless alternative: taste and season the finished plain sauce with salt and pepper before '
         'measuring and assembling. Omit both meats and use 4½–5 cups plain tomato sauce with the same 1 lb '
         'pasta and unchanged cheeses/egg. Use ½ cup on the bottom, 3½ cups to toss with pasta, and ½–1 cup '
         'on top. Skip browning and the meat-sauce simmer; use a regular 9×13-inch dish and bake 20 minutes '
         'covered plus 15–20 uncovered, still to 165°F. Keep the three-can sauce batch and save extra sauce. '
         'Shopping adjustment: omit only the two meat items; other listed batch ingredients stay the same. '
         'Proposed recipe, not yet family-tested.'}

ziti_sauce = {'id': 'ziti-red-sauce',
 'title': 'Homemade Red Sauce for Baked Ziti',
 'course': 'Companion sauce',
 'seafood': [],
 'tags': ['Tomato', 'Basil', 'Flat-leaf parsley', 'Tuttorosso'],
 'time': 'About 10 min prep + 35–45 min cooking',
 'method': 'Stovetop · Gentle simmer',
 'intro': 'Three 28-oz cans of whole peeled tomatoes with proportionally scaled onion, garlic, basil and '
          'Italian flat-leaf parsley. Measure 6 cups for the two-meat ziti and save surplus.',
 'ingredients': ['3 (28 oz) cans whole peeled tomatoes, with all their juice',
                 '4½ tbsp olive oil',
                 '1½ medium onions, finely diced',
                 '6 garlic cloves, minced',
                 '6 tbsp chopped fresh Italian flat-leaf parsley',
                 '6 tbsp loosely packed fresh basil leaves, torn just before adding',
                 'Salt and black pepper, to taste (salt the ziti meat sauce after adding sausage)',
                 'Optional: pinch of red pepper flakes',
                 'Water or reserved pasta water, only as needed to adjust final consistency'],
 'equipment': ['Heavy saucepan or Dutch oven', 'Measuring jug', 'Spoon or potato masher'],
 'steps': ['Choose three 28 oz cans of regular Tuttorosso Peeled Plum Tomatoes or San Marzano-style whole '
           'peeled tomatoes, such as Tuttorosso Whole Peeled Pear Tomatoes with Basil & Sea Salt. Use '
           'whichever is a good value; no premium DOP tomatoes are required. Both options use the same '
           'method. Check the can for existing salt and basil.',
           'Crush the tomatoes in a bowl with your hands or a potato masher, keeping all can juices. For '
           'smoother sauce, briefly blend instead.',
           'Warm 4½ tbsp olive oil over medium-low heat. Soften the diced onion 8–10 minutes, stirring, '
           'without dark browning. Add garlic and optional pepper flakes; stir 30–60 seconds until fragrant.',
           'Add the tomatoes and all juices with a little pepper. Simmer gently, partly covered, about 25–35 '
           'minutes, stirring occasionally, until the onion is tender and raw tomato flavor has mellowed; '
           'this larger batch may need longer. Crush large pieces. Do not boil hard or reduce to a thick '
           'paste.',
           'Add the parsley and basil for the final 2–3 minutes. Measure 6 cups of loose, spoonable tomato '
           'sauce for the two-meat ziti before adding meat; save surplus for another meal or serving. Actual '
           'yield varies. If over-reduced below 6 cups, loosen gradually with water. Leave final salt '
           'adjustment of the meat sauce until after adding sausage.',
           'In the ziti recipe, reserve ½ cup plain sauce for the bottom and 1 cup for the top. Simmer all '
           'cooked meat in the remaining 4½ cups for 5–10 minutes. For the meatless alternative, use only '
           '4½–5 cups of this sauce and save the extra. Avoid an hours-long reduction or added tomato paste: '
           'baked pasta needs moisture.'],
 'note': 'Scaled 1½ times from the original two-can companion sauce: three cans, 4½ tbsp oil, 1½ onions, 6 '
         'garlic cloves and 6 tbsp each parsley and loosely packed basil. Measure the needed sauce rather '
         'than assuming a fixed yield; keep and save surplus. Original proposed adaptation, not a tested '
         'family recipe.'}

ziti_menu = {'id': 'baked-ziti',
 'title': 'Baked Ziti',
 'shortTitle': 'Baked Ziti · Comfort food',
 'eyebrow': 'Comfort food · Sausage & beef',
 'intro': 'Hearty baked ziti with mild Italian sausage, lean ground beef, ricotta, mozzarella and Parmesan, '
          'plus a homemade red sauce and clear meatless alternative.',
 'statValue': '375°F',
 'statLabel': 'oven temperature',
 'servings': '6–8',
 'quantitiesComplete': True,
 'noticeTitle': 'Two-meat version · one batch.',
 'notice': '1 lb dry ziti, 1 lb mild Italian sausage, 1 lb 93/7 ground beef and 6 cups tomato sauce measured '
           'before meat. Use a deep 9×13-inch dish or two smaller dishes. The shopping list follows this '
           'version; the recipe note explains the meatless alternative. Yield is approximate; not yet '
           'family-tested.',
 'shoppingGroups': {'Pasta, cheese & filling — two-meat batch': ['1 lb dry ziti',
                                                                 '1 lb mild Italian pork sausage, casings '
                                                                 'removed',
                                                                 '1 lb 93/7 ground beef',
                                                                 '15 oz whole-milk ricotta',
                                                                 '12 oz low-moisture mozzarella, shredded '
                                                                 'and divided',
                                                                 '½ cup grated Parmesan, divided',
                                                                 '1 large egg',
                                                                 'Salt and black pepper, to taste after '
                                                                 'adding sausage',
                                                                 'Butter or oil, enough to lightly grease '
                                                                 'the baking dishes',
                                                                 'Reserve 1 cup pasta water; use only as '
                                                                 'needed',
                                                                 'Optional: chopped basil or parsley, to '
                                                                 'finish'],
                    'Homemade sauce — three cans, save surplus': ['3 (28 oz) cans whole peeled tomatoes, '
                                                                  'with all their juice',
                                                                  '4½ tbsp olive oil',
                                                                  '1½ medium onions, finely diced',
                                                                  '6 garlic cloves, minced',
                                                                  '6 tbsp chopped fresh Italian flat-leaf '
                                                                  'parsley',
                                                                  '6 tbsp loosely packed fresh basil leaves, '
                                                                  'torn just before adding',
                                                                  'Salt and black pepper, to taste (salt the '
                                                                  'ziti meat sauce after adding sausage)',
                                                                  'Optional: pinch of red pepper flakes',
                                                                  'Water or reserved pasta water, only as '
                                                                  'needed to adjust final consistency']},
 'storageKey': 'recipebook-baked-ziti-two-meat-shopping-v1',
 'exportName': 'baked-ziti-checklist.txt',
 'shoppingTab': 'Shopping list',
 'shoppingTitle': 'Shop for the two-meat ziti and homemade sauce.',
 'shoppingIntro': 'One batch: both meats, unchanged pasta/cheeses, and a three-can homemade sauce. Do not '
                  'also buy prepared sauce. Measure 6 cups sauce before meat and save surplus. For meatless, '
                  'omit both meat items, use 4½–5 cups sauce and save more surplus. Shared oil, salt, pepper '
                  'and garnish are not consolidated. Checks stay in this browser.',
 'exportNote': 'Two-meat batch: 1 lb ziti + 1 lb mild Italian sausage + 1 lb 93/7 beef; unchanged cheeses. '
               'Three 28 oz tomato cans make sauce: measure 6 cups before meat, save surplus. Deep 9×13 or '
               'two dishes. Meatless: omit both meats, use 4½–5 cups sauce; remaining shopping amounts '
               'unchanged. Shared seasonings are not consolidated.',
 'prepIntro': 'Start the three-can sauce first. While it simmers, brown the meats separately, heat the oven '
              'and prepare the cheeses. Allow about 100–120 minutes from scratch including the rest, '
              'depending on equipment and overlap. Bake with warm sauce and freshly cooked pasta. For '
              'same-day make-ahead, choose one of the two fully described options at the end of the ziti '
              'method; both also apply to the meatless alternative.',
 'prep': [{'title': 'Start the three-can sauce',
           'text': 'Soften onion, add garlic, then gently simmer crushed tomatoes and juices. Add parsley '
                   'and basil late. Measure 6 cups plain sauce; save surplus. Reserve ½ cup for the bottom '
                   'and 1 cup for the top.'},
          {'title': 'Brown both meats and simmer',
           'text': 'Remove sausage casings. Brown 1 lb sausage and 1 lb 93/7 beef in separate batches to '
                   '160°F each; drain excess fat. Combine with the remaining 4½ cups measured tomato sauce '
                   'and simmer 5–10 minutes. Taste for salt after sausage.'},
          {'title': 'Pasta, filling and layers',
           'text': 'Cook 1 lb ziti 2 minutes short of al dente; reserve pasta water. Mix ricotta, egg and '
                   'half the Parmesan. Grease a deep 9×13 or two dishes. Bottom sauce, two layers of '
                   'meat-sauced pasta/ricotta/mozzarella, top sauce and remaining Parmesan.'},
          {'title': 'Bake and rest',
           'text': '375°F: 20 minutes covered, then 15–25 minutes uncovered. Check every dish reaches 165°F '
                   'in the center and pasta is tender. Rest 10 minutes. Meatless adjustments are in the '
                   'recipe note.'},
          {'title': 'If dinner is later: choose one make-ahead path',
           'text': 'Either assemble and promptly refrigerate in shallow dishes at 40°F or below, then bake '
                   'refrigerator-cold at 375°F (about 30–35 minutes covered plus 15–25 uncovered, always to '
                   '165°F); or fully bake now, divide into shallow portions and refrigerate promptly, then '
                   'reheat covered portions at 350°F to 165°F throughout. Follow the complete cooling, '
                   'time-limit and bakeware instructions in the recipe.'}],
 'notes': [{'title': 'Recipe provenance',
            'text': 'Original assistant-proposed recipe, updated November 14, 2026 for the owner-approved '
                    'two-meat version. Quantities and yield are proposed, not inherited family measurements '
                    'or a tested result. Pasta and cheese amounts are unchanged.'},
           {'title': 'Sauce quantity and consistency',
            'text': 'Measure 6 cups tomato sauce before adding meat. Reserve ½ cup bottom sauce and 1 cup '
                    'top sauce; the remaining 4½ cups become meat sauce. Three cans provide a margin for '
                    'variation: save extra rather than reducing it all down to 6 cups. Loosen overly thick '
                    'sauce with water.'},
           {'title': 'Meatless alternative and shopping',
            'text': 'The recipe note preserves the original meatless base with 4½–5 cups sauce and the same '
                    'pasta, cheeses and egg. The grocery list defaults to the two-meat batch: omit its two '
                    'meat items for meatless. Keeping the three-can sauce recipe avoids a second confusing '
                    'shopping list; save unused sauce. This version uses a fresh checklist key because the '
                    'shopping quantities changed.'},
           {'title': 'Sauce research and choices',
            'text': 'Linked published methods informed the original companion sauce, now scaled '
                    'proportionally from two cans to three. The requested onion, garlic, Italian flat-leaf '
                    'parsley and basil remain. Regular Tuttorosso and San Marzano-style whole peeled '
                    'tomatoes both work; no price or local-stock claim is made.'},
           {'title': 'Same-day make-ahead: safety versus timing',
            'text': 'Both options apply to the two-meat and meatless versions without changing their '
                    'ingredient amounts or shopping list. USDA supports prompt refrigeration, shallow '
                    'containers, 40°F storage, the 2-hour/1-hour limits and checking reheated leftovers in '
                    'several places to 165°F. The suggested 375°F cold-bake and 350°F portion-reheat oven '
                    'schedules are practical estimates, not USDA timing guarantees; the thermometer decides. '
                    'Follow your bakeware maker for thermal-shock restrictions.'}],
 'pairings': [],
 'sources': [{'id': 'temps',
              'url': 'https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures',
              'label': 'FoodSafety.gov · Safe minimum internal temperatures',
              'detail': 'Checked November 14, 2026. Supports 160°F for ground meat and pork sausage, and '
                        '165°F for casseroles and reheated leftovers. Recipe quantities and bake times are '
                        'proposed cooking guidance.'},
             {'id': 'regular-tomatoes',
              'url': 'https://tuttorossotomatoes.com/products/detail/peeled-plum-tomatoes',
              'label': 'Tuttorosso · Regular Peeled Plum Tomatoes',
              'detail': 'Manufacturer identifies the regular 28 oz whole peeled tomato option. Check the '
                        'actual can for ingredients and seasoning.'},
             {'id': 'style-tomatoes',
              'url': 'https://tuttorossotomatoes.com/products/detail/san-marzano-style-whole-peeled-pear-tomatoes-with-basil-sea-salt-28-oz',
              'label': 'Tuttorosso · San Marzano Style Whole Peeled Pear Tomatoes',
              'detail': 'Manufacturer identifies the 28 oz whole peeled option with basil and sea salt; '
                        'reduce added salt to taste.'},
             {'id': 'sauce-method',
              'url': 'https://www.seriouseats.com/easy-italian-amercian-red-sauce-recipe',
              'label': 'Serious Eats · Quick Italian-American Red Sauce',
              'detail': 'Research reference for a quick sauce using two cans of whole peeled tomatoes. The '
                        'companion recipe uses its own quantities and the requested herbs, and omits tomato '
                        'paste.'},
             {'id': 'late-basil',
              'url': 'https://tuttorossotomatoes.com/recipes/detail/marinara-sauce',
              'label': 'Tuttorosso · Marinara Sauce',
              'detail': 'Research reference for adding fresh basil toward the end. Its chopped-tomato and '
                        'prepared-sauce formula is not reproduced here.'},
             {'id': 'leftovers-storage',
              'url': 'https://ask.fsis.usda.gov/article/How-do-I-handle-leftovers-safely',
              'label': 'USDA FSIS · How do I handle leftovers safely?',
              'detail': 'Checked November 14, 2026. Prompt refrigeration at 40°F or below, shallow '
                        'containers, and no more than 2 hours out (1 hour above 90°F).'},
             {'id': 'leftovers-reheat',
              'url': 'https://ask.fsis.usda.gov/article/How-do-I-reheat-leftovers-safely',
              'label': 'USDA FSIS · How do I reheat leftovers safely?',
              'detail': 'Checked November 14, 2026. Check several places with a food thermometer for 165°F '
                        'throughout. The oven temperatures and timing estimates here are editorial cooking '
                        'guidance.'}],
 'safety': 'Use a food thermometer: ground pork sausage and ground beef each reach 160°F before combining; '
           'the finished casserole and reheated leftovers reach 165°F. Check each baking dish. See '
           'FoodSafety.gov in Source & notes.'}
ziti_menu['recipes'] = [ziti_recipe, ziti_sauce]
menus.append(ziti_menu)
