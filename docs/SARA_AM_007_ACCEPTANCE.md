# WO-SARA-AM-007 — accepted: BUILD_READY

2026-10-26. PM (Claude): ACCEPT_BUILD. Diagnostic probe, not a fix; BUG-THAI-003 OPEN.

## PM verification (independent)

- Probe bundles (3) re-hashed against manifest probe_sha256; parents match local 005. 25 protected hashes from reports/sara-am-007-preservation-before.json: all local ones re-hashed, none changed. Game-folder files accepted from the analyst record (outside PM mount); re-checked by the runtime lifecycle.
- Font extracted from the 005 and probe bundles (UnityPy + fontTools): embedded font SHA 49554400... matches the report; glyph count 459 -> 474, old glyph order preserved, cmap identical, 0 old glyphs changed, old hmtx identical; only maxp/hhea/head/loca/hmtx/post/glyf differ. For all 15 new glyphs PM recomputed: components are (base, glyph 82, tone), glyph 82 x = advance(base), tone centre offset from ring centre 0.0 (mai-ek) or 0.5 unit (mai-tho), gap to ring top = 74 for every glyph, advance = advance(base) + advance(82). Matches the report table.
- Not independently parsed by PM: the TMP ligature records (24 expected, first 9 original) and the localisation diff (relies on the analyst's readback); atlas estimate (7.3-7.7% of 512x512, estimate only).
- Reference sheet and the census-derived specimen reviewed from the report; the 64 px sheet is font evidence, not game evidence.

## Notes accepted

- ต่ำ is glyph 464 here with tone x 616 (outline-centred) versus 612 in glyph-001; 4-unit difference is deliberate per the WO. The accepted runtime result applies to the glyph-001 geometry; ต่ำ in this probe is re-tested.
- All 15 composites reach top 1083 (tone 42) or 1080 (tone 47) versus ascent 1061; runtime must show no clipping for every item, not just the first one.
- Bases have outline tops 548-559 (below the ring); no base-specific GSUB substitution or conflicting original ligature found. First-glyph sharing among new rules is resolved by the tone component, no prefix shadowing.

## Next

Single-run runtime WO docs/qa/WO_SARA_AM_GLYPH_002.md, 15 targets inspected individually.
