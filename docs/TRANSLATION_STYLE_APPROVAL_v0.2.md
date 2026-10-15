# Controller approval — translation style v0.2

Date: 2026-10-15
Decision: APPROVED as a provisional editorial baseline. Reviewed proposals/TRANSLATION_STYLE_PROPOSAL_v0.2.md and proposals/GLOSSARY_v0.2.md. The submitted style file matches the user-provided Downloads file by SHA-256. Original submissions remain unchanged.

## Clarifications that take precedence

- NEW_CHAR means a character newly introduced outside the project's tested/approved glyph repertoire, not every character absent from the corresponding English source string. Otherwise virtually every Thai translation would be flagged. Until a repertoire is verified, track unique code points at corpus level and keep font coverage pending; do not mark every Thai row defective.
- Automated token validation is pending confirmed grammar and tooling. Before that, manual comparison is allowed and required, with validation recorded as manual/provisional. Do not claim a script check passed unless a real check ran. A token multiset alone cannot verify sequential argument order, nesting or meaning.
- The opening precedence sentence is ambiguous: docs/TRANSLATION_STYLE_REVIEW.md is the Controller review of v0.1; proposals/TRANSLATION_STYLE_PROPOSAL.md is Claude's original proposal, not a Controller ruling. This approval overrides both where specified, followed by the Controller review and then style v0.2.
- Glossary G001–G003 retain provisional approval. Other statuses remain as submitted. G010 prohibits defaulting Assistant to ผู้ช่วยสอน without evidence; it is not a permanent ban on that translation when context supports it. Role descriptions such as Janitor duties are hypotheses until supported by source context.
- The glossary's Campus row should refer to style section 8 for proper names. Candidate terms are available for proposal and pilot translation; they are not global substitutions.

## Next step

No further style rewrite is needed before the pilot. Claude waits for Controller's extracted source batch and then proposes context-specific glossary entries while translating that batch. Bulk translation and runtime fitness remain unapproved. Font coverage, wrapping, placeholders and actual UI context still require engineering and QA evidence.
