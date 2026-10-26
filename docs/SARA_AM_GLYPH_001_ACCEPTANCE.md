# WO-SARA-AM-GLYPH-001 — accepted: STACKED_OK

2026-10-26. PM (Claude): ACCEPT_DIAGNOSTIC_RESULT. Report docs/qa/WO_SARA_AM_GLYPH_001_REPORT.md, reports/sara-am-glyph-001-runtime.json.

## PM verification

- Native image local/qa/WO-SARA-AM-GLYPH-001/01-modal-native.png: SHA256 993a727d... matches the report, 3840x2160. PM inspected a 3x crop of the specimen area directly: L1 shows ต่ำ with a complete base and sara-aa, the ring below a raised tone mark with a clear gap, no visible top truncation; L2 (ต้ำ) and L3 (ค่ำ) keep the old crowded form; L4 (ตา ถี่) and L5 (ทำ) are ordinary.
- PM independently diffed the aligned control regions against the saved LIG-001 modal image: L2, L3 and L4 regions have 0 changed pixels (same crops as the report).
- Protected files: local ones unchanged (PM re-hash in WO-006 acceptance still the latest PM check; the tester's final check covers all 21). Game-folder files accepted from the tester's final manager check (original/original/original), not re-hashed by PM.
- Lifecycle complete; Slot1/8000.sav unchanged (hash matches the earlier recorded value 5b4dac72...); 7 career/profile files changed as in every run that enters the game; backup retained, no rollback.
- Cadence this run: observations every ~6.7 s, all within the 15 s limit. Tester was ChatGPT under the user's authorization; PM compensated by direct image and pixel checks.

## What this establishes

VERIFIED (runtime, this modal context): the game can load and draw a NEW glyph appended to the embedded Thai font and reached only through an exact 3-component ligature, and a composite built from existing outlines stacks ต่ำ correctly (tone above ring, clear gap) without visible clipping, with specificity preserved (other tone/base unchanged). The 22-unit ascent excess did not cause visible clipping here.

NOT established: other bases/tones (the 15-cluster census set), other consumers/UI scales/wrapping, atlas behavior with many appended glyphs, long-session/caching behavior, normal/bold/rich-text variants, production safety. BUG-THAI-003 stays OPEN.

## Scope decision (PM)

Proceed with option D+B for the 15 census clusters (440 occurrences in the 005 corpus). Stored text is NOT changed: the fix lives only in the font bundle (embedded font + TMP ligature records). The production candidate will therefore be 005 + a changed fonts bundle, built only after a 15-cluster diagnostic probe passes runtime QA. Clusters outside the census (none exist in the current corpus) stay unfixed and must be added by a later, separate change; no generic/auto generation for all possible bases/tones is approved now. Next: WO-SARA-AM-007 (offline build of the 15-cluster diagnostic probe).
