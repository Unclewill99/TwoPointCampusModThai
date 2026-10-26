# WO-SARA-AM-FRESH006-001 — runtime report

2026-10-26 (Asia/Bangkok). Tester **ChatGPT**, authorized by the user to test instead of Antigravity. **PASS_SCOPED**, pending PM acceptance. All3 requested target surfaces reached, all class a; **NOT_REACHED: none**. BUG-THAI-003 remains **OPEN**. No production or other-scale acceptance.

## Results

**VERIFIED — visual:** real candidate text, not diagnostic specimen. Every inspected ต่ำ (`U+0E15 U+0E48 U+0E33`) shows a complete tone above the ring, clear gap, normal base/sara-aa baseline and spacing; no visibly clipped tone top, tofu, neighbour overlap or new wrapping. Inspected original native captures and stated derived nearest-neighbour crops. No pixel-level contour guarantee.

| Surface | Exact text / target | Class | Notes |
|---|---|---|---|
| Settings > Game, Advisor Filter open option | ซ่อนความสำคัญต่ำ / ต่ำ | a | Complete stack; option inside dropdown, neighbours normal; no selection made. |
| Settings > Video, Ambient Occlusion Quality tooltip | การตั้งค่าต่ำภาพสวยน้อยกว่าแต่เพิ่มประสิทธิภาพ / ต่ำ | a | Third of3 lines; separated tone/ring, normal ค่า, no line clipping/collision or additional wrap. |
| Real opening-course modal | ที่ชีวิตเคลื่อนไปอย่างเชื่องช้าและความคาดหวังก็... ต่ำเตี้ย / ต่ำ | a | Original defect site now visibly stacked; เตี้ย remains ordinary; second paragraph complete. |

**VERIFIED controls:** C1 ความถี่บันทึกอัตโนมัติของโหมดอาชีพ; C2 ความถี่บันทึกอัตโนมัติของเกม: ถี่ (`U+0E16 U+0E35 U+0E48`) visibly separates upper vowel/tone, both full labels fit. C4 ตัวกรองที่ปรึกษา has ordinary ที่ (`U+0E17 U+0E35 U+0E48`). UI Scale caption read directly **กลาง (Medium)**; never opened/changed UI Scale. C3 intro has ordinary ที่ชีวิต, เชื่องช้า, เตี้ย (`U+0E40 U+0E15 U+0E35 U+0E49 U+0E22`), and second-paragraph ที่ที่, เริ่ม, พื้น, ยิ้ม. No visible ordinary-mark deviation. **VERIFIED text detail:** exact token ซึ่ง is not in this actual005 intro; it is NOT_TESTED as a literal word, while upper-vowel/tone controls are reached. This is not a missing surface.

**VERIFIED qualitative comparison:** inspected saved accepted pre-fix real-modal image `local/qa/WO-FRESH-SMOKE-001-RESUME/02-campus-modal.png` (1920×1080). Surrounding body layout remains2 intro lines, paragraph gap,2 second-paragraph lines, in the same panel with no new wrap. Previously crowded ต่ำ is now stacked. Ordinary ที่/เตี้ย remain qualitatively normal. The older image is downscaled relative to this3840×2160 original, so no pixel-identity/pen-advance claim. **UNKNOWN:** exact native code path, font-consumer identity, subpixel contour preservation, other contexts/scales, repeat-load/atlas stress and production safety.

## Exact stored text and codepoints

**VERIFIED:** candidate localization/UI equal005; full codepoints for each target and control record retained in `reports/sara-am-fresh006-001-runtime.json`. Below is the real multiline tooltip and modal, checked visually against the stored records. Newlines below are stored LF; the modal also visually breaks after its greeting and before its final line as before.

`I2LS_UI_Settings` segment108, `UI/Settings/Tooltips/AmbientOcclusionModeQuality`:

```text
ควบคุมคุณภาพของการบดบังแสงแวดล้อม
การตั้งค่าสูงและสูงมากให้ภาพสวยกว่า
การตั้งค่าต่ำภาพสวยน้อยกว่าแต่เพิ่มประสิทธิภาพ
```

`I2LS_Levels` segment533, `Levels/Freshleigh/Level_Intro_Text`:

```text
ยินดีต้อนรับสู่ Freshleigh Meadows ที่ชีวิตเคลื่อนไปอย่างเชื่องช้าและความคาดหวังก็... ต่ำเตี้ย

ชนบทของ Two Point เป็นที่ที่เหมาะจะเริ่มต้นอาชีพ เรียนรู้งาน ทำผิดพลาด และก้าวเท้าลงพื้นพร้อมรอยยิ้ม
```

## Native evidence

**VERIFIED:**4 primary native PNGs, each3840×2160; within cap5. Originals untouched. No fifth capture needed.

| Image | SHA256 |
|---|---|
| `local\qa\WO-SARA-AM-FRESH006-001\01-settings-game-native.png` | `ce4cfcdf489ce90593bc9a380919114b5d3619100a800cdf4fe930d85c9d5bb7` |
| `local\qa\WO-SARA-AM-FRESH006-001\02-advisor-filter-native.png` | `4e4803c49847c504047b20c9c60fabe7e312eb3ba1474da7f1f5bd28e6fd7bf1` |
| `local\qa\WO-SARA-AM-FRESH006-001\03-video-tooltip-native.png` | `f18ecdd4d9295e22ff6f81e389669a39072fdb6dd406ed5ab6c492a39074eda5` |
| `local\qa\WO-SARA-AM-FRESH006-001\04-real-modal-native.png` | `98523cc1dafbaf00550cf684e6444c23d73d1a973e890e00a67b9cbe3cd0c3e9` |

Derived from originals only (native ROI `[left,top,right,bottom)`, NEAREST):

- `05-derived-filter-4x.png`: image02, `[1080,1640,1440,1710)`,4×.
- `06-derived-tooltip-3x.png`: image03, `[1880,1630,2715,1845)`,3×.
- `07-derived-modal-3x.png`: image04, `[1370,745,2430,1080)`,3×.
- `08-derived-controls-3x.png`: image01, `[50,850,800,1080)`,3×.

## Ownership, mapping and actions

**VERIFIED:** unique window HWND1249258, PID24828, exact owner `D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe`; native3840×2160, origin(0,0), rect(0,0,3840,2160); observed1920×1080. Mapping normalized=native×1920/W,×1080/H; here native=2× normalized. Game version visible `10.3.169253+2024-12-06.1241`; Video shows3840×2160@60hz, fullscreen window. Every fresh driver subprocess set_desktop() first, then unique-window/exact-owner/foreground guard before input/capture. Driver unchanged SHA256 `6e243c022dfb80e5e13431dbadba917415c475daeb78e74994c05f282dfff78d`.

Fresh-pixel hover/hand verification before each single pointer click. Coordinates below are normalized1920, native=2×:

| Order | Action | Target | Result |
|---|---|---|---|
| 1 | Main-menu Settings | (274,855) | Hover hand then click; Settings > Game opens |
| 2 | Read Game controls and Medium | no input | Native01 |
| 3 | Scroll Game list | (460,770),−480 then−720 wheel | Advisor label/filter visible; no values changed |
| 4 | Open Advisor Filter arrow | (891,759) | Hover then click; native02 |
| 5 | Escape | key | Did **not** close dropdown; no value selection; fresh observation recorded |
| 6 | Close same arrow | (891,759) | Fresh hover then click; closed; caption remains แสดงทั้งหมด |
| 7 | Video tab | (133,135) | Fresh hover then click |
| 8 | Scroll Video list | (460,770),−1200 wheel | Ambient Occlusion Quality label visible |
| 9 | Hover parent gap | (460,866),1.8s hold |3-line correct tooltip; native03; no click |
| 10 | Close Settings X | (1855,48) | Hover then click; no Apply prompt; back at menu |
| 11 | Main Continue | (274,420) | Hover hand then one click |
| 12 | Existing Slot1 Continue | (223,851) | Fresh green hover then one click; Restart untouched |
| 13 | Natural wait | none | Modal observed48.428s; native04; modal not dismissed |
| 14 | Exit | Alt+F4 | Normal close; process absence independently verified |

**VERIFIED:** pointer hover moves accepted1/1; each click's move/down/up accepted1/1 each; wheel events accepted1/1, no input/foreground guard error or bypass. **0/1 focus recoveries.** Key acceptance counts are **UNKNOWN** (Computer Use does not expose them); effects checked visually/process independently. Escape's ineffective dismissal was not repeated; arrow used only after fresh observation/hover. No setting value, graphics/preset/language/autosave/filter, scale, build/spend/hire/year start or tutorial action. No hidden state fabrication.

**VERIFIED launcher error:** single Steam launch via `steam://rungameid/1649080` reported “launched app did not expose a targetable window.” Fresh list found unique correct game; no retry/relaunch, no second candidate. Window activation wasn't needed as a recovery.

## Actual natural-wait cadence

Campaign Continue completion Unix1793003267.0818634. No skip/click/key until normal exit after modal capture. Observations:

| Seconds after Continue | Interval (s) | State |
|---:|---:|---|
| 0.233 | — | loading transition |
| 7.845 | 7.612 | loading card |
| 17.358 | 9.513 | transition/flyover |
| 23.590 | 6.232 | transition/flyover |
| 29.785 | 6.195 | transition/flyover |
| 36.060 | 6.275 | transition/flyover |
| 42.257 | 6.197 | transition/flyover |
| 48.428 | 6.171 | real modal |

**VERIFIED:** maximum interval9.513s, all≤15s. Modal first observed48.428s (within60); exact appearance instant UNKNOWN. Observation loop stopped on modal recognition. Original capture Unix1793003340.6258433 (73.544s after Continue); capture delay is after modal recognition, not continued arrival waiting. Launch through normal exit486.749s (~8m07), within15-minute active budget. Reporting/integrity work followed exit/restoration.

## Lifecycle, hashes and saves

| Step | Verified result |
|---|---|
| Initial manager check | original/original/original |
| Backup before install | verified=true,11 files |
| Install | probe/probe/probe |
| Post-install check | probe/probe/probe; expected staged hashes |
| Launch/test | one run, one candidate; A/B/C all reached |
| Exit | normal Alt+F4; no forced termination |
| Restore | original/original/original |
| Final check | original/original/original |
| Independent guard / Computer Use list | campus_running=False; no TPC window |

**VERIFIED:** all29 protected files match WO008 before hashes; saved evidence `local/qa/WO-SARA-AM-FRESH006-001/protected-verification.json`. All3 staged006 bundles rehashed and still match manifest. Candidate manifest original/probe/parent hashes copied into runtime JSON. Installed state manager verified all3 originals. Previous work preserved, no probe rebuild/edit, commit/push or Cloud edits.

| Bundle | Candidate SHA256 | Original SHA256 verified after restore |
|---|---|---|
| fonts_assets_all.bundle | `0d1f3dfe9a88f0be453023c96a4753b5d50990a6bda2ff0613d5375bd3385274` | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` |
| localisation_assets_localisationenglish.bundle | `74a3c5ef4466df886f6ee432f4bb02a136dd7b5377d6ed220b4770fd75d8565a` | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` |
| ui-prefabs-general_assets_all.bundle | `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df` | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` |

**VERIFIED retained backup:** `local/backups/gameplay-save-snapshots/20261026T082043381243Z.zip` and same-stem JSON. ZIP SHA256 `4f6c33f92c768e81b53c680608671e4c520c812508873d98fe9c3ef10eb45a5a`; manifest SHA256 `ce9dc70fced37c64b38d115e744ab6a10b47a56a54e14002c1ca08b66d8fdae7`.

**VERIFIED save comparison:**11 files,7 changed,4 unchanged,0 new,0 missing. Changed `career.csav`, its `.2.bak`–`.6.bak`, and `userprofile.sav`. Unchanged `8000.sav`, `preferences.json`, `steam_autocloud.vdf`, `localpreferences.json`; the preferences hashes support no settings change. `8000.sav` stays SHA256 `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d`. Semantic contents of changed career/profile files UNKNOWN; no progress inferred from hashes. Live saves and backup retained without rollback/deletion. Full before/after hashes: `local/qa/WO-SARA-AM-FRESH006-001/save-comparison.json` and runtime JSON.

**PASS_SCOPED:**3 requested real surfaces at Medium show correct ต่ำ, ordinary controls normal; no NOT_REACHED cells. Other scales, in-campus screens, radio/character/DLC clusters and production safety remain NOT_TESTED/UNKNOWN. Stop after report; BUG-THAI-003 OPEN pending PM and user decision.
