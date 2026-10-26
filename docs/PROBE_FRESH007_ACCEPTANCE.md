# fresh-translation-007 — Controller acceptance of WO-VISUAL-019 (2026-10-26)

Decision: ACCEPT_SCOPED_BENEFIT. BUG-THAI-002 → FIX_VERIFIED_SCOPED (not closed). fresh-translation-007 stays installed as the live candidate by the user's choice; 006 remains the fallback (`restore --probe fresh-translation-007` then `install --probe fresh-translation-006`).

Basis: Controller inspected the four user captures (docs/qa/WO_VISUAL_019_REPORT.md). The production defect that triggered SEGMENTATION-002 (Level_Description `ต่ำแล|ะมี`) no longer occurs; two further wrapped texts (a loading tip, a mail body) break only at proposed word boundaries; the ต่ำ ligature from BUG-THAI-003 is unaffected; no visible artifact at any U+200B. Build on Windows matched Controller's Linux dry-run exactly (11,429 records, 84,223 U+200B, strip-check identical to 006).

Limits: UI Scale of the captures not recorded; the originally reported loading tip (Tips_LS_Paths_Text) was not reached; 006-verified regression screens not re-captured; no tooltip/rich-text container checked under 007; segmentation quality beyond the viewed screens rests on the dictionary + guard, not on review. One unrelated header-font shaping gap (เยี่ ยม in a bold header) is logged under BUG-THAI-001 pending a 006 comparison.

Next: keep playing on 007 and report any screen with a bad break, visible gap, or missing text with its UI Scale. Controller backlog: UI Scale Small/Large regression sweep on 007, header-font shaping item, residual segmentation cases (extra-words.txt → re-run segment_corpus_002.py → rebuild 008), terminology items.
