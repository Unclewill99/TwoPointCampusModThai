# Probe-001 failure and probe-002 comparison design

Date: 2026-10-15. Visual report received from desktop testing agent. Controller read the report and command evidence, inspected 05-probe-game-settings.jpg, and independently checked current installed hashes via probe-002 manager: both original.

Accepted result: probe-001 runtime loading and some Thai Settings labels observed; overall FAIL due to blank closed dropdown selected values, reported reproducible after restart. No original Settings baseline exists, so causality remains unproven. Full shaping and diagnostic matrix remain untested.

Hypothesis: global font-term mapping to the reused dynamic font may interact with selected-value rendering/material setup. Other causes remain possible. Probe-002 tests a narrower approach: original English font mapping/materials retained, reused dynamic Thai font appended last in 22 serialized TMP fallback tables. Dynamic slot has no fallback links, so this addition does not introduce a path back from it into the static font graph. No synthetic diagnostic injection is included.

Build checks passed: reload 22 fallback references, exact original font-localisation mapping, all 50 r3 substitutions. Installed originals remain unchanged. Runtime status of probe-002: NOT_RUN. Work order: docs/qa/WO_VISUAL_002.md. Do not label this a verified fix before the comparison.
