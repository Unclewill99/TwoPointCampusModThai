# Project status

Updated: 2026-10-16 (Asia/Bangkok)
Owner: ChatGPT — Project Controller

## Completed

- Central GitHub repository established; initial commit 5d27e6c visible in the user's GitHub screenshot.
- Read-only initial Campus/Museum inventory and reproducible inspection tool completed.
- Translation editorial baseline v0.2 and provisional glossary approved with Controller clarifications (c2f4238).
- Antigravity QA matrix, report template and synthetic corpus reviewed and accepted for prototype planning, with corrections in docs/qa/CONTROLLER_ACCEPTANCE.md.
- Extracted 15,677 English records from 25 Campus TextAssets; exact decoded-text roundtrip passed. Two duplicate keys retained with segment-qualified IDs. Full corpus is local-only.
- Prepared 50-source-record PILOT-001 and docs/PILOT_001_HANDOFF.md for Claude.
- Received and reviewed Claude's pilot through local r3; independent structural checks passed with zero errors. Selected linguistic QA edits integrated; 21 contextual ambiguities and 3 humor flags remain. On 2026-10-16 the r3 file hash still matches its validation report.
- Audited 23 serialized Campus TMP font character tables; no Thai-range entries in those tables, zero read errors. Dynamic/runtime coverage remains unknown.

## Current assignments

**BUG-THAI-001: MITIGATED / TARGET-WORD VERIFIED ใน probe-003** — คำว่า “ความถี่” แยกสระอี/ไม้เอกสอดคล้อง reference ตาม WO-VISUAL-003 พร้อมผล Small/Large/restart/dropdown ตามขอบเขตที่ตรวจ ยังเปิดเพื่อ regression ของอักษรซ้อนอื่น ไม่ใช่ full shaping PASS.

| Owner | Work | State |
|---|---|---|
| Controller | Resolve Museum physical font bundles and inspect fallback/shaping configuration | Named Thai bundles found; mapping, feature counts and fallback references inspected; runtime behavior unverified |
| Controller | Extract Campus source IDs and confirm text/token format | Source extraction done; runtime token grammar/import validation pending |
| Controller | Reversible Thai rendering prototype | Read-only audit of 8 PC tooltip prefabs completed; TMP/custom layout/fitter references recorded. Runtime Settings binding remains unknown; no new speculative patch |
| Claude | 50-source-string PILOT-001 | Linguistic review integrated into local r3; four selected wording changes structurally validated; no further revision assigned |
| Antigravity | Independent pilot language/token review; diagnostic QA planning | Linguistic review integrated; synthetic shaping/wrapping matrix remains unexecuted |
| Desktop visual agent | Original multiline baseline | WO-VISUAL-006 complete: 3 explicit-LF multiline tooltips; automatic wrapping NOT_ESTABLISHED; no probe installed; originals verified |

## Limits and handoff

Probe-003 remains the translation engineering baseline after target-word PASS. Probe-004 gave five scoped passes; WO-VISUAL-005 additionally closes STACK-02's reference gap, while VOWEL-02 needs higher-detail game evidence. The width-tag English control failed with a blank oversized tooltip, so Thai wrapping A/B remains BLOCKED/NOT_RUN and uninstalled. Originals independently hash-checked after restoration. Next inspect actual tooltip TMP/layout settings or select an existing readable bounded English multiline component before rebuilding. Do not rerun unchanged probe-005 A/B. Full shaping, atlas stress, token/plural semantics and gameplay coverage remain pending. Agent messages are relayed by the user. Remote GitHub synchronization has not been freshly verified; local commits alone do not establish upload success.

Update this file on a completed handoff, meaningful finding, blocker or assignment change. Record tests as executed only with evidence; do not infer progress from elapsed time. Game binaries and local extracted assets remain outside version control.

## WO-VISUAL-006 checkpoint

Controller independently verified source LF positions in all three reported tooltips and original installed hashes. Readable explicit multiline display is established; automatic wrapping remains NOT_ESTABLISHED. Next trace Settings tooltip binding/layout constraints, then design a tag-free English length control. No new runtime work order yet.

## Current engineering handoff — WO-VISUAL-007

Two tag-free English length controls built/reloaded: probe-007-short and probe-007-long. Fonts identical to probe-003; only long's Resolution tooltip middle segment changes. WO-VISUAL-007 is ready, runtime NOT_RUN. Binding scan found four Resolution-related direct-string components and one explicit read error; complete tooltip runtime binding remains unverified. Installed originals hash-check successfully. This handoff supersedes the earlier no-new-work-order statement; no Thai A/B yet.

## Latest result — WO-VISUAL-007 completed

Short baseline PASS; long expanded horizontally and clipped off screen without establishing automatic wrapping. No width tags were used. Both variants restored between runs; originals independently verified after report receipt. No more unchanged content-only Resolution wrapping trials. Next resolve effective tooltip layout/provider references and bounded-width ownership before another English control. No new visual WO issued. This result supersedes the earlier ready/NOT_RUN status above; Thai/ZWSP comparison remains unexecuted.

## Current handoff — probe-008

Static Resolution row/provider to arrowLeft tooltip/layout/fitter chain resolved. Probe-008 stages a two-object UI edit (horizontal fit disabled, content width requested 800) with unchanged long English stimulus/TMP settings. Three bundles reload/preflight checked, originals intact. WO-VISUAL-008 ready, runtime NOT_RUN. Actual effective width, wrapping and shared-tooltip regressions require testing; this supersedes the earlier no-new-WO status.

## Latest result — WO-VISUAL-008

Width experiment did not bound the visible long tooltip; English automatic wrapping remains NOT_ESTABLISHED. All THREE originals independently hash-checked. Runtime override causality is unproven; verify actual prefab instantiation/constraint ownership before another patch. Regression-image citations need correction before accepting full VSync/QualityPresets claims. See docs/PROBE_008_DISPOSITION.md. No new visual WO issued; supersedes probe-008 ready/NOT_RUN above.

## Current handoff — probe-009 marker

probe-009 staged/reloaded: one TMP asset colour changed to opaque magenta, layout unchanged, original English short tooltip. Three-file original preflight passed; NOT INSTALLED/runtime NOT_RUN. WO-VISUAL-009 ready to test serialized path consumption. Positive marker supports usage; negative result remains inconclusive. No layout fix, loader or assembly change.

## Latest accepted result — WO-VISUAL-009

POSITIVE MARKER accepted: Resolution's three lines magenta; Antialiasing also magenta per tester. Quality Presets not observed in this run. All THREE originals independently verified. Patched TMP path consumption is supported; runtime layout overrides remain unproven. Next verify actual wrapping enum/version and text-object constraints before a single-factor English control. No new visual WO yet. This supersedes the marker ready/NOT_RUN paragraph above.

## Current handoff — probe-010

Local metadata confirms wrapping type/member names, but numeric mapping/package version remain unresolved. probe-010 stages a clearly labelled raw-mode candidate 1 to 0 on one TMP field, with original UI layout and identical probe-007-long English stimulus/fonts. Reload comparison passed, three originals verified; not installed. WO-VISUAL-010 ready, runtime NOT_RUN. Do not call raw 0 verified Normal or assume bounded wrapping. Supersedes earlier no-new-WO status.

## Probe-010 execution blocker and retry

First WO-VISUAL-010 attempt BLOCKED before writes: tasklist execution failed. All three originals independently verified; no probe runtime result. Manager now uses fail-closed Windows Toolhelp process enumeration; standalone closed-game enumeration succeeds. Probe bundles unchanged. WO_VISUAL_010_RETRY.md ready; enforce sequential install/check success before Steam launch. No rendering result yet.

## Latest result — probe-010 retry completed

Retry installed and restored successfully. NO OBSERVED IMPROVEMENT for raw wrapping-mode 1 to 0 alone: long tooltip still viewport-spanning/clipped, automatic wrapping NOT_ESTABLISHED. Separate Antialiasing explicit multiline check passed per report. All three originals independently verified. Next decode actual build enum constants or scope runtime property inspection; no unchanged repeat or new visual WO. This supersedes the earlier retry ready/NOT_RUN paragraphs.
