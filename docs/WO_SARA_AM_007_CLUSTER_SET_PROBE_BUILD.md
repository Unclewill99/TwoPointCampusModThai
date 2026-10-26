# WO-SARA-AM-007 — 15-cluster diagnostic probe (build + offline verification)

Issued 2026-10-26 (Asia/Bangkok) by Claude (PM/Controller). Assignee: ChatGPT (engineering). READY_FOR_HANDOFF via user; not confirmed until the report exists. OFFLINE BUILD + VERIFY ONLY: no game launch, no install, no runtime test, no commit/push. Read first: SARA_AM_GLYPH_001_ACCEPTANCE.md, SARA_AM_006_CENSUS_AND_GLYPH_PROBE.md (geometry method, build checks, preservation method), reports/sara-am-006-census.json, the glyph-001 build script, manage_probe support.

## 1. Goal

Extend the proven one-cluster mechanism (appended composite glyph + exact 3-component ligature) to all 15 census clusters in a NEW diagnostic probe, probe-sara-am-glyph-002, so one runtime run can check all of them in the real modal. Stored text is not modified in this probe other than the diagnostic specimen record.

Clusters (base, tone): น้ำ ซ้ำ ต่ำ ล้ำ ร่ำ ค่ำ ถ้ำ ด่ำ ฉ่ำ ล่ำ ค้ำ ย้ำ ว่ำ น่ำ ม่ำ, i.e. tones U+0E48 and U+0E49 only, bases U+0E19 U+0E0B U+0E15 U+0E25 U+0E23 U+0E04 U+0E16 U+0E14 U+0E09 U+0E22 U+0E27 U+0E21 (re-read the exact list from the census JSON; if the census JSON differs from this list, trust the JSON and say so).

## 2. Build specification

New directory, exclusive create: local/prototype/probe-sara-am-glyph-002 (never overwrite any existing probe). Base = fresh-translation-005, read-only copy.

Font (embedded Thai font object 7716434233879021909; baseline f9855a70... must stay the baseline): append 15 composite glyphs (expected IDs 459..473 in a deterministic order; verify and record), each = base glyph at (0,0) + glyph 82 at x = advance(base) + tone glyph at the offset that places it above the ring of glyph 82 with a clear gap. Derive each from actual outlines, not from the ต่ำ numbers: the ring offset depends on advance(base); the tone offset x must centre the tone over the ring using that tone glyph's own outline (tone 42 and tone 47 have different outlines); y must give a visible gap (record the gap per glyph; target at least the 74 units achieved and accepted for ต่ำ unless an outline forces otherwise, and explain any difference). Check every base glyph: if a base has anything that interacts with the stack (anchors, ascender, alternate/variant forms in GSUB that the browser or TMP would use instead of the plain base glyph), report it and do not guess. Advance = advance(base) + advance(82). No cmap entry, no change to existing glyphs/metrics/cmap, no change to hhea/OS/2 ascent values (known 22-unit excess stays visible as a risk; report the new maximum top over all 15 glyphs).

TMP (object -1239755799206566947 only): add 15 LigatureSubstitution records [base, tone, 82] -> new glyph. Required pre-checks as in WO-005/006, now for every base glyph ID: none of the 9 original ligature records may share the first glyph with any new record, otherwise the first-match order matters and you must analyse and report it (do not reorder originals). Also check that no new record's component prefix shadows another (e.g. a 2-component record starting with the same two glyphs). Add nothing else (no pair/anchor/MarkToMark records, flags, atlas settings, glyph/character tables).

Localisation: change only I2LS_Levels533 to a labelled specimen with all 15 clusters plus controls, laid out so nothing wraps or clips at the same modal size as before (the modal accepted 5 short lines; if more lines are needed, group about 3 words per line and keep line count modest; report how you verified fit, using the offline width estimate and noting that fit is a runtime question). Include: all 15 clusters in real words or bare clusters as labelled items; at least these negative/unaffected controls: a cluster NOT in the set (e.g. ท่ำ U+0E17 U+0E48 U+0E33, expected to keep the old crowded form), ตา ถี่ (ordinary), ทำ (untoned sara-am), นำ. Use the Latin labels used previously. Record exact codepoints per line in the manifest.

## 3. Offline verification required

fontTools reopen with no errors; glyph count 459 -> 474; all old glyph slices, hmtx, cmap byte-equal; list per new glyph: components, offsets, bbox, advance, gap to ring, top; render each new glyph at 64 px as a font-evidence sheet and visually compare against the accepted atomic Chrome reference (state this is not game evidence); Font object and TMP raw-object diff only (as WO-006); TMP readback shows 9 + 15 = 24 ligature records, originals unchanged, new ones exact; only I2LS_Levels533 differs in localisation; UI bundle identical; manifest with all hashes, codepoints and expected-observation table per row (stacked / flawed / unchanged-crowded / blank-tofu); manage_probe check original/original/original (extend manager for the new name); 21+ protected hashes before/after (include glyph-001 files). Also report estimated atlas use for the 15 new glyphs vs the 512x512 atlas (glyph raster size at point 30 plus padding), as an estimate only.

## 4. Constraints

Offline only; do not modify frozen005, 001a/b, lig-001, glyph-001, installed originals, the baseline font object in 005, or any production text. No corpus rewrite, no global shift, no cmap entries, no guessed patching; new outputs exclusive-create; VERIFIED / INFERRED / UNKNOWN labels; no claim of a production fix. If a base glyph or ligature conflict blocks one cluster, finish the rest, list the blocked clusters with evidence, and mark the status accordingly.

## 5. Deliverables and status

NEW docs/SARA_AM_007_CLUSTER_SET_PROBE.md (geometry table, verification, specimen text, expected outcomes, risks, atlas estimate), reports/sara-am-glyph-002-build.json, scripts under tools/ (exclusive create), manage_probe support. Status: BUILD_READY / PARTIAL (list blocked clusters) / BLOCKED / INCONCLUSIVE. Stop after the report; PM issues the runtime WO.
