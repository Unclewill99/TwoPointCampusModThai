# WO-SARA-AM-LIG-001 — runtime report

2026-10-26 (Asia/Bangkok). Tester: ChatGPT, explicitly authorized by the user to perform this run in place of Antigravity. **Verdict: EXECUTED.** BUG-THAI-003 remains **OPEN** pending PM acceptance/analysis. This deliberately wrong sentinel is not a Thai shaping fix.

## Result and evidence

**VERIFIED — observation:** one variant, one Steam launch, one campaign entry. Opening-course modal displayed all five labels. L1 contains a single ก-shaped glyph matching the visible L5 reference; L2–L4 retain their control sequences, without a sentinel replacement. No blank/tofu, missing row or crash observed. All five rows fit inside the blue specimen area without automatic wrapping or clipping; a larger gap before L4 is visible. Modal was not dismissed and tutorials were not advanced.

| Row | Built specimen | Visible result | Assessment |
|---|---|---|---|
| L1 | ต่ำ — `U+0E15 U+0E48 U+0E33` | `L1: ก`, one sentinel glyph | VERIFIED target substituted |
| L2 | ต้ำ — `U+0E15 U+0E49 U+0E33` | `L2: ต้ำ`, no ก sentinel | VERIFIED negative sequence intact |
| L3 | ค่ำ — `U+0E04 U+0E48 U+0E33` | `L3: ค่ำ`, no ก sentinel | VERIFIED negative sequence intact |
| L4 | ตา ถี่ — `U+0E15 U+0E32 U+0020 U+0E16 U+0E35 U+0E48` | `L4: ตา ถี่`, vowel/tone control visible | VERIFIED ordinary sequences intact |
| L5 | ก — `U+0E01` | `L5: ก`, visible standalone sentinel | VERIFIED glyph reference available |

**VERIFIED — original evidence:** `local/qa/WO-SARA-AM-LIG-001/01-modal-native.png`, native **3840×2160**, 6,972,358 bytes, SHA256 `82bada62d034ac67143153a528f611185facbea316a93488b10fd6ba6f6cc377`. One primary native PNG retained; no failure-screen PNG needed. The image was saved without resizing. Computer Use navigation observations were 1920×1080; the native file viewer displayed a reduced preview, not a replacement evidence file.

**VERIFIED — comparison limit:** matching L1/L5 is a visual character-shape observation, not a pixel-identity claim. Native thresholded glyph measurements are L1 bbox `[1918,786,1934,806)` (16×20, 138 dark pixels), L5 `[1920,1008,1936,1029)` (16×21, 142 dark pixels), using all RGB channels <100. Masks are not identical. See `local/qa/WO-SARA-AM-LIG-001/sentinel-comparison.json`; no image was edited. **UNKNOWN:** cause of the small raster difference. Negative controls were assessed as intact visible character sequences, not through pixel comparison against an identical baseline screen.

**INFERRED — interpretation:** this meets the WO's EXECUTED criterion and supports consumption of the exact serialized `[118,42,82] → 29` three-component ligature in this modal context. **UNKNOWN:** exact internal implementation, runtime fallback/asset identity, active-feature state elsewhere and exact package/fork version. This does not demonstrate correct ต่ำ rendering, new/appended-glyph loading, global ligature support or production safety. No further run/build was performed.

## Geometry, guard and navigation

**VERIFIED:** game build visible in main menu: `10.3.169253+2024-12-06.1241`; Steam AppID1649080. Returned window `462646`, PID9076; exact owner path `D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe`, one matching window. Native display3840×2160, origin(0,0), window rect(0,0,3840,2160). Normalized input uses `(native_x*1920/W, native_y*1080/H)`; here native coordinates equal twice the 1920×1080 observation coordinates. Targets were derived from fresh images, not reused historical points.

| Action | Fresh observed 1920-space bounds | Normalized target | Native target | Observed hover / checked acceptance |
|---|---|---|---|---|
| Main-menu Continue | `[82,393,466,446]` | `(274.0,420.0)` | `(548,840)` | Pointer/hand on Continue, then one click |
| Existing campaign Continue | `[111,814,335,889]` | `(223.0,851.0)` | `(446,1702)` | Green Continue brightened, then one click; Restart untouched |

**VERIFIED:** every fresh driver subprocess called `qa_driver.set_desktop()` before window/foreground/cursor queries or capture/input, then unique-window and exact-owner foreground guards. Driver SHA256 `6e243c022dfb80e5e13431dbadba917415c475daeb78e74994c05f282dfff78d`. Each hover move passed the driver's `SendInput == 1` check. Each click passed move1/down1/up1 checks; these are acceptance checks, not proof of navigation by themselves. Fresh screens confirmed navigation. No pointer-injection error after owner validation; **focus recoveries: 0/1**.

**VERIFIED — setup errors, no bypass:** `sky.launch_app(steam://rungameid/1649080)` reported “launched app did not expose a targetable window.” A subsequent fresh window listing found the running game; no second launch was issued. The restricted Python context could not open/query the game's process and returned no guarded windows; no input was sent there. The same unmodified exact-path guard succeeded under approved host execution and verified the foreground game. No guard code was weakened. Launch discovery and process-query limitation did not require a focus recovery.

## Natural wait and deviations

**VERIFIED:** after campaign Continue, no key/click/skip was sent during loading/flyover. Timestamps are observations, not exact transition times. Campaign click completion recorded Unix1792998011.338435.

| Elapsed after campaign click | Observation |
|---|---|
| 0.224s | Loading transition |
| 18.360s | Campus flyover |
| 40.271s | Campus flyover |
| 51.057s | Diagnostic modal, L1–L5 present |

**VERIFIED — cadence deviation:** observation intervals were **18.136s, 21.911s, 10.786s**. The first two exceed the WO's maximum15s; orchestration/call spacing was not kept within that requirement. This is an explicit procedural deviation for PM review, not a claim of full timing compliance. The modal was first observed within60s, then waiting stopped. Original native capture was saved at elapsed74.895s, after modal recognition; that is capture time, not claimed modal appearance time. No rerun was used to conceal/correct cadence.

**VERIFIED:** launch-through-exit/restoration confirmation interval was approximately279s (4m39s), below10 minutes for the runtime interval. Setup/report-writing duration was not separately timed. Normal exit and restoration were prioritized.

## Lifecycle and hashes

Executed outputs, transcribed from tool results:

| Step | Result |
|---|---|
| `manage_probe.py check --probe probe-sara-am-lig-001` | VERIFIED original/original/original |
| `backup_gameplay_saves.py` | VERIFIED `verified=true`, 11 files |
| `manage_probe.py install --probe probe-sara-am-lig-001` | VERIFIED probe/probe/probe |
| Post-install `check` | VERIFIED probe/probe/probe; staged and installed hashes matched manifest |
| Steam launch / entry | VERIFIED one variant/run; main Continue once, campaign Continue once |
| Exit | VERIFIED normal Alt+F4, no modal-dismiss input; `campus_running=false`, driver windows `[]`, Computer Use windows `[]` |
| `manage_probe.py restore --probe probe-sara-am-lig-001` | VERIFIED original/original/original; manager game-closed guard passed |
| Final `check` | VERIFIED original/original/original |

**UNKNOWN:** Computer Use does not expose an input acceptance count for Alt+F4; process absence verifies exit independently. No forced termination or settings/UI-scale change. No building, hiring, spending, year start or tutorial advancement input.

**VERIFIED — bundle hashes:** exact original/staged hashes are retained in `reports/sara-am-lig-001-runtime.json:staged_files`, the candidate manifest, and the build report. Final checks re-hashed all17 protected files from WO005's before snapshot (frozen005/001a/b, installed originals, GameAssembly.dll and global-metadata.dat); all match. Staged bundles also still match the manifest. Detailed expected/actual hashes: runtime JSON `protected_final`. This WO did not rebuild or modify the diagnostic probe.

## Save comparison and retained backup

**VERIFIED:** backup ZIP `local/backups/gameplay-save-snapshots/20261026T065651657176Z.zip`, manifest same stem `.json`. ZIP SHA256 `189f39b04387d89f135e50b773f4b07b8cf2d7ebde0818d392ef02221a26bd5f`; manifest SHA256 `f64f1243e05e9bcb40d58b7625f7b35f7e06b6d6823ca2aceda8305dde8fc3b2`. Backup tool read back every ZIP entry and reported verified=true before installation.

**VERIFIED:** before11/after11 save-related files: **7 changed, 4 unchanged, 0 new, 0 missing**. Unchanged: Slot1/8000.sav, preferences.json, steam_autocloud.vdf and localpreferences.json. Changed: career.csav, career.csav.2.bak through .6.bak, userprofile.sav. Full before/after hashes are in `local/qa/WO-SARA-AM-LIG-001/save-comparison.json` and runtime JSON. **UNKNOWN:** semantic contents of changed career/profile files; hash differences are not asserted to be harmless or rolled back. All live saves and the verified backup were retained. No save deletion/rollback or Cloud edits.

## Delivery boundary

**EXECUTED — pending PM acceptance.** Evidence summary: `reports/sara-am-lig-001-runtime.json`; original image and local measurement/save JSONs under `local/qa/WO-SARA-AM-LIG-001/`. Installed originals restored and game closed. No commit/push, automation, agent dispatch or additional runtime WO. Stop here; BUG-THAI-003 remains OPEN.
