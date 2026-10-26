"""Package TWO POINT / เคาน์ตี as an independently reversible texture change."""
import hashlib
import json
from pathlib import Path

import UnityPy
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'local/prototype/county-logo-001'
SOURCE = ROOT / 'local/review/county-logo-001/TwoPointCounty-thai.png'
NAME = 'ui-art-mainmenu_assets_all.bundle'
PATH_ID = -3724424202125531811
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if (OUT / 'manifest.json').exists():
        raise SystemExit('Candidate already built; refusing overwrite.')
    original = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64' / NAME
    env = UnityPy.load(str(original))
    before = {o.path_id: o.get_raw_data() for o in env.objects}
    obj = next(o for o in env.objects if o.path_id == PATH_ID)
    texture = obj.read()
    assert texture.m_Name == 'TwoPointCounty_logo'
    assert (texture.m_Width, texture.m_Height) == (512, 186)
    logo = Image.open(SOURCE).convert('RGBA')
    assert logo.getchannel('A').getextrema() == (0, 255)
    expected = logo.resize((512, 186), Image.Resampling.LANCZOS)
    texture.set_image(expected, target_format=4, mipmap_count=1)
    texture.save()
    target = OUT / NAME
    target.write_bytes(env.file.save(packer='lz4'))
    loaded = UnityPy.load(str(target))
    after = {o.path_id: o.get_raw_data() for o in loaded.objects}
    assert before.keys() == after.keys()
    assert [key for key in before if before[key] != after[key]] == [PATH_ID]
    decoded = next(o for o in loaded.objects if o.path_id == PATH_ID).read().image.convert('RGBA')
    assert ImageChops.difference(expected, decoded).getbbox(alpha_only=False) is None
    decoded.save(OUT / 'county-logo-readback.png')
    report = {'candidate': 'county-logo-001', 'text': 'TWO POINT / เคาน์ตี',
              'source_sha256': sha(SOURCE), 'runtime': 'NOT_TESTED',
              'files': [{'name': NAME, 'original_sha256': sha(original), 'probe_sha256': sha(target),
                         'changed_object': PATH_ID, 'all_other_objects_identical': True,
                         'decoded_pixels_match_expected': True, 'size': [512, 186]}]}
    (OUT / 'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'reports/county-logo-001-build.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()
