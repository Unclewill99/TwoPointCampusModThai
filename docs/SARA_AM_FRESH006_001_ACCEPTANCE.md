# WO-SARA-AM-FRESH006-001 — accepted: PASS_SCOPED

2026-10-26. PM (Claude): ACCEPT. Report docs/qa/WO_SARA_AM_FRESH006_001_REPORT.md, reports/sara-am-fresh006-001-runtime.json.

## PM verification

- The four native PNGs (3840x2160) re-hashed: all match the report. PM cropped and inspected three of them directly from the native files: (1) Settings > Game dropdown option "ซ่อนความสำคัญต่ำ": ต่ำ shows tone above ring with a gap, ordinary ำ in สำคัญ normal; (2) Settings > Video Ambient Occlusion tooltip (3 lines): the ต่ำ in the third line is stacked, ค่า and the other lines normal, no clipping or extra wrap; (3) the real opening-course modal: "...ความคาดหวังก็... ต่ำเตี้ย" shows ต่ำ stacked at the original defect site, เตี้ย, ที่ชีวิต, ที่ที่ and the second paragraph normal, same 2 + 2 line layout.
- Lifecycle complete (check original -> backup verified -> install probe/probe/probe -> one run -> normal Alt+F4 -> restore -> check original); 29 protected files unchanged per the tester; Slot1/8000.sav hash unchanged; preferences/localpreferences unchanged (no settings change); 7 career/profile files changed as in every run entering the game; backup retained, no rollback. Game-folder files not independently re-hashed by PM.
- Cadence ≤ 9.5 s while waiting; modal first seen at 48.4 s. Tester ChatGPT under the user's authorization; PM compensated by direct image inspection. The Escape key did not close the dropdown (recorded; arrow used instead, nothing selected).
- Literal word ซึ่ง is not in this intro; upper-vowel/tone controls (ที่, ถี่, เตี้ย) were checked instead. Not a missing surface.

## Disposition

Candidate fresh-translation-006 (005 text/UI + fonts-only 15-cluster fix) PASSES scoped real-screen regression at Medium UI scale on three surfaces, including the original BUG-THAI-003 defect site. It supersedes 005 as the best installable candidate for the sara-am issue. BUG-THAI-003 status: FIX_VERIFIED_SCOPED (not CLOSED): remaining NOT_TESTED/UNKNOWN: UI Scale Small/Large, in-campus screens (staff/event/item/course surfaces), radio/character/DLC-only clusters (ค้ำ ย้ำ ม่ำ ล่ำ น่ำ), bold/rich-text and other consumers, long-session behavior. No clusters outside the 15 exist in the current corpus; future text additions need a new ligature+glyph per new cluster. Installing 006 into the user's live game is a user decision, not made here. BUG-THAI-002 (mid-word breaks), broader BUG-THAI-001 and terminology items are unaffected by this work and remain open.
