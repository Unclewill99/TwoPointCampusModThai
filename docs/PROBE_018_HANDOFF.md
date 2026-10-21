# Probe-018 controlled matrix handoff

Date: 2026-10-18. Four local candidates built/reloaded and guarded preflight checked; none installed. Runtime NOT_RUN. Independent linguistic maps accepted unchanged in SEGMENTATION_001_ACCEPTANCE.md. This is an experimental matrix, not a production translation candidate.

| Exact probe | Requested text-child width | Input | UI relative to probe-013 | Localisation relative to probe-013 |
|---|---:|---|---|---|
| probe-018-800a | 800 units | Plain A | Identical bytes | Identical bytes |
| probe-018-800b | 800 units | Reviewed marked B | Identical bytes | Only MSAASamples / WorldDetail segments differ |
| probe-018-600a | 600 units | Plain A | Only RectTransform 3218277146759428662 m_SizeDelta.x: 800→600 | Identical bytes |
| probe-018-600b | 600 units | Reviewed marked B | Same bytes as 600a | Same bytes as 800b |

All font bundles match probe-013. Normal wrapping, font settings, layout group's ChildControlWidth=0 and every other UI object's raw data remain unchanged. Source translations, reviewed proposal package and earlier probes are preserved. Per-width A/B UI/font equality and cross-width A/B localisation equality are asserted. B-minus-U+200B equals A literally, including existing source LF/spaces and Latin text. MSAASamples has ten reviewed optional cuts; WorldDetail twenty-four. No new word-cut proposal, tags or manual LF.

Reproduction: tools/build_probe_018.py. It requires all installed originals and frozen input/review hashes, refuses existing output directories, writes only new local candidate folders and reports/probe-018-build.json, and reloads to verify exact source-segment/UI-object isolation. Do not rerun it over frozen outputs. Manager choices now include all four exact names. All four read-only check commands succeeded, reporting all THREE installed originals. Manager install/restore safeguards are unchanged.

Ready assignment: qa/WO_VISUAL_018.md, two keys × two requested widths × A/B = eight prospective cells, all at Medium. Requested Unity width is not runtime evidence; measure actual box widths and compare within/between pairs. If 600 is not materially narrower in the actual captures, the two-width question is not exercised. No need to rerun the 18-key accepted scale matrix, WO-017's synthetic paragraph or hidden rows.

Candidates are experimental: global shared-width suitability, automatic segmentation, production ZWSP, BUG-THAI-002 closure, native shaping and release remain unapproved. Antigravity receives the brief through user relay; no other chat was messaged. No game launch, installation, commit/push or font/binary upload occurred in this preparation.


## Active assignment revision — 2026-10-21

The revised scope section in qa/WO_VISUAL_018.md supersedes the eight-cell runtime assignment above: run only 800a/800b (four cells); 600a/600b deferred. All four frozen candidates remain unchanged. Reuse static evidence, bound capture recovery, issue a compact screening report and stop after restoration. The second-width question remains untested.
