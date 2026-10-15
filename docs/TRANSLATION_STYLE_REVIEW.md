# Controller review of Claude's translation style proposal

Date: 2026-10-15
Status: Approved as a provisional editorial baseline WITH the amendments below. Runtime-dependent rules and terminology remain provisional. This review takes precedence over the submitted proposal where they differ. Bulk translation is not yet assigned.

Source: proposals/TRANSLATION_STYLE_PROPOSAL.md, preserved as submitted. Its statements about Claude's access and local clone are author-reported, not independently verified by Controller.

## Accepted

Use natural, concise Thai; clear gameplay instructions; neutral system text without gendered endings; character-specific voice when supported by context. Preserve intentional humor and document adaptations. Keep stable IDs and all runtime token identities, counts and format specifications. Do not silently fix suspicious source tokens. Keep source and translation separate and flag ambiguity.

## Required amendments

1. Length: the proposed 1.3 character-count ratio is NOT a pass/fail threshold. Thai combining characters and font metrics make character counts unsuitable for UI fit. Record known UI width/line constraints; use LENGTH or WRAP_CONCERN for triage until visual QA measures actual rendering. Do not assume Thai is generally wider than English.
2. Unicode: remove the Thai-plus-ASCII-only restriction. Existing punctuation, other scripts in proper names and source symbols may be necessary. Flag newly introduced characters for glyph coverage checks. Reject accidental controls, replacement characters and invisible additions, but preserve intentional source controls according to the confirmed format. Do not use a universal consonant-vowel-tone ordering rule: Thai orthography includes context-dependent sequences. Prefer normal keyboard input and flag suspicious sequences; do not silently normalize or reorder text. Use precomposed U+0E33 for newly authored sara am as an editorial preference, not a claim about renderer requirements; test relevant sequences in QA.
3. Tokens and formatting: distinguish decoded text from serialized bytes. Preserve exact token syntax and escape semantics; export/import tooling owns encoding and escaping. Indexed/named token reordering is allowed only after the actual parser supports it. Sequential printf arguments retain order. Validate markup semantically, including self-closing tags, rather than requiring every tag to have a closing pair. Newline changes need review against actual source format and context.
4. Plural/gender: retain every original key, branch, selector and token. Thai forms may coincide when semantically appropriate; do not collapse runtime structures or remove a meaningful singular/plural distinction without checking context.
5. Glossary: accept Campus=วิทยาเขต, Student=นักศึกษา and Staff=บุคลากร as provisional defaults. Assistant must remain unresolved; do not use ผู้ช่วยสอน as a default without evidence of that role. Prestige, Rating, Stars, Class, Lecture and Course need distinct contextual entries and examples before approval. Other proposed terms remain candidates, not globally enforced replacements.
6. Proper names: preserve source spelling provisionally. Consider translation/transliteration case by case, especially gameplay-facing room and course names; do not assume English names save width. Record approved choices by entity/key in the glossary.
7. Record schema: translator_note, flags and alternatives are useful proposed fields. joke_tier is optional for ordinary text. Defer a mandatory schema until extraction identifies actual IDs and token grammar. A numeric max_len_hint is advisory and must specify its unit; rendered width and line constraints are preferred when available.

## Answers to pending questions

- Source schema and complete context: not yet established. The initial inspection only inventories assets; no translation-ready corpus has been approved.
- Thai wrapping, font fallback, glyph coverage and optional ZWSP/NBSP: awaiting prototype and QA. Do not insert invisible characters as a workaround.
- Museum: use as a rendering research reference. No Museum text corpus has been supplied or approved for terminology reuse.
- Handoff: files relayed by the user are acceptable while direct agent/GitHub access is unresolved. GitHub initial commit 5d27e6c was visible in the user's screenshot; Controller CLI access remains unresolved. Do not claim a PR or remote upload without verification.

## Next task for Claude

Revise the proposal to v0.2 incorporating this review and produce a provisional glossary with a status/context column. Do not invent source strings. Wait for Controller's extracted batch before the proposed 40–60-string pilot. Submit files for Controller review; keep the source proposal intact.
