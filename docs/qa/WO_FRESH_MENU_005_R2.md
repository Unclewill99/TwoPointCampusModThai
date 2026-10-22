# WO-FRESH-MENU-005-R2 — Mod destination only

2026-10-22. Assigned to Antigravity. READY_FOR_HANDOFF; receipt not confirmed. Controller does not operate game UI. User authorized continuation after partial result.

## Inputs and acceptance

Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod. Read WO_FRESH_MENU_005.md, WO_FRESH_MENU_005_REPORT.md and ../FRESH_MENU_005_DISPOSITION.md. Use unchanged fresh-translation-005; verify all three hashes using local/prototype/fresh-translation-005/manifest.json and reports/fresh-translation-005-build.json. Localisation SHA256 74a3c5ef4466df886f6ee432f4bb02a136dd7b5377d6ed220b4770fd75d8565a. No rebuild or text changes.

Main-menu Mod label already PASS. Only remaining target: click that actual button once, verify Mod management opens, capture actual heading and note shared-key wording if visible. No installation, downloads, activation/deactivation of mods, login, subscription or setting changes. No Settings/campus/staff testing. No broad rendering approval.

## Corrected target selection and mapping

Before installation, review mapping without launching the game: qa_driver.click/move_mouse expects coordinates in a normalized 1920x1080 full-primary-display space. to_phys scales by current GetSystemMetrics dimensions. For an ORIGINAL full-display capture W x H, a visually selected point (xc,yc) maps to driver (xc*1920/W, yc*1080/H). Retain capture dimensions and selected button rectangle in the report. Never pass native 3840x2160 coordinates directly to this driver, and never scale an already normalized point twice. For window-bounded screenshots, a different tool or explicit verified origin mapping is needed; do not apply this formula blindly. If full-display origin/geometry cannot be established, stop before installation with SETUP_LIMIT.

Previous recovery coordinates (1856,48) are consistent with halving (3712,96) on 3840x2160. Their failure does NOT prove a scaling bug. No speculative driver patch or claim that pointer control is fixed. Identify actual target from fresh pixels, not color-band order, negative indexes, historical coordinates, or filename. Do not use bands[-3] or a partial vertical search.

After launch, select the unique process-owned TPC.exe window at D:/SteamLibrary/steamapps/common/Two Point Campus/TPC.exe; activate and verify foreground and actual menu pixels. Save fresh menu observation. Identify the button visibly labeled Mod between Sandbox and Settings, state its rectangle/center and coordinate mapping BEFORE input. If the tool supports pointer-only movement, move to its center and verify cursor/hover is on Mod before the one click; do not click to calibrate. No sweeps. Use a fresh observation if layout/focus changes.

Click verified Mod once and capture result. If wrong screen appears, record actual screen and stop input; do not recover by guessing a close-button location. A valid guard result alone is not destination proof. No repeated trial clicks. Maximum 5 minutes after menu ready, two primary evidence images (menu and resulting destination), one recovery only for focus/target acquisition before the click. Restore/exit takes priority over budget.

## Lifecycle — separate steps, inspect each result

1. With game closed: `python tools/manage_probe.py check --probe fresh-translation-005` requires three originals.
2. `python tools/backup_gameplay_saves.py` requires verified=true; record fresh ZIP/manifest.
3. `python tools/manage_probe.py install --probe fresh-translation-005`.
4. `python tools/manage_probe.py check --probe fresh-translation-005` requires three probe files.
5. Launch through Steam, reacquire process/window identity, perform only target above.
6. Exit normally via visible controls or Alt+F4/WM_CLOSE; no force termination. Confirm TPC.exe absent. If blocked, report immediately, do not bypass guard.
7. `python tools/manage_probe.py restore --probe fresh-translation-005`.
8. `python tools/manage_probe.py check --probe fresh-translation-005` requires three originals.

Always restore after installed paths, including setup failures. Keep live saves and verified backup, compare changed/new/missing hashes, no rollback/delete/Cloud changes. No commit/push.

## Delivery

Write NEW docs/qa/WO_FRESH_MENU_005_R2_REPORT.md; original images under local/qa/WO-FRESH-MENU-005-R2/. Preserve first report/images. Include candidate hashes, build, tools, capture size/origin/display geometry, selected Mod rectangle, native and input coordinates and conversion, pre-click target evidence, destination actual heading, elapsed/recovery count, lifecycle and save comparison. Verdict DESTINATION_PASS / SETUP_LIMIT / INCONCLUSIVE / OBSERVED_DEFECT; a wrong click is not a routing defect. Known Thai shaping/wrapping bugs stay open. Stop after report for Controller acceptance.
