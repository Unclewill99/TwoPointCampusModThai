UPDATE 2026-10-26 (PM): INSTALLED_006. Live game now runs fresh-translation-006 (005 text + 15-cluster sara-am font fix); originals backed up, restore available. BUG-THAI-003 FIX_VERIFIED_SCOPED (Medium UI scale, 3 surfaces); wider coverage pending reports from play. Installed bundles are NOT original until restore.

UPDATE 2026-10-26 (PM): fresh-translation-006 PASS_SCOPED on real screens (incl. the original defect site). BUG-THAI-003 FIX_VERIFIED_SCOPED, not closed. No active WO. Installed bundles original. Decision pending from user.

UPDATE 2026-10-26 (PM): fresh-translation-006 (005 + fonts-only 15-cluster fix) built and accepted offline. Runtime WO qa/WO_SARA_AM_FRESH006_001.md ready (menu surfaces + real opening modal, Medium scale). Installed bundles original. BUG-THAI-003 OPEN.

UPDATE 2026-10-26 (PM): GLYPH-002 accepted: all 15 census clusters render stacked in the modal. WO-008 issued (fresh-translation-006 fonts-only candidate + real-screen regression plan). Installed bundles original. BUG-THAI-003 OPEN.

UPDATE 2026-10-26 (PM): WO-007 accepted (15 composite glyphs + 15 ligatures, font independently verified). Runtime WO qa/WO_SARA_AM_GLYPH_002.md ready, not yet executed. Installed bundles original. BUG-THAI-003 OPEN.

UPDATE 2026-10-26 (PM): GLYPH-001 accepted STACKED_OK: appended composite glyph via exact ligature stacks correctly in the game. Scope: 15 census clusters, fonts-bundle-only fix. WO-007 issued (offline 15-cluster probe build). Installed bundles original. BUG-THAI-003 OPEN.

UPDATE 2026-10-26 (PM): WO-006 accepted (census 440 occurrences/15 clusters; glyph probe built and independently font-verified). Runtime WO qa/WO_SARA_AM_GLYPH_001.md ready, not yet executed. Installed bundles original. BUG-THAI-003 OPEN.

UPDATE 2026-10-26 (PM): LIG-001 accepted EXECUTED: exact 3-component ligature runs in game. WO-SARA-AM-006 issued (census + appended-glyph probe, offline). Installed bundles original. BUG-THAI-003 OPEN.

UPDATE 2026-10-26 (PM): WO-005 build accepted; Antigravity runtime WO qa/WO_SARA_AM_LIG_001.md ready (not yet received/executed). Probe installed? NO - originals installed. BUG-THAI-003 OPEN.

UPDATE 2026-10-26 (PM): WO-004 accepted INCONCLUSIVE; offline provenance path dropped. WO-SARA-AM-005 issued to ChatGPT (build/verify-only ligature-executor probe). BUG-THAI-003 OPEN; no runtime WO active.

UPDATE 2026-10-26: Claude now acts as Project Manager/Controller (user decision; replaces ChatGPT in that role). Issued WO-SARA-AM-004 (ChatGPT, offline analysis only) for atomic-text-preserving fix of atomic ต่ำ. READY_FOR_HANDOFF through user; not yet received/executed. BUG-THAI-003 OPEN. No active runtime/Antigravity WO.

# Project status

PAUSED BY USER for tonight (2026-10-22); resume tomorrow 2026-10-23. Latest authority: SESSION_CHECKPOINT_2026-10-22_EVENING.md. Mod005 complete; sara-am A/B diagnostic accepted, atomic ต่ำ still OPEN; installed bundles original. No active QA dispatch or automation.

Latest: sara-am A/B R2 DIAGNOSTIC_RESULT accepted. Both variants reach opening modal; adding mark pair59->42 separates reordered decomposed specimen only. Ordinary atomic ต่ำ unchanged; BUG-THAI-003 OPEN. Three installed originals verified. See SARA_AM_002_AB_R2_ACCEPTANCE.md. Next offline engineering evaluates atomic-text-preserving solution; no unchanged A/B rerun.

Latest sara-am QA: originals control gate reached campus flyover; modal NOT_OBSERVED due 30-second cap, not failed click. Three originals independently confirmed. Revised A/B R2 WO qa/WO_SARA_AM_002_AB_R2.md ready with 60-second natural wait; candidates unchanged, BUG-THAI-003 OPEN. See SARA_AM_003_CONTROL_DISPOSITION.md.

Latest 2026-10-22: staged sara-am diagnostic A/B (probe-sara-am-001a/b), structurally verified; originals installed. Antigravity WO qa/WO_SARA_AM_002_AB.md ready. Static MessageTutorialUI text/font fallback trace found; runtime instance remains to confirm. BUG-THAI-003 OPEN. See SARA_AM_003_EXPERIMENT.md.

Latest font investigation: offline same-embedded-font reference accepted (SARA_AM_001_REFERENCE_ACCEPTANCE.md). Atomic ต่ำ separates correctly in browser reference; game evidence crowds sara-am upper component/tone. BUG-THAI-003 OPEN, root cause and actual modal font binding unresolved. Controller next inspects native TMP handling; no new game run or fix candidate yet.

Latest acceptance (2026-10-22): WO-FRESH-MENU-005-R2 DESTINATION_PASS accepted after direct destination-image review; combined with menu-label PASS, requested Mod correction is complete in fresh-translation-005. Three originals independently confirmed. See FRESH_MENU_005_R2_ACCEPTANCE.md; this supersedes the destination NOT_RUN below. No further unchanged menu retest. Font/wrapping and terminology work remains open.

Latest QA disposition (2026-10-22): fresh-translation-005 main-menu **Mod PASS**, directly verified from Antigravity image. Mod-management destination NOT_RUN/INCONCLUSIVE due wrong-button input and exhausted recovery; overall SETUP_LIMIT. Three originals independently confirmed. See FRESH_MENU_005_DISPOSITION.md. Controller performs no desktop testing per user direction. No automatic repeat test or candidate rebuild.

Updated: 2026-10-22 (Asia/Bangkok)
Owner: ChatGPT — Project Controller

## Current checkpoint

Probe-013 naturally reachable actual Settings tooltip milestone is COMPLETE WITH EXPLICIT GAPS: 18/20 keys at Small/Medium/Large (54 cells), accepted through WO-013/014/015. Two hidden rows remain NOT_RUN/control not exposed. No release/global layout/full shaping approval. All THREE installed originals, staged candidates and retained backups independently verified; tooltip-r2 and pilot-r3 structural rechecks pass with zero errors.

Current authority: [PROBE_013_MILESTONE.md](PROBE_013_MILESTONE.md), [coverage tracker](qa/TOOLTIPS_001_COVERAGE.md), and [machine-readable checkpoint](../reports/probe-013-milestone.json). The dated entries below are preserved history and may describe superseded blockers/assignments.

| Owner | Current next work | State |
|---|---|---|
| Controller | Smoke setup limit accepted; exact-process foreground guard patched | Compile/mock checks passed; live control preflight pending |
| Claude | Round5 delivery complete | No further full glossary round assigned; context exceptions retained |
| Antigravity / desktop QA | Original-game capability gate before fresh smoke resume | Target views NOT_RUN; resume only after verified target/navigation |

## Historical project log

## Completed

- Central GitHub repository established; initial commit 5d27e6c visible in the user's GitHub screenshot.
- Read-only initial Campus/Museum inventory and reproducible inspection tool completed.
- Translation editorial baseline v0.2 and provisional glossary approved with Controller clarifications (c2f4238).
- Antigravity QA matrix, report template and synthetic corpus reviewed and accepted for prototype planning, with corrections in docs/qa/CONTROLLER_ACCEPTANCE.md.
- Extracted 15,677 English records from 25 Campus TextAssets; exact decoded-text roundtrip passed. Two duplicate keys retained with segment-qualified IDs. Full corpus is local-only.
- Prepared 50-source-record PILOT-001 and docs/PILOT_001_HANDOFF.md for Claude.
- Received and reviewed Claude's pilot through local r3; independent structural checks passed with zero errors. Selected linguistic QA edits integrated; 21 contextual ambiguities and 3 humor flags remain. On 2026-10-16 the r3 file hash still matches its validation report.
- Audited 23 serialized Campus TMP font character tables; no Thai-range entries in those tables, zero read errors. Dynamic/runtime coverage remains unknown.

## Historical assignments — superseded by current checkpoint

**BUG-THAI-001: MITIGATED / TARGET-WORD VERIFIED ใน probe-003** — คำว่า “ความถี่” แยกสระอี/ไม้เอกสอดคล้อง reference ตาม WO-VISUAL-003 พร้อมผล Small/Large/restart/dropdown ตามขอบเขตที่ตรวจ ยังเปิดเพื่อ regression ของอักษรซ้อนอื่น ไม่ใช่ full shaping PASS.

| Owner | Work | State |
|---|---|---|
| Controller | Resolve Museum physical font bundles and inspect fallback/shaping configuration | Named Thai bundles found; mapping, feature counts and fallback references inspected; runtime behavior unverified |
| Controller | Extract Campus source IDs and confirm text/token format | Source extraction done; runtime token grammar/import validation pending |
| Controller | Reversible Thai rendering prototype | Read-only audit of 8 PC tooltip prefabs completed; TMP/custom layout/fitter references recorded. Runtime Settings binding remains unknown; no new speculative patch |
| Claude | 50-source-string PILOT-001 | Linguistic review integrated into local r3; four selected wording changes structurally validated; no further revision assigned |
| Antigravity | Independent pilot language/token review; diagnostic QA planning | Linguistic review integrated; synthetic shaping/wrapping matrix remains unexecuted |
| Desktop visual agent | Original multiline baseline | WO-VISUAL-006 complete: 3 explicit-LF multiline tooltips; automatic wrapping NOT_ESTABLISHED; no probe installed; originals verified |

## Historical limits and handoff

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

## Latest engineering finding — actual enum decoded

Build metadata directly confirms NoWrap=0, Normal=1, PreserveWhitespace=2, PreserveWhitespaceNoWrap=3. Reproducible decoder/report committed; original serialized mode is Normal. Probe-010 changed Normal to NoWrap, not an enable-wrapping fix. Runtime values/bounded width remain unverified. Next investigate effective width/text layout constraints, not more raw enum guesses. No new build or visual WO; three installed originals verified. See docs/WRAPPING_ENUM_FINDINGS.md.

## Current handoff — text child constraint / probe-011

Traced text rect width=0 and parent layout ChildControlWidth=1; no separate LayoutElement on text object. probe-011 tests paired child width=800 plus ChildControlWidth=0, keeping original Normal mode/fitter/custom wrapper and long English stimulus. Exactly two UI object edits reload-verified; three originals checked. WO-VISUAL-011 ready, runtime NOT_RUN. Supersedes earlier no-new-build status; no loader installed.

## Latest accepted result — probe-011 English control PASS

WO-VISUAL-011 establishes bounded readable automatic English wrapping: 17 rows reported, middle segment 14 rows with 13 extra breaks. Controller inspected the bounded multiline image and independently verified originals for all three bundles. Antialiasing remains readable but width changes, per report. Paired edit accepted as experimental configuration, not a release/global layout fix. Next same-slot Thai A/B should keep probe-011 UI/font bytes identical; no production ZWSP approval. Supersedes ready/NOT_RUN above; no new WO in this review.

## Current handoff — bounded Thai A/B probe-012

probe-012a/b built/reloaded on identical probe-011 UI/font bytes. Same synthetic Thai paragraph repeated three times, no manual LF; B differs only by mapped U+200B, removal matches A exactly. Only Resolution tooltip segment changes; r3 untouched. WO-VISUAL-012 ready, runtime NOT_RUN; originals verified for all three files. No production ZWSP/layout rollout approval.

## Latest acceptance — probe-012 A/B complete

Both variants readable in six rows with equal observed bounds/boundaries; all three repeats accounted. No visible base/mark split at five observed boundaries. B shows NO OBSERVED IMPROVEMENT; keep ordinary Thai/no automatic production ZWSP. Scoped paragraph result only, not dictionary/full Thai wrapping approval. All three originals independently verified. Next representative real tooltip translations and width/scale regression, plus adversarial boundary backlog. No new WO yet; supersedes prior NOT_RUN.

## Current assignment — actual tooltip translation

TOOLTIPS-001 prepared: 20 actual Settings tooltip records in local/source/TOOLTIPS-001.json, hashes verified; one token-bearing record. Claude assigned docs/WO_TRANSLATION_TOOLTIPS_001.md, output local/translations/TOOLTIPS-001.th.json. User relay pending. Preserve LF/tokens; no ZWSP. Controller integration/independent QA precede a new visual build and Small/Medium/Large regression. No new game mutation; three originals verified.

## Latest tooltip handoff — independent language QA

Claude's 20-record draft received; Controller independent validation zero errors (reports/tooltips-001-validation.json), nine AMBIGUOUS flags retained. Draft accepted for Antigravity review per docs/TOOLTIPS_001_CONTROLLER_REVIEW.md (WO-QA-TOOLTIPS-001). Output docs/qa/TOOLTIPS_001_LINGUISTIC_REVIEW.md. No runtime/visual approval, glossary promotion or game installation. Desktop agent waits for reviewed real-tooltip build.

## Latest tooltip QA integration

Antigravity review received. Eight selected editorial changes integrated into local/translations/TOOLTIPS-001.th.r2.json; r1 preserved. Controller validation: 20 records, zero structural errors, nine AMBIGUOUS flags retained. Runtime assertions in QA qualified in docs/TOOLTIPS_001_QA_DISPOSITION.md. Next checked real-tooltip build with pilot r3 and bounded experimental layout, then scale WO. No new installation; three originals verified.

## Current handoff — probe-013 actual tooltips

Built/reloaded 20 actual reviewed tooltips plus 50 pilot-r3 records; exact matches verified. Font/UI bytes match probe-011 bounded experiment, no synthetic bodies/ZWSP. WO-VISUAL-013 ready for five primary tooltip keys at Small/Medium/Large and Medium restart; other unseen records remain untested. Three originals verified, not installed/runtime NOT_RUN. No release approval.

## Latest accepted result — actual tooltip visual coverage

WO-VISUAL-013: five primary keys PASS at Small/Medium/Large; two Medium restart rechecks passed. Six additional keys complete/readable at Medium (five show extra runtime breaks); nine of twenty still NOT_RUN, plus six Small/Large gaps. CharacterLimits variables and graphics-option-list expansion untested. Original three bundles independently verified; Medium restored. Next consolidate remaining naturally reachable coverage using unchanged probe-013, avoid repeating passed primary matrix. Shared fixed-width whitespace/short-line tradeoffs remain; no release/global layout or ZWSP approval. Supersedes prior NOT_RUN handoff.

## Current handoff — WO-VISUAL-014 remaining coverage

Unchanged staged probe-013 and tooltip-map hashes independently verified; three installed originals verified. WO-VISUAL-014 ready: six Small/Large gaps, five newly attempted controls at all scales, bounded QualityPresets/reachability observations; no repeat of accepted primary matrix. Exact current tracker docs/qa/TOOLTIPS_001_COVERAGE.md. No new build or installation by Controller; WO-014 runtime NOT_RUN.

## Latest blocker — WO-VISUAL-014 desktop capability

Attempt BLOCKED before install: wrong-target capture and no supported hover/pointer operation established in tester session. New coverage stays NOT_RUN; no new defect or control-absence evidence. Originals independently verified; no rebuild required. Resume via docs/qa/WO_VISUAL_014_RESUME.md after correct Windows target capture and documented pointer-placement capability. Current Medium/build/resolution not newly observed; prior WO-013 values historical only. No new visual acceptance.


## Latest acceptance — WO-VISUAL-014 completed (2026-10-18)

Completed desktop run supersedes capability blockers. Controller accepted 27 new Video cells plus CharacterLimits at all scales; combined scoped coverage is 17/20 keys across Small/Medium/Large. CharacterLimits displayed variables/colour verified, functional limits untested. QualityPresets NOT_OBSERVED at Medium; AnimationSkinningQuality/RenderScale NOT_RUN/control not exposed. Three originals independently checked; final Medium attributed to tester evidence. No release/global layout/ZWSP approval. See WO_VISUAL_014_ACCEPTANCE.md and updated qa/TOOLTIPS_001_COVERAGE.md.

Next engineering milestone started: read-only serialized context scan finds references for all three remaining keys (six objects, one decode failure). Continue owner/provider/visibility tracing per WO_TOOLTIP_CONTEXT_001.md before another runtime assignment. No rebuild or repeated passed matrix.

Static hierarchy finding: RenderScale and Animation Quality rows are serialized inactive; QualityPresets/title active. These defaults do not prove runtime visibility. External script/provider activation conditions remain unresolved; do not force-enable hidden controls or assign identical hover repeats. Initial context disposition is recorded in WO_TOOLTIP_CONTEXT_001.md.


## Binding trace completed — 2026-10-18

See TOOLTIP_GAP_BINDING_FINDINGS.md and reports/tooltip-gap-binding-trace.json. All three providers positively resolved to TPC.TooltipSpawner. QualityPresets provider is on OptionsQuality with an enabled raycast graphic; event dispatch/runtime gating remains unresolved. Both hidden rows retain PreferencesPanelVideo references. Exact visibility predicates require native method bodies, beyond serialized/metadata evidence. No new supported activation established, so no new visual WO/rebuild is issued; 17/20 acceptance unchanged.


## Native investigation completed — next WO-VISUAL-015 (2026-10-18)

Existing LibCpp2IL successfully mapped native methods; 65 target-class pointers independently checked against codegen table. Chained PE unwind bounds and complete disassembly validated. TooltipManager searches raycast objects and stops on a raycast-target Image without walking to parent providers; QualityPresets parent OptionsQuality has the provider, title/button Images can intercept it. This supports a new bounded empty-parent-gap diagnostic, not a confirmed runtime root cause. WO-VISUAL-015 prepared for desktop QA, NOT_RUN, unchanged probe-013. Hidden rows remain default-inactive with no supported activation route established in reviewed lifecycle code. See TOOLTIP_NATIVE_FINDINGS.md. Current acceptance stays 17/20; no rebuild or release approval.


## Accepted WO-VISUAL-015 — 2026-10-18

QualityPresets parent-gap activation and scoped visual PASS accepted at Medium/Small/Large after Controller image inspection and text comparison. Combined accepted coverage 18/20 keys (54 scale cells). WO-015 complete; prior prepared/NOT_RUN status is historical. Two hidden rows remain NOT_RUN/control not exposed. All three originals independently checked, final Medium attributed to tester evidence. No new build/repeat WO or release approval. See docs/WO_VISUAL_015_ACCEPTANCE.md (repository-relative path) and current coverage tracker. Next consolidate candidate scope and known limits before expanding work.


## VOWEL-02 preflight completed — 2026-10-18

Eight injected pairs exactly match map, reloaded bundle, corpus target elements and exact reference. Embedded TTF hash matches actual staged game font. Existing Medium/Large originals inspected; detailed shaping remains PARTIAL. Documented sky capture route verified on Steam after wrong-target recovery, but higher-detail/lossless game acquisition not established; no new desktop WO/install. See VOWEL_02_EVIDENCE_PREFLIGHT.md and reports/vowel-02-evidence-audit.json. Continue independent source-backed boundary planning; no new translation batch or release approval.


## Next boundary handoff — WO-VISUAL-016 (2026-10-18)

Existing actual-tooltip transcriptions contain nine unique extra cut positions; WO-012 five cuts reduce to two contexts. CRP-WRAP-03 previously had no wrapping in WO-004. New probe-016 stages its unchanged 79-codepoint paragraph three times in bounded Resolution: exactly one localisation segment changed, identical probe-013 font/UI, no LF/ZWSP/tags. Build/reload checks and guarded all-three original check passed. WO-VISUAL-016 ready for Antigravity via user relay, runtime NOT_RUN, Medium only. No VOWEL-02 detail closure, forced all-cluster coverage, production change or release approval. See LINE_BOUNDARY_FOLLOWUP.md.


## WO-VISUAL-016 reviewed — segmentation defect (2026-10-18)

Five readable contained rows preserve all 237 codepoints exactly. Four runtime cuts observed; three cut inside เรียน/ทุก. BUG-THAI-002 OPEN. Content/containment scoped PASS; word segmentation OBSERVED FAIL; direct leading-vowel/base or base/mark edge challenges NOT_EXERCISED, fine shaping unresolved. Originals/retained backups/staged hashes independently checked. See PROBE_016_DISPOSITION.md and qa/BUG_THAI_002.md. Next Controller investigates actual text line-breaking configuration before choosing a targeted control; no new candidate or repeat WO yet. Original probe-013 18/20 coverage remains unchanged, no broad wrapping/release approval.


## Targeted segmentation control — WO-VISUAL-017 ready (2026-10-18)

Normal wrapping retained; two resource linebreaking tables contain no Thai codepoints, without establishing dictionary absence/root cause. Native U+200B branches support a targeted intervention test. New probe-017 adds 47 explicitly mapped proposed break opportunities to the exact WO-016 text; removing U+200B matches A literally, font/UI unchanged, one segment reload-verified. Guarded check all-three original passes. WO-017 prepared for Antigravity/user relay, runtime NOT_RUN, B-only Medium. BUG-THAI-002 stays OPEN; no production ZWSP/global rewrite/release policy change. See THAI_LINEBREAKING_FINDINGS.md.


## WO-VISUAL-017 accepted — scoped experimental benefit (2026-10-18)

B preserves all 237 underlying codepoints, cuts at 49/100/154/207 (three distinct contexts), no cut inside any เรียน/ทุก occurrence and no new bad edge observed. Controller inspected B and independently verified literal equality/offsets/evidence/hashes. BUG-THAI-002 stays OPEN with experimental mitigation only. All three originals/backups/candidates verified; final Medium attributed to tester. No production ZWSP/default policy change, full wrapping or release approval. See PROBE_017_ACCEPTANCE.md. Next Controller defines broader evidence/implementation constraints before choosing further contexts; no new WO/build yet.


## Next independent review — SEGMENTATION-001 (2026-10-18)

Defined source-preserving, opt-in experimental-map gate and prospective 2-text x 2-width x A/B matrix (not executed or automatically approved). Prepared MSAASamples/WorldDetail proposals separate from translations: 10/24 cuts, exact source hashes and underlying equality; 8 negative controls reject unsafe changes, CharacterLimits identity preservation passes. WO-QA-SEGMENTATION-001 ready for Antigravity/user relay, NO GAME. No new candidate/runtime WO, production ZWSP or release approval. See SEGMENTATION_EVIDENCE_GATE.md. BUG-THAI-002 stays OPEN.


## SEGMENTATION-001 review accepted — 2026-10-18

Controller verified both input hashes, all 34 per-cut reviewed offsets, source equality and structural guards. Accept both maps unchanged for experimental-build preparation; optional cuts 50/63 retained. Original/marked whitespace coordinates clarified in SEGMENTATION_001_ACCEPTANCE.md. No runtime or production approval. Controller next prepares four width/A/B variants and checks reload/hash isolation before any desktop assignment. All three originals checked; BUG-THAI-002 OPEN, probe-013 coverage 18/20 unchanged.


## WO-VISUAL-018 ready — 2026-10-18

Built four frozen width/input variants from probe-013 and accepted SEGMENTATION-001 maps. A800 retains baseline localisation/UI; B changes only two reviewed tooltip segments; 600 changes only text-child width 800 to600. Per-width A/B font/UI and cross-width input hashes equal as controlled. Reload checks isolate exactly two B source segments and one narrow UI object; all four guarded checks return original/original/original. No installation. Eight-cell Medium matrix ready for Antigravity/user relay, actual effective widths/runtime NOT_RUN. See PROBE_018_HANDOFF.md and qa/WO_VISUAL_018.md. No production ZWSP/global width/release approval.


## Token-conscious screening revision — 2026-10-21

User approved trying a reduced workflow. WO-VISUAL-018 now starts with two texts x A/B at width 800 only (four cells). Width 600 is deferred. Reuse static validation and prior acceptance; capture once per cell with one recovery maximum, inspect changed/problem edges, and use a compact report. Target 45 minutes active work, then stop collection and restore. Full matrix/codepoint transcription and additional review are deferred; unresolved evidence stays unresolved. This reduces initial experimental scope and cannot establish multi-width behavior. No game run/install or production approval in this revision.


## WO-018 screening accepted — 2026-10-21

Controller inspected the four primary images: MSAASamples B uses a later clean break; WorldDetail matches A. Accepted as scoped screening benefit at requested 800/Medium. Fresh manager check confirms three originals. Downsampled captures do not resolve fine shaping; BUG-THAI-002 stays OPEN. 600 cells deferred; no additional desktop run assigned. Capture/time/token budget compliance is not established because additional exploratory captures exist. See PROBE_018_ACCEPTANCE.md.


## Community translation reuse — 2026-10-21

User supplied existing Thai mod. community-merge-001 built locally with project font/UI and 70 project translations preserved; all 15,677 records reload-match. 15,602 imported, five English fallbacks. Candidate NOT_RUN/not installed. Current direction is reuse plus targeted correction instead of bulk retranslation. Next: resolve five fallbacks and prepare bounded smoke test. See COMMUNITY_MERGE_001.md.


## Merged mod smoke test blocked — 2026-10-21

Blank Thai dropdown selected values confirmed from report and Controller image inspection; labels/buttons render. Main menu passed per tester, tooltip inconclusive. Static caption font audit is an investigation lead only. Three originals freshly verified. Next Controller investigates font/material/fallback path; no new runtime assignment. See SMOKE_MERGE_001_DISPOSITION.md.


## Dropdown diagnostic prepared — 2026-10-21

Font localisation maps in merge-002 and probe-013 are identical, so no imported font-name remap was found. Existing fallback references include the Thai dynamic slot; static absence of Thai in primary character table alone does not explain blank captions. community-merge-003 changes only LogLevel selected-caption font/material to that existing Thai slot; all other UI objects and localisation/font bytes preserved. Read-only check confirms three originals. WO-DROPDOWN-001 prepared; no installation or runtime result.


## WO-DROPDOWN-001 negative result accepted — 2026-10-21

LogLevel stays blank after direct Thai font/material assignment. One primary image inspected; three originals freshly checked. Font-only patch is not adopted. Option text exists and font localisation mapping matches baseline; runtime population/processing/overrides need investigation. No new desktop run assigned. See DROPDOWN_001_DISPOSITION.md.


## Native dropdown trace and ASCII control — 2026-10-21

Option getter delegates to numeric LocalisedString lookup; TMP caption refresh supplies option text or empty fallback through virtual setter. Runtime branch/text/font state not established. merge-004 changes only six LogLevel strings to CHECK + original English, fonts/UI identical to merge-002; reload-isolation check passed and three originals verified. WO-DROPDOWN-002 ready, NOT_RUN. See DROPDOWN_NATIVE_TRACE.md.


## ASCII control accepted — 2026-10-21

CHECK Error directly verified in submitted image; adjacent captions still blank. Marked Error option is loaded and reaches visible caption with unchanged merge-002 UI/font. Thai-specific processing/rendering remains unresolved; no automatic font-cause claim or new test. Three originals freshly checked. See DROPDOWN_002_DISPOSITION.md.


## Caption overflow control — 2026-10-21

Working Thai labels use same primary font/material but overflow mode0 versus caption1 and different vertical bounds/font size. merge-005 changes only LogLevel caption overflow to0; Thai input retained. Root cause unconfirmed. Reload isolation passes, three originals checked. See DROPDOWN_CAPTION_COMPARISON.md; WO-DROPDOWN-003 ready, NOT_RUN.


## LogLevel mitigation accepted — 2026-10-21

Thai ข้อผิดพลาด visible/contained after overflow1 to0, primary image inspected. Fine shaping/general root cause remain unproven. merge-006 applies overflow0 to19 Settings captions (12 mode1, seven mode3); mode3 extension explicitly untested. Other fields/objects, font/localisation unchanged; reload isolation verified, three originals checked. WO-DROPDOWN-004 ready, no installation. See DROPDOWN_003_ACCEPTANCE.md.


## Settings caption milestone accepted — 2026-10-21

merge-006: eight Thai and two ASCII selected values visible/contained in directly inspected Game/Video initial views; Medium directly observed. Original blocking defect mitigated within this scope, not general all-option approval. Three originals freshly verified. No repeated Settings matrix. Next select bounded practical gameplay context. See DROPDOWN_004_ACCEPTANCE.md.


## Practical trial ready — 2026-10-21

Existing career.csav identified, no campus save confirmed. Five Cloud/local preference files locally snapshotted and hash-verified, no source writes. WO-GAMEPLAY-001 requires a fresh snapshot before install, then existing career/map and only an existing resumable campus if available; stop on creation/overwrite requirement. Saves may auto-update; record hash changes, do not auto-restore. No installation/runtime yet.


## Campaign intro accepted; campus setup limit — 2026-10-21

Advisor intro Thai readable in inspected map image. Existing brief prohibits advancing intro/new campus; no resumable campus established, so two campus views NOT_RUN. Snapshot ZIP verified and live changes independently match two changed/one new/zero missing/three unchanged. Three game bundles original. Next requires a new-campus trial scope or existing campus context, not identical rerun. See GAMEPLAY_001_DISPOSITION.md.


## First-campus setup authorized — 2026-10-21

User authorized continuing after explanation of Slot1 progression. WO-GAMEPLAY-002 allows advancing initial intro and starting Freshleigh Meadows, normal saves permitted to current Slot1. Fresh save snapshot required, no rollback/other-slot overwrite. Pause and inspect initial text only; no building/hiring/spending/year start. Ready for relay, NOT_RUN; no install by Controller.


## Initial campus trial accepted with known issues — 2026-10-21

Freshleigh entry/opening modal readable; internal ของคุ/ณ split is an observed wrapping defect (BUG-THAI-002 remains OPEN), with targeted language backlog. Source says lowly, so ต่ำต้อย needs contextual style review rather than automatic mistranslation classification. HUD/overview untested. Snapshot verified; live3 changed/4 new/0 missing/3 unchanged; campus save exists. Three originals checked. See GAMEPLAY_002_ACCEPTANCE.md; next targeted correction, no same-view repeat.


## User-reported sara-am collision — 2026-10-21

BUG-THAI-003 OPEN: mai ek and upper sara-am component overlap in ต่ำ, Freshleigh opening modal. User PNG preserved byte-for-byte with provenance. Initial campus acceptance now explicitly includes observed shaping defect plus wrapping/language issues. Next static same-font sara-am/modal investigation; no repeated screen capture needed. See qa/BUG_THAI_003.md.


## Full fresh translation authorized — 2026-10-21

User selected all15,677 messages incl dialogue/descriptions, superseding reuse-first approach. Fresh190 drafts authored from English;15,487 pending. Known injected promo at3 keys replaced while original legal/developer credits preserved. fresh-translation-001 built/reload-verified, not installed. Other imported values temporarily retained in that draft and explicitly not freshly translated. Source/provenance retained locally. See FRESH_RETRANSLATION.md and reports/fresh-retranslation-progress.json.


## Claude translation handoff prepared — 2026-10-21

User assigned full translation to Claude. Prepared local/handoffs/CLAUDE-FULL-RETRANSLATION-001.zip and unpacked folder:171 asset-context packages,15,677 unique records exactly once. No imported Thai authority; old190 drafts retained for later comparison, not exemption from Claude pass. Output contract/glossary/progress and editorial override included. Tool inventory has no direct Claude connector, so delivery is via user relay; not marked received/started. Older RETRANSLATE source batches are alternate inventory, not additional assignments. See CLAUDE_FULL_RETRANSLATION_HANDOFF.md.


## Full Claude delivery received — 2026-10-21

Independent source/token checks pass171 batches/15,677 unique rows, no missing translations as delivery. Full draft fresh-translation-002 built/reload-verified, font/UI same as merge-006, three originals checked, no install. Language212 glossary proposals and2,277 primary-flagged rows pending review. Supplemental997-row uncertainty summary has307 stale field comparisons; queue rebuilt from actual batch rows. See CLAUDE_FULL_RETRANSLATION_RECEIPT.md.


## Claude review R1–4 received — 2026-10-22

292 changed rows/58 batches verified against original files and TSV; frozen source identities and ordered token/control checks pass. Current translated12,721/source identities2,956. fresh-translation-003 built/reload-verified with old font/UI, no runtime. Controller wrote scoped terminology decisions for round5, not yet applied or dispatched. No blanket glossary/language approval. See CLAUDE_REVIEW_R1_4_RECEIPT.md and CONTROLLER_TERMINOLOGY_DECISIONS_2026-10-22.md.


## Round5 integrated; full fresh runtime sample ready — 2026-10-22

321 rows/62 sparse batches verified, no removed flags,11 new PROPER_NAME identities.12,710 translated/2,967 source identities pending review. fresh-translation-004 reload verified, font/UI retained, three originals checked. Good Friends/Pastoral Support/disease/joke backlog remains. Antigravity WO-FRESH-SMOKE-001 prepared for first full fresh corpus runtime, no install yet. See CLAUDE_REVIEW_R5_RECEIPT.md.


## Full fresh smoke setup limit — 2026-10-22

Main menu observed; requested Settings/campus/HUD views unreached, no new translation blocker established. Title-substring driver bug patched to exact executable/foreground guards and actual display coordinate denominators; compile+mock8 checks pass, no live verification. Three originals and10-file snapshot/live save comparison verified, campus unchanged. Original-game capability gate required before any reinstall. See FRESH_SMOKE_001_DISPOSITION.md and qa/WO_FRESH_SMOKE_001_RESUME.md.


## User menu wording override — 2026-10-22

Main-menu Mod approved by user, replacing ม็อด at UI/Modding/Mods (FRESH-036). Logged as pending integration, frozen fresh-translation-004 unchanged. Do not rebuild/reinstall merely to capture this wording. See USER_TEXT_CORRECTIONS.md; include in next text integration.


## Session checkpoint saved — 2026-10-22

User is stopping for rest. See SESSION_CHECKPOINT_2026-10-22.md for exact resume order, pending Mod menu override, original-game capability gate and local-only inputs. No automation/delegated work started. Fresh manager check confirms all3installed originals. Candidate remains fresh-translation-004; no new build or gameplay during checkpoint.

## Latest staged candidate — fresh-translation-005 (2026-10-22)

User-approved Mod integrated at I2LS_UI / UI/Modding/Mods / segment 964 only. 15,677 records read back exactly; one changed segment; all other TextAsset segments unchanged. Font/UI byte-identical to frozen 004, whose hashes remain unchanged. New candidate staged only, runtime NOT_RUN; no inherited runtime approval. Manager supports 005. See reports/fresh-translation-005-build.json and USER_TEXT_CORRECTIONS.md. Prior smoke resume reached Thai Settings and initial campus modal, paused HUD; staff remained NOT_RUN due tutorial. Originals restored; see qa/WO_FRESH_SMOKE_001_RESUME_REPORT.md.
