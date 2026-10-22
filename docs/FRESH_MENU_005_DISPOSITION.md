# WO-FRESH-MENU-005 — Controller disposition

Follow-up review: full report specifies native recovery (3712,96) converted to driver (1856,48), consistent with qa_driver's 1920x1080 normalized contract. Previous scaling concern was a hypothesis, not a confirmed defect. User subsequently authorized continuation; revised destination-only WO is docs/qa/WO_FRESH_MENU_005_R2.md. Do not repeat the previous band-index selection.

2026-10-22. ACCEPT_PARTIAL_RESULT / SETUP_LIMIT. Controller read Antigravity report and directly inspected both retained images, without launching or controlling the game.

- Main-menu label PASS: 01-main-menu.png shows exact Mod, centered and without obvious clipping, blank text or raw tags. User-approved menu wording is integrated and visually verified in fresh-translation-005.
- Destination NOT_RUN / INCONCLUSIVE: 02-mod-screen.png actually shows โหลดเกม (Load Game), not Mod management. Filename is not destination evidence. No new translation or button-routing defect established because the intended Mod button was not clicked.
- Tester reports truncated color-band search and bands[-3] selected the wrong button. Recovery used (1856,48) against a 3840x2160 capture; coordinate-space mismatch is a plausible additional issue, not independently established from these two images. Do not repeat index-based selection or reuse 1920x1080 coordinates against full-resolution capture without an explicit mapping.
- Independent manage_probe.py check confirms all three game bundles original. Tester reports normal exit and unchanged 11 save files; save comparison not independently rerun in this review.
- No new candidate/rebuild or repeat installation authorized by this disposition. Any destination retest requires a revised WO with visually identified target and explicit capture-to-input coordinate mapping. Existing recovery budget is exhausted.

No whole-candidate runtime, font/shaping, staff screen or full translation approval. Known BUG-THAI-002/003 and broader BUG-THAI-001 regression tracking remain open.
