# QA package acceptance — 2026-10-15

Accepted for prototype planning; runtime approval remains pending. Controller inspected all three delivered files and corrected missing currency text and diagnostic sequences in rendering-corpus.json. Original diagnostic examples incorrectly implied that words such as กุญแจ or มงกุฎ contain ญุ or ฎุ. The corpus now contains explicit synthetic base-plus-mark sequences with matching code points.

Execution clarifications (take precedence over the matrix):

- Corpus JSON is the exact input authority; matrix excerpts are descriptive. DESC-01/02 use the corrected explicit sequences, not the original matrix word lists. These are diagnostic combinations, not necessarily lexical words. Validate expected glyph forms against a trusted reference using the same font before asserting substitution requirements.
- Run every narrow-button label separately; the slash-separated corpus string is a label list, not one intended button caption.
- Placeholder substitution requires confirmed parser grammar and sample values. Static glyph rendering alone cannot pass substitution. Mark unsupported candidate syntax BLOCKED pending evidence, rather than reporting a game defect.
- A cold restart does not prove persistent caches were cleared. Record the actual startup and cache state; do not delete caches without a defined reversible procedure.
- Malformed and decomposed cases are diagnostic observations. Do not require automatic correction of malformed input; lack of normalization alone is not a production defect.
- Full per-item code_points_generated and NOT_RUN statuses were added by Controller. ZWSP offsets are zero-based Python Unicode code-point indices, not UTF-16 offsets. The ZWSP experiment must match its baseline exactly after removing U+200B.
- Do not grade all glyph placement against fixed universal vertical levels. Use the chosen font's trusted shaping reference and legibility/layout evidence.

All runtime cases remain NOT_RUN. No game launch, rendering approval or prototype installation is implied by document acceptance.
