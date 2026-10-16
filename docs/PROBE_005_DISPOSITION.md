# Controller disposition — WO-VISUAL-005

Date: 2026-10-16. Source: docs/qa/WO_VISUAL_005_REPORT.md, preserved as submitted.

Controller read the report, inspected 11-control-tooltip-confirmed.jpg and independently ran manage_probe.py check --probe probe-005-control: both installed bundles original. Other reference comparisons are attributed to the tester's report; Controller has not run a new game session.

## Accepted results

- STACK-02: PASS for the six injected groups using prior runtime imagery and newly unobscured exact reference.
- VOWEL-02: reference-availability gap closed; detailed ascender/upper-vowel assessment remains PARTIAL because the existing game capture cannot resolve every mark reliably. No new valid-mark defect established.
- English wrapping control: FAIL as an experimental setup. The viewport-spanning blank white tooltip provides zero readable lines and no verified usable width. Absence of visible literal tags does not prove tag parsing succeeded.
- Thai A/B: BLOCKED / NOT_RUN, correctly not installed after control failure. No Thai-breaking defect, ZWSP benefit, dictionary support or production invisible-character decision can be inferred.
- Restoration: originals hash-checked; control backup retained. No direct probe-to-probe switching reported.

## Engineering decision

Retire the width-tag tooltip approach from the immediate test queue. Do not rerun probe-005 A/B unchanged, weaken the control gate, or patch additional tags speculatively. Exact cause of the blank control is unconfirmed; it could involve tooltip sizing, text measurement, rich-text configuration or another runtime path.

Next work: inspect the actual Campus tooltip/prefab TMP and layout settings, or identify an existing bounded multiline UI whose English baseline wraps normally. Establish readable bounded English behavior before Thai A/B. Keep probe-003 as the accepted translation engineering baseline; probe-004/005 contain synthetic diagnostics and are not release candidates.

Close VOWEL-02 evidence quality separately via sufficiently detailed capture of the same unchanged input if needed; enlarging compressed pixels cannot create missing detail. Full shaping, wrapping, atlas stress and gameplay/token/plural coverage remain pending. No new installation or release authorized by this disposition itself.
