# VOWEL-02 evidence preflight

Date: 2026-10-18 (Asia/Bangkok). Controller preparation complete. Exact input/reference/font checks PASS; detailed runtime shaping remains PARTIAL. No new game session or probe installation.

## Exact authority

The probe-004 diagnostic map assigns CRP-VOWEL-02 to I2LS_UI_Settings / UI/Settings/CameraPanSensitivity, segment 4. The actual injected text is:

ปิ ปี ปึ ปื ฝี ฟิ ปั ฟั

These are the eight target pairs from the corpus, not the corpus's longer lexical examples. Byte-preserving bundle reload confirms the same decoded text at the mapped key/segment. No manual LF, ZWSP or alternate spelling is present. Each pair's Unicode sequence is in ../reports/vowel-02-evidence-audit.json.

The exact-reference HTML's first sample equals the injected text. Its embedded font SHA-256 is f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0, equal to probe-003's recorded matching font and one actual Font object embedded in the staged probe-004 font bundle. Probe-004 font bundle bytes equal probe-003 and the current probe-013 font candidate. Map and staged candidate hashes pass their frozen manifests. This verifies input/font identity, not browser/game shaping equivalence or a live font-loading check.

Reproduce with tools/audit_vowel_02_evidence.py. The audit is read-only apart from its new report. References and embedded font data remain local; no font/reference HTML is published.

## Existing evidence review

Controller inspected the original 08-controls-unclipped.jpg, 18-controls-large.jpg and WO-005 03-exact-both.jpg, without altering or enlarging them. All eight groups are visible in the game rows and exact reference. Large makes the row somewhat larger but still leaves only limited pixels for upper-vowel shapes and ascender clearance; it does not close every pair's detailed comparison. No new valid-mark collision or full shaping PASS is established.

The available Medium/Small/Large/restart game captures inventoried by the audit are all 1920x1080 JPEG. The exact browser reference capture is 1073x771 JPEG. Broad similarity is compatible with the prior scoped observations. Upscaling, sharpening or converting existing JPEG to PNG cannot recover missing detail. Keep PROBE_005_DISPOSITION.md's VOWEL-02 PARTIAL state. STACK-02's accepted six-group result is unchanged.

## Current capture capability checked

Read the installed computer-use SKILL.md, API, guidance and confirmation policy. Initialized the documented sky API and listed current windows; Campus was absent. Selected the unique returned Steam window. First requested capture showed foreground chat, so it was rejected as wrong-target evidence. Activating the selected Steam window and refreshing recovered a visually correct Steam capture, JPEG 1137x675. No game launch, pointer test, graphics/OS setting or installation occurred.

Current GetWindowStateInput documents only window, include_screenshot and include_text. It has no native-pixel-size, lossless-format, quality or capture-region argument. This session therefore has not established a higher-detail game capture route. Steam's dimensions are not proof of the current game capture size, monitor size or render resolution. The earlier 3840x2160 game setting and 1920x1080 returned images must remain distinct.

This is an evidence-method limitation, not proof that high-detail capture is impossible on the computer. Do not guess undocumented screenshot arguments, use another native-capture implementation as a bypass, or reinstall unchanged probe-004 merely to produce the same limited image again.

## Requirement before another visual WO

A capable desktop tester or user-operated capture route must first demonstrate an original game image that resolves the target marks, including enough context to identify Controls / UI scale / row. Prefer lossless native pixels where supported, but dimensions or file extension alone are insufficient: all eight upper marks and their clearance from ascenders must be inspectable. Retain the unmodified original file; an original-pixel crop may supplement it only with traceable provenance and cannot be presented as a new higher-detail acquisition.

Once that method is verified, define a narrow re-observation of the unchanged probe-004 input with the same font reference. Start with all installed files original, use guarded install/check/normal exit/restore/check, and separately preserve the original third UI bundle. No sliders, resolution/Apply changes, new font-feature edits, text replacements, hidden controls or gameplay are required. Record each pair independently; if any pair remains unclear, keep that pair unresolved instead of accepting the whole case. Browser reference must again show the actual face loaded. Existing reference identity alone is not a fresh runtime face check.

No desktop WO is issued yet because the requisite improved acquisition method is not verified. This follows the evidence gate in PROBE_013_MILESTONE.md, not an additional permission requirement. No user confirmation is pending; independent work can continue.

## Independent boundary-planning backlog

The existing corpus offers a separate next preparation route while detail acquisition remains unresolved:

| Case | Existing exact input authority | Future observation |
|---|---|---|
| CRP-WRAP-03 | qa/rendering-corpus.json, full original paragraph | At actual runtime breaks, record whether เ แ โ ใ ไ remain with following base; source paragraph must remain byte-equivalent as decoded text |
| CRP-STACK-01 | Existing corpus / exact mapped subset | Record whether an actual line boundary separates a base from its upper-vowel/tone sequence |
| CRP-WRAP-02 | Existing corpus and prior A/B maps | Retain no-ZWSP default; no new A/B run justified without a distinct unanswered boundary question |

These are planning entries, not executed tests or a new build assignment. Controller should next select a single source-backed boundary question and compare it with existing WO-012/013/014/015 observed boundaries before proposing another candidate. Bulk translation and full renderer acceptance remain unapproved.

Final read-only manage_probe check --probe probe-013 confirms all THREE originals, with staged/retained-backup verification. Candidate and original evidence were not modified.
