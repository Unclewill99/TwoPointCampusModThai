# BUG-THAI-003 — ไม้เอกกับนิคหิตของสระอำชนกันใน “ต่ำ”

- Status: OPEN / USER-REPORTED_OBSERVED; Controller inspected supplied image. No root cause or mitigation established.
- Candidate: community-merge-006, attributed to user's current WO-GAMEPLAY-002 session; not a new Controller runtime run.
- Context: Freshleigh Meadows opening “วันแรกของการเปิดเรียน” modal, phrase “และความคาดหวังก็... ต่ำต้อย”.
- Source record: I2LS_Levels::Levels/Freshleigh/Level_Intro_Text::segment-533.
- Sequence: ต่ำ = ต U+0E15 + ่ U+0E48 + ำ U+0E33. The upper circle/nikkhahit component of sara am collides/crowds with mai ek per user evidence; this is distinct from the older ถี่ upper-vowel/tone case.
- Expected: separate, readable Thai mark placement for mai ek and sara-am upper component using an appropriate same-font shaping reference.
- Actual: user identifies overlapping upper components; supplied closer PNG makes a visible positioning concern explicit. Readable base text does not imply correct shaping.
- Evidence: local/qa/BUG-THAI-003/user-native-evidence.png copied byte-for-byte from Screenshot 2026-10-21 221631.png; provenance/hash/dimensions in evidence.json. Do not assume native full-display size or lossless game acquisition merely because file is PNG; preserve user file exactly.

## Scope correction

WO-GAMEPLAY-002 remains usable for initial entry with known defects, not technical-defect-free. Fine shaping now has a positive observed user defect in this word rather than solely untested status. BUG-THAI-001 remains a separate historically mitigated ถี่ case; BUG-THAI-002 word splitting remains OPEN. No universal shaping PASS.

## Follow-up constraints

Trace the actual modal TMP/font/fallback and same embedded font reference for exact ต่ำ sequence. Investigate sara-am decomposition/reordering and mark positioning as hypotheses, not a proven engine deficiency. Do not silently rewrite Unicode source, patch all glyphs, inject global ZWSP, or claim font feature table presence proves runtime shaping. No new game run needed merely to reproduce the supplied image. Keep the word ต่ำ in the targeted technical case even if editorial wording is later changed; replacing it to hide the collision does not fix Thai rendering.
