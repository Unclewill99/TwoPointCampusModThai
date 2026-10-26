# WO-SARA-AM-GLYPH-002 — accepted: ALL_STACKED_OK (PM disposition; tester reported INCONCLUSIVE for a timing deviation)

2026-10-26. PM (Claude): ACCEPT_EVIDENCE. Report docs/qa/WO_SARA_AM_GLYPH_002_REPORT.md, reports/sara-am-glyph-002-runtime.json.

## PM verification

- Native image local/qa/WO-SARA-AM-GLYPH-002/01-modal-native.png: SHA256 fffbf022... matches the report, 3840x2160. PM inspected the full frame (downscaled) and a 3x nearest-neighbour crop of the specimen area. All 15 targets show the tone mark above the ring with a visible gap, base and sara-aa on the normal baseline, no clipped tone tops, no overlap with neighbours: L1 น้ำ ซ้ำ ต่ำ ล้ำ; L2 ร่ำ ค่ำ ถ้ำ ด่ำ; L3 ฉ่ำ ล่ำ ค้ำ ย้ำ; L4 ว่ำ น่ำ ม่ำ. The out-of-set negative control ท่ำ keeps the old crowded form; L5 ตา ถี่ ทำ นำ are ordinary. All five rows sit inside the specimen panel with no wrapping or clipping. This is a visual judgement at the observed scale, not a contour-level guarantee.
- Lifecycle in the report complete: original -> backup verified -> install probe/probe/probe -> normal Alt+F4 -> restore -> original/original/original; 25 protected files unchanged per the tester; Slot1/8000.sav hash unchanged; 7 career/profile files changed as in every run entering the game; backup retained, no rollback. Game-folder files not independently re-hashed by PM.

## Disposition of the timing deviation

The observation loop had a 110.3 s gap (limit 15 s), so the modal's first-appearance time is unknown and the 60 s modal-arrival condition cannot be confirmed. PM decision: the cadence and 60 s rules bound unattended waiting and input risk; they are not part of the question this probe answers (does each cluster render stacked). No input was sent during the gap, the modal persists until dismissed, and the rendering evidence is a single native capture whose integrity is verified. The result is therefore accepted as valid evidence and the verdict is set to ALL_STACKED_OK, with the deviation recorded. No rerun. Arrival time of the modal must not be cited from this run. Tester was ChatGPT under the user's authorization; PM compensated by direct image inspection.

## What this establishes

VERIFIED (runtime, this modal context): all 15 census clusters render correctly through the appended composites and exact 3-component ligatures; the out-of-set cluster and ordinary text are unaffected; no visible clipping from the 19-22 unit ascent excess; ต่ำ with the re-centred geometry (glyph 464) is correct.

NOT established: real in-game screens containing these words, other UI scales, wrapping across lines, bold/rich-text contexts, other text consumers, repeated loads/atlas behavior over a longer session. BUG-THAI-003 stays OPEN until those are covered.

## Next

Production candidate: stored text unchanged; fonts bundle = glyph-002 fonts bundle; localisation and UI bundles identical to 005. WO-SARA-AM-008 builds it and plans real-screen regression.
