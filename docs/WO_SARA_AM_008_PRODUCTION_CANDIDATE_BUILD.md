# WO-SARA-AM-008 — production candidate fresh-translation-006 (fonts-only) + real-screen regression plan

Issued 2026-10-26 (Asia/Bangkok) by Claude (PM/Controller). Assignee: ChatGPT (engineering). READY_FOR_HANDOFF via user; not confirmed until the report exists. OFFLINE BUILD + PLAN ONLY: no game launch, no install, no runtime test, no commit/push. Read first: SARA_AM_GLYPH_002_ACCEPTANCE.md, SARA_AM_007_CLUSTER_SET_PROBE.md, reports/sara-am-006-census.json, reports/sara-am-glyph-002-build.json, tools/build_fresh_translation_005.py and manage_probe support.

## 1. Goal

Build candidate fresh-translation-006 = frozen005 text/UI with the 15-cluster fix in the fonts bundle only. The probe's specimen text must NOT be included.

Specification: new directory, exclusive create, local/prototype/fresh-translation-006 (never overwrite 005 or any probe). Contents: fonts_assets_all.bundle = the glyph-002 fonts bundle (embedded font with 15 appended composites + TMP with 15 added ligatures); localisation_assets_localisationenglish.bundle and ui-prefabs-general_assets_all.bundle byte-identical to fresh-translation-005. Do not rebuild the font independently: reuse the accepted glyph-002 font/TMP result and PROVE equivalence (fonts bundle hash identical to probe-sara-am-glyph-002's, or, if you must rebuild, identical embedded font bytes and identical TMP object bytes). Ensure the 006 manifest records parent 005, source probe glyph-002, all hashes, the 15 cluster list with glyph IDs, and the statement that text is unchanged.

## 2. Offline verification

Reload all bundles; localisation and UI bundle SHA256 equal 005's; fonts raw object diff vs 005 = Font 7716434233879021909 (embedded bytes) + TMP -1239755799206566947 (15 added ligatures) only; ligature records 24 with 9 originals unchanged; font checks as in WO-007 (459 old glyphs byte-equal, cmap equal, 474 glyphs); census cross-check: every cluster found in the 005 corpus (440 occurrences / 15 clusters) has a ligature, and no localisation string contains a [consonant][tone]U+0E33 cluster outside the 15 (report the count; expected 0); also confirm no 3-glyph sequence in the 005 corpus that matches a new ligature but is NOT a census cluster (e.g. through a different TMP font consumer or a differently segmented string). manage_probe: add 'fresh-translation-006', run check original/original/original; protected hashes (include glyph-002 files) before/after; report installed-state hashes. Verify that installing 006 would restore cleanly through the existing install/restore/backup lifecycle (read-only analysis of manage_probe, no install).

## 3. Real-screen regression plan (design only; the PM issues the runtime WO)

From the census (reports/sara-am-006-census.json and the 005 corpus) map the 15 clusters to where they appear in game: for each record containing a cluster give asset/segment, kind (UI label, tooltip, item description, character, level text, radio/VO captions, etc.) and, where it can be determined from the corpus structure, which screen or flow shows it. Pick a minimum set of naturally reachable screens that together cover: the highest-count clusters (น้ำ 250, ซ้ำ 55, ต่ำ 51, ล้ำ 36) in at least two different UI contexts each, at least one cluster from each tone, at least one multi-line or wrapped context (32 occurrences sit in LF-containing records; identify a visible one), and different text sizes (UI scale Small/Medium/Large per earlier QA conventions) if reachable without changing Settings beyond what the earlier QA allowed. For each chosen screen: how to reach it without progressing the game destructively, the exact text expected (codepoints), what correct looks like, and the risk. Mark anything not reachable. Also include 3-4 non-target Thai screens as regression for unaffected text (ถี่ and other upper-vowel/tone cases from the accepted BUG-THAI-001 controls). Keep within QA rules used so far (no build/spend/hire/year start; no Settings change unless the plan states the exact change and revert).

## 4. Constraints

Offline only; do not modify frozen005, any probe, installed originals or text. No corpus rewrite, no font rebuild unless proven equivalent, no cmap entries, no metric changes. New outputs exclusive-create; VERIFIED / INFERRED / UNKNOWN labels; no claim of a production fix until runtime regression is accepted.

## 5. Deliverables and status

NEW docs/SARA_AM_008_PRODUCTION_CANDIDATE.md (build/verification results, equivalence proof, census cross-check, install-lifecycle analysis, screen map and regression plan, risks), reports/sara-am-006-candidate-build.json (name it sara-am-fresh006-build.json to avoid confusion with WO-006), the build script under tools/ (exclusive create), manage_probe support. Status: BUILD_READY / PARTIAL (say what is missing) / BLOCKED / INCONCLUSIVE. Stop after the report; the PM issues the runtime WO.
