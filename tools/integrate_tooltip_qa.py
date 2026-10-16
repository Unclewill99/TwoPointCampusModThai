"""Selected Controller editorial changes; new local revision only."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
rows=json.loads((ROOT/'local/translations/TOOLTIPS-001.th.json').read_text(encoding='utf-8'))
out=ROOT/'local/translations/TOOLTIPS-001.th.r2.json'
assert not out.exists(),'Refusing overwrite'
changes={
'FullScreenMode':('เลือกระหว่างโหมดเต็มหน้าจอ','เลือกโหมดการแสดงผล'),
'Resolution':('กำหนดความละเอียดของหน้าต่างเกม','กำหนดความละเอียดการแสดงผลของเกม'),
'WorldDetail':('เลือกระดับรายละเอียดโดยรวมของโลกในเกม\nรายละเอียดโลกที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น','เลือกระดับรายละเอียดโดยรวมของฉาก\nระดับรายละเอียดฉากที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น'),
'AmbientOcclusionModeQuality':('คุณภาพระดับสูงและสูงมากทำให้ภาพดูดีกว่า\nคุณภาพต่ำทำให้ภาพดูดีไม่เท่า','คุณภาพระดับสูงและสูงมากทำให้ภาพดูดีขึ้น\nคุณภาพระดับต่ำทำให้ภาพดูดีไม่เท่า'),
'AnimationSkinningQuality':('ใช้กระดูกมากขึ้นและภาพดูดีกว่า','ใช้กระดูกมากขึ้นและทำให้ภาพดูดีขึ้น'),
'QualityPresets':('พรีเซ็ตที่ต่ำลงลดคุณภาพกราฟิกเพื่อให้ประสิทธิภาพดีขึ้น','พรีเซ็ตระดับต่ำกว่าจะลดคุณภาพกราฟิกเพื่อให้ประสิทธิภาพดีขึ้น'),
'ShadowQuality':('ความละเอียดของเงาที่สูงขึ้นทำให้ดูคมชัดกว่า','ความละเอียดของเงาที่สูงขึ้นทำให้เงาดูคมชัดขึ้น'),
'MSAASamples':('หรือลดลงเพื่อเพิ่มประสิทธิภาพกราฟิก','หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก')}
done=[]
for r in rows:
 k=r['key'].split('/')[-1]
 if k in changes:
  a,b=changes[k];assert a in r['thai'];r['thai']=r['thai'].replace(a,b,1)
  r['controller_review_note']='Selected QA naturalness edit; runtime claims/flags remain unverified.';done.append(k)
assert len(done)==len(changes)
out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'changed_records':len(done),'source_unchanged':True}))
