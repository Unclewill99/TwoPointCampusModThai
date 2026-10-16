# Controller review — actual tooltip translation draft

Date: 2026-10-16. Received local/translations/TOOLTIPS-001.th.json, 20 records. Independently ran tools/validate_tooltips.py: zero structural errors. Exact source/translation hashes in reports/tooltips-001-validation.json. Includes token order, all immutable source fields, LF/tab/blank-line structure and trailing whitespace checks. No runtime or visual approval implied.

Decision: accept draft for independent linguistic QA; no request for another full translator rewrite now. Nine AMBIGUOUS flags remain. Pilot r3/source files unchanged.

## Editorial decisions and questions

- Resolution: current literal wording is acceptable as a draft; alternative ความละเอียดหน้าจอของเกม may suit multiple display modes. Keep unresolved until QA assesses terminology consistency; do not change actual graphics behavior to settle wording.
- FullScreenMode: source is generic; no need to add mode names. Assess whether เลือกโหมดการแสดงผล is clearer than the literal full-screen-only phrasing, using actual available options where evidenced. Not yet a glossary promotion.
- MaxFPS: retain ambiguity and source behavior claim. “ไม่มีผลเมื่อเปิดใช้ VSync” requires actual behavioral evidence; do not infer it from general graphics knowledge or UI availability.
- AntialiasingMode/Quality: translating the evident comparative meaning of the source typo is acceptable; source bytes stay intact. Do not reproduce incorrect English grammar mechanically in Thai.
- CharacterLimits: preserve all four variables, colour tags and all source whitespace. Variable names containing UNLIMITED do not authorize rewriting visible text as unlimited. Runtime values/selection remain unverified.
- Technical English names and proposed Thai terms are provisional within this batch. Check consistency and user clarity rather than claiming they are approved industry standards. Parentheses are ordinary ASCII; no per-row NEW_CHAR flag required merely for adding them. Actual font coverage still belongs to rendering QA.
- Keep no automatic ZWSP and no added manual line breaks. Existing LF structure is preserved; potential visual fit waits for the bounded-layout test.

## Antigravity assignment — WO-QA-TOOLTIPS-001

Read this review, approved style/glossary, local/source/TOOLTIPS-001.json and local/translations/TOOLTIPS-001.th.json. Independently check all 20 meanings, quality/performance tradeoffs, consistent technical terminology, placeholders/markup and whitespace. Do not mistake “characters” for text glyphs in draw-distance/limits contexts. Separate source ambiguity from a translation defect.

Write docs/qa/TOOLTIPS_001_LINGUISTIC_REVIEW.md with exact IDs/keys, findings, severity/impact, proposed alternatives and explicit unresolved runtime questions. Scope is language/data only. Do not assign in-game PASS, run graphics experiments or alter translation/source/tools/game files. Do not switch branch, commit or push in shared checkout. Do not publish the full source corpus; concise key-based findings are enough.

Controller will integrate selected changes into a NEW local revision, validate and build a real-tooltip visual candidate. Desktop visual agent waits for a separate Small/Medium/Large work order. No translation install or shared-width rollout authorized by this review.
