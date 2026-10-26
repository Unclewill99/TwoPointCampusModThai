# WO-SARA-AM-004 — accepted as INCONCLUSIVE

2026-10-26. PM (Claude): ACCEPT_AS_INCONCLUSIVE. Report docs/SARA_AM_004_OFFLINE_ANALYSIS.md, reports/sara-am-004-analysis.json.

## Checks performed by PM

- Claim labelling (VERIFIED/INFERRED/UNKNOWN), constraint compliance, option table with scope/rollback, 41-case regression matrix with exact codepoints and offline/runtime split: acceptable. Synthetic tall-base/tone strings (ป๊ำ, ฝ๋ำ etc.) are coverage strings, not linguistic claims.
- Protected-input hashes: PM independently re-hashed 12 of the 17 files in reports/sara-am-004-preservation-before.json (local prototypes/manifests under ThaiCampusMod) — all unchanged. The 5 files in the game folder (3 installed bundles, GameAssembly.dll, global-metadata.dat) are outside the PM's mounted folder and were NOT independently re-hashed; the analyst's before/after record is accepted for those, flagged as not independently verified.
- New scripts use exist_ok=False for new output directories. Git: only expected untracked/modified docs, reports, tools; no frozen file touched.

## Findings accepted

- Exact shipped TMP package/fork is UNKNOWN (IL2CPP, no package lock; get_version literal 1.4.0 is not a package version; custom loading fields suggest a fork). Do not claim pre4/pre10.
- Glyph 82 is a TrueType composite (uni0E32 + uni0E4D): one text glyph with a baked ring. Under inspected TMP source a preceding tone attaches via MarkToBase to ต, not to the ring, which is consistent with A/B R2 but not proof.
- Options A (code plugin) remains BLOCKED_NEEDS_DECISION. B alone, C, D alone are low-confidence; D+B (one fixed [118,42,82] ligature + appended full-cluster glyph) is the only asset-only branch with plausible efficacy, but its gates (live liga execution, dynamic glyph loading, layout) are UNKNOWN.

## PM changes to the proposed next step

The analyst's single next step (obtain offline provenance of the shipped TMP) is judged unlikely to close the gate: the build is IL2CPP without a package manifest and the native inspection already reached its limit. PM, with user approval (2026-10-26), replaces it with a bounded runtime probe: does the game execute a serialized 3-component LigatureSubstitution record at all? That is a new question the offline evidence cannot answer, it needs no new glyph artwork, and its result decides whether D+B is viable. Issued as WO-SARA-AM-005 (docs/WO_SARA_AM_005_LIGATURE_PROBE_BUILD.md): build/verify only. A separate Antigravity runtime WO follows only after the PM accepts the build.

BUG-THAI-003 stays OPEN. No fix, no production candidate, no change to frozen005.
