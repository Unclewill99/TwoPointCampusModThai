# Controller review — Antigravity initial QA plan

Date: 2026-10-15
Decision: Accept as a provisional test plan with the corrections below. No runtime test has passed yet. Original submission: proposals/ANTIGRAVITY_QA_SUBMISSION.txt. Agent execution logs and claims about its actions are self-reported.

## Evidence corrections

- Replace “Campus has no Thai font/localisation assets at all” with “the initial inspected catalog did not reveal explicit Thai-named references.” This is not a complete glyph-coverage, fallback, embedded-resource or DLC audit.
- Do not treat catalog_keys as asset keys: this report field contains the catalog JSON property names. catalog_relevant_ids contains filtered internal IDs. Font/localisation references are inventory evidence, not verified runtime configuration.
- Remove the unverified language count and blanket claim about the runtime localisation library. I2LS naming is a useful clue; actual parser and runtime integration must be inspected.
- UI scaling values, sliders, resolutions and aspect ratios are proposed coverage, not verified available settings. Record actual supported options; mark unavailable cases N/A with a reason.

## Corpus corrections

- Label every authored sentence synthetic rendering data, not extracted Campus text or an approved translation. Keep case labels outside displayed strings unless intentionally testing label rendering.
- Separate valid orthographic sequences from malformed-input robustness tests. For sara am, น + ้ + ำ is a valid sequence; น + ำ + ้ must not be treated as an equivalent valid spelling. Also test the decomposed sara-am representation separately, recording exact code points and whether any transformation occurred.
- Correct category examples: ผ is not an ascender case like ป/ฝ/ฟ; ตั๋ว includes an upper vowel, so it does not belong in the no-upper-vowel group. Test words must actually contain the target base-plus-mark combination; several proposed lower-tail examples do not.
- Add explicit base-plus-lower-mark diagnostic strings for ญ/ฐ/ฎ/ฏ and have their expected forms checked against a trusted Thai-capable reference renderer. Distinguish descender substitution from mark positioning; not every base is expected to lose its descender.
- Mark placeholders and tags as candidate syntax until extraction confirms supported grammar. Separate static text rendering from runtime variable substitution tests.
- ZWSP experiments are permitted only in the isolated reversible prototype. Keep an unmodified baseline, record insertion positions and code points, and test copying/search where available. This is not approval to add ZWSP to production translations.

## Test record requirements

Assign a case ID and status: NOT_RUN, PASS, FAIL, BLOCKED or N/A. Record game build, prototype revision, font identity/configuration, screen/string ID, exact input (including code points for diagnostic cases), resolution, actual UI scale, expected result, actual result and screenshot. For dynamic fonts, repeat after a cold restart and after visiting multiple screens to expose missing dynamic glyphs or atlas exhaustion.

Severity follows impact: unreadable text or lost meaning can be Major regardless of whether the cause is a tone mark or clipping. Do not set severity solely by visual category. Suggested fixes remain hypotheses until reproduced and verified.

## Next assignment for Antigravity

Produce docs/qa/TEST_MATRIX.md, docs/qa/BUG_REPORT_TEMPLATE.md and docs/qa/rendering-corpus.json incorporating this review. Use a new branch if working in a separate clone; if sharing the Controller checkout, write only these assigned new paths and do not switch branches, commit or push without coordination. Do not edit the original submission or Controller documents. All runtime cases start NOT_RUN. Wait for the Controller prototype before modifying or launching game tests.
