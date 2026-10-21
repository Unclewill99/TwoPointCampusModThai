# WO-DROPDOWN-002 disposition — 2026-10-21

Decision ACCEPT_DIAGNOSTIC_CHECK_VISIBLE. Controller read the submitted report and inspected the single original linked capture: LogLevel visibly reads CHECK Error, adjacent five unchanged captions remain blank. One image, zero recovery and approximately three minutes are tester-reported. UI Scale unverified in-screen; fine shaping outside scope.

The merge-004 build changed only six LogLevel values to ASCII CHECK + original English; font/UI identical to merge-002. This establishes active loading/lookup/display of the marked Error option at this target. It weakens a generic missing-key, wrong-caption, or unloaded-localisation explanation for that option. It does not demonstrate that the Thai string arrives unmodified at TMP, nor prove a font-only cause. merge-003 direct font/material change was insufficient, so do not repeat it broadly.

Next investigate Thai-specific translation processing and TMP caption generation/overflow/masking, including runtime font overrides. Prefer static comparison of working labels with caption before another bounded runtime control. No new candidate or desktop WO assigned in this acceptance. A practical English-caption fallback may be considered separately but is not a Thai rendering fix.

Fresh manage_probe.py check --probe community-merge-004 validates staged hashes and confirms three installed originals. merge-002 remains BLOCKED; merge-004 is a retained diagnostic only, not the general trial build. No commit/push or game run by Controller.
