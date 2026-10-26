# WO-SARA-AM-004 — offline analysis: atomic-text-preserving fix for "ต่ำ" (BUG-THAI-003)

Issued: 2026-10-26 (Asia/Bangkok). Issuer: Claude, acting as Project Manager / Controller (promoted by the user on 2026-10-26, replacing ChatGPT in that role). Assignee: ChatGPT, acting as offline engineering analyst for this WO only. Status: READY_FOR_HANDOFF. There is no direct dispatch channel; the user relays this file, and receipt/execution must not be claimed until ChatGPT's report exists.

Type: ANALYSIS ONLY. No game launch, no install, no candidate build, no runtime WO.

## 1. Objective

Find and rank solutions that make atomic Thai text "ต่ำ" (U+0E15 U+0E48 U+0E33; sara am preceded by a tone mark) render with correctly separated stacking in the game, WITHOUT changing the original text (no Unicode rewrite, no normalization to decomposed order). Decide which option, if any, is worth a bounded candidate build, and define the regression coverage that candidate must pass.

## 2. Established facts (accepted evidence; do not re-derive, do not re-run)

Read these first: SESSION_CHECKPOINT_2026-10-22_EVENING.md, PROJECT_STATUS.md (head), SARA_AM_001_FINDINGS.md, SARA_AM_001_REFERENCE_ACCEPTANCE.md, SARA_AM_003_EXPERIMENT.md, SARA_AM_002_AB_R2_ACCEPTANCE.md, qa/WO_SARA_AM_002_AB_R2_REPORT.md, reports/sara-am-font-audit.json, reports/sara-am-gsub-mappings.json, reports/sara-am-tutorial-*.json, reports/sara-am-002-ab-r2-image-diff.json.

- Same embedded Thai font in Chrome 155 / CSS 64px renders atomic ต่ำ correctly (reference accepted, hash 8d28b449...). Font bytes SHA256 f9855a70...; cmap: ต=glyph118, ่=42, ำ=82, ํ=59, า=78.
- Font GSUB lookup5 (type 2) maps U+0E33 -> [U+0E4D, U+0E32]; source GPOS has MarkToMark 59 -> 42 (anchors: base (-3.45, 23.16), mark (-2.58, 16.08)); the font also has narrow/small mark variants.
- Serialized TMP (reused Thai fallback TMP -1239755799206566947) has 0 MultipleSubstitution, 9 LigatureSubstitution, 1734 GlyphPairAdjustment, 1677 MarkToBase, 357 MarkToMark; fallback list empty. Missing records do NOT by themselves prove absence of runtime decomposition.
- In-game diagnostic (A/B R2, modal reached in both): atomic row A (0E15 0E48 0E33) crowds in A and B; reordered decomposed row B (0E15 0E4D 0E48 0E32) crowds in a but separates in b after adding the single mark pair (59,42); original-order decomposed row C (0E15 0E48 0E4D 0E32) is unchanged and reversed in both. 74 pixels changed, row B only. Conclusion: mark-pair positioning alone does not fix atomic ต่ำ.
- Static text path: TPC.MessageTutorialUI; MAIN controller 4694779218175474965 -> TMP 7894969370473676053 (size 36, kerning and rich text on), font via PalanquinDark_Regular external8 with fallback to the reused Thai TMP. Which TMP/fallback is chosen at runtime is NOT proven.

Anything outside this list is unverified. Label every new claim as VERIFIED (with command/file evidence), INFERRED (with reasoning), or UNKNOWN.

## 3. Questions to answer

Q1. How does the game's TMP pipeline treat atomic U+0E33 after a tone mark? Specifically: is sara am passed to the shaper as one glyph (82, with the ํ component baked into the glyph), and if so where does the tone mark's position come from (MarkToBase from ต, MarkToMark against ำ's built-in component, or neither)? Use the TMP version actually shipped (identify it from the game's assemblies/serialized types) and the TMP source for that version; cite versions.

Q2. Does the shipped TMP version support the substitution/positioning feature types needed by each option below (MultipleSubstitution at runtime, ligature with 3 components, contextual rules, mark-to-mark between a mark and a base-like glyph)? Which records are consumed and which are only serialized?

Q3. Feasibility, risk and bounded scope of each candidate approach (Section 4). For each: what exactly changes (which object/bytes/records), what stays untouched, what can be built and verified offline, what only runtime QA can confirm, blast radius on other text, reversibility.

Q4. What regression matrix would prove a candidate safe (Section 5)?

## 4. Candidate approaches to evaluate (not exhaustive; add others if evidence supports)

A. Renderer-level decomposition/reordering (e.g. a text-preprocessing hook or patch that converts atomic ำ after a tone mark into 0E4D 0E48 0E32 at render time only, leaving stored text intact). Determine whether the mod can legally and technically do this within the project's current scope (data/asset bundles only, no code injection so far). If it requires a code plugin/loader, do NOT design it in depth: describe the requirement, risks (updates, stability, scope creep) and flag BLOCKED_NEEDS_DECISION for the user.

B. TMP table solution: add records to the serialized TMP (e.g. MultipleSubstitution U+0E33 -> 0E4D 0E32 with contextual limiting to after-tone-mark, a ligature record for tone + sara am, and/or the missing mark-to-mark / glyph-pair adjustments) so that atomic input is shaped like the font's browser result. Confirm from TMP source which record types actually execute at runtime in this version, and whether the earlier mark pair (59,42) is sufficient once decomposition happens.

C. Narrow glyph-pair/anchor adjustment: a scoped adjustment for the specific pair (tone mark 42/43/44/45 after ำ-bearing context, or ต/ท/ถ-class base) that does not shift marks globally. Quantify how it could work given that the tone mark must sit above the built-in ํ of glyph 82, and where the offset must come from.

D. Font-level change: replace or add precomposed glyphs/variants (e.g. tone-mark-above-sara-am combinations) in the embedded Thai font with accompanying TMP glyph records. Assess feasibility offline (glyph table edits, atlas population mode, dynamic atlas rebuild) and size/regeneration risk. Keep Font hash f9855a70... as the baseline; any output goes to a NEW file.

E. Baseline for comparison only: normalizing text to decomposed order. This is REJECTED as a silent production shortcut; include it only to state what it would fix and break (e.g. copy/paste, search, other consumers) so the comparison is explicit.

Rank the options by (confidence it fixes atomic ต่ำ) x (blast radius containment) x (offline verifiability). Give a single recommended next step.

## 5. Regression matrix to propose (explicit codepoints)

At minimum: ต่ำ (control of interest), plus ค่ำ, ช้ำ, ค้ำ, ถ้ำ, น้ำ, จำ, ทำ, ลำ (sara am without tone mark), a tall-consonant set (ป ฝ ฟ with tone + ำ), a mai-tho/mai-tri/mai-chattawa variant of the target, an upper-vowel + tone case (ถี่ as existing control, ที่, ปี้), a mixed Thai/Latin/number line, and a multi-line wrapped case. For each: codepoints, expected stacking, and whether it can be checked offline (shaper/structure) or only at runtime. Reuse the existing ต่ำ + ถี่ specimen format so results are comparable to A/B R2.

## 6. Hard constraints

- OFFLINE ONLY. No game launch, installation, save access, screen testing, or runtime WO. Screen testing remains Antigravity's job; the PM does not test screens either.
- Do not modify, overwrite or rebuild: fresh-translation-005 / frozen005, probe-sara-am-001a/b, the installed originals, the font bundle, any translation file, or local/ backups. Read-only inspection of them is fine.
- No Unicode rewrite of the corpus, no global glyph shift, no guessed binary patching, no blind GSUB import. Any experimental artifact (script, scratch bundle, JSON) goes to NEW paths only; build scripts must not overwrite outputs (exist_ok=False).
- No commit, no push, no automation, no messages to other agents. Local-only assets (inputs, images, saves, zips, bundles) stay local.
- Do not claim root cause, global fix, or runtime behavior without evidence. Offline shaper results (e.g. HarfBuzz/browser) are evidence about the font, not about the game's TMP runtime; say so wherever relevant. Do not repeat the earlier report's incorrect "Edge/HarfBuzz and 48px" reference-environment claim; the accepted reference is Chrome 155 at CSS 64px.
- If a step needs a tool you cannot run, or the evidence needed is unavailable, stop that thread, record it as UNKNOWN, and continue with the remaining questions.

## 7. Deliverables

1. NEW docs/SARA_AM_004_OFFLINE_ANALYSIS.md — answers to Q1-Q4, option comparison table (what changes / confidence / blast radius / offline vs runtime verifiability / reversibility), ranked recommendation, proposed bounded candidate spec (exact records/objects, expected diff, structural checks, hashes to record, rollback), and proposed regression matrix. Keep VERIFIED / INFERRED / UNKNOWN labels. Keep it concise; no narrative history.
2. NEW reports/sara-am-004-*.json for machine-readable evidence (version identification, record-type support table, any offline shaping outputs), plus any new script under tools/ with a header stating inputs, outputs and read-only behavior.
3. A status line, one of: RECOMMENDATION_READY (a bounded candidate is justified), BLOCKED_NEEDS_DECISION (needs a user decision, e.g. code injection), or INCONCLUSIVE (what evidence is missing and how to get it offline).

No candidate build in this WO. The candidate build and any Antigravity runtime WO will be issued by the PM only after the report is accepted.

## 8. Acceptance (PM)

The PM will check: every claim carries VERIFIED/INFERRED/UNKNOWN with evidence paths; no frozen or installed file changed (hash check); constraints in Section 6 respected; options ranked with an explicit scope and rollback; regression matrix has exact codepoints and offline/runtime split; the recommendation does not depend on normalizing stored text. BUG-THAI-003 stays OPEN until a runtime-accepted fix exists.
