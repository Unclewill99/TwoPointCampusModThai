# WO-VISUAL-018 screening acceptance

Date: 2026-10-21. Decision: ACCEPT_SCOPED_SCREENING_BENEFIT.

Controller read qa/WO_VISUAL_018_REPORT.md and inspected the four linked primary A/B images directly. MSAASamples B moves the visible break to หรือลดจำนวน / ลงเพื่อ, while A breaks at the earlier natural space. WorldDetail retains the same four visible rows. Both pairs appear complete and contained at capture detail, with no obvious new word split or missing glyph. Tooltip bodies span approximately x=936..1356 in the 1920x1080 captures (about 420 pixels, visual uncertainty approximately 3 pixels); apparent font scale is comparable. This supports an input-associated wrapping change within the screened scope, not an exact runtime layout measurement.

Accept BENEFIT_OBSERVED for two actual keys, requested width 800, Medium only. MSAASamples demonstrates later use of available width; its baseline was already clean, so this is not evidence of correcting a baseline word-split defect. WorldDetail supplies a no-observed-regression comparison, not a second independent improvement. Reported offsets 50/87 refer to existing reviewed maps; no new exhaustive codepoint audit was performed.

The report identifies 3840x2160 display with LANCZOS downsampling to 1920x1080. These captures support coarse wrapping/containment findings, not fine native vowel/tone-mark positioning. Fine shaping remains unresolved. Four 600-width cells remain DEFERRED, not passed. BUG-THAI-002 remains OPEN; no production ZWSP, global width, automatic tokenizer or release approval.

Fresh Controller manage_probe.py check --probe probe-018-800b reports original for all three installed bundles, and validates that candidate via the existing manager. Per-run installation/restoration and input verification are attributed to the QA report; Controller did not rerun the game or independently reconstruct the entire lifecycle.

Process budget outcome is unverified: the evidence directory includes many additional exploratory captures beyond the compact four-image submission. Do not claim the one-recovery/45-minute target or token savings was demonstrated without execution accounting. No additional desktop test is assigned automatically. Next: Controller selects a bounded non-runtime translation/context task; width-600 and shaping work stay in the backlog.
