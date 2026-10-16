"""Same-key width-tag experiment plus unobscured exact-input reference. Local only."""
import hashlib
import html
import json
import re
from pathlib import Path
import UnityPy
ROOT=Path(__file__).resolve().parents[1]
base=ROOT/'local/prototype/probe-003'
bm=json.loads((base/'manifest.json').read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
for f in bm['files']:
    assert sha(base/f['name'])==f['probe_sha256']
    assert sha(ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'/f['name'])==f['original_sha256']
corpus=json.loads((ROOT/'docs/qa/rendering-corpus.json').read_text(encoding='utf-8'))
cases={r['id']:r['text'] for r in corpus['items']}
plain=cases['CRP-WRAP-01']*2
zwsp=(cases['CRP-WRAP-02']+'\u200b')*2
assert zwsp.replace('\u200b','')==plain
variants={'probe-005-control':('English spaced control','This is a controlled width test with ordinary spaces. '*8),
          'probe-005a':('Thai unmodified',plain),'probe-005b':('Thai ZWSP',zwsp)}
key='UI/Settings/Tooltips/Resolution'
UnityPy.config.FALLBACK_UNITY_VERSION='2020.3.47f1'
summaries=[]
for revision,(label,body) in variants.items():
    out=ROOT/'local/prototype'/revision;out.mkdir(parents=True,exist_ok=True)
    name='localisation_assets_localisationenglish.bundle'
    env=UnityPy.load(str(base/name))
    o=next(o for o in env.objects if o.type.name=='TextAsset' and o.read().m_Name=='I2LS_UI_Settings')
    d=o.read();parts=d.m_Script.split('[i2t]')
    indexes=[i for i,p in enumerate(parts) if p.split('=',1)[0]==key];assert len(indexes)==1
    i=indexes[0];text='<width=400>'+body+'</width>'
    assert '\n' not in text and '[i2t]' not in text
    parts[i]=key+'='+text;d.m_Script='[i2t]'.join(parts);d.save()
    (out/name).write_bytes(next(iter(env.files.values())).save())
    (out/'fonts_assets_all.bundle').write_bytes((base/'fonts_assets_all.bundle').read_bytes())
    def assets(e): return {o.read().m_Name:o.read().m_Script for o in e.objects if o.type.name=='TextAsset'}
    before=assets(UnityPy.load(str(base/name)));after=assets(UnityPy.load(str(out/name)))
    assert set(before)==set(after)
    for a in before:
        if a!='I2LS_UI_Settings':assert before[a]==after[a]
    old=before['I2LS_UI_Settings'].split('[i2t]');new=after['I2LS_UI_Settings'].split('[i2t]')
    assert len(old)==len(new)
    assert [n for n,(x,y) in enumerate(zip(old,new)) if x!=y]==[i]
    assert new[i]==key+'='+text
    diag={'label':label,'key':key,'text':text,'body':body,'width_tag':'<width=400>',
      'codepoints':['U+%04X'%ord(c) for c in text], 'zwsp_offsets':[n for n,c in enumerate(body) if c=='\u200b'],
      'status':'NOT_RUN','manual_newlines':0}
    (out/'diagnostic-map.json').write_text(json.dumps(diag,ensure_ascii=False,indent=2),encoding='utf-8')
    m={'probe':revision,'installed':False,'runtime_status':'NOT_RUN','only_changed_key':key,
       'font_identical_to_probe003':True,'diagnostic_map_sha256':sha(out/'diagnostic-map.json'),
       'limits':'Width tag and actual wrapping require control run. Same key is not proof of equal runtime bounds. Raw tags or differing measured widths invalidate controlled comparison.',
       'files':[{'name':f['name'],'original_sha256':f['original_sha256'],'probe_sha256':sha(out/f['name'])} for f in bm['files']]}
    (out/'manifest.json').write_text(json.dumps(m,indent=2),encoding='utf-8');summaries.append(m)
# Exact reference inputs matching the two partially compared probe-004 labels.
reference=ROOT/'local/qa/references/WO-VISUAL-005';reference.mkdir(parents=True,exist_ok=True)
source=(base/'same-font-reference.html').read_text(encoding='utf-8')
encoded=re.search(r'data:font/ttf;base64,([A-Za-z0-9+/=]+)',source).group(1)
exact=[('CRP-VOWEL-02 exact injected subset','ปิ ปี ปึ ปื ฝี ฟิ ปั ฟั'),('CRP-STACK-02 exact injected subset','พ่อ แม่ ช้า น่า ป้า กู้')]
page='''<!doctype html><meta charset="utf-8"><title>Exact Thai reference 005</title><style>@font-face{font-family:ProbeThai;src:url(data:font/ttf;base64,'''+encoded+''') format('truetype');font-weight:500}body{margin:28px;color:#111;background:#faf7ef;font-family:Arial}pre{white-space:pre-wrap}p.sample{font-family:ProbeThai;font-weight:500;font-size:48px;line-height:2.2}section{border-top:1px solid #aaa;padding:12px 0}</style><h1>Exact injected sequences — browser reference only</h1><pre id="evidence">Font loading pending</pre>'''
for label,text in exact:
    page+='<section><h2>'+html.escape(label)+'</h2><p class="sample">'+text+'</p><code>'+' '.join('U+%04X'%ord(c) for c in text)+'</code></section>'
page+='''<script>document.fonts.load('500 48px ProbeThai','ปิ พ่อ กู้').then(f=>{document.getElementById('evidence').textContent=JSON.stringify({family:'ProbeThai',loadCount:f.length,faces:f.map(x=>({family:x.family,status:x.status,weight:x.weight})),check:document.fonts.check('500 48px ProbeThai','ปิ พ่อ กู้')},null,2)}).catch(e=>document.getElementById('evidence').textContent=String(e))</script>'''
(reference/'exact-reference.html').write_text(page,encoding='utf-8')
(ROOT/'reports/probe-005-build.json').write_text(json.dumps({'variants':summaries,'same_key':key,'same_fonts':True,'tag_width_requested':400,'runtime_width_verified':False,'reference_exact_cases':2},indent=2),encoding='utf-8')
print(json.dumps({'variants_built':len(summaries),'changes_per_variant':1,'exact_reference_cases':2,'installed':False}))
