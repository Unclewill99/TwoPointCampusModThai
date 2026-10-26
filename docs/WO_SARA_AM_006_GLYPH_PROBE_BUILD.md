# WO-SARA-AM-006 — census + appended-glyph probe build (D+B, one cluster)

Issued 2026-10-26 (Asia/Bangkok) by Claude (PM/Controller). Assignee: ChatGPT (engineering). READY_FOR_HANDOFF via user; not confirmed until the report exists. OFFLINE BUILD + VERIFY ONLY: no game launch, no install, no runtime test, no commit/push. Read first: SARA_AM_LIG_001_ACCEPTANCE.md, SARA_AM_005_LIGATURE_PROBE_BUILD.md, SARA_AM_004_OFFLINE_ANALYSIS.md (D+B section, geometry bounds), tools/build_sara_am_lig_001 script and manage_probe support, reports/sara-am-font-audit.json.

## 1. Questions

Q-A (census, offline, no build risk): in the current 005 localisation corpus (15,677 records), which atomic sequences [Thai consonant][tone U+0E48-U+0E4B]U+0E33 actually occur, how often, in which segments? Also U+0E33 preceded by other marks (e.g. after upper vowels) and any other atomic cluster that shares the same defect pattern. Output counts per (base, tone) cluster, with segment ids and a few context samples. Include text-wrapping contexts if detectable. This sizes the real fix (number of ligatures/glyphs) and lets the PM choose scope later. Do not alter any text.

Q-B (probe): can the game render a NEW glyph appended to the embedded Thai font as the target of the ligature, and can a composite glyph stack the tone mark correctly above the sara-am ring? Build ONE probe for ONE cluster, ต่ำ [118,42,82].

## 2. Probe specification

New directory, exclusive create: local/prototype/probe-sara-am-glyph-001 (never reuse/overwrite any probe). Base = fresh-translation-005 read-only copy. Localisation: change only I2LS_Levels533, with the same labelled specimen format as the ligature probe so results compare directly:
L1 ต่ำ (target) · L2 ต้ำ (negative control; should remain the old crowded form) · L3 ค่ำ (negative control) · L4 ตา ถี่ (ordinary controls) · L5 น้ำ or ทำ, whichever is more informative as a sara-am control without ligature (justify in report) · L6 the sentinel is NOT used here.

Font change (new embedded font bytes; baseline hash f9855a70... is retained and must stay unchanged in the baseline): append exactly ONE glyph to the Thai font (target Font object 7716434233879021909) as a TrueType composite built from existing glyphs only: base ต (glyph 118) at its origin, glyph 82 (uni0E32+uni0E4D composite) at x = advance(ต), and tone mark glyph 42 translated so that it sits above the ring of glyph 82 with clear separation (the analysis bounds: glyph82 top 794, tone42 bottom 632, so rise must exceed 162 font units plus a visible gap; derive x and y from actual outlines, not guesses; record the geometry and the reasoning). Advance width of the new glyph = advance(ต) + advance(82). Update glyf/loca/hmtx/maxp/hhea/head/checksums as required; add no cmap entry (the glyph must be reachable only through the ligature) and change no existing glyph, metric or cmap. Record the new glyph ID (expected first free index; verify) and keep IDs 0..N-1 intact.

TMP change (object -1239755799206566947 only): add exactly one LigatureSubstitution record [118,42,82] -> new glyph ID. Same pre-checks as WO-005 (no conflicting 118 record, lookup rebuilt from list, 9 original records unchanged). Do NOT add MarkToMark/pair/anchor records, flags, or atlas settings. If the new glyph needs a serialized TMP glyph-table/character-table entry or atlas population hint to be rendered (because the TMP uses dynamic atlas population with an empty table), determine from source and the existing serialized layout whether that is required; if it is, STOP and report BLOCKED with the exact requirement instead of improvising.

## 3. Offline verification required

fontTools reopen with no errors; glyph count +1; all old glyph outlines/advances/cmap byte-equal in a table-level comparison; new glyph bbox and component offsets as designed; render the new glyph and the surrounding ต่ำ at 64px in a browser/shaper reference (state that this is font evidence, not game runtime evidence) and compare against the accepted Chrome155/64px atomic reference; raw object diff of the fonts bundle: changes only the Font object (embedded bytes) and the target TMP; localisation: only I2LS_Levels533 differs from 005; UI bundle identical; manifest with bundle/object/font hashes, exact specimen codepoints, expected observations table (glyph renders correctly stacked / renders but mis-stacked / blank-tofu / unchanged crowded atomic = ligature not applied because the new glyph is unavailable / other); report any reason a negative could be non-informative. manage_probe.py check must pass; installed files original/original/original (report hashes before/after for the 17 protected files). Extend manage_probe for the new probe name.

## 4. Constraints

Offline only; do not modify frozen005, 001a/b, lig-001, installed originals, the baseline font object in 005, or any text. No corpus rewrite, no global shift, no guessed binary patching, no cmap entry. New outputs exclusive-create. Label VERIFIED / INFERRED / UNKNOWN; no claim of a production fix. If you must stop, still deliver Q-A.

## 5. Deliverables and status

NEW docs/SARA_AM_006_CENSUS_AND_GLYPH_PROBE.md (census tables, geometry, build/verification results, expected-outcome table, interpretation rules, risks, and a one-paragraph scaling estimate for covering the census set: number of glyphs/records, bundle size impact, per-cluster generation approach), reports/sara-am-006-census.json, reports/sara-am-glyph-001-build.json, build/census scripts under tools/ with exclusive-create. Status: BUILD_READY / BLOCKED / INCONCLUSIVE. Stop after the report; PM issues any runtime WO.
