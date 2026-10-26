# WO-SARA-AM-006 — accepted: BUILD_READY

2026-10-26. PM (Claude): ACCEPT_BUILD. Diagnostic probe, not a fix; BUG-THAI-003 OPEN.

## PM verification (independent)

- Probe bundles (3) re-hashed against manifest probe_sha256 and parent hashes against local 005: all match. 21 protected hashes from reports/sara-am-006-preservation-before.json: the local ones re-hashed, none changed. Game-folder files accepted from the analyst record (outside PM mount), re-checked by the runtime lifecycle.
- Font: PM extracted the embedded Font 7716434233879021909 from the 005 and probe bundles with UnityPy (fallback Unity version set; bundle header has none) and compared with fontTools: baseline SHA f9855a70... and probe SHA bcf8e126... match the report; glyph count 459 -> 460, old glyph order preserved, new glyph saraAm006_tomaiEkAm; cmap identical; 0 of 459 old glyphs changed (compiled-glyph comparison); old hmtx identical; differing tables only maxp/hhea/head/loca/hmtx/post/glyf. New glyph is composite uni0E15@(0,0) + uni0E33@(641,0) + uni0E48@(612,236), advance 1056, LSB 60, bbox [60,-10,978,1083], as specified. PM did not independently parse the TMP ligature record or localisation diff (relies on analyst readback).
- Reference image (Chrome 155 / 64px) inspected by PM: the appended composite draws ต + ring + tone mark with the tone clearly above and separated from the ring, qualitatively like the accepted atomic reference. Font evidence only, not game evidence.

## Census (Q-A) accepted

440 direct [consonant][tone]ำ occurrences in 15 distinct clusters across the 005 corpus (น้ำ 250, ซ้ำ 55, ต่ำ 51, ล้ำ 36, ร่ำ 13, ค่ำ 10, ถ้ำ 6, ด่ำ 5, others <=3 each); 0 other mark-preceded atomic ำ runs; 32 occurrences sit in records with explicit LF. Details reports/sara-am-006-census.json. Scaling estimate: 15 composites + 15 ligatures (459 -> 474 glyphs), ~1-2 KiB bundle growth (not measured). Real unknowns remain atlas capacity/cache and layout across consumers.

## PM decision on the ascent risk

The new glyph top (1083) exceeds the font hhea/typo/win ascent (1061) by 22 units (1.4 px at 64 px) while the TMP FaceInfo ascent (41.22 at point 30) exceeds the glyph top (32.49 at point 30). Metrics are NOT to be raised to mask this: the runtime probe is the test. The runtime WO therefore requires explicit inspection of tone-mark clipping at the top of the glyph and line height. If clipping or line-height change is observed, that is a finding for the full design, not a reason to alter the probe.

## Next

Single-run runtime WO docs/qa/WO_SARA_AM_GLYPH_001.md. It resolves the largest remaining unknown: can the game load and draw a NEW glyph reached only through the ligature, and does the composite stack correctly in the game.
