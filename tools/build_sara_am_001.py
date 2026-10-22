"""Explicit diagnostic text + isolated missing mark-pair A/B; never installs."""
from pathlib import Path
import copy, hashlib, json
import UnityPy
import io
from fontTools.ttLib import TTFont
R=Path(__file__).resolve().parents[1]
base=R/'local/prototype/fresh-translation-005'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
m=json.loads((base/'manifest.json').read_text(encoding='utf-8'))
for f in m['files']:assert sha(base/f['name'])==f['probe_sha256']
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
diag='A: ต่ำ ถี่\nB: ต\u0e4d\u0e48\u0e32 ถี่\nC: ต\u0e48\u0e4d\u0e32 ถี่'
loc='localisation_assets_localisationenglish.bundle';font='fonts_assets_all.bundle'
e=UnityPy.load(str(base/loc));before={o.read().m_Name:o.read().m_Script for o in e.objects if o.type.name=='TextAsset'}
obj=next(o for o in e.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_Levels')
t=obj.read();parts=t.m_Script.split('[i2t]');assert parts[533].startswith('Levels/Freshleigh/Level_Intro_Text=')
parts[533]=parts[533].split('=',1)[0]+'='+diag;t.m_Script='[i2t]'.join(parts);t.save()
locbytes=next(iter(e.files.values())).save()
fenv=UnityPy.load(str(base/font));target=next(o for o in fenv.objects if o.path_id==-1239755799206566947)
old=target.read_typetree();new=copy.deepcopy(old)
audit=json.loads((R/'reports/sara-am-native-feature-audit.json').read_text())
assert audit['serialized_matching_records']==[] and len(audit['gpos_mark_to_mark'])==1
h=audit['gpos_mark_to_mark'][0]
source_bytes=next(bytes(o.read_typetree()['m_FontData']) for o in fenv.objects if o.type.name=='Font' and o.path_id==7716434233879021909)
assert hashlib.sha256(source_bytes).hexdigest()==audit['font_sha256']
assert old['m_FaceInfo']['m_PointSize']==30 and TTFont(io.BytesIO(source_bytes))['head'].unitsPerEm==1000
record={'m_BaseMarkGlyphID':59,'m_BaseMarkGlyphAnchorPoint':dict(zip(['m_XCoordinate','m_YCoordinate'],h['tmp_at_point30_base_anchor'])),'m_CombiningMarkGlyphID':42,'m_CombiningMarkPositionAdjustment':dict(zip(['m_XPositionAdjustment','m_YPositionAdjustment'],h['tmp_at_point30_mark_anchor']))}
new['m_FontFeatureTable']['m_MarkToMarkAdjustmentRecords'].append(record)
target.save_typetree(new);fontbytes=next(iter(fenv.files.values())).save()
outputs=[]
for suffix in ['a','b']:
    name='probe-sara-am-001'+suffix;out=R/'local/prototype'/name;out.mkdir(exist_ok=False)
    for f in m['files']:
        data=locbytes if f['name']==loc else fontbytes if suffix=='b' and f['name']==font else (base/f['name']).read_bytes()
        (out/f['name']).write_bytes(data)
    re=UnityPy.load(str(out/loc));after={o.read().m_Name:o.read().m_Script for o in re.objects if o.type.name=='TextAsset'}
    changes=[]
    assert before.keys()==after.keys()
    for asset in before:
        a,b=before[asset].split('[i2t]'),after[asset].split('[i2t]');assert len(a)==len(b)
        changes.extend((asset,i) for i,(x,y) in enumerate(zip(a,b)) if x!=y)
    assert changes==[('I2LS_Levels',533)]
    assert after['I2LS_Levels'].split('[i2t]')[533].split('=',1)[1]==diag
    if suffix=='b':
        re=UnityPy.load(str(out/font));actual=next(o.read_typetree() for o in re.objects if o.path_id==target.path_id)
        vals=actual['m_FontFeatureTable']['m_MarkToMarkAdjustmentRecords'];assert len(vals)==358
        restored=copy.deepcopy(actual);added=restored['m_FontFeatureTable']['m_MarkToMarkAdjustmentRecords'].pop()
        assert restored==old
        for key in ['m_BaseMarkGlyphID','m_CombiningMarkGlyphID']:assert added[key]==record[key]
        for key in ['m_BaseMarkGlyphAnchorPoint','m_CombiningMarkPositionAdjustment']:
            for k,v in record[key].items():assert abs(added[key][k]-v)<0.00001
    files=[dict(name=f['name'],original_sha256=f['original_sha256'],probe_sha256=sha(out/f['name'])) for f in m['files']]
    report=dict(probe=name,parent='fresh-translation-005',installed=False,runtime_status='NOT_RUN',files=files,diagnostic_text=diag,diagnostic_codepoints=[[f'U+{ord(c):04X}' for c in line] for line in diag.splitlines()],changed_localization=[['I2LS_Levels',533]],font_change='none' if suffix=='a' else 'One MarkToMark pair 59->42, source GPOS anchors at point30',added_record=None if suffix=='a' else record,limits='DIAGNOSTIC ONLY. Explicit temporary Unicode specimens in one intro record; not production translation. Actual modal binding/runtime effect unproven. No fix approval.')
    (out/'manifest.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8');outputs.append(report)
assert (R/'local/prototype/probe-sara-am-001a'/loc).read_bytes()==(R/'local/prototype/probe-sara-am-001b'/loc).read_bytes()
for f in m['files']:assert sha(base/f['name'])==f['probe_sha256']
(R/'reports/sara-am-001-build.json').write_text(json.dumps(outputs,indent=2,ensure_ascii=False),encoding='utf-8')
print('A/B reload checks passed; one diagnostic text record; B adds only exact mark pair; frozen 005 unchanged; no install.')
