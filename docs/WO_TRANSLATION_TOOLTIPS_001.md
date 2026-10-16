# WO-TRANSLATION-TOOLTIPS-001 — actual Settings tooltip translations

Date: 2026-10-16. Owner: Claude (Translator); Controller: ChatGPT.

Input: local/source/TOOLTIPS-001.json, 20 actual extracted Campus Settings tooltip records. Output NEW local/translations/TOOLTIPS-001.th.json. Read docs/TRANSLATION_STYLE_APPROVAL_v0.2.md, docs/proposals/GLOSSARY_v0.2.md and docs/PROBE_012_ACCEPTANCE.md. Do not edit source, pilot r3, game bundles or other agent files. No branch switches, commit/push in shared checkout.

Preserve all existing fields except populate thai and change status to TRANSLATED_PENDING_REVIEW; add translator_note, flags and optional alt. Preserve exact source/id/key/path_id/segment_index/hash/context/candidate_tokens/batch. Every record must be retained, including unobserved UI terms. No production ZWSP, NBSP or other invisible insertion; no manual newlines added/removed. Keep original LF boundaries; automatic wrapping is handled by the runtime experiment, not manually emulated.

Use natural concise technical Thai, preserving meaning and tradeoffs (quality vs performance, CPU/GPU, memory). Preserve all variable identities/counts/order, formatting, numeric values and abbreviations unless a contextual term is explicitly proposed. Do not silently correct source typos or tags. Flag ambiguous technical meaning or terminology and explain. Do not apply a character-count width threshold; requested layout units are not a text-length limit. Do not add generic disclaimers to in-game text.

Prioritize meaning of Resolution, FullScreenMode, MaxFPS, AntialiasingMode and Vsync for later visual review, but translate all 20. Some other tooltip activation was not observed; do not claim which screen definitely exposes each. Candidate tokens are extraction observations, not a proven grammar. CharacterLimits contains runtime variables and must retain them exactly.

Run structural comparisons to the input and report what was actually checked, plus unresolved flags. Do not modify Controller validators. Deliver filename, counts and key-based decisions. This WO authorizes translation only, not installation or a global glossary promotion. Controller validates/integrates; Antigravity reviews independently; desktop agent later tests actual translated tooltips across Small/Medium/Large with restoration.
