# Controller review — PILOT-001

Date: 2026-10-15
Decision: Translation draft received. Structural checks run independently using tools/validate_pilot.py; results and exact input hash in reports/pilot-001-validation.json. Not approved for production import or runtime use.

## Decisions

- Retain Advisor_Course_Licensed_Title and its unchanged `SHOULDN'T_HAVE_TITLE` source sentinel. Do not delete the record or translate it without proof that it is player-facing. Treat as PRESERVE_SOURCE_PENDING_RUNTIME in review tracking; do not alter its original key.
- Preserve [i2p_One] and both branches exactly in structure. The source establishes a marker, not its runtime branch-selection semantics. Keep PLURAL_REVIEW; do not collapse keys or branches. Extraction's candidate_tokens currently omit square-bracket markers; validation now includes them heuristically.
- Accept omission of English full stops in normal Thai prose when sentence boundaries remain clear. Do not change decimal punctuation, tokens, markup or source data.
- Keep the three JOKE_UNRESOLVED entries pending a focused editorial pass. Do not describe a proposed interpretation of an English joke as verified authorial intent.
- Keep Advisor, Career, Level, Course License and other context-dependent glossary suggestions provisional. Do not globally replace them. Key paths suggest context but do not establish screen behavior.
- Pilot references must use exact IDs/keys rather than row numbers: several row numbers in the relay summary and translator notes are off by one. Source/target records, not the summary, are authoritative.

## Focused revision requested

Create local/translations/PILOT-001.th.r2.json, leaving the submitted file intact. Preserve all source fields and IDs. Attach a controller_review_note where changing a translation; keep uncertain flags until resolved.

1. Advisor_Characters_Personal_Goals: replace the redundant ยังมี...ที่ยัง... phrasing. Responding to requests does not necessarily mean accepting them; prefer ตอบกลับคำขอ or จัดการคำขอ until behavior is confirmed.
2. Archaeology_YearOne_Lecture_1 (Can You Dig It?): offer a concise alternative that preserves natural Thai and the excavation theme. Existing ขุดแล้วเข้าใจไหม? needs editorial comparison, not automatic rejection.
3. Archaeology_YearThree_Science (Dating Algorithms): provide literal and adapted alternatives, explicitly noting the possible dating pun is an interpretation. Do not sacrifice the age-determination subject.
4. Archaeology_YearTwo_DigSite_1: offer an alternative retaining the caution and the consequence of breaking an object, avoiding an unsupported stronger gameplay claim such as game over.
5. Replace note-only row cross-references with exact keys where practical. No unrelated translation changes or glossary promotion required.

## QA handoff boundary

Antigravity may perform independent linguistic and token review of this local draft now. In-game font, wrapping, fallback and substitution tests remain NOT_RUN pending prototype. Whitespace around ROOM/CLASS remains a hypothesis to evaluate visually.
