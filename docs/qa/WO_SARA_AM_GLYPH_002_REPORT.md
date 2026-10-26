# WO-SARA-AM-GLYPH-002 — runtime report

2026-10-26 (Asia/Bangkok). Tester: **ChatGPT**, acting under the user's explicit authorization to replace Antigravity. **Verdict: INCONCLUSIVE — protocol timing deviation.** BUG-THAI-003 remains **OPEN**, pending PM analysis. One diagnostic run; no production acceptance.

## Findings and blocker

**VERIFIED — visual:** the saved opening-course modal contains the exact L1–L5 specimen. All 15 target clusters are individually class **a** in this image. Their tones are above the rings with visible separation; base/sara-aa placement is visually normal. Each tone-top region was inspected in the native image's nearest-neighbour enlargement: none visibly truncates, touches the line/crop boundary, overlaps a neighbour or disappears. No tofu, missing component, wrapped row or clipped row is visible. This is bounded visual evidence at the observed scale, not a contour-level guarantee.

**VERIFIED — protocol deviation:** the observation loop has a **110.319-second gap**, exceeding the required15 seconds. The later modal observations and capture occurred after the60-second limit; the required60-second stop/failure-screen path was not followed. **UNKNOWN:** when the modal appeared, and whether it appeared within60 seconds. The execution was interrupted/delayed across this gap; the exact source of the delay is not established. Consequently this report does **not** claim ALL_STACKED_OK as the WO verdict despite the15 visually successful targets. No second run was performed. PM must decide the disposition of this evidence/timing deviation before any further runtime work.

## Individual observations

All entries below are **VERIFIED — visual** at this captured modal. Class a means complete visible stacked form; it does not prove the internal renderer path.

| Row | Target | Atomic codepoints | Class | Observation |
|---|---|---|---|---|
| L1 | น้ำ | `U+0E19 U+0E49 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L1 | ซ้ำ | `U+0E0B U+0E49 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L1 | ต่ำ | `U+0E15 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L1 | ล้ำ | `U+0E25 U+0E49 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L2 | ร่ำ | `U+0E23 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L2 | ค่ำ | `U+0E04 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L2 | ถ้ำ | `U+0E16 U+0E49 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L2 | ด่ำ | `U+0E14 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L3 | ฉ่ำ | `U+0E09 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L3 | ล่ำ | `U+0E25 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L3 | ค้ำ | `U+0E04 U+0E49 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L3 | ย้ำ | `U+0E22 U+0E49 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L4 | ว่ำ | `U+0E27 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L4 | น่ำ | `U+0E19 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |
| L4 | ม่ำ | `U+0E21 U+0E48 U+0E33` | a | Tone complete above ring, gap visible; baseline/spacing normal visually; no visible clipping or overlap. |

**VERIFIED — controls:** L4 ท่ำ (`U+0E17 U+0E48 U+0E33`) retains the old crowded tone/ring form, unlike the15 targets. L5 ตา (`U+0E15 U+0E32`), ถี่ (`U+0E16 U+0E35 U+0E48`), ทำ (`U+0E17 U+0E33`), นำ (`U+0E19 U+0E33`) are complete ordinary controls with visually normal placement. Unchanged placement is a qualitative comparison, not a pixel-identity claim for the differently centered rows.

**VERIFIED — qualitative comparison:** compared with saved GLYPH-001, ต่ำ still shows a complete tone, separated ring and normal base/aa baseline. The deliberate4-unit tone-x difference is a build fact; this screenshot alone does not resolve that small translation. Both modals have5 labeled rows, but the contents differ substantially. New L1–L4 are regularly spaced; the larger inter-row gap now precedes L5 (previous specimen had a larger gap before L4). No line collision or wrapping is visible. **UNKNOWN:** reason for this gap/layout difference, exact runtime pen advance, subpixel contour equivalence, behavior at other scales/consumers or production safety. Known19–22-unit ascent excess was left untouched.

**INFERRED:** appearance of all15 expected stacks while out-of-set ท่ำ stays crowded supports application of the intended bounded ligature/composite set in this consumer. **UNKNOWN:** exact native execution path, package/fork identity, fallback/cache behavior and repeat-load/atlas-stress behavior. No source-level shaping conclusion or font-metric approval.

## Capture and derived inspection

**VERIFIED:** exactly one primary original native PNG, [01-modal-native.png](../../local/qa/WO-SARA-AM-GLYPH-002/01-modal-native.png),3840×2160, SHA256 `fffbf02217414113ddb2e762336b618c3993ff9088053666bd0e62d6fef9f276`. Capture Unix `1793002040.8694198`, elapsed **160.529s** after campaign Continue. No modal dismissal.

- Derived target crop `02-derived-text-4x.png`: native ROI `[1758,760,2040,1070)`,282×310, enlarged4× with **NEAREST** to1128×1240; includes all targets and controls.
- Derived prior-reference crop `03-derived-glyph001-reference-2x.png`: GLYPH-001 original ROI `[1740,750,2050,1055)`,310×305, enlarged2× with **NEAREST** to620×610. Reference original SHA256 `993a727d8485dbb21983b7242499cb2cbe06b2a67c74730aebd0376765372cfb`.

Derived crops are from saved originals, not extra game captures. Original evidence was not edited.

## Ownership, geometry and input

**VERIFIED:** unique exact-owner `D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe`, HWND790818, PID42388. Native display3840×2160, origin(0,0), rect(0,0,3840,2160); observation1920×1080, native coordinates=2× observed coordinates.

| Action | Fresh observed bounds | Observed target | Native target | Result |
|---|---|---|---|---|
| Main Continue | `[82,393,466,446]` | `(274,420)` | `(548,840)` | Hover/hand verified; single click |
| Existing Slot1 Continue | `[111,814,335,889]` | `(223,851)` | `(446,1702)` | Green hover verified; single click; Restart untouched |

**VERIFIED:** every fresh driver subprocess called `set_desktop()` before queries/capture/input, then unique exact-owner/foreground checks. Driver SHA256 `6e243c022dfb80e5e13431dbadba917415c475daeb78e74994c05f282dfff78d` unchanged. Both hover moves accepted1/1; both clicks accepted move/down/up1/1 each. Main click Unix1793001844.3752904; campaign click Unix1793001880.34038. No pointer/foreground error or guard bypass. **0/1 focus recoveries.** Normal Alt+F4 sent through Computer Use; **UNKNOWN:** key acceptance count, which that API does not expose. Process absence independently verified.

**VERIFIED — launch discovery error:** single Steam launch `steam://rungameid/1649080` reported “launched app did not expose a targetable window”; fresh listing found the unique correct game. No relaunch/retry or additional variant run.

## Observation timing

**VERIFIED:** no skip/click/key between campaign Continue and final normal Alt+F4. Raw timestamps are preserved in the JSON. Initial observation showed loading, subsequent early observations loading/flyover; later observations show the specimen modal. The missing interval prevents reliable first-appearance timing.

| Seconds after campaign click | Interval since preceding observation (seconds) |
|---:|---:|
| 0.230 | — |
| 8.318 | 8.088 |
| 15.038 | 6.720 |
| 21.751 | 6.713 |
| 28.467 | 6.716 |
| 138.786 | 110.319 |
| 145.467 | 6.681 |
| 152.137 | 6.670 |
| 158.817 | 6.680 |

**VERIFIED:** launch-to-normal-exit approximately272.980s, under10 minutes; report/integrity work followed restoration. No exact modal-appearance timestamp is asserted. The first retained later modal observation is139s after campaign Continue; this cannot establish timely arrival.

## Lifecycle and integrity

| Step | Verified output |
|---|---|
| Initial manager check | original/original/original |
| Save backup before install | verified=true,11 files |
| Install and post-install check | probe/probe/probe, manifest hashes |
| Launch | one Steam run, existing Slot1 only |
| Exit | normal Alt+F4, no modal dismissal or gameplay progression |
| Restore | original/original/original |
| Final manager check | original/original/original |
| Independent process guard | campus_running=False |

**VERIFIED:** all25 protected files match `reports/sara-am-007-preservation-before.json`; all3 staged bundles still match their manifest. Per-file evidence is `local/qa/WO-SARA-AM-GLYPH-002/protected-verification.json` and runtime JSON. No rebuild/probe edit, settings/scale change, frozen005/probe001a/b edit, binary patch, commit or push. Existing Git modifications/untracked prior work remain preserved; no unrelated edits made.

| Bundle | Staged probe SHA256 (verified) | Restored original SHA256 (manager verified) |
|---|---|---|
| fonts_assets_all.bundle | `0d1f3dfe9a88f0be453023c96a4753b5d50990a6bda2ff0613d5375bd3385274` | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` |
| localisation_assets_localisationenglish.bundle | `1f90326c105c08b862bf4ba97f2b28630aba7d79e3c930c44feee6e55fe20809` | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` |
| ui-prefabs-general_assets_all.bundle | `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df` | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` |

## Saves and retained backup

**VERIFIED:** retained verified backup `local/backups/gameplay-save-snapshots/20261026T080234504672Z.zip` and same-stem JSON. ZIP SHA256 `a60d855e1390d0b589606fd1e44f70a143d456e159837f37bc9e591f160a2895`. Full per-file before/after hashes are in `local/qa/WO-SARA-AM-GLYPH-002/save-comparison.json` and runtime JSON.

**VERIFIED:**11 files compared: **7 changed,4 unchanged,0 new,0 missing**. Changed: Slot1 `career.csav`, `career.csav.2.bak` through `.6.bak`, and `userprofile.sav`. Unchanged: `8000.sav`, `preferences.json`, `steam_autocloud.vdf`, `localpreferences.json`. Slot1 `8000.sav` remains SHA256 `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d`. **UNKNOWN:** semantic contents of changed save files; no gameplay-progress inference from hashes. Live saves and backup retained, no rollback/deletion/Cloud edit.

Stop after this report. **INCONCLUSIVE pending PM decision**, with15/15 successful bounded visual observations and a recorded timing-protocol failure. BUG-THAI-003 OPEN.
