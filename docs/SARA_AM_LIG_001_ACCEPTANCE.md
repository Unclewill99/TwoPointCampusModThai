# WO-SARA-AM-LIG-001 — accepted: EXECUTED

2026-10-26. PM (Claude): ACCEPT_DIAGNOSTIC_RESULT. Report docs/qa/WO_SARA_AM_LIG_001_REPORT.md, reports/sara-am-lig-001-runtime.json.

## PM verification

- Native image local/qa/WO-SARA-AM-LIG-001/01-modal-native.png: SHA256 82bada62... matches report; 3840x2160. PM inspected a crop of the specimen area directly: L1 shows a single ก glyph, L5 shows ก, L2 (ต้ำ), L3 (ค่ำ) and L4 (ตา ถี่) show their ordinary sequences with no sentinel. L2/L3 still display the known crowded/overlapping atomic tone+sara-am defect, as expected (the probe only targets the exact [118,42,82] sequence).
- 17 protected files from the WO-004 before snapshot: the 12 local ones re-hashed by PM, unchanged. Game-folder files accepted from the tester's final check (not independently re-hashed by PM).
- Lifecycle in report is complete: check original -> backup verified -> install -> check probe -> normal exit -> restore -> check original. Save comparison 7 changed / 4 unchanged / 0 new / 0 missing (career/profile files change on entering the game, same pattern as earlier runs); backup retained; no rollback.

## Procedural notes (accepted, not result-affecting)

- The tester was ChatGPT, explicitly authorized by the user in place of Antigravity. Because of this the independent-tester separation was not in force for this run; PM compensated by direct image inspection and hash checks.
- Observation intervals were 18.1 s and 21.9 s (WO limit 15 s). No input was sent during the wait and the modal was seen at 51 s, within the 60 s limit, so the result is unaffected. Logged as a deviation.
- The L1 vs L5 glyph masks differ slightly (138 vs 142 dark pixels, 16x20 vs 16x21); accepted as same character shape by visual inspection, not pixel identity.

## What this establishes

VERIFIED (runtime, this modal context): the game executes a serialized 3-component LigatureSubstitution record [118,42,82] -> glyph 29 on the target Thai TMP and does not apply it to different tone (L2) or different base (L3). This resolves the executor gate from WO-004 for the exact-sequence ligature case. It does NOT show: that an appended/new glyph can be loaded, correct ต่ำ rendering, other bases/tones, other text consumers, longest-match behavior, or production safety. BUG-THAI-003 stays OPEN.

Consequence: option D+B (one ligature per exact cluster -> a full-cluster glyph) is now a justified asset-only path. The largest remaining unknown is whether the game can render a ligature target glyph that is NEW (not in the original font) and whether a composite glyph can be made to stack correctly. That is the next probe (WO-SARA-AM-006). Option A (code plugin) is no longer the only route and needs no decision for now.
