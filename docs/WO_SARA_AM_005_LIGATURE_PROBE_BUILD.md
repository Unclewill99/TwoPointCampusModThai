# WO-SARA-AM-005 — build and structurally verify the ligature-executor probe

Issued 2026-10-26 (Asia/Bangkok) by Claude (PM/Controller). Assignee: ChatGPT (engineering). READY_FOR_HANDOFF via the user; receipt/execution not confirmed until the report exists. BUILD + OFFLINE VERIFY ONLY: no game launch, no install, no runtime test, no Antigravity dispatch, no commit/push. Read first: SARA_AM_004_ACCEPTANCE.md, SARA_AM_004_OFFLINE_ANALYSIS.md, SARA_AM_003_EXPERIMENT.md, SARA_AM_002_AB_R2_ACCEPTANCE.md, tools/build_sara_am_001.py (reuse its structure and checks).

## 1. Question the probe must answer (and only this)

Does the game's TMP runtime EXECUTE a serialized 3-component LigatureSubstitution record on the target Thai TMP when the atomic sequence U+0E15 U+0E48 U+0E33 (glyphs [118,42,82]) is rendered in the opening-course modal? Efficacy for the real ต่ำ fix is NOT being tested: the replacement glyph is a deliberately unmistakable existing glyph so that "executed" vs "not executed" is visible at a glance. This is a diagnostic, not a production wording or a fix candidate.

## 2. Build specification

New candidate directory, exclusive create (exist_ok=False): local/prototype/probe-sara-am-lig-001 (do not reuse or overwrite any existing probe). Base = fresh-translation-005 (frozen005), read-only copy. Reuse the diagnostic intro record mechanism of probe-sara-am-001a (the path already proven to reach the modal), changing only the specimen text of I2LS_Levels533.

Specimen text (3 to 6 lines, exact codepoints recorded in the manifest), each row labelled with a Latin prefix as in A/B R2:
- L1: ต่ำ atomic U+0E15 U+0E48 U+0E33. Target of the ligature. If executed it shows the sentinel glyph.
- L2: ต้ำ U+0E15 U+0E49 U+0E33 (different tone, glyphs [118,47,82]). Negative control: must NOT change.
- L3: ค่ำ U+0E04 U+0E48 U+0E33 (different base). Negative control: must NOT change.
- L4: ตา U+0E15 U+0E32 and ถี่ U+0E16 U+0E35 U+0E48. Ordinary controls.
- L5: the sentinel character itself, shown alone (e.g. ก U+0E01), so the sentinel glyph is certainly loaded/populated in the atlas independent of the ligature. This removes "glyph never populated" as an alternative explanation.

Font/TMP change: target TMP object -1239755799206566947 only. Add exactly ONE LigatureSubstitution record: m_ComponentGlyphIDs = [118,42,82] -> m_LigatureGlyphID = the existing glyph ID of the sentinel (choose a Thai consonant with a distinct shape and a glyph already present in the font; record its ID/codepoint and justify). Before adding: verify (a) no existing record already starts with glyph 118 and none can conflict or shadow, (b) how the runtime lookup is built from the serialized list (whether the first-glyph lookup dictionary is rebuilt on load, or is itself serialized and therefore also needs an entry; if the latter, the build must update both consistently), (c) whether the record order matters for longest-match, (d) that the existing 9 ligature records are unchanged. If (b) shows a serialized lookup that cannot be updated safely, STOP and report BLOCKED with evidence.

Do NOT: change the embedded font bytes, any cmap/outline/metric, other TMP fields (atlas, flags, glyph tables), other localisation segments, UI/prefab bundles, the 001a/b probes, or frozen005.

## 3. Structural verification required (offline)

Reload every output bundle and verify, as for 001a/b: all localisation segments identical to 005 except I2LS_Levels533; specimen codepoints exact; raw object byte diff of the fonts bundle changes ONLY the target TMP object, and within it only the one added ligature record (plus any lookup entry if (b) requires); font object bytes (hash f9855a70...) unchanged; readback of the TMP shows exactly 10 ligature records with the new one as specified; record bundle/object/font hashes and the diff in a manifest and reports/sara-am-lig-001-build.json; run manage_probe.py check (extend the manager for the new probe if needed) and confirm installed files are original/original/original; compute and report the same hashes of frozen005 before and after. State expected observable outcomes per row for each of: ligature executed, ligature not executed, and a failure mode (blank/tofu/crash risk). Identify any way the record could be inert for non-runtime reasons (flag gating, lookup not rebuilt) so QA can interpret a negative result.

## 4. Constraints

Offline only; screen testing is Antigravity's job and only after PM acceptance of this build. No Unicode rewrite of production text, no global glyph shift, no guessed binary patching. New outputs exclusive-create. Label VERIFIED / INFERRED / UNKNOWN. No claim that this fixes ต่ำ. Local-only assets stay out of Git. Protected-file hashes (including the three installed bundles) before/after in the report.

## 5. Deliverables and status

NEW docs/SARA_AM_005_LIGATURE_PROBE_BUILD.md (spec, verification results, expected-outcome table, interpretation rules, risks), reports/sara-am-lig-001-build.json, the build script under tools/ (header: inputs/outputs, exclusive create), updated manage_probe support. Status: BUILD_READY (verified, ready for PM acceptance), BLOCKED (with evidence), or INCONCLUSIVE. Stop after the report; the PM issues the Antigravity runtime WO.
