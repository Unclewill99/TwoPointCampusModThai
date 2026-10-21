# Segmentation evidence and implementation gate

Date: 2026-10-18. Controller decision after WO-017: explicit break opportunities can help one observed failing paragraph, but broader policy remains unapproved. BUG-THAI-002 stays OPEN. Ordinary Thai without automatic ZWSP remains the production/default translation pipeline.

## Implementation constraints for experiments

Store proposed cuts in a separate, explicitly opted-in map keyed by stable ID/key and an exact source SHA-256. Count offsets in original Unicode codepoints, not bytes, UTF-16 or glyphs. Keep baseline translations, source LF/tabs/spaces, placeholder sequence, rich-text syntax, mixed Latin/number runs and archived candidates unchanged. Reject stale hashes, duplicate/out-of-range offsets, cuts immediately after a Thai leading vowel, cuts before combining marks, or cuts inside protected syntax/runs. An insertion at existing whitespace is redundant and is excluded from the proposals.

Generate marked text only as a derived experimental value. Stripping ONLY the injected U+200B must reproduce the entire original decoded text literally, without normalization or mark removal. Keep the exact insertion map and reversal check alongside the candidate manifest. No automatic dictionary or blanket source rewrite is introduced. Cluster guards are necessary but do not validate words, compounds or sentence meaning.

tools/prepare_segmentation_review.py implements a proposal-stage guard and ran eight rejection controls: token, rich tag, combining mark, leading vowel, Latin run, LF-adjacent cut, duplicate offset and changed source hash. CharacterLimits with its real placeholders/tags/blank/tab lines passes identity-only preservation; no break proposal or gameplay test is assigned for it. This is not a complete parser or runtime-token proof.

## Minimum next evidence package

Before a broader recommendation, assess at least TWO additional representative texts beyond the synthetic WO-016/017 paragraph, at TWO materially different measured container widths, with plain A and mapped B at each width. This produces eight prospective key/width/variant cells, not eight passes. Proposed serialized widths are 800 (established experiment) and 600 Unity units; actual runtime width must be observed and meaningfully different. UI Scale changes alone do not establish a new effective width or new boundary contexts.

At each width, pair A/B with identical font, layout, underlying text, environment and apparent glyph scale. Changing width is a separate experimental factor, never silently confounded with inserting opportunities. Any future narrow layout variant remains local and temporary; no global width deployment. If effective bounds differ between A/B, qualify attribution instead of accepting a controlled comparison. No baseline re-run is needed now: no runtime matrix is assigned until language review and a separately checked build exist.

For every actual edge: preserve exact rows, verify complete underlying text including source LF/whitespace, distinguish source LF from extra wraps, record original codepoint cut offsets and context, independently assess word/syllable quality and mark integrity, and compare all new edges rather than only disappearance of old bad offsets. Record genuine new contexts, not repeated scales/paragraph joins. No wrapping means NOT_EXERCISED; unreadable detail means UNRESOLVED. All representative words occurring in a row is not targeted edge coverage.

No regression is acceptable in source completeness, syntax/tokens, visible artifacts, containment or readable apparent size. Failure/uncertainty in a required cell remains open. Successful samples would support an experimental approach only; selecting a maintainable production segmenter and validating its broader corpus, formatting, performance and fallback behavior is a separate decision. Neither eight cells nor this gate automatically grants release/full shaping approval.

## Selected next texts and review gate

- MSAASamples: real Thai plus MSAA Samples, one source paragraph. Plain original remains unchanged; ten proposed non-whitespace opportunities.
- WorldDetail: real Thai/CPU across three original LF segments. Preserve LF and original spaces; twenty-four proposed opportunities.

Both come from the frozen probe-013 reviewed tooltip map. Existing ordinary-Thai visual acceptance remains valid for its inspected bounds and does not count as the prospective narrow-width comparison. Prior wording/ambiguity flags remain unchanged. Source and proposed marked values are local in local/segmentation/SEGMENTATION-001/proposals.json; concise preparation hashes/checks are in ../reports/segmentation-001-preparation.json.

Antigravity should independently assess the actual proposed Thai units/offsets before Controller builds any new candidate. That review is WO-QA-SEGMENTATION-001, requires NO GAME, and must not approve production ZWSP or alter source translations. Claude receives no translation rewrite now: the question concerns where the existing wording may break. No new runtime WO, probe or installation is assigned by this gate.


## Independent review completed — 2026-10-18

WO-QA-SEGMENTATION-001 returned ACCEPT_EXPERIMENTAL_MAP. Controller independently verified all 34 reviewed cuts and accepted both frozen maps unchanged in SEGMENTATION_001_ACCEPTANCE.md. Runtime matrix remains NOT_RUN; next owner Controller for checked candidate preparation. No production policy change.
