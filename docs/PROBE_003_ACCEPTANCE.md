# Controller acceptance — probe-003 target-word test

Date: 2026-10-16. Evidence: docs/qa/WO_VISUAL_003_REPORT.md, including its chronological reference and zoom follow-ups. Earlier BLOCKED statements in the report are superseded only within the final scoped acceptance.

Controller inspected 02-medium-close.png and 09-user-same-font-reference.png: the tone mark above sara ii in ถี่ is visibly separated in the probe-003 crop and consistent in relative arrangement with the reference. Reference screenshot reports the custom ProbeThai face loaded with check=true. The desktop agent records 100% browser zoom evidence in its final follow-up and Small/Large/restart/dropdown results from its runtime session; Controller has not rerun that session. This is not a pixel-identical positioning comparison.

Decision: accept PASS for the reported target-word test, retaining the scope of each observation. Probe-003 becomes the candidate engineering baseline for broader diagnostic work. BUG-THAI-001 is MITIGATED / TARGET-WORD VERIFIED in probe-003; keep it open for broader stacked-mark regression rather than claiming all Thai shaping fixed.

Independent manage_probe.py check --probe probe-003 returned original for both installed bundles. Backups remain. No permanent installation or production release approved.

Remaining: synthetic in-game upper/lower mark and ascender/descender coverage, sara am variants, mixed-script fallback, wrapping, atlas stress and runtime token/plural semantics. Browser-only corpus display is not game coverage. Next milestone is a separately mapped synthetic diagnostic build; do not repeat the completed target-word test absent changes or new failures.
