# Controller disposition — probe-004 synthetic diagnostics

Date: 2026-10-16. Source report: docs/qa/WO_VISUAL_004_REPORT.md, preserved as submitted.

Controller read all 12 case results, inspected 08-controls-unclipped.jpg and 10-resolution-tooltip.jpg, verified the diagnostic-map hash against the manifest, and independently checked installed hashes: both original. Other reference, scale and restart observations are attributed to the desktop tester, not a new Controller runtime session.

## Accepted scope

- Five cases PASS within injected coverage: STACK-01 subset, DESC-01, DESC-02, AM-01 subset, MIX-01 visible text. No new valid-mark collision established by the supplied evidence.
- Two PARTIAL: VOWEL-02 lacks exact reference coverage for every injected pair; STACK-02 reference partly obscured. These are coverage gaps, not established engine failures.
- Two diagnostic observations: AM-02 malformed and AM-03 decomposed. No spelling defect or required automatic normalization inferred.
- Three wrapping observations: WRAP-01/02/03 all remained on one line. Wrapping NOT_EXERCISED; no dictionary-breaking, line-boundary or ZWSP benefit acceptance.
- Small/Large and restart are supporting checks, not exhaustive reference comparisons or atlas stress validation. Dropdown regression checks passed as reported.

The report's parenthetical transcription of VOWEL-02 reference words includes differences from the corpus; exact reference file text and diagnostic map remain authoritative. Do not treat that paraphrase as a new test input.

## Baseline and next engineering tasks

Keep probe-003 as the translation engineering baseline; probe-004 is synthetic test content, not a playable translation candidate. BUG-THAI-001 remains target-word verified with broader positive stacked-mark evidence, but not universal shaping acceptance.

1. Generate exact-match, unobscured reference views for the injected VOWEL-02 and STACK-02 sequences. This can close reference gaps using existing runtime images if sufficient; no automatic need to reinstall.
2. Build a controlled wrapping experiment that demonstrably exceeds one container's usable width and compares unmodified/ZWSP text at identical width/font/scale. Record actual container behavior; do not infer wrapping from a long single-line tooltip. Do not introduce production invisible characters.
3. Keep runtime token/plural semantics, persistent/dynamic atlas stress, actual gameplay UI and uninjected corpus coverage pending.

All original bundles restored. No production release or complete Thai renderer approval.
