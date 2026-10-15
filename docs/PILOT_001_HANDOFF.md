# Claude handoff — PILOT-001

Approved assignment: translate the 50 records in local/source/PILOT-001.json into a NEW file local/translations/PILOT-001.th.json. Keep the source file intact. This is a pilot for review, not a production import or runtime approval. The input is intentionally excluded from Git; use the shared local folder or ask the user to transfer it if running elsewhere.

Read TRANSLATION_STYLE_APPROVAL_v0.2.md and the approved style/glossary proposals. Preserve every id, key, asset, segment_index, source and source_sha256 exactly. Populate thai, translator_note and flags; set status to TRANSLATED_PENDING_REVIEW. Do not modify game files, tools or other agents' files. Do not switch branches or commit in the shared checkout.

Context is limited to TextAsset and key path. screen=null means unknown; do not invent screen location or width limits. Flag uncertainty, missing context and jokes needing review. The deterministic selection covers UI settings, short UI text, token-bearing text, course text and advisor text; it does not guarantee every humor/tag/newline category is present.

Candidate tokens are observations only, not a verified runtime grammar. Keep their spelling, counts and order in this pilot; flag REORDER_NEEDED rather than silently reordering. Do not insert [i2t], which is the observed record delimiter. Line breaks and markup must be retained pending review.

ID includes TextAsset, key and segment index because the full source contains duplicate keys. IDs are stable for this captured build and source hash, not guaranteed across future game updates. Duplicate runtime-key precedence is still unknown; do not merge duplicate records.

Engineering validation: decoded text splits on [i2t] and the first = per nonempty segment and reconstructs exactly. This does not yet prove serialized byte preservation, bundle rebuild or runtime loading. Report: reports/source-extraction.json.
