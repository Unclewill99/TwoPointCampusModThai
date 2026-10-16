# Controller acceptance — bounded English wrapping

Date: 2026-10-16. Controller read WO_VISUAL_011_REPORT.md, inspected 07-resolution-tooltip.jpg, and independently checked originals for all three bundles. Other session observations and exact row counts/transcriptions are attributed to tester; no new Controller runtime session.

Accept scoped PASS: readable bounded long-English Resolution tooltip, additional automatic breaks within the newline-free middle segment, and all source segments visible. Report records 17 visual rows, 14 for the middle segment (13 extra breaks), plus one automatic break in the final segment. The inspected image corroborates a bounded multiline readable result. This establishes an English control for this path/environment, not dictionary or Thai behavior.

The paired text-child width plus parent ChildControlWidth patch is a successful experimental configuration. It does not isolate which field is sufficient alone or establish a particular C# override cause. Antialiasing retains four readable explicit lines per report, with a wider box: shared-layout effects exist and need broader release review.

Keep probe-003 as the translation baseline; probe-011 is the bounded-layout experimental baseline for the next same-slot Thai comparison. Next build should preserve its font/UI bundle bytes across Thai A/B and vary only ZWSP insertions in matching underlying text; verify actual bounds/font scale in each run. Do not approve production ZWSP or permanent fixed width from English results.

Three originals restored/hash-checked; backups retained. No further English repeat needed absent changes/failure. Full Thai wrapping, scales, gameplay and atlas/token/plural coverage remain pending.
