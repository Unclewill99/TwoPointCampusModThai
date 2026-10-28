"""Build a radio probe: replace AudioClip FSB5 blobs in audio-radio_assets_english.bundle with externally
encoded FSB5 files (Vorbis from fsbankcl, see tools/fsb_vorbis_windows.py).

  python tools/build_radio_thai.py --probe radio-thai-001
      reads  local/review/radio-thai-001/fsb/<ClipName>.fsb   (one single-subsound FSB5 per clip)
      writes local/prototype/radio-thai-001/audio-radio_assets_english.bundle + manifest.json
             reports/radio-thai-001-build.json
  --header-tail original   copy bytes 28..60 of the ORIGINAL blob (flags/GUID) over the fsbankcl header
                           (default: keep fsbankcl header as-is)
  --force                  overwrite an existing candidate

Only AudioClip objects change (m_Length/m_Frequency/m_Channels of replaced clips, and every clip's
resource offset/size because the .resource blob is rebuilt). All other objects stay byte-identical.
Builds from the pristine original saved at local/backups/radio-original/ (sha 6566f540...).
"""
import argparse
import hashlib
import json
import struct
from pathlib import Path

import UnityPy
from UnityPy.streams import EndianBinaryReader

ROOT = Path(__file__).resolve().parents[1]
NAME = 'audio-radio_assets_english.bundle'
ORIGINAL_SHA = '6566f54008825a6b91b71c024a2950dc01a702830753463c63104d6bc44a4ebf'
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
FREQ = {0: 4000, 1: 8000, 2: 11000, 3: 11025, 4: 16000, 5: 22050, 6: 24000, 7: 32000, 8: 44100, 9: 48000, 10: 96000}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def parse_fsb5(b):
    magic, ver, nsamp, shdr, nametab, datasz, mode = struct.unpack('<4sIIIIII', b[:28])
    assert magic == b'FSB5', 'not an FSB5 file'
    assert nsamp == 1, f'expected 1 subsound, got {nsamp}'
    sh = struct.unpack('<Q', b[60:68])[0]
    freq = FREQ[(sh >> 1) & 15]
    ch = ((sh >> 5) & 1) + 1
    frames = sh >> 34
    return {'version': ver, 'mode': mode, 'freq': freq, 'channels': ch, 'frames': frames,
            'sample_header_size': shdr, 'name_table_size': nametab, 'data_size': datasz, 'total': len(b)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--probe', required=True)
    ap.add_argument('--header-tail', choices=['fsbankcl', 'original'], default='fsbankcl')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    probe = a.probe
    out = ROOT / 'local/prototype' / probe
    fsb_dir = ROOT / 'local/review' / probe / 'fsb'
    out.mkdir(parents=True, exist_ok=True)
    if (out / 'manifest.json').exists() and not a.force:
        raise SystemExit('Candidate already built; use --force to overwrite.')
    original = ROOT / 'local/backups/radio-original' / NAME
    assert sha(original) == ORIGINAL_SHA, 'pristine original bundle not found / hash mismatch'
    replace = {p.stem: p for p in sorted(fsb_dir.glob('*.fsb'))}
    assert replace, f'no .fsb in {fsb_dir}'
    env = UnityPy.load(str(original))
    before = {o.path_id: o.get_raw_data() for o in env.objects}
    bf = env.assets[0].parent
    res_key = next(k for k in bf.files if k.endswith('.resource'))
    old_res = bytes(bf.files[res_key].bytes)
    clips = [(o, o.read()) for o in env.objects if o.type.name == 'AudioClip']
    assert len(clips) == 342, len(clips)
    by_name = {d.m_Name for _, d in clips}
    unknown = [n for n in replace if n not in by_name]
    assert not unknown, f'fsb names not in bundle: {unknown}'
    order = sorted(clips, key=lambda t: t[1].m_Resource.m_Offset)
    new_res = bytearray()
    changed = {}
    for obj, d in order:
        r = d.m_Resource
        assert r.m_Source.endswith(res_key)
        blob = old_res[r.m_Offset:r.m_Offset + r.m_Size]
        assert blob[:4] == b'FSB5'
        if d.m_Name in replace:
            new = bytearray(replace[d.m_Name].read_bytes())
            info = parse_fsb5(new)
            if a.header_tail == 'original':
                new[28:60] = blob[28:60]
            orig_info = parse_fsb5(blob)
            changed[d.m_Name] = {'old_seconds': d.m_Length, 'new_seconds': info['frames'] / info['freq'],
                                 'old_bytes': len(blob), 'new_bytes': len(new), 'old': orig_info, 'new': info,
                                 'path_id': obj.path_id}
            assert info['mode'] == 15, f'{d.m_Name}: expected Vorbis (mode 15), got {info["mode"]}'
            d.m_Length = info['frames'] / info['freq']
            d.m_Frequency = info['freq']
            d.m_Channels = info['channels']
            d.m_CompressionFormat = 1
            blob = bytes(new)
        new_res += b'\0' * ((-len(new_res)) % 16)
        r.m_Offset = len(new_res)
        r.m_Size = len(blob)
        new_res += blob
        d.save()
    reader = EndianBinaryReader(bytes(new_res))
    reader.flags = bf.files[res_key].flags
    bf.files[res_key] = reader
    target = out / NAME
    target.write_bytes(bf.save(packer='lz4'))

    loaded = UnityPy.load(str(target))
    after = {o.path_id: o.get_raw_data() for o in loaded.objects}
    assert before.keys() == after.keys()
    diff = {k for k in before if before[k] != after[k]}
    audio_ids = {o.path_id for o in loaded.objects if o.type.name == 'AudioClip'}
    assert diff <= audio_ids, 'non-AudioClip object changed'
    decoded = {}
    for o in loaded.objects:
        if o.type.name == 'AudioClip':
            d = o.read()
            if d.m_Name in changed:
                try:
                    wav = next(iter(d.samples.values()))
                    decoded[d.m_Name] = {'fmod_decode_ok': True, 'wav_bytes': len(wav)}
                except Exception as e:  # FMOD could not decode the fsbankcl output
                    decoded[d.m_Name] = {'fmod_decode_ok': False, 'error': repr(e)[:200]}
    report = {'candidate': probe, 'runtime': 'NOT_TESTED', 'header_tail': a.header_tail,
              'replaced_count': len(changed), 'replaced': changed, 'decode_check': decoded,
              'audioclip_objects_rewritten': len(diff), 'non_audioclip_objects_identical': True,
              'files': [{'name': NAME, 'original_sha256': ORIGINAL_SHA, 'probe_sha256': sha(target),
                         'original_size': original.stat().st_size, 'probe_size': target.stat().st_size}]}
    (out / 'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'reports').mkdir(exist_ok=True)
    (ROOT / 'reports' / f'{probe}-build.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: report[k] for k in ('candidate', 'replaced_count', 'decode_check', 'files')}, indent=2))
    if not all(v['fmod_decode_ok'] for v in decoded.values()):
        print('WARNING: FMOD could not decode some replaced clips offline; do not install.')


if __name__ == '__main__':
    main()
