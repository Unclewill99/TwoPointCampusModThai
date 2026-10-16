# Controller acceptance — bounded Thai paragraph A/B

Date: 2026-10-16. Read WO_VISUAL_012_REPORT.md; Controller inspected 07-a-resolution.jpg and independently verified all three installed originals. B comparison, row alignment and exact boundary accounting are attributed to the tester's supplied evidence; no new Controller game session.

Accept scoped positive baseline: A (no ZWSP) displays the synthetic paragraph across six bounded readable rows; all three repeats accounted by report. B reports identical bounds, rows and five boundaries. No observed base/combining-mark separation or internal word split at those five boundaries, within capture detail. No observed B improvement. Antialiasing remains readable in both per report.

Decision: continue using ordinary Thai without automatic ZWSP insertion as the default pipeline behavior. This is consistent with the existing no-production-ZWSP rule; it does not ban future evidence-backed per-context proposals. Favorable results for one paragraph/width do not establish dictionary breaking, universal line-boundary correctness, all scales or complete shaping. No permanent global width rollout approved.

Engineering baselines remain distinct: probe-003 for pilot translation/font behavior; probe-011 for experimental bounded layout. probe-012 contains synthetic test content, not a translation release. All three originals restored/hash-checked; backups retained.

Next prioritize representative actual translated tooltips and width/scale regression coverage over repeating this unchanged A/B. Also retain adversarial boundary cases and VOWEL-02 high-detail gap in the QA backlog. Runtime token/plural semantics, atlas stress and gameplay UI remain pending. No new runtime work order issued in this acceptance review.
