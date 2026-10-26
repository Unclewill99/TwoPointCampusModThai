"""WO-004 final evidence collation. Read-only inputs: reports, local official TMP
sources, native listings and 17 protected files captured before analysis.
Outputs: NEW analysis Markdown, report JSON and preservation-after JSON. Uses
exclusive creation; never overwrites. No builds, game execution or input mutation.
"""
from pathlib import Path
import json,hashlib,re
R=Path(__file__).resolve().parents[1]
def read(p):return json.loads((R/p).read_bytes())
def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
before=read('reports/sara-am-004-preservation-before.json')
after={p:{'size':Path(p).stat().st_size,'sha256':sha(Path(p))} for p in before}
assert after==before,'Protected input changed; stop before reporting preservation PASS'
assets=read('reports/sara-am-004-asset-evidence.json')
packages=read('reports/sara-am-004-package-evidence.json')
S='local/review/sara-am-004/official-packages/3.2.0-pre.4/'
claims=[
 {'id':'V1','label':'VERIFIED','claim':'Official registry SHA1 and package.json verify downloaded source package versions 3.2.0-pre.4 and 3.2.0-pre.10; these do not identify the game package.','evidence':['reports/sara-am-004-package-evidence.json','local/review/sara-am-004/unity-registry.json']},
 {'id':'V2','label':'UNKNOWN','claim':'Exact shipped TMP package version and matching source revision. Assembly 0.0.0.0 and TMP_Settings.version literal 1.4.0 are not reliable package identifiers.','evidence':['local/review/sara-am-004/metadata-v3.txt','local/review/sara-am-004/globals.tsv',S+'TMP_Settings.cs']},
 {'id':'V3','label':'VERIFIED','claim':'Native initializer calls ligature, pair, mark-to-base and mark-to-mark dictionary initializers; no multiple-substitution initializer in this method. This is static call evidence only.','evidence':['local/review/sara-am-004/native/TMPro.TMP_FontAsset.InitializeDictionaryLookupTables.asm.txt']},
 {'id':'Q1a','label':'VERIFIED','claim':'Font glyph82 is a composite containing uni0E32 and uni0E4D; target TMP has empty serialized glyph/character tables, atlas mode1, 512x512, padding3, multiatlas disabled.','evidence':['reports/sara-am-004-asset-evidence.json']},
 {'id':'Q1b','label':'INFERRED','claim':'If the game follows the inspected source path and selects this fallback, atomic sequence [118,42,82] retains one composite sara-am; tone42 is placed from preceding base118, not from a future embedded ring.','evidence':[S+'TMPro_UGUI_Private.cs:2217-2335',S+'TMP_TextParsingUtilities.cs:IsBaseGlyph','reports/sara-am-004-asset-evidence.json'],'reason':'Source processes current marks against prior glyphs; U+0E33 is classified as a base and comes after the tone. A/B accepted atomic row is unchanged.'},
 {'id':'Q1c','label':'UNKNOWN','claim':'Actual runtime fallback, glyph stream, active feature flags and exact chosen placement branch; no runtime trace acquired by this WO.','evidence':['docs/SARA_AM_002_AB_R2_ACCEPTANCE.md']},
 {'id':'C1','label':'INFERRED','claim':'Pair42->82 cannot be assumed to lift tone42: successful mark placement subsequently assigns x/yPlacement rather than adding pair placement. Changing base118/mark42 anchor affects all uses of that base/mark pair, without sara-am context.','evidence':[S+'TMPro_UGUI_Private.cs:2217-2335','reports/sara-am-004-asset-evidence.json']},
 {'id':'C2','label':'VERIFIED','claim':'Actual tone glyph IDs are U+0E48=42, U+0E49=47, U+0E4A=50, U+0E4B=39; do not use assumed IDs43/44/45.','evidence':['reports/sara-am-004-asset-evidence.json']},
]
support=[
 {'record':'MultipleSubstitution','source_label':'VERIFIED','source_result':'Serialized list/record exists; no lookup or consumption in inspected TMP_FontFeatureTable, TMP_FontAsset, TMP_Text and UGUI paths. Record has target/substitute IDs only, no contextual guard.','game_label':'UNKNOWN','game_result':'No executing path established; adding a list record is not justified. Native initializer has no such lookup.','evidence':[S+'TMP_FontFeatureTable.cs',S+'FontFeatureCommonGSUB.cs',S+'TMPro_UGUI_Private.cs']},
 {'record':'Ligature (including 3 components)','source_label':'VERIFIED','source_result':'componentGlyphIDs.Length loop matches components; TryAddGlyphInternal supplies replacement; gated on active liga.','game_label':'INFERRED','game_result':'Initializer exists and schema matches; exact executing matcher and active liga for modal UNKNOWN.','evidence':[S+'TMPro_UGUI_Private.cs:1093,1298-1364','local/review/sara-am-004/native/TMPro.TMP_FontAsset.InitializeDictionaryLookupTables.asm.txt']},
 {'record':'Contextual GSUB / reordering','source_label':'VERIFIED','source_result':'Inspected MultipleSubstitution record has no preceding-tone condition. Inspected ligature path matches a fixed component sequence; it is not a contextual decomposition engine.','game_label':'UNKNOWN','game_result':'No supported serialized contextual rule or Thai reorder path demonstrated.','evidence':[S+'FontFeatureCommonGSUB.cs',S+'TMP_FontFeatureTable.cs']},
 {'record':'GlyphPairAdjustment','source_label':'VERIFIED','source_result':'Adjacent pair first/second adjustment consumed when kern active, then mark placement may overwrite x/yPlacement.','game_label':'INFERRED','game_result':'Native GenerateTextMesh contains pair-adjustment getter calls before IsBaseGlyph; exact inputs/flags UNKNOWN.','evidence':[S+'TMPro_UGUI_Private.cs:2217-2255','local/tools/native-inspection/TMPro.TextMeshProUGUI.GenerateTextMesh.asm.txt:2819-3065']},
 {'record':'MarkToBase','source_label':'VERIFIED','source_result':'Current nonbase glyph attaches to earlier last-base using mark/base glyph IDs.','game_label':'INFERRED','game_result':'Initializer and native anchor getter calls present; actual atomic branch UNKNOWN.','evidence':[S+'TMPro_UGUI_Private.cs:2259-2335','local/tools/native-inspection/TMPro.TextMeshProUGUI.GenerateTextMesh.asm.txt:3065-3220']},
 {'record':'MarkToMark','source_label':'VERIFIED','source_result':'Current nonbase mark scans backward toward last base. Cannot position an earlier tone relative to a later base-like sara-am.','game_label':'VERIFIED','game_result':'Accepted A/B establishes localized effect of added59->42 in reordered rowB only; complete implementation/fallback identity still UNKNOWN.','evidence':['docs/SARA_AM_002_AB_R2_ACCEPTANCE.md','reports/sara-am-002-ab-r2-image-diff.json',S+'TMPro_UGUI_Private.cs:2284-2320']}
]
options=[
 {'option':'D+B (new full-cluster glyph + fixed ligature)','label':'INFERRED','rank':1,'score':[2,3,2],'product':12,'status':'INCONCLUSIVE','scope':'New font file and new scratch font bundle only; new glyph appended and one target TMP ligature.','runtime':'UNKNOWN active liga, replacement glyph packing, fallback and layout behavior.'},
 {'option':'A (renderer hook)','label':'INFERRED','rank':2,'score':[3,2,1],'product':6,'status':'BLOCKED_NEEDS_DECISION','scope':'Code plugin/loader required; exceeds asset-bundle-only project. No implementation design supplied.','runtime':'UNKNOWN hook coverage, indexing, update compatibility and stability.'},
 {'option':'B alone (table decomposition)','label':'INFERRED','rank':3,'score':[1,3,2],'product':6,'status':'INCONCLUSIVE','scope':'Would change target TMP feature table only. No demonstrated executor for multiple/contextual substitution.','runtime':'UNKNOWN; decomposition82->[59,78] alone also does not reorder a preceding tone.'},
 {'option':'C (pair/anchor)','label':'INFERRED','rank':4,'score':[1,1,2],'product':2,'status':'INCONCLUSIVE','scope':'Pair42->82 is narrow but may be overwritten; base118->tone42 anchor reaches every such pair.','runtime':'UNKNOWN; global tone shift is prohibited.'},
 {'option':'D alone (font GSUB/GPOS)','label':'INFERRED','rank':5,'score':[1,1,2],'product':2,'status':'INCONCLUSIVE','scope':'Changing existing glyph82/cmap/GSUB without an executing selection path risks all sara-am text.','runtime':'UNKNOWN source-font feature import/execution; no automatic atlas regeneration guarantee.'},
 {'option':'E (stored-text decomposition)','label':'VERIFIED','rank':None,'score':None,'product':None,'status':'REJECTED_BY_WO','scope':'Comparison only; prohibited production shortcut.','runtime':'Accepted reordered specimen+pair separates; broader behavior UNKNOWN.'}
]
rows=[]
def row(text,expected,group='required',runtime='NOT_RUN'):
    rows.append({'text':text,'codepoints':[f'U+{ord(c):04X}' for c in text],'codepoint_label':'VERIFIED','expectation_label':'INFERRED','expected':expected,'offline':'Codepoint/cmap/structure and source-algorithm checks; no game visual PASS.','runtime':runtime+': actual fallback, stacking, clipping, advance, wrapping at Small/Medium/Large and after restart.','group':group})
for word in ['ต่ำ','ค่ำ','ช้ำ','ค้ำ','ถ้ำ','น้ำ']:
    row(word,'Nikkhahit below tone, visible separation, sara-aa stays on normal baseline.')
for word in ['จำ','ทำ','ลำ']:
    row(word,'Single nikkhahit above base and sara-aa on normal baseline; no spurious tone or width change.')
for base in ['ป','ฝ','ฟ']:
    for tone in ['่','้','๊','๋']:
        row(base+tone+'ำ','Tone above nikkhahit; tall ascender remains clear; narrow variant/offset must suit this base.','tall-base synthetic coverage')
for word in ['ต้ำ','ต๊ำ','ต๋ำ']:
    row(word,'Correct mai-tho/mai-tri/mai-chattawa above nikkhahit.','tone synthetic coverage')
for word in ['ถี่','ที่','ปี้','ตี่','ตา','ต่า','ต้า','นำ','ตำ','ต่ำต่ำ','ต่ำ ต่ำ']:
    row(word,'Preserve ordinary vowel/tone stacking, base baseline and spacing; no unintended substitution.','negative and boundary controls')
row('A: ต่ำ ถี่','Atomic target separates and ถี่ control unchanged; reuse A/B R2 specimen format.','specimen')
row('B: ต\u0e4d\u0e48\u0e32 ถี่','Historical reordered-decomposed diagnostic; do not convert production text.','diagnostic only')
row('C: ต\u0e48\u0e4d\u0e32 ถี่','Preserve recorded original-order diagnostic interpretation; not a production spelling/fix.','diagnostic only')
row('Campus 2026: ต่ำ ถี่ 123','No Latin/number/colon/space change; Thai stacking preserved.','mixed')
row('ต่ำ ถี่ น้ำ\nCampus 123 ต่ำ ถี่','Explicit LF retained; also test same text without LF in a narrow box for automatic wrap.','multiline')
row('<b>ต่ำ</b> <color=#FFFFFF>ถี่</color>','Rich-text indices/tags preserved; cluster stays intact across layout operations.','rich text')
report={'work_order':'WO-SARA-AM-004','date':'2026-10-26 Asia/Bangkok','status':'INCONCLUSIVE','option_A_status':'BLOCKED_NEEDS_DECISION','bug':'BUG-THAI-003 OPEN','claims':claims,'record_support':support,'options':options,'regression_matrix':rows,'ranking_scale':{'label':'INFERRED','description':'Ordinal 1 low / 2 medium / 3 high: expected efficacy x containment x offline verifiability. Not probabilities; scope gate overrides score.'},'single_next_step':'PM obtains the exact shipped TMP package/build provenance and corresponding custom source (offline), sufficient to resolve the ligature/mark execution and feature-flag gates before authorizing any candidate.','blockers':[{'label':'UNKNOWN','item':'Exact shipped package version/source revision and custom-loading modifications.'},{'label':'UNKNOWN','item':'Actual glyph stream, selected fallback and active liga/mark/mkmk on the modal.'},{'label':'INFERRED','item':'A requires an explicit scope decision permitting code plugin/loader.'}],'protected_files':{'label':'VERIFIED','count':len(after),'unchanged':True,'before':'reports/sara-am-004-preservation-before.json','after':'reports/sara-am-004-preservation-after.json'},'completed_operations':['Read accepted references without rerunning browser or A/B','Read-only metadata inspection and bounded native decoding','Verified official source package metadata/checksums','Inspected targeted font configuration/anchors/glyph IDs','Created analysis and machine-readable report'],'not_executed':['Game launch','Install','Candidate build','Runtime work order','Corpus Unicode rewrite','Commit','Push','Automation','Messages to agents'],'limitations':['No offline shaping rerun: existing reference accepted.','Native leaf methods without exact unwind bounds were not guessed/decompiled.','Downloaded package identity is not shipped package identity.','No whole-workspace immutability claim; preservation covers the 17 snapshotted protected files.']}
doc='''# WO-SARA-AM-004 — Offline solution analysis

Date: 2026-10-26 (Asia/Bangkok). Analyst: ChatGPT. **INCONCLUSIVE**.

**VERIFIED — delivery boundary.** Analysis only; no candidate, install, game launch, runtime WO, commit or push. Protected-input hashes match for all 17 files captured before analysis. See `reports/sara-am-004-preservation-{before,after}.json`. Existing changes to `docs/PROJECT_STATUS.md` and `docs/AGENT_TASKS.md` predate this analysis and were preserved. This report does not change PM authority or close BUG-THAI-003.

## Evidence and version gate (Q1/Q2)

**VERIFIED — accepted baseline, not repeated.** Use `SARA_AM_001_REFERENCE_ACCEPTANCE.md`, `SARA_AM_003_EXPERIMENT.md`, `SARA_AM_002_AB_R2_ACCEPTANCE.md`, the corresponding QA report, `reports/sara-am-font-audit.json`, `sara-am-gsub-mappings.json`, `sara-am-tutorial-{provider,text,font-chain}.json` and `sara-am-002-ab-r2-image-diff.json`. Accepted reference is Chrome155/CSS64px, embedded font SHA256 `f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0`. Added59→42 changed 74 pixels in reordered row B; atomic A/original-order C unchanged. Do not interpret browser shaping as game runtime evidence.

**VERIFIED — authoritative source packages.** Unity registry metadata at [packages.unity.com/com.unity.textmeshpro](https://packages.unity.com/com.unity.textmeshpro) identifies downloaded `3.2.0-pre.4` (repository revision `26fadfb632ffe5cb14bab5019ef8097eece1e62a`, tar SHA1 `22accec50ea3c1d608e223c2eff5effdb7269e2b`) and `3.2.0-pre.10` (`8fca90baea965bab48c88326f1d4ca248b64097b`, SHA1 `e75768cd64591d1817bac4c54b9fe98fdf87d280`). Tarballs were checked against registry SHA1 and their package.json identities. Evidence: `reports/sara-am-004-package-evidence.json`; sources retained under `local/review/sara-am-004/official-packages/`. Earlier pre4 mirror text matches official source after BOM/line-ending normalization; analysis below cites official pre4 source, not an assumed shipped version.

**UNKNOWN — exact shipped package.** No binding project `packages-lock.json`/package manifest was found in the inspected game/local trees. Metadata identifies `Unity.TextMeshPro.dll`, assembly version `0.0.0.0`; independently checked codegen table maps get_version to `0x181fc9b20`, whose literal is `1.4.0`. The downloaded source also uses that stale literal. Neither number proves package version. Metadata contains custom loading fields (`DynamicFontLoadingMode`, `OnAsyncLoadRequiredFilesCompleted`, `m_fontFile`) absent from the two inspected standard TMP_FontAsset sources. A custom fork/backport is **INFERRED**, exact provenance **UNKNOWN**. Evidence: `metadata-v3.txt`, `globals.tsv`, `native/TMPro.TMP_Settings.get_version.asm.txt`, official TMP_Settings.cs. It would be incorrect to claim the game uses pre4 or pre10.

## Atomic sara am (Q1)

**VERIFIED — assets.** `reports/sara-am-004-asset-evidence.json` shows glyph82 is a TrueType composite of uni0E32 + uni0E4D. This is one glyph with two outlines, not two text glyphs. TMP object `-1239755799206566947` has empty serialized glyph/character tables, atlas mode1, 512×512, padding3, multiatlas disabled, point size30, reimport flag0. Existing base118/mark42 anchor y values both16.08 give zero vertical adjustment; no42→82 pair exists. Actual tones: `่=42`, `้=47`, `๊=50`, `๋=39` (not assumed43/44/45).

**VERIFIED — source behavior, conditional applicability.** Official pre4 `TMP_TextParsingUtilities.cs:IsBaseGlyph` treats U+0E48 as a mark and U+0E33 as a base. `TMPro_UGUI_Private.cs:2217–2335` applies pair positioning, then current-mark attachment to prior base/marks; it does not look ahead to an embedded component of a future glyph. `:1298–1364` implements fixed ligatures. No multiple-substitution consumer or Thai-specific reorder was found in the inspected TMP_FontAsset/TMP_Text/UGUI/feature-table paths. A type/list existing is not an executor.

**INFERRED — likely atomic path.** If this game follows that inspected path and uses the target fallback, ต่ำ maps `[118,42,82]`; tone42 attaches to ต118 through MarkToBase, while sara-am82 keeps its baked ring. It cannot use MarkToMark(82,42) to place an earlier tone over a later sara-am. This is consistent with accepted A/B, not proof of the actual glyph stream or root cause. **UNKNOWN:** runtime font selection, substitutions, active flags and exact branch. Static text route remains MAIN4694779218175474965 → TMP7894969370473676053 → PalanquinDark external8 → Thai fallback; it does not establish live selection.

## Executing records versus storage (Q2)

Each row separates **VERIFIED inspected-source/static evidence** from applicability to the shipped runtime. Detailed machine table: `reports/sara-am-004-analysis.json:record_support`.

| Record | Source/static result | Shipped-runtime conclusion |
|---|---|---|
| MultipleSubstitution | VERIFIED: record/list only in inspected paths; no lookup; no contextual field | UNKNOWN executor. Do not add82→[59,78] blindly; even substitution alone leaves preceding-tone order unresolved. |
| Ligature, 3 components | VERIFIED: length-driven matching and TryAddGlyphInternal, gated on liga | INFERRED support from native initializer/schema; active liga and exact matcher UNKNOWN. |
| Contextual GSUB/reordering | VERIFIED: no contextual guard in inspected multiple record; fixed ligature is not a general context shaper | UNKNOWN supported game path; no proven table-only contextual decomposition. |
| GlyphPairAdjustment | VERIFIED: pair getter calls before IsBaseGlyph in native GenerateTextMesh; source consumes first/second values under kern | INFERRED consumption; actual flags/inputs UNKNOWN. Mark placement can overwrite source pair x/yPlacement. |
| MarkToBase | VERIFIED: native initializer/getter sites; source uses prior base/current mark | INFERRED atomic branch; exact live branch UNKNOWN. |
| MarkToMark | VERIFIED: accepted59→42 effect for reordered rowB; native initializer/getter sites | VERIFIED only within accepted A/B scope; no atomic fix or universal fallback claim. |

**VERIFIED — native limits.** New bounded initializer listing at `0x182c08770` calls ligature/pair/MarkToBase/MarkToMark initialization, no multiple lookup. Existing GenerateTextMesh listing calls IsBaseGlyph at `0x183508ea9` after pair getter sites and before anchor getter sites. Several leaf initializers/IsBaseGlyph lack exact unwind bounds in the decoder; their internals remain **UNKNOWN**, not guessed. Existing shared-RET GSUB entry does not exclude other shaping paths. Source ImportFontFeatures/UpdateGSUB extraction is compile-flag dependent; serialization and dynamic feature import are separate questions.

## Options, ranking and impact (Q3)

**INFERRED — heuristic rank.** Scores are ordinal 1–3, efficacy × containment × offline verifiability, not measured probabilities. Scope/evidence gates override product. D+B is a possible asset-only branch, not an authorized build or proven fix.

| Rank / score | Option and exact change boundary | Confidence / blast radius | Offline verification / runtime gap / reversibility |
|---|---|---|---|
| 1 / 12 | D+B: new appended full-cluster glyph plus one fixed `[118,42,82]` ligature in target TMP | INFERRED medium efficacy, narrow exact sequence. Layout/index behavior risk; other occurrences of ต่ำ also match | Offline font validity, exact object diff and atlas inputs; UNKNOWN live liga/packing/fallback/layout. Revert future scratch bundle, preserve baseline. |
| 2 / 6 | A: renderer processing hook; requires code plugin/loader beyond data bundles | INFERRED highest conceptual shaping coverage; update/stability/indexing and hook-coverage risks | Offline algorithm checks cannot establish integration. **BLOCKED_NEEDS_DECISION** on scope; no plugin design here. Rollback would require separate plugin removal contract. |
| 3 / 6 | B alone: serialized substitution/positioning records in TMP only | INFERRED low efficacy: missing demonstrated multiple/contextual executor; existing glyphs do not provide a proven full replacement | Structure can pass while rules never execute. UNKNOWN runtime. A ligature without a suitable replacement glyph is incomplete. Revert new TMP-only scratch output. |
| 4 / 2 | C: pair42→82 or base118/mark42 anchors | INFERRED low efficacy or inadequate containment | Source mark assignment overwrites pair yPlacement. Raising base118/mark42 changes ต่า/ตี่ etc; pair has no third-context predicate. UNKNOWN game applicability. Rollback exact record delta; no global shifts. |
| 5 / 2 | D alone: GSUB/GPOS or existing82/cmap replacement | INFERRED low efficacy without consuming/selection path, broader sara-am impact | Font validation is possible, engine application UNKNOWN. Altering82 globally changes จำ/ทำ/ลำ too; source bytes and cached TMP atlas can diverge. New file only, revert scratch bundle. |
| excluded | E: convert stored text to reordered decomposition | VERIFIED rejected by WO; accepted diagnostic only | INFERRED changes codepoint identity, search/copy/index consumers; broader effects UNKNOWN. No corpus conversion performed or recommended. |

**INFERRED — C geometry bound.** Font glyph82 top794 and tone42 bottom632 imply a purely vertical separation would require tone rise greater than162 font units plus desired gap (greater than4.86 at point30), assuming unchanged origins and overlapping x extents. The known59→42 anchors imply236 units /7.08 at point30; that is not a validated atomic offset. Source successful MarkToBase currently assigns y=16.08−16.08=0, overwriting a pair placement. Raising the base anchor to23.16 would change all118/42 attachments; it cannot be confined to following sara-am by this record. Moving glyph82 instead moves sara-aa off baseline as well. These numbers are geometry/source bounds, not screen pixel predictions.

### Conditional bounded candidate specification — NOT READY / NOT BUILT

**INFERRED — D+B branch only after the evidence gate.** Start from frozen005 by read-only copy into a new, exclusive scratch directory. Target font object7716434233879021909 and TMP object−1239755799206566947 only. Append one full ต่ำ glyph (potential ID459 only if the new font still has459 glyphs and preserves all IDs0–458); ligature record fields `m_ComponentGlyphIDs=[118,42,82]`, `m_LigatureGlyphID=459`. No cmap/text change and no alteration of existing outlines/metrics. This selects a full cluster whose first character is a base, avoiding a tone-class replacement that would itself be attached as a mark. **UNKNOWN:** final composite placement/metrics and whether live liga and dynamic glyph loading accept it. No guessed final outlines or offsets are approved.

**INFERRED — expected future diff/checks.** Only embedded font bytes (new glyph plus required glyf/loca/maxp/hmtx/hhea/head/checksum changes as applicable) and one TMP ligature list entry; localization/UI bundles and all unrelated raw objects must compare byte-identical. Keep existing atlas settings, face metrics and all previous glyph IDs/advances. Current dynamic tables are empty; source TryAddGlyphInternal can populate a glyph at runtime, but this is **UNKNOWN** for the game. Do not assume replacing the TTF regenerates cached/static atlases. If static prepacking is needed, stop and respecify glyph records/rects/textures/materials with exact diffs; none are specified or built here.

**INFERRED — future acceptance/rollback contract.** Require fontTools reopen/checksums, preserved cmap and old glyph bounds/advances, parsed ligature uniqueness/no duplicate first-key conflict, exact component IDs, source hash and baseline bundle/object hashes, new font/bundle/object hashes, raw object diff, target TMP readback, unchanged localization hash/codepoints, no output overwrite. Active liga, actual replacement, glyph-cache lifetime, wrapping/index mapping and raster quality need later authorized runtime QA. Reversion is removal of the future scratch artifact / restoration of original installed bundle via the PM-approved lifecycle, never mutation of frozen005. This WO authorizes neither build nor runtime WO.

## Regression matrix (Q4)

**VERIFIED — codepoints; INFERRED — expected presentation.** All rows below are proposed coverage, **NOT_RUN** in this WO. Offline can check encoded sequence, cmap/record/outline structure and reason about the inspected source; only later runtime QA can confirm the game's fallback, visible stacking, clipping, advances and automatic wrap. Existing ต่ำ+ถี่ specimen format is retained. Synthetic tall-base/tone cases are coverage strings, not a linguistic approval. Test Small/Medium/Large, restart/cache, normal/bold/rich text and narrow/wide boxes; use actual screen captures and preserve input codepoints.

{MATRIX}

## Status and one next step

**INCONCLUSIVE.** **UNKNOWN:** exact shipped package/custom source, executing atomic path and live feature flags. A separately remains **BLOCKED_NEEDS_DECISION** because it requires code scope. No bounded candidate is justified for build yet, and BUG-THAI-003 remains OPEN.

**INFERRED — single next step:** PM obtains offline provenance for the exact shipped TMP package/custom source (build lock/package metadata plus matching source/revision or equivalent build artifacts), resolving the execution/feature-flag gates before authorizing a candidate. Public package metadata verifies source downloads, not the game's dependency selection. If provenance is unavailable, retain UNKNOWN and do not treat a structurally valid table patch as a fix.
'''
matrix='| Specimen | Exact codepoints (VERIFIED) | Expected (INFERRED) | Offline / runtime |\n|---|---|---|---|\n'
for x in rows:
    text=x['text'].replace('\n',' ⏎ ').replace('|','&#124;').replace('<','&lt;').replace('>','&gt;')
    matrix+='| '+text+' | '+' '.join(x['codepoints'])+' | '+x['expected']+' | Structure only / runtime NOT_RUN |\n'
doc=doc.replace('{MATRIX}',matrix)
# All paths below are new outputs. Preflight ensures a partial earlier delivery is not overwritten.
outputs=[R/'reports/sara-am-004-preservation-after.json',R/'reports/sara-am-004-analysis.json',R/'docs/SARA_AM_004_OFFLINE_ANALYSIS.md']
assert not any(p.exists() for p in outputs)
outputs[0].open('x',encoding='utf-8').write(json.dumps(after,indent=2))
outputs[1].open('x',encoding='utf-8').write(json.dumps(report,ensure_ascii=False,indent=2))
outputs[2].open('x',encoding='utf-8').write(doc)
print(json.dumps({'status':report['status'],'protected_files_unchanged':len(after),'regression_rows':len(rows),'outputs':[str(p.relative_to(R)) for p in outputs]}))
