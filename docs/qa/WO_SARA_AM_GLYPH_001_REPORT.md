# WO-SARA-AM-GLYPH-001 — runtime report

2026-10-26 (Asia/Bangkok). Tester: **ChatGPT**, continuing the user's explicit authorization to test in place of Antigravity. **Verdict: STACKED_OK**, pending PM acceptance. BUG-THAI-003 stays **OPEN**; this is one diagnostic cluster/modal, not a production fix.

## Observed result

**VERIFIED — visual:** opening-course modal displays all five labels. L1 shows ต่ำ with a complete base and sara-aa, ring below a raised tone, and a visible gap. No visible top truncation, blank/tofu, abnormal extra spacing, row clipping or wrapping. L2/L3 retain the old crowded form. L4 and L5 are ordinary controls. No modal dismissal, tutorial advancement or other gameplay action.

| Row | Exact specimen | Observation / classification |
|---|---|---|
| L1 | ต่ำ — `U+0E15 U+0E48 U+0E33` | VERIFIED: complete stacked cluster, tone above ring with gap; normal visual base/aa baseline. Class(a). |
| L2 | ต้ำ — `U+0E15 U+0E49 U+0E33` | VERIFIED: original crowded tone/ring; negative control intact. |
| L3 | ค่ำ — `U+0E04 U+0E48 U+0E33` | VERIFIED: original crowded tone/ring; negative control intact. |
| L4 | ตา ถี่ — `U+0E15 U+0E32 U+0020 U+0E16 U+0E35 U+0E48` | VERIFIED: ordinary base/vowel/tone control, unchanged placement. |
| L5 | ทำ — `U+0E17 U+0E33` | VERIFIED: untoned sara-am ordinary; base/aa baseline normal. Deliberately differs from LIG-001's ก. |

**INFERRED — bounded conclusion:** with the unchanged probe's only target `[118,42,82]→459`, the expected new composite appears while the two negative clusters remain crowded. This supports loading/drawing the appended glyph through this exact ligature in this modal. **UNKNOWN:** exact native code path, package/fork/fallback identity, behavior in other consumers/scales, repeated loading/atlas stress or production safety. No generalized Thai-shaping conclusion.

## Native image and derived inspection

**VERIFIED:** original `local/qa/WO-SARA-AM-GLYPH-001/01-modal-native.png`, **3840×2160**, 6,974,098 bytes; SHA256 `993a727d8485dbb21983b7242499cb2cbe06b2a67c74730aebd0376765372cfb`. Exactly **one primary native capture**. Derived files from this image only:

- `02-derived-specimens-native.png`: crop `(1780,750)–(2020,1050)`,240×300 at1×; no interpolation.
- `03-derived-specimens-4x-nearest.png`: same crop at4× **NEAREST**,960×1200. No extra game capture.

**VERIFIED — comparison to saved LIG-001:** source image `local/qa/WO-SARA-AM-LIG-001/01-modal-native.png`, SHA256 `82bada62d034ac67143153a528f611185facbea316a93488b10fd6ba6f6cc377`. Pixel comparisons on aligned native control regions:

| Control | Native crop `[left,top,right,bottom)` | Changed RGB pixels |
|---|---|---:|
| L2 | `[1820,815,1980,875)` | 0 |
| L3 | `[1820,875,1980,935)` | 0 |
| L4 | `[1800,940,2000,996)` | 0 |

**VERIFIED — ROI boundary note:** an initial L4 region ending998 included3 changed antialias pixels from the *new L5 word* at y997. The final L4-only region ends996, includes L4's complete visible ink/edge, and excludes L5. Both measurements are retained (`pixel-comparison.json`, `tone-clipping-check.json`, `aligned-controls-comparison.json`); no image alteration or hidden resampling.

**VERIFIED — tone/ring separation:** threshold all RGB channels<100 gives L1 Thai bands y765–771 (tone),777–781 (ring),785–805 (base/aa), inclusive. There are5 rows between dark tone/ring bands (y772–776). Antialias-inclusive threshold<180 yields tone764–772, ring776–782, body785–806, retaining3 intervening rows. These are threshold-dependent pixel measurements, not universal gap requirements.

**VERIFIED — explicit top-clipping observation:** no visible truncation or contact with the modal/crop boundary. At threshold100, L1 tone bbox`[1922,765,1925,772)` and L4 tone bbox`[1959,950,1962,957)` both have3×7 dark-pixel extent; masks are not identical (21 versus18 dark pixels). At threshold180 L1 spans9 rows and L4 spans7; no pixel-equivalence claim. **UNKNOWN:** subpixel contour equivalence or clipping at other scales. The known22-unit ascent excess was left unmodified; no metrics were raised.

**VERIFIED — width/baseline/line assessment:** L1 Thai visible ink width33 native pixels versus L2=34 and L3=33; no conspicuous extra gap or displaced sara-aa. The first prefix shifts horizontally relative to the earlier single ก sentinel, consistent with a different centered text width. **UNKNOWN:** true pen advance from a screenshot alone (offline nominal1056 units remains a build fact, not a runtime measurement). L2–L4 pixel-identical regions retain their previous baseline/line positions; all5 rows fit without wrap. L5 label remains on its previous line, though its text is intentionally different. The pre-existing larger gap before L4 persists. No generalized line-height approval.

## Geometry, ownership and input

**VERIFIED:** one matching window HWND528388, PID29476, exact owner `D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe`. Native display3840×2160, origin(0,0), window rect(0,0,3840,2160); Computer Use observation1920×1080. Mapping: normalized=`(native_x*1920/W,native_y*1080/H)`; here native=2× observed1920 coordinates. Game version visible in main menu: `10.3.169253+2024-12-06.1241`.

| Action | Fresh observed1920 bounds | Normalized target | Native target | Execution |
|---|---|---|---|---|
| Main Continue | `[82,393,466,446]` | `(274,420)` | `(548,840)` | Hover/hand verified, one click |
| Existing Slot1 Continue | `[111,814,335,889]` | `(223,851)` | `(446,1702)` | Green hover brightening verified, one click; Restart untouched |

**VERIFIED:** every fresh driver subprocess called `set_desktop()` before queries/capture/input, then unique-window/exact-owner/foreground guard. Driver SHA256 `6e243c022dfb80e5e13431dbadba917415c475daeb78e74994c05f282dfff78d`. Each hover passed move1/1; each click passed move1/down1/up1 acceptance checks. Actual navigation verified separately from screens. No pointer/foreground input error, **0/1 focus recoveries**, no guard changes/bypass. Host execution was used so the unmodified guard could query the actual process, as established in LIG-001.

**VERIFIED — launcher discovery error:** Computer Use launch via `steam://rungameid/1649080` reported “launched app did not expose a targetable window.” Fresh listing immediately found the unique correct running game. Only one launch was issued; no retry/relaunch or extra candidate. This discovery error is recorded, not counted as a focus recovery.

## Natural wait / actual cadence

**VERIFIED:** no skip/click/key after campaign Continue until normal exit following capture. Campaign click completion Unix1793000004.9424655. A timed observation loop produced the following snapshots without input:

| Elapsed seconds | Observed state |
|---:|---|
| 0.226 | Loading transition |
| 6.411 | Loading card |
| 13.114 | Loading transition |
| 19.823 | Campus flyover |
| 26.538 | Campus flyover |
| 33.255 | Campus flyover |
| 39.961 | Campus flyover |
| 46.656 | Campus, no modal |
| **53.346** | Modal with L1–L5 |

**VERIFIED:** actual intervals **6.185,6.703,6.709,6.715,6.717,6.706,6.695,6.690 seconds**, all≤15s. Modal first observed within60s; this is observation time, not exact appearance time. Waiting stopped on that observation. Native PNG saved at elapsed73.288s after recognition; that later value is capture time. Launch-through-exit/restoration confirmation approximately211.226s (3m31s). No cadence deviation this run; setup/report-writing duration was not separately timed.

## Lifecycle, integrity and save comparison

| Step | Executed output |
|---|---|
| Initial `manage_probe.py check --probe probe-sara-am-glyph-001` | VERIFIED original/original/original |
| `backup_gameplay_saves.py` | VERIFIED true,11 files; backup before install |
| `manage_probe.py install --probe probe-sara-am-glyph-001` | VERIFIED probe/probe/probe |
| Post-install check | VERIFIED probe/probe/probe; expected manifest hashes |
| Steam launch and navigation | VERIFIED one run/variant; two Continue clicks total |
| Normal exit | VERIFIED Alt+F4, no modal dismiss; manager process guard subsequently confirms closed |
| `manage_probe.py restore --probe probe-sara-am-glyph-001` | VERIFIED original/original/original |
| Final check | VERIFIED original/original/original; `campus_running=false`, driver windows`[]`, Computer Use game windows`[]` |

**UNKNOWN:** Alt+F4 acceptance count is not exposed by Computer Use; normal exit was independently confirmed by process absence. No forced termination. Exit/restore completed before report work.

**VERIFIED:** all21 protected files match their WO006 before hashes (required17 plus lig-001 bundles/manifest), and all3 staged glyph-probe bundles still match the manifest. Full original/staged/parent/object/font hashes remain in build manifest/report; final staged and protected hashes are in `reports/sara-am-glyph-001-runtime.json`. No rebuild/probe edit, metrics/Settings/UI-scale change or other-variant/original run.

**VERIFIED — retained backup:** `local/backups/gameplay-save-snapshots/20261026T073110682749Z.zip`, manifest same stem`.json`. ZIP SHA256`6959a23461951765c74942ec73be9d9ed45d57b72967e596d5f64bbd3a43e78d`; manifest SHA256`635420bc10f26f33f44ff063a267d83ab361a4663c1bdaab28713b1b1cc6cd67`. Backup tool verified every ZIP entry before install.

**VERIFIED — saves:** before11/after11:7 changed,4 unchanged,0 new,0 missing. Slot1/8000.sav unchanged SHA256`5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d`; preferences.json, steam_autocloud.vdf and localpreferences.json also unchanged. Changed: career.csav, career.csav.2.bak–.6.bak, userprofile.sav. **UNKNOWN:** semantic contents/impact of those changes; no harmlessness claim. Full before/after hashes in `local/qa/WO-SARA-AM-GLYPH-001/save-comparison.json` and runtime JSON. Both live saves and backup retained; no rollback, deletion or Cloud edits.

## Delivery boundary

**STACKED_OK — pending PM acceptance.** `reports/sara-am-glyph-001-runtime.json` contains machine-readable evidence. One primary capture plus two permitted derived crops. Game closed; originals restored. No build/spend/hire/year-start/tutorial progression, runtime WO/agent dispatch, automation, commit or push. Stop after this report. BUG-THAI-003 remains OPEN for PM's bounded next decision.
