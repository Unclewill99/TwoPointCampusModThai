"""WO-SARA-AM-005: build + offline verification only; never installs/launches.
Inputs (read-only): frozen005, protected001a/b, installed bundle hashes, retained
official TMP pre4 source/native initializer evidence. Outputs (exclusive create):
local/prototype/probe-sara-am-lig-001, reports/sara-am-lig-001-build.json,
docs/SARA_AM_005_LIGATURE_PROBE_BUILD.md. Existing outputs cause abort.
No embedded-font edit, Unicode corpus rewrite, UI edit, commit or push.
"""
from pathlib import Path
import copy,hashlib,io,json,subprocess,sys
import UnityPy
from fontTools.ttLib import TTFont

R=Path(__file__).resolve().parents[1]
BASE=R/'local/prototype/fresh-translation-005'
OUT=R/'local/prototype/probe-sara-am-lig-001'
REPORT=R/'reports/sara-am-lig-001-build.json'
DOC=R/'docs/SARA_AM_005_LIGATURE_PROBE_BUILD.md'
for path in [OUT,REPORT,DOC]:
    if path.exists():raise SystemExit('Refusing to overwrite '+str(path))
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
def digest(data):return hashlib.sha256(data).hexdigest()
def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def snapshot(paths):return {str(p.relative_to(R.parent)):{'size':p.stat().st_size,'sha256':sha(p)} for p in sorted(paths)}
manifest=json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
names=[f['name'] for f in manifest['files']]
assert len(names)==3 and all(Path(n).name==n for n in names)
font_name='fonts_assets_all.bundle';loc_name='localisation_assets_localisationenglish.bundle'
game=R.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
protected=[p for root in [BASE,R/'local/prototype/probe-sara-am-001a',R/'local/prototype/probe-sara-am-001b'] for p in root.rglob('*') if p.is_file()]
protected += [game/n for n in names]+[R.parent/'GameAssembly.dll',R.parent/'TPC_Data/il2cpp_data/Metadata/global-metadata.dat']
before=snapshot(protected)
for f in manifest['files']:
    assert sha(BASE/f['name'])==f['probe_sha256']
    assert sha(game/f['name'])==f['original_sha256'],'Installed bundle not original'

diag='L1: ต่ำ\nL2: ต้ำ\nL3: ค่ำ\nL4: ตา ถี่\nL5: ก'
expected_words=['\u0e15\u0e48\u0e33','\u0e15\u0e49\u0e33','\u0e04\u0e48\u0e33','\u0e15\u0e32 \u0e16\u0e35\u0e48','\u0e01']
assert [s.split(': ',1)[1] for s in diag.splitlines()]==expected_words
locenv=UnityPy.load(str(BASE/loc_name))
def texts(env):return {o.read().m_Name:o.read().m_Script for o in env.objects if o.type.name=='TextAsset'}
loc_before=texts(locenv)
locobj=next(o for o in locenv.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_Levels')
locid=locobj.path_id
t=locobj.read();parts=t.m_Script.split('[i2t]')
assert parts[533].startswith('Levels/Freshleigh/Level_Intro_Text=')
parts[533]=parts[533].split('=',1)[0]+'='+diag
t.m_Script='[i2t]'.join(parts);t.save()
locbytes=next(iter(locenv.files.values())).save()

fenv=UnityPy.load(str(BASE/font_name))
targetid=-1239755799206566947;fontid=7716434233879021909
target=next(o for o in fenv.objects if o.path_id==targetid)
old=target.read_typetree();new=copy.deepcopy(old)
fontobj=next(o for o in fenv.objects if o.path_id==fontid)
fontbytes=bytes(fontobj.read_typetree()['m_FontData'])
assert digest(fontbytes)=='f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0'
ft=TTFont(io.BytesIO(fontbytes));cmap=ft.getBestCmap()
mapping={f'U+{cp:04X}':ft.getGlyphID(cmap[cp]) for cp in [0xe01,0xe04,0xe15,0xe16,0xe32,0xe33,0xe35,0xe48,0xe49]}
assert [mapping[f'U+{cp:04X}'] for cp in [0xe15,0xe48,0xe33]]==[118,42,82]
assert mapping['U+0E49']==47 and mapping['U+0E01']==29
records=old['m_FontFeatureTable']['m_LigatureSubstitutionRecords']
assert len(records)==9
assert all(x['m_ComponentGlyphIDs'] and x['m_ComponentGlyphIDs'][0]!=118 for x in records)
def fields(x):
    if isinstance(x,dict):
        for k,v in x.items():yield k;yield from fields(v)
    elif isinstance(x,list):
        for v in x:yield from fields(v)
serialized_lookups=sorted({k for k in fields(old) if 'lookup' in k.lower() and k!='m_FeatureLookupFlags'})
assert not serialized_lookups,'Serialized lookup requires separate safe update; STOP'
source_dir=R/'local/review/sara-am-004/official-packages/3.2.0-pre.4'
source=(source_dir/'TMP_FontAsset.cs').read_text(encoding='utf-8-sig')
assert 'InitializeLigatureSubstitutionLookupDictionary();' in source
assert 'm_LigatureSubstitutionRecordLookup.Clear();' in source
assert 'record.componentGlyphIDs[0]' in source
matcher=(source_dir/'TMPro_UGUI_Private.cs').read_text(encoding='utf-8-sig')
assert 'for (int j = 0; j < records.Count; j++)' in matcher
record={'m_ComponentGlyphIDs':[118,42,82],'m_LigatureGlyphID':29}
new['m_FontFeatureTable']['m_LigatureSubstitutionRecords'].append(record)
target.save_typetree(new)
newfontbundle=next(iter(fenv.files.values())).save()
OUT.mkdir(exist_ok=False)
for n in names:
    data=locbytes if n==loc_name else newfontbundle if n==font_name else (BASE/n).read_bytes()
    with (OUT/n).open('xb') as f:f.write(data)

def objects(env):
    return {(o.assets_file.name,str(o.path_id),o.type.name):o.get_raw_data() for o in env.objects}
diffs={};object_hashes={}
for n in names:
    a=objects(UnityPy.load(str(BASE/n)));b=objects(UnityPy.load(str(OUT/n)))
    assert a.keys()==b.keys()
    changed=[k for k in a if a[k]!=b[k]]
    expected=[targetid] if n==font_name else [locid] if n==loc_name else []
    assert sorted(int(k[1]) for k in changed)==sorted(expected),(n,changed)
    diffs[n]=[{'asset':k[0],'path_id':int(k[1]),'type':k[2],'before_sha256':digest(a[k]),'after_sha256':digest(b[k])} for k in changed]
    if n==font_name:
        object_hashes={str(k[1]):{'before_sha256':digest(a[k]),'after_sha256':digest(b[k])} for k in a if int(k[1]) in [targetid,fontid]}
    if not expected:assert sha(BASE/n)==sha(OUT/n)
actualenv=UnityPy.load(str(OUT/font_name))
actual=next(o.read_typetree() for o in actualenv.objects if o.path_id==targetid)
assert len(actual['m_FontFeatureTable']['m_LigatureSubstitutionRecords'])==10
restored=copy.deepcopy(actual)
assert restored['m_FontFeatureTable']['m_LigatureSubstitutionRecords'].pop()==record
assert restored==old,'Unexpected TMP change beyond added record'
assert actual['m_FontFeatureTable']['m_LigatureSubstitutionRecords'][:9]==records
actualfont=bytes(next(o for o in actualenv.objects if o.path_id==fontid).read_typetree()['m_FontData'])
assert actualfont==fontbytes
loc_after=texts(UnityPy.load(str(OUT/loc_name)));assert loc_before.keys()==loc_after.keys()
changes=[];segment_count=0
for asset in loc_before:
    a,b=loc_before[asset].split('[i2t]'),loc_after[asset].split('[i2t]')
    assert len(a)==len(b);segment_count+=len(a)
    changes.extend([asset,i] for i,(x,y) in enumerate(zip(a,b)) if x!=y)
assert changes==[['I2LS_Levels',533]]
assert loc_after['I2LS_Levels'].split('[i2t]')[533].split('=',1)[1]==diag
after=snapshot(protected);assert before==after
files=[{'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(OUT/f['name']),'parent_sha256':sha(BASE/f['name'])} for f in manifest['files']]
rows=[{'row':f'L{i+1}','text':line.split(': ',1)[1],'full_line':line,'codepoints':[f'U+{ord(c):04X}' for c in line],'specimen_codepoints':[f'U+{ord(c):04X}' for c in line.split(': ',1)[1]],'label':'VERIFIED'} for i,line in enumerate(diag.splitlines())]
outcomes=[
 {'row':'L1','executed':'INFERRED: one ก-shaped sentinel replaces ต่ำ; prefix L1 remains.','not_executed':'INFERRED: original atomic ต่ำ remains (crowding may persist).','failure':'UNKNOWN: blank/tofu, partial sequence, clipping or crash is an invalid/inconclusive result.'},
 {'row':'L2','executed':'INFERRED: ต้ำ remains unchanged; tone47 cannot match42.','not_executed':'INFERRED: ต้ำ unchanged.','failure':'INFERRED: any sentinel/substitution here violates specificity.'},
 {'row':'L3','executed':'INFERRED: ค่ำ unchanged; different base cannot match118.','not_executed':'INFERRED: ค่ำ unchanged.','failure':'INFERRED: sentinel here violates specificity.'},
 {'row':'L4','executed':'INFERRED: ตา ถี่ unchanged.','not_executed':'INFERRED: ตา ถี่ unchanged.','failure':'INFERRED: missing/changed controls invalidate clean comparison.'},
 {'row':'L5','executed':'INFERRED: ก visible as standalone reference.','not_executed':'INFERRED: ก still visible if loading succeeds.','failure':'INFERRED: absent/tofu ก leaves glyph loading unresolved; do not call executor absent.'}
]
report={'work_order':'WO-SARA-AM-005','date':'2026-10-26 Asia/Bangkok','status':'BUILD_READY','label':'VERIFIED','probe':OUT.name,'parent':BASE.name,'installed':False,'runtime_status':'NOT_RUN','files':files,'diagnostic_text':diag,'diagnostic_codepoints':[x['codepoints'] for x in rows],'specimens':rows,'sentinel':{'character':'ก','codepoint':'U+0E01','glyph_id':29,'label':'VERIFIED','justification':'Existing cmap glyph; visually distinct from full ต่ำ cluster; standalone L5 supplies loading/reference control. Actual visibility/population remains runtime UNKNOWN.'},'added_record':record,'existing_ligatures_before':records,'ligature_count_after':10,'serialized_lookup_fields':serialized_lookups,'lookup_assessment':{'serialized_storage':'VERIFIED: no serialized lookup dictionary fields in target tree; scalar m_FeatureLookupFlags belong to unchanged pair records, not a dictionary. Only the ligature record list is edited.','source':'VERIFIED: official pre4 clears/creates dictionary then appends records into first-component buckets in list order.','native':'VERIFIED: shipped InitializeDictionaryLookupTables calls InitializeLigatureSubstitutionLookupDictionary (WO004 bounded listing).','game_rebuild_semantics':'INFERRED from schema/native call/source agreement; exact fork initializer internal execution remains UNKNOWN. No serialized lookup entry to patch.','ordering':'VERIFIED source: records tested in list order; first successful replacement wins, no automatic longest-match sort. VERIFIED data: no existing first118 bucket, so no competing prefix/shadow regardless of append position.'},'verification':{'all_output_bundles_reloaded':True,'localization_text_assets':len(loc_before),'localization_segments_compared':segment_count,'changed_localization':changes,'raw_object_diffs':diffs,'target_only_one_record_delta':True,'previous_nine_records_unchanged':True,'embedded_font_sha256':digest(actualfont),'object_hashes':object_hashes,'protected_before':before,'protected_after':after,'protected_unchanged':True},'expected_outcomes':outcomes,'negative_result_limits':['UNKNOWN live liga gating; m_enableKerning=1 does not prove liga enabled. No flags changed.','UNKNOWN actual fallback, lookup initialization/refresh, runtime import/override or text preprocessing.','UNKNOWN dynamic atlas/font loading despite existing source glyph and standalone L5; visible L5 is required, not assumed.','UNKNOWN exact TMP package/fork. Negative result does not prove serialized ligatures unsupported globally.'],'source_evidence':[{'path':str((source_dir/n).relative_to(R)),'sha256':sha(source_dir/n)} for n in ['package.json','TMP_FontAsset.cs','TMP_FontFeatureTable.cs','TMPro_UGUI_Private.cs']]+[{'path':'local/review/sara-am-004/native/TMPro.TMP_FontAsset.InitializeDictionaryLookupTables.asm.txt','sha256':sha(R/'local/review/sara-am-004/native/TMPro.TMP_FontAsset.InitializeDictionaryLookupTables.asm.txt')}],'limits':'Diagnostic executor probe only, not a ต่ำ fix. Build/offline verification only. No install, game launch, runtime WO/dispatch, commit or push. Existing frozen005/001a/b and installed originals unchanged.'}
with (OUT/'manifest.json').open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2)
cmd=[sys.executable,str(R/'tools/manage_probe.py'),'check','--probe',OUT.name]
check=subprocess.run(cmd,cwd=R,capture_output=True,text=True,check=True)
manager=json.loads(check.stdout)
assert manager['action']=='check' and len(manager['files'])==3 and all(x['state']=='original' for x in manager['files'])
report['manager_check']={'label':'VERIFIED','command':'python tools/manage_probe.py check --probe '+OUT.name,'result':manager}
assert snapshot(protected)==before
with REPORT.open('x',encoding='utf-8') as f:json.dump(report,f,ensure_ascii=False,indent=2)
doc='''# WO-SARA-AM-005 — Ligature executor probe build

2026-10-26 (Asia/Bangkok). **BUILD_READY — ready for PM acceptance only.**

**VERIFIED:** built `local/prototype/probe-sara-am-lig-001` from frozen `fresh-translation-005` using exclusive creation. No install, game launch, screen operation, runtime WO, dispatch, commit or push. BUG-THAI-003 remains OPEN; this is a deliberately wrong sentinel substitution, not a fix.

## Specification and checks

**VERIFIED:** only `I2LS_Levels` segment533 (`Levels/Freshleigh/Level_Intro_Text`) changes in localisation, reusing the accepted001a diagnostic binding. Exact labelled specimen text and Unicode values are in the manifest/report. Five lines:

```text
L1: ต่ำ
L2: ต้ำ
L3: ค่ำ
L4: ตา ถี่
L5: ก
```

**VERIFIED:** target TMP−1239755799206566947 gains exactly one `m_LigatureSubstitutionRecords` entry, `m_ComponentGlyphIDs=[118,42,82]`, `m_LigatureGlyphID=29`. Existing font cmap maps ก/U+0E01 to29, different-tone ต้ำ to[118,47,82], and ค has a different base ID (full mapping recorded by build checks). ก is a distinct existing consonant; no glyph artwork/metrics/cmap/atlas edit. **INFERRED:** L5 makes the same glyph an explicit ordinary-text loading/reference control. **UNKNOWN:** actual atlas population/visibility until runtime; L5 is evidence only if QA sees it.

**VERIFIED — conflicts/order:** all nine original ligatures retained exactly, none starts118; consequently there is no matching first-glyph bucket/prefix that can shadow this new record. Official pre4 source `TMP_FontAsset.cs:InitializeLigatureSubstitutionLookupDictionary` clears/creates a nonserialized dictionary then adds list records to buckets keyed by first component. `TMPro_UGUI_Private.cs:LIGATURES` traverses records in order, first successful match wins; no automatic longest-match sorting. No competing118 record means order is immaterial for this probe. This is verified source behavior, not a verified shipped package identity.

**VERIFIED — lookup storage:** target serialized tree contains no lookup dictionary fields, and feature table stores only five record lists. Existing scalar m_FeatureLookupFlags in pair records are flags, not serialized dictionaries, and remain unchanged. No serialized dictionary entry exists to update. Shipped native initializer calls `InitializeLigatureSubstitutionLookupDictionary` (retained WO004 bounded listing). **INFERRED:** lookup rebuild from list is the intended path. **UNKNOWN:** exact custom initializer internals/live execution; absence of exact unwind bounds was not bypassed with guessed decoding. The unsafe serialized-lookup STOP condition was not encountered. Source/package hashes retained in build JSON; game package version remains UNKNOWN.

**VERIFIED — structural PASS:** reloaded every output bundle; localisation TextAsset names/segment counts identical except533 and exact five-line codepoints; fonts raw object bytes change only target TMP; removing the added record makes its complete type tree equal baseline; count9→10, previous9 unchanged. Embedded font object raw bytes and embedded font SHA256 `f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0` unchanged. UI/prefab bundle byte-identical. All bundle and changed-object hashes, protected before/after hashes (frozen005,001a/b, three installed bundles, binary and metadata) are in `reports/sara-am-lig-001-build.json` and candidate manifest. Installed files were checked original/original/original by manager check; no install/restore action executed.

## Expected observations — all runtime NOT_RUN

{TABLE}

## Interpretation and risks

**INFERRED:** positive evidence requires L1 visibly replaced by a single ก-shaped glyph matching L5 while L2–L4 remain intact. This supports the exact target-sequence executor in this modal context only, not correct Thai shaping, all consumers, longest-match behavior or a production fix. Screenshot should preserve labels/negative controls and visible L5. Do not infer execution from bundle readback alone.

**UNKNOWN:** unchanged L1 may reflect liga disabled, different fallback, runtime lookup not initialized/refreshed, record override/import, preprocessing/alternative glyphs or atlas/font loading. Existing kerning flag does not establish liga; this probe intentionally changes no flags. Visible L5 narrows glyph availability but does not prove the ligature executor or target-font identity. A negative result is INCONCLUSIVE about global ligature support unless these gates are resolved. Blank/tofu/partial substitutions, unintended L2–L4 changes or crash are failure modes; screen/runtime behavior was not tested here. Three-component consumption may affect index/line-layout behavior, and the five-line specimen may clip; do not treat an unseen row as a negative test.

**VERIFIED — handoff boundary:** build/offline verification complete. Stop here for PM acceptance. Only PM may issue the later Antigravity runtime WO. Frozen005/001a/b and installed originals unchanged; no production wording/Unicode rewrite. This diagnostic must never ship as a fix. Any later rollback/install lifecycle is outside this WO.
'''
table='| Row | Ligature executes (INFERRED) | Does not execute (INFERRED) | Failure / uncertainty |\n|---|---|---|---|\n'
for x in outcomes:table+='| '+x['row']+' | '+x['executed']+' | '+x['not_executed']+' | '+x['failure']+' |\n'
with DOC.open('x',encoding='utf-8') as f:f.write(doc.replace('{TABLE}',table))
print(json.dumps({'status':report['status'],'probe':OUT.name,'protected_files_unchanged':len(before),'changed_localization':changes,'ligatures':10,'manager':manager},ensure_ascii=False))
