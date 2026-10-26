"""Package the approved Thai logo; preserve other objects and decoded atlas pixels."""
import hashlib
import json
from pathlib import Path

import UnityPy
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
OUT = ROOT / 'local/prototype/thai-logo-001'
SOURCE = ROOT / 'local/review/thai-logo-001/TPC_Logo_THAI-preview-001.png'
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if (OUT / 'manifest.json').exists():
        raise SystemExit('Candidate already built; refusing to overwrite its provenance.')
    logo = Image.open(SOURCE).convert('RGBA')
    files = []
    specs = [
        ('ui-tpc-logos_assets_all.bundle', 5170340876847722712, [(0, 0, 512, 186)]),
        ('ui-frontend-art_assets_all.bundle', -3387433540026353637,
         [(1, 1, 1162, 422), (1, 1815, 512, 186)]),
    ]
    for name, path_id, regions in specs:
        source = GAME / name
        env = UnityPy.load(str(source))
        original = {o.path_id: o.get_raw_data() for o in env.objects}
        obj = next(o for o in env.objects if o.path_id == path_id)
        texture = obj.read()
        canvas = texture.image.convert('RGBA')
        expected = canvas.copy()
        for x, y, width, height in regions:
            expected.paste(logo.resize((width, height), Image.Resampling.LANCZOS), (x, y))
        # RGBA32 avoids lossy recompression changes to unrelated atlas regions.
        texture.set_image(expected, target_format=4, mipmap_count=1)
        texture.save()
        target = OUT / name
        target.write_bytes(env.file.save(packer='lz4'))
        loaded = UnityPy.load(str(target))
        after = {o.path_id: o.get_raw_data() for o in loaded.objects}
        assert original.keys() == after.keys()
        assert [key for key in original if original[key] != after[key]] == [path_id]
        decoded = next(o for o in loaded.objects if o.path_id == path_id).read().image.convert('RGBA')
        assert ImageChops.difference(expected, decoded).getbbox(alpha_only=False) is None
        for i, (x, y, width, height) in enumerate(regions):
            decoded.crop((x, y, x + width, y + height)).save(OUT / f'{source.stem}-readback-{i}.png')
        files.append({'name': name, 'original_sha256': sha(source), 'probe_sha256': sha(target),
                      'changed_object': path_id, 'regions_top_left': regions,
                      'all_other_objects_identical': True, 'decoded_pixels_match_expected': True})
    report = {'candidate': 'thai-logo-001', 'source_sha256': sha(SOURCE),
              'text': 'TWO POINT / แคมปัส', 'files': files,
              'runtime': 'NOT_TESTED', 'seasonal_logos': 'UNCHANGED'}
    (OUT / 'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'reports/thai-logo-001-build.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()
