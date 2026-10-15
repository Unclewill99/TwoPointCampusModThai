"""Apply Controller's selected editorial changes into a new local-only revision."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
input_path = ROOT/'local/translations/PILOT-001.th.r2.json'
output_path = ROOT/'local/translations/PILOT-001.th.r3.json'
if output_path.exists():
    raise SystemExit('Refusing to overwrite existing r3')
rows = json.loads(input_path.read_text(encoding='utf-8'))
changes = {
    'UI/Settings/AudioLanuuage': ('ภาษาเสียง', 'ภาษาเสียงพากย์'),
    'UI/Settings/CameraShake': ('กล้องสั่น', 'การสั่นของกล้อง'),
}
class_keys = {'Advisor/Advisor_Favourite_Student_Class_Complete', 'Advisor/Advisor_Favourite_Student_Class_Risk'}
applied = []
for r in rows:
    if r['key'] in changes:
        before, after = changes[r['key']]
        assert r['thai'] == before
        r['thai'] = after
    elif r['key'] in class_keys:
        assert 'เรียนจบคาบเรียน:' in r['thai']
        r['thai'] = r['thai'].replace('เรียนจบคาบเรียน:', 'เรียนจบคาบ:')
    else:
        continue
    r['controller_review_note'] = 'Controller r3: selected independent QA naturalness edit; runtime fit remains untested.'
    applied.append(r['key'])
assert len(applied) == 4
output_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
print(json.dumps({'revision':'r3','changed_translations':len(applied),'keys':applied}))
