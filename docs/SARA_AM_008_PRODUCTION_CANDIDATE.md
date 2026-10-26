# WO-SARA-AM-008 — fresh-translation-006 candidate and regression design

2026-10-26. ChatGPT engineering. **Overall: PARTIAL; offline candidate BUILD_READY.** Real-screen regression **NOT_RUN**, subject to PM's separate runtime WO. BUG-THAI-003 remains OPEN. No game launch, install, runtime test, commit or push.

## Build and equivalence

**VERIFIED:** exclusively created `local/prototype/fresh-translation-006`. Fonts bundle copied directly from accepted glyph-002; localisation and UI copied directly from frozen005. No font reconstruction, Unicode rewrite, diagnostic specimen, cmap addition or metric edit. The complete fonts bundle is byte-identical to glyph-002, so both embedded font and TMP object bytes are identical to the accepted source. The exact five-line probe specimen is excluded by localisation bundle equality with005; the real opening modal text remains original005.

**VERIFIED:** reloaded all3 candidate bundles. Raw object keys unchanged; fonts diff versus005 is only Font7716434233879021909 and TMP−1239755799206566947. In Font only m_FontData differs; in TMP only the15 appended ligature records differ. First9 unchanged,24 total. fontTools reload:474 glyphs,459 original raw glyf slices byte-equal, original glyph order/loca prefix/cmap/metrics equal; OS/2 bytes and hhea ascent unchanged. These independently repeated checks plus source bundle identity preserve WO007's accepted geometry/checksums without rebuilding it.

| Bundle | Candidate SHA256 | Relation |
|---|---|---|
| fonts_assets_all.bundle | `0d1f3dfe9a88f0be453023c96a4753b5d50990a6bda2ff0613d5375bd3385274` | glyph-002 exact |
| localisation_assets_localisationenglish.bundle | `74a3c5ef4466df886f6ee432f4bb02a136dd7b5377d6ed220b4770fd75d8565a` | 005 exact |
| ui-prefabs-general_assets_all.bundle | `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df` | 005 exact |

**VERIFIED:** embedded font SHA256 `49554400797971424cb9057481e2dd55744cec5fa603ee6b21ae24bcff3b2607`. Manifest includes parent005, source glyph-002, original/parent/candidate hashes and all15 clusters with glyph IDs/geometry, plus explicit text-unchanged statement. Full object/font/installed hashes: `reports/sara-am-fresh006-build.json`.

## Corpus and collision check

**VERIFIED:** all15,677 stored values reloaded;440 direct consonant-tone-am occurrences,15 distinct clusters; count agrees exactly with WO006 census. Every cluster maps via the original cmap to its intended new three-glyph record. **0** outside-set consonant-tone-U+0E33 occurrences. **0** same-font cmap-derived three-glyph matches whose stored substring is not a census cluster. Scanned each complete stored value independently, not across record boundaries.32 occurrences are in LF-containing records.

**UNKNOWN / required runtime limitation:** this is a stored-codepoint and inspected-font sequence proof. It cannot confirm glyph IDs of another TMP consumer/fallback font, rich-text segmentation, dynamic substitutions or cross-run concatenation. No assertion that the broader cross-consumer collision question is proven. No synthetic corpus/text rewrite used.

| Cluster | Occurrences | Glyph ID |
|---|---:|---:|
| น้ำ | 250 | 467 |
| ซ้ำ | 55 | 462 |
| ต่ำ | 51 | 464 |
| ล้ำ | 36 | 472 |
| ร่ำ | 13 | 470 |
| ค่ำ | 10 | 459 |
| ถ้ำ | 6 | 465 |
| ด่ำ | 5 | 463 |
| ฉ่ำ | 3 | 461 |
| ล่ำ | 3 | 471 |
| ว่ำ | 2 | 473 |
| ย้ำ | 2 | 469 |
| ค้ำ | 2 | 460 |
| ม่ำ | 1 | 468 |
| น่ำ | 1 | 466 |

## Complete screen inventory

**VERIFIED corpus:** `reports/sara-am-008-screen-map.json` enumerates **all410 records** containing the440 occurrences: asset, segment, key, exact full stored text, codepoints, clusters, explicit LF, kind/flow and uncertainty label. This is the per-record screen map; no samples substituted for the complete inventory.

**INFERRED screens:** UI path prefixes suggest labels/inspectors/event setup; Items descriptions suggest catalogue cards; Courses suggests course info; Characters suggests name/trait inspectors; Levels suggests triggered dialogue; VO_Radio/Tannoy suggests radio/announcement captions. **UNKNOWN:** actual bindings, unlocks, caption visibility and availability in the current save. Radio-only ค้ำ/ย้ำ/ม่ำ, character-only ล่ำ, DLC/triggered น่ำ and other rare contexts must remain unverified if not naturally present. Never wait for random VO, spawn characters, change DLC state, start a year or progress tutorial to manufacture coverage.

## Proposed minimum context set (design only)

**INFERRED:** nine context observations grouped into Settings, character/staff inspectors, event/timetable views, item catalogue and course overview. They cover น้ำ/ซ้ำ/ต่ำ/ล้ำ twice each in distinct intended contexts, both mai-ek/mai-tho, and one explicit multiline tooltip. This is a proposed compact set, **not a proven reachable/global minimum**. If any required screen is locked or absent, report that coverage cell UNREACHABLE and stop that branch; do not substitute a second item description as a different context or claim overall coverage complete.

Each exact full text and codepoint sequence below is retained additionally in `reports/sara-am-008-regression-plan.json`. All navigation is INFERRED; actual reachability UNKNOWN until permitted runtime. Each target requires separated complete tone/ring, normal base/aa baseline and width, no clipped top, neighbour overlap, missing/tofu or new wrap/clipping. Capture full context and native crop; no conclusion from readable body alone.

### P1. Character needs inspector — I2LS_UI segment26

**VERIFIED key:** `UI/Attribute/ToiletComfort`. Target(s): น้ำ.

```text
ความสบายของห้องน้ำ
```

Codepoints: `U+0E04 U+0E27 U+0E32 U+0E21 U+0E2A U+0E1A U+0E32 U+0E22 U+0E02 U+0E2D U+0E07 U+0E2B U+0E49 U+0E2D U+0E07 U+0E19 U+0E49 U+0E33`.

**INFERRED route:** Paused existing campus: select existing character, inspect needs; do not alter anything. **Risk / UNKNOWN:** Character availability/needs-panel binding UNKNOWN; tooltip may require hover.

### P2. Staff jobs panel — I2LS_UI segment1411

**VERIFIED key:** `UI/StaffJobs/CleaningToilet`. Target(s): น้ำ.

```text
ล้างห้องน้ำ
```

Codepoints: `U+0E25 U+0E49 U+0E32 U+0E07 U+0E2B U+0E49 U+0E2D U+0E07 U+0E19 U+0E49 U+0E33`.

**INFERRED route:** Select existing janitor, read cleaning job label; do not toggle assignments. **Risk / UNKNOWN:** Janitor availability UNKNOWN; no hire allowed.

### P3. Event setup label — I2LS_UI segment245

**VERIFIED key:** `UI/EventSetup/AnnualRepeat`. Target(s): ซ้ำ.

```text
ทำซ้ำทุกปี
```

Codepoints: `U+0E17 U+0E33 U+0E0B U+0E49 U+0E33 U+0E17 U+0E38 U+0E01 U+0E1B U+0E35`.

**INFERRED route:** Open read-only event setup from existing timetable if available; do not confirm/schedule. Close with Cancel. **Risk / UNKNOWN:** UNREACHABLE if opening requires advancing tutorial or creating event; do not proceed.

### P4. Existing event inspector — I2LS_UI segment717

**VERIFIED key:** `UI/Inspector/RepeatAnnually`. Target(s): ซ้ำ.

```text
ทำซ้ำทุกปี
```

Codepoints: `U+0E17 U+0E33 U+0E0B U+0E49 U+0E33 U+0E17 U+0E38 U+0E01 U+0E1B U+0E35`.

**INFERRED route:** Select an existing calendar event; read RepeatAnnually without toggling. **Risk / UNKNOWN:** Existing event UNKNOWN. Label and setup are distinct UI contexts, not proven distinct font consumers.

### P5. Game settings filter option — I2LS_UI_Settings segment35

**VERIFIED key:** `UI/Settings/Game/AdvisorFilter_HideLowPriority`. Target(s): ต่ำ.

```text
ซ่อนความสำคัญต่ำ
```

Codepoints: `U+0E0B U+0E48 U+0E2D U+0E19 U+0E04 U+0E27 U+0E32 U+0E21 U+0E2A U+0E33 U+0E04 U+0E31 U+0E0D U+0E15 U+0E48 U+0E33`.

**INFERRED route:** Main menu Settings > Game: inspect filter label/option without selecting a different filter. **Risk / UNKNOWN:** Exact dropdown binding UNKNOWN; open only if runtime WO authorizes inspection.

### P6. Radiator catalogue description — I2LS_Items segment904

**VERIFIED key:** `Items/General/Radiator_Flat_Description`. Target(s): ต่ำ.

```text
เจ้าตัวเตี้ยห้อยต่ำ
```

Codepoints: `U+0E40 U+0E08 U+0E49 U+0E32 U+0E15 U+0E31 U+0E27 U+0E40 U+0E15 U+0E35 U+0E49 U+0E22 U+0E2B U+0E49 U+0E2D U+0E22 U+0E15 U+0E48 U+0E33`.

**INFERRED route:** Paused existing campus: open Items catalogue, hover flat radiator; never place/purchase. **Risk / UNKNOWN:** Unlock/catalogue accessibility UNKNOWN; no room creation.

### P7. Computer catalogue description — I2LS_Items segment224

**VERIFIED key:** `Items/ComputerLab/Computer_Analogue_Description`. Target(s): ล้ำ.

```text
ล้ำหน้ากว่ายุค
```

Codepoints: `U+0E25 U+0E49 U+0E33 U+0E2B U+0E19 U+0E49 U+0E32 U+0E01 U+0E27 U+0E48 U+0E32 U+0E22 U+0E38 U+0E04`.

**INFERRED route:** Same read-only catalogue, computer lab category: hover analogue computer. **Risk / UNKNOWN:** UNREACHABLE if room/category locked; no unlock/progress.

### P8. Robotics course overview — I2LS_Courses segment214

**VERIFIED key:** `Courses/Courses/Robotics_Overview`. Target(s): ล้ำ.

```text
วิทยาศาสตร์ล้ำสมัยสำหรับทุกคนที่ทะเยอทะยานพอจะสร้างพ่อบ้านของตัวเอง ทำไมต้องศึกษาเซลล์จิ๋วหรือกลไกซับซ้อนของจักรวาล ในเมื่อสอนเจ้าหุ่นโลหะน้อยให้เอารองเท้าแตะมาให้ได้
```

Codepoints: `U+0E27 U+0E34 U+0E17 U+0E22 U+0E32 U+0E28 U+0E32 U+0E2A U+0E15 U+0E23 U+0E4C U+0E25 U+0E49 U+0E33 U+0E2A U+0E21 U+0E31 U+0E22 U+0E2A U+0E33 U+0E2B U+0E23 U+0E31 U+0E1A U+0E17 U+0E38 U+0E01 U+0E04 U+0E19 U+0E17 U+0E35 U+0E48 U+0E17 U+0E30 U+0E40 U+0E22 U+0E2D U+0E17 U+0E30 U+0E22 U+0E32 U+0E19 U+0E1E U+0E2D U+0E08 U+0E30 U+0E2A U+0E23 U+0E49 U+0E32 U+0E07 U+0E1E U+0E48 U+0E2D U+0E1A U+0E49 U+0E32 U+0E19 U+0E02 U+0E2D U+0E07 U+0E15 U+0E31 U+0E27 U+0E40 U+0E2D U+0E07 U+0020 U+0E17 U+0E33 U+0E44 U+0E21 U+0E15 U+0E49 U+0E2D U+0E07 U+0E28 U+0E36 U+0E01 U+0E29 U+0E32 U+0E40 U+0E0B U+0E25 U+0E25 U+0E4C U+0E08 U+0E34 U+0E4B U+0E27 U+0E2B U+0E23 U+0E37 U+0E2D U+0E01 U+0E25 U+0E44 U+0E01 U+0E0B U+0E31 U+0E1A U+0E0B U+0E49 U+0E2D U+0E19 U+0E02 U+0E2D U+0E07 U+0E08 U+0E31 U+0E01 U+0E23 U+0E27 U+0E32 U+0E25 U+0020 U+0E43 U+0E19 U+0E40 U+0E21 U+0E37 U+0E48 U+0E2D U+0E2A U+0E2D U+0E19 U+0E40 U+0E08 U+0E49 U+0E32 U+0E2B U+0E38 U+0E48 U+0E19 U+0E42 U+0E25 U+0E2B U+0E30 U+0E19 U+0E49 U+0E2D U+0E22 U+0E43 U+0E2B U+0E49 U+0E40 U+0E2D U+0E32 U+0E23 U+0E2D U+0E07 U+0E40 U+0E17 U+0E49 U+0E32 U+0E41 U+0E15 U+0E30 U+0E21 U+0E32 U+0E43 U+0E2B U+0E49 U+0E44 U+0E14 U+0E49`.

**INFERRED route:** Read existing course information/catalogue preview for Robotics; never add/upgrade a course. **Risk / UNKNOWN:** UNREACHABLE unless read-only preview available in existing save; no replacement evidence from an item card.

### P9. Video settings multiline tooltip — I2LS_UI_Settings segment108

**VERIFIED key:** `UI/Settings/Tooltips/AmbientOcclusionModeQuality`. Target(s): ต่ำ.

```text
ควบคุมคุณภาพของการบดบังแสงแวดล้อม
การตั้งค่าสูงและสูงมากให้ภาพสวยกว่า
การตั้งค่าต่ำภาพสวยน้อยกว่าแต่เพิ่มประสิทธิภาพ
```

Codepoints: `U+0E04 U+0E27 U+0E1A U+0E04 U+0E38 U+0E21 U+0E04 U+0E38 U+0E13 U+0E20 U+0E32 U+0E1E U+0E02 U+0E2D U+0E07 U+0E01 U+0E32 U+0E23 U+0E1A U+0E14 U+0E1A U+0E31 U+0E07 U+0E41 U+0E2A U+0E07 U+0E41 U+0E27 U+0E14 U+0E25 U+0E49 U+0E2D U+0E21 U+000A U+0E01 U+0E32 U+0E23 U+0E15 U+0E31 U+0E49 U+0E07 U+0E04 U+0E48 U+0E32 U+0E2A U+0E39 U+0E07 U+0E41 U+0E25 U+0E30 U+0E2A U+0E39 U+0E07 U+0E21 U+0E32 U+0E01 U+0E43 U+0E2B U+0E49 U+0E20 U+0E32 U+0E1E U+0E2A U+0E27 U+0E22 U+0E01 U+0E27 U+0E48 U+0E32 U+000A U+0E01 U+0E32 U+0E23 U+0E15 U+0E31 U+0E49 U+0E07 U+0E04 U+0E48 U+0E32 U+0E15 U+0E48 U+0E33 U+0E20 U+0E32 U+0E1E U+0E2A U+0E27 U+0E22 U+0E19 U+0E49 U+0E2D U+0E22 U+0E01 U+0E27 U+0E48 U+0E32 U+0E41 U+0E15 U+0E48 U+0E40 U+0E1E U+0E34 U+0E48 U+0E21 U+0E1B U+0E23 U+0E30 U+0E2A U+0E34 U+0E17 U+0E18 U+0E34 U+0E20 U+0E32 U+0E1E`.

**INFERRED route:** Main menu Settings > Video, hover Ambient Occlusion Quality row/parent gap per prior tooltip convention; do not change graphics value. **Risk / UNKNOWN:** Hover target/binding must be verified fresh; hover tooltip may be unavailable.

## Sizes, controls and QA boundaries

**VERIFIED precedent:** WO_VISUAL_003 permits Small/Large comparison and return to Medium; earlier tooltip reports use all three scales. **Plan only, conditional on PM's runtime WO:** first record actual Settings > Game > UI Scale caption; test current Medium, change **only UI Scale to Small**, repeat selected visible contexts, then **Large**, repeat, and restore **Medium** before normal exit (or restore recorded starting scale if it was not Medium). Read each selected caption back; do not infer scale from a blank value. If navigation becomes difficult, immediately revert; one focus recovery total. No graphics/preset/language/autosave/filter change. If runtime WO disallows Settings changes, leave Small/Large cells NOT_TESTED rather than bypass the restriction. Small/Medium/Large are UI scales, not claims about actual font pixel sizes.

**Plan:** retain established unique-owner/foreground guard, fresh pixel-derived navigation and hover verification; verified pre-install original check, gameplay save ZIP backup, install/check via manager, one candidate only, normal exit, restore/check, save comparison. PM must bound sessions/screens and capture budget in its runtime WO. Nine contexts at three scales should not be squeezed into a10-minute run by skipping guards; split future work if PM chooses. No runtime task issued here.

Four unaffected-text context checks follow; these are read-only screen observations. One is a real opening modal, not an injected test. Several controls share Settings or modal surfaces deliberately: **four distinct unaffected screens are not proven available** from this evidence. Compare unchanged ordinary text at same scale to accepted controls; inspect both vowel and tone shapes, baselines, spacing and wrapping. Never dismiss opening modal to gain other screens during a modal-bounded run.

- C1: `I2LS_UI_Settings` segment9, `UI/Settings/CareerAutosaveFreq`. Route: Main menu Settings > Game: inspect existing autosave label; do not change frequency. Exact text: "ความถี่บันทึกอัตโนมัติของโหมดอาชีพ". Codepoints: `U+0E04 U+0E27 U+0E32 U+0E21 U+0E16 U+0E35 U+0E48 U+0E1A U+0E31 U+0E19 U+0E17 U+0E36 U+0E01 U+0E2D U+0E31 U+0E15 U+0E42 U+0E19 U+0E21 U+0E31 U+0E15 U+0E34 U+0E02 U+0E2D U+0E07 U+0E42 U+0E2B U+0E21 U+0E14 U+0E2D U+0E32 U+0E0A U+0E35 U+0E1E`.

- C2: `I2LS_UI_Settings` segment83, `UI/Settings/GameAutosaveFreq`. Route: Main menu Settings > Game: inspect existing autosave label; do not change frequency. Exact text: "ความถี่บันทึกอัตโนมัติของเกม". Codepoints: `U+0E04 U+0E27 U+0E32 U+0E21 U+0E16 U+0E35 U+0E48 U+0E1A U+0E31 U+0E19 U+0E17 U+0E36 U+0E01 U+0E2D U+0E31 U+0E15 U+0E42 U+0E19 U+0E21 U+0E31 U+0E15 U+0E34 U+0E02 U+0E2D U+0E07 U+0E40 U+0E01 U+0E21`.

- C3: `I2LS_Levels` segment533, `Levels/Freshleigh/Level_Intro_Text`. Route: Existing Slot1 Continue, natural opening-course modal only if not gated by progression; inspect ที่ซึ่ง / ที่ชีวิต / เตี้ย. Do not dismiss or start year. Exact text: "ยินดีต้อนรับสู่ Freshleigh Meadows ที่ชีวิตเคลื่อนไปอย่างเชื่องช้าและความคาดหวังก็... ต่ำเตี้ย\n\nชนบทของ Two Point เป็นที่ที่เหมาะจะเริ่มต้นอาชีพ เรียนรู้งาน ทำผิดพลาด และก้าวเท้าลงพื้นพร้อมรอยยิ้ม". Codepoints: `U+0E22 U+0E34 U+0E19 U+0E14 U+0E35 U+0E15 U+0E49 U+0E2D U+0E19 U+0E23 U+0E31 U+0E1A U+0E2A U+0E39 U+0E48 U+0020 U+0046 U+0072 U+0065 U+0073 U+0068 U+006C U+0065 U+0069 U+0067 U+0068 U+0020 U+004D U+0065 U+0061 U+0064 U+006F U+0077 U+0073 U+0020 U+0E17 U+0E35 U+0E48 U+0E0A U+0E35 U+0E27 U+0E34 U+0E15 U+0E40 U+0E04 U+0E25 U+0E37 U+0E48 U+0E2D U+0E19 U+0E44 U+0E1B U+0E2D U+0E22 U+0E48 U+0E32 U+0E07 U+0E40 U+0E0A U+0E37 U+0E48 U+0E2D U+0E07 U+0E0A U+0E49 U+0E32 U+0E41 U+0E25 U+0E30 U+0E04 U+0E27 U+0E32 U+0E21 U+0E04 U+0E32 U+0E14 U+0E2B U+0E27 U+0E31 U+0E07 U+0E01 U+0E47 U+002E U+002E U+002E U+0020 U+0E15 U+0E48 U+0E33 U+0E40 U+0E15 U+0E35 U+0E49 U+0E22 U+000A U+000A U+0E0A U+0E19 U+0E1A U+0E17 U+0E02 U+0E2D U+0E07 U+0020 U+0054 U+0077 U+006F U+0020 U+0050 U+006F U+0069 U+006E U+0074 U+0020 U+0E40 U+0E1B U+0E47 U+0E19 U+0E17 U+0E35 U+0E48 U+0E17 U+0E35 U+0E48 U+0E40 U+0E2B U+0E21 U+0E32 U+0E30 U+0E08 U+0E30 U+0E40 U+0E23 U+0E34 U+0E48 U+0E21 U+0E15 U+0E49 U+0E19 U+0E2D U+0E32 U+0E0A U+0E35 U+0E1E U+0020 U+0E40 U+0E23 U+0E35 U+0E22 U+0E19 U+0E23 U+0E39 U+0E49 U+0E07 U+0E32 U+0E19 U+0020 U+0E17 U+0E33 U+0E1C U+0E34 U+0E14 U+0E1E U+0E25 U+0E32 U+0E14 U+0020 U+0E41 U+0E25 U+0E30 U+0E01 U+0E49 U+0E32 U+0E27 U+0E40 U+0E17 U+0E49 U+0E32 U+0E25 U+0E07 U+0E1E U+0E37 U+0E49 U+0E19 U+0E1E U+0E23 U+0E49 U+0E2D U+0E21 U+0E23 U+0E2D U+0E22 U+0E22 U+0E34 U+0E49 U+0E21`.

- C4: `I2LS_UI_Settings` segment1, `UI/Settings/AdvisorFilter`. Route: Read corresponding Settings label/tooltip from key; exact binding UNKNOWN, no setting change. Exact text: "ตัวกรองที่ปรึกษา". Codepoints: `U+0E15 U+0E31 U+0E27 U+0E01 U+0E23 U+0E2D U+0E07 U+0E17 U+0E35 U+0E48 U+0E1B U+0E23 U+0E36 U+0E01 U+0E29 U+0E32`.

**VERIFIED reference:** accepted BUG-THAI-001 scope is ถี่ (`U+0E16 U+0E35 U+0E48`) in Career Autosave Frequency; accepted sara-am reference also identifies ที่/ซึ่ง/เตี้ย in the real intro. Expected ordinary upper vowel below separated tone, no regression, not generalized Thai shaping approval.

## Installation lifecycle analysis (read-only)

**VERIFIED:** added only `fresh-translation-006` to manager's allowed names. Ran manager **check**, output original/original/original. Independently hashed installed3 bundles against manifest originals. No install/restore invocation. Manager validates safe basenames and staged hashes; rejects unknown installed hashes or bad originals backup; mutation actions require game closed. It verifies every original backup before copying staged files; install copy failures trigger original copies; restore copies saved originals only when staged hash installed, verifying result. A successful standard install followed by restore is supported by this unchanged mechanism and006's compatible manifest. Separate gameplay-save backup remains required before future runtime, and is not performed by manager.

**INFERRED:**006 will restore cleanly under the verified preconditions and available writable storage. **UNKNOWN:** future I/O failures/interruption. Multi-file copy is not transactional; rollback itself can fail, so no unconditional restoration guarantee. Existing backup state checked by manager; future lifecycle must inspect every output.

**VERIFIED:**29 protected files before/after match (prior25 plus glyph-002 bundles/manifest), including installed originals/frozen005/probes/binary/metadata. New snapshots: `reports/sara-am-008-preservation-before.json` and `...-after.json`. Existing Git work preserved. New outputs exclusive-create; builder intentionally refuses rerun when outputs exist.

## Status and remaining acceptance work

**PARTIAL overall; BUILD_READY** for offline candidate. Missing: cross-consumer collision exclusion, verified reachability for full two-context coverage, and3–4 independently established unaffected screens. These cannot be proved offline from the available bindings/corpus; the four proposed control observations share surfaces. **UNKNOWN / pending:** cross-consumer sequence behavior; live screen reachability; actual text sizes, multiline/rich-text/fallback rendering, repeat loads/atlas capacity and production safety. The plan has explicit unavailable branches and cannot certify required two-context coverage until runtime. PM decides whether to accept the design or narrow/split runtime WOs. No production fix/release claim; stop here.
