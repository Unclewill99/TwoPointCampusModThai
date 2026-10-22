# BUG-THAI-003 — static investigation 001

Follow-up: tools/trace_sara_am_modal.py traverses four MessagePopup candidate roots in ui-level, retaining eight read errors; reports/sara-am-popup-trace.json. Generic InfoText components point to font fileID5/pathID1456777345258535221, but those popups are not established as the opening course-information modal. No actual-modal binding claim. Prepared exact embedded-font reference local/review/sara-am-001/reference.html and manifest; offline visual comparison assigned in qa/WO_SARA_AM_001_REFERENCE.md. No game rerun required.

2026-10-22. OPEN; no fix candidate or game run. Controller performed read-only asset inspection. Base fresh-translation-005 unchanged.

## Findings

Embedded Thai-capable Font object 7716434233879021909 retains legacy name NotoSansArabic-Regular but bytes SHA256 f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0 are the Thai font established by probe-003. Font cmap includes ต glyph118, ่ glyph42, ำ glyph82, ํ glyph59, า glyph78.

Font GSUB lookup5 type2 explicitly maps uni0E33 to [uni0E4D, uni0E32]. It also contains substitutions for narrow/small mark variants. Serialized reused TMP slot NotoSans_Arabic_Dynamic has zero MultipleSubstitution records, nine LigatureSubstitution, 1734 GlyphPairAdjustment, 1677 MarkToBase and 357 MarkToMark records, with empty serialized fallback list. Font source reference uses GUID 8ea2df6db11572548a2fb4d8b7f4e305.

Hypothesis: sara-am decomposition/reordering or substitution handling differs between font shaping and Campus rendering. Missing serialized MultipleSubstitution records alone does NOT prove lack of runtime decomposition or establish root cause. Do not import GSUB mappings blindly: reorder/mark handling must also be understood.

## Modal trace limitations

Searches of GameObject names and selected intro fields in ui-prefabs-general, ui-prefabs-ingame, ui-level and ui-prefabs bundles did not establish the opening modal binding. 32 MonoBehaviour type-tree read errors were recorded in field search; no match is not proof of absence. Actual modal TMP/font/fallback and runtime overrides remain unresolved. Do not patch guessed prefab or globally shift marks. Existing user image remains positive defect evidence; no additional game reproduction requested.

## Artifacts and next engineering work

- tools/audit_sara_am.py and reports/sara-am-font-audit.json: reproducible embedded font/TMP inventory.
- reports/sara-am-gsub-mappings.json: selected substitution mappings.
- reports/sara-am-modal-candidates.json and sara-am-modal-field-search.json: exploratory search, not binding proof.

Next resolve serialized script/type mapping for unreadable modal candidates and trace text references; then prepare same-embedded-font reference for exact ต่ำ plus ถี่ regression, with explicit codepoints. No runtime WO until there is a controlled change or reference comparison that answers a new question. No Unicode/source rewrite, glyph patch, candidate build, installation, save edits, commit or push in this investigation. Screen testing remains Antigravity responsibility.
