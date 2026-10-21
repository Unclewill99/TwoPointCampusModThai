# BUG-THAI-002 — internal Thai word splits at bounded tooltip edges

- Status: OPEN / OBSERVED in probe-016; WO-017 demonstrates experimental mitigation for the same paragraph/container/Medium. Production extent and general remedy remain unproven.
- Provisional impact: Moderate readability/segmentation issue; no content loss observed.
- Build: Campus 10.3.169253+2024-12-06.1241, English / Medium, Full Screen Window, reported 3840x2160 @60hz; returned capture 1920x1080 JPEG.
- Slot: UI/Settings/Tooltips/Resolution, temporarily replaced with three unchanged CRP-WRAP-03 paragraphs; not the production Resolution translation.
- Reproduction: frozen probe-016, main-menu Settings > Video, hover Resolution label. Font/UI bytes equal probe-013; source has no whitespace, LF, ZWSP or tags.
- Evidence: ../../local/qa/WO-VISUAL-016/06-resolution-paragraph.jpg and 93-row-boundary-accounting.json; submitted WO_VISUAL_016_REPORT.md.

Expected: avoid cutting inside words such as เรียน and ทุก in natural Thai wrapping while retaining all input text and complete base/mark sequences. This is a word-boundary expectation, not a claim that dictionary segmentation is implemented.

Observed: five readable rows with all 237 codepoints preserved; global cut 113 gives เรีย / น within เรียน, cut 172 gives ทุ / ก within ทุก, and cut 227 gives เรี / ยน within เรียน. Paragraph-local offsets are 34,14,69. Cut 55 gives เตรียม / ตัว and is tracked separately as a broader-expression boundary. The three word cuts occur inside individual paragraph copies, not synthetic joins at 79/158.

No visible glyph loss, clipping or detached combining mark at these edges. That does not resolve the internal word split. No cut immediately follows a leading-vowel codepoint or begins with a combining mark; those direct risky edges were not forced. Do not conflate segmentation, mark attachment and content completeness.

Controller independently inspected the original image and verified exact row/map equality without normalization plus offsets. Scope remains this synthetic paragraph at the tested bounded width/Medium. Native shaping and dictionary algorithm are not established, and source-spelling or game font defects are not inferred. First research the actual line-breaking configuration before designing a same-text controlled remedy.

All three game files restored to original and independently verified, backups retained. No fix applied, no new build/runtime assignment, automatic production ZWSP or global layout rollout. Prior actual-tooltip scoped acceptance remains evidence for those inspected strings only.


## Experimental follow-up prepared — 2026-10-18

probe-017 proposes 47 manual U+200B opportunities in the exact same underlying text/font/UI. WO-VISUAL-017 ready, NOT_RUN; no fix accepted or production policy changed. See ../THAI_LINEBREAKING_FINDINGS.md.


## WO-017 reviewed — scoped experimental mitigation (2026-10-18)

B retains all 237 underlying codepoints. Cuts 49/100/154/207 correspond to proposed opportunities and give three distinct contexts; no occurrence of เรียน or ทุก is split at any B edge. Complete/contained/readable image, no new bad edge or visible U+200B artifact observed. Controller image/text/offset/hash review passed. Accept experimental benefit versus historical A only; bug remains OPEN, no production ZWSP or automatic tokenizer approval. See ../PROBE_017_ACCEPTANCE.md.
