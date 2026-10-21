# WO-QA-SEGMENTATION-001 — independent review of two break maps

Date: 2026-10-18. Assigned role: Antigravity / independent linguistic QA via user relay. **Document/data review only; no game launch or installation.** State: READY, NOT_REVIEWED. This is not WO-VISUAL-018 and no probe-018 exists from this assignment.

Read ../SEGMENTATION_EVIDENCE_GATE.md, ../PROBE_017_ACCEPTANCE.md, BUG_THAI_002.md, ../THAI_LINEBREAKING_FINDINGS.md and reports/segmentation-001-preparation.json (repository-root reports folder). Inputs: local/segmentation/SEGMENTATION-001/proposals.json and frozen local/prototype/probe-013/tooltip-map.json. Verify package/source-map hashes before review; do not infer language approval from structural checks.

Scope is ONLY the existing MSAASamples and WorldDetail Thai texts. The exact original/source hash, proposed source-line units, codepoint offsets and derived marked text are in the proposal package. Existing spaces/LF, mixed English/CPU and source wording must stay unchanged. The displayed unit lists may contain whitespace-preserving units; only cut_offsets_codepoints specifies actual proposed insertions. Existing natural spaces need no insertion. CharacterLimits is an identity-only validator fixture, outside segmentation review/runtime scope.

For each proposed insertion offset:

1. Confirm it refers to the exact frozen source, then show a short left/right context and assess whether it is a reasonable optional Thai word/compound/sentence boundary in this specific text.
2. Keep clusters, mixed Latin terms and formatting intact. Existing AMBIGUOUS wording flags are not resolved by choosing cuts. Do not rewrite text or insert manual LF.
3. Distinguish clearly invalid cuts from optional style/compound preferences. If suggesting a move/add/remove, provide exact original codepoint offset and rationale. Source remains unchanged; Controller will integrate any selected revision in a new derived proposal, preserving the current package.
4. Evaluate whether the two samples add useful contexts beyond WO-017, especially mixed Thai/English and source-LF preservation. Do not claim all-Thai or dictionary coverage.

Independently recheck source equality after removing only U+200B, exact existing LF/spaces, placeholder/tag/Latin-run preservation and each original-coordinate offset. An automated structural PASS cannot replace contextual review. Source mutation or protected-syntax damage is a blocking finding; do not silently fix it.

Write docs/qa/SEGMENTATION_001_REVIEW.md with input hashes, per-key/per-cut decisions (a concise table is suitable), exact suggested offsets, severity/rationale and an overall verdict: ACCEPT_EXPERIMENTAL_MAP, REVISE_MAP, or BLOCKED_INPUT. ACCEPT means the map is suitable for a future controlled experiment, not production. Record unresolved linguistic ambiguity explicitly.

Do not edit proposals, translations, corpus, game bundles, tools or current candidate manifests. No branch switch, commit/push, other-chat messaging or asset/font upload. Only the review document is the deliverable. No runtime PASS, comparison result, BUG closure or production ZWSP/release approval. Controller prepares any later width/A/B candidates and runtime brief after review.
