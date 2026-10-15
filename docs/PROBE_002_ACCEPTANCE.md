# Controller acceptance — probe-002 Settings comparison

Date: 2026-10-15
Evidence: docs/qa/WO_VISUAL_002_REPORT.md and local/qa/WO-VISUAL-002/command-evidence.json (desktop agent records). Controller read the report, inspected 06-probe-game-closed.jpg, and independently ran manage_probe.py check --probe probe-002: both installed files are original.

Decision: PASS for the reported Settings comparison only. Promote probe-002's original-primary-font plus Thai-fallback strategy as the engineering baseline for the next diagnostic probe. probe-001 remains failed and is not the installation candidate.

Observed scope: selected dropdown values and option lists visible against original baseline; Thai pilot Settings labels remain visible; reported Game/Video behavior persists after restart. Test environment: English, Medium UI Scale, 3840 x 2160 @ 60hz as read from the game, not inferred from screenshot dimensions. Controller's inspected image corroborates closed Game dropdown values and Thai labels; remaining paired views and restart outcomes are documented by the desktop agent.

This result supports the fallback strategy but does not establish the precise internal cause of probe-001's failure. It does not approve all 50 strings, all UI scales, arbitrary glyphs, mark positioning, word wrapping, plural selection, runtime argument semantics, saved gameplay or release distribution.

Next engineering milestone: a separate diagnostic probe containing explicitly mapped synthetic corpus cases, with exact code-point evidence and trusted same-font rendering references for mark-placement comparisons. Keep synthetic inputs separate from the translation pilot. Only after staged data reload checks should a new visual work order be issued. No further reinstall of probe-002 is needed solely to repeat this already-passed comparison.

Both original bundles are restored, backups retained. No production release approved.
