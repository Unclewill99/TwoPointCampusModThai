"""Probe tannoy-thai-004: tannoy-thai-003 (runtime PASS, loudness OK) with clips overridden from
local/review/tannoy-thai-004/ (ElevenLabs eleven_v4, voice George JBFqnCBsd6RMkjVDRZzb, tag [sarcastic]; PA effect, -15 LUFS).
Base clips stay in local/review/tannoy-thai-003/; only files present in the 004 folder are replaced.

Only AudioClip objects change (the replaced clips' format/length, and every clip's
resource offset/size because the .resource blob is rebuilt). All other objects are
byte-identical. Verification decodes the new clips back through FMOD (UnityPy samples).
"""
import hashlib
import json
import struct
import wave
from pathlib import Path

import UnityPy
from UnityPy.streams import EndianBinaryReader

ROOT = Path(__file__).resolve().parents[1]
PROBE = 'tannoy-thai-004'
ORIGINAL_SHA = '39d1997baa450d6cdcffae8802b23350e88cacf765810529dca7863f2fb209c3'
OUT = ROOT / 'local/prototype' / PROBE
BASE = ROOT / 'local/review/tannoy-thai-003'
OVER = ROOT / 'local/review/tannoy-thai-004'


def clip_path(name):
    p = OVER / f'{name}.wav'
    return p if p.exists() else BASE / f'{name}.wav'


NAME = 'audio-tannoy_assets_english.bundle'
REPLACE = sorted(p.stem for p in BASE.glob('*.wav'))
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
SPOT = {'Tannoy_Calling_Janitor_BlockedToilets_1', 'Tannoy_Calendar_ClassStart_1', 'Tannoy_General_01', 'Tannoy_Weather_Rain_1', 'Tannoy_Colour_70',
        'Campus_Tannoy_Session1_Colour_Line_1', 'Tannoy_Visitor_Invader_1'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_wav(path):
    with wave.open(str(path), 'rb') as w:
        assert (w.getnchannels(), w.getsampwidth(), w.getframerate()) == (2, 2, 48000), path
        frames = w.getnframes()
        return w.readframes(frames), frames


def fsb5_pcm16(pcm, frames, template):
    """Build a single-subsound FSB5 (mode 2 = PCM16, 48 kHz stereo). Header tail copied from template."""
    pad = (-len(pcm)) % 32
    data = pcm + b'\0' * pad
    sample_header = struct.pack('<Q', (0) | (9 << 1) | (1 << 5) | (0 << 6) | (frames << 34))
    head = struct.pack('<4sIIIIII', b'FSB5', 1, 1, len(sample_header), 0, len(data), 2) + template[28:60]
    return head + sample_header + data


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if (OUT / 'manifest.json').exists():
        raise SystemExit('Candidate already built; refusing overwrite.')
    aa = ROOT.parent / 'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
    if not aa.exists():  # Claude's Linux VM mounts StreamingAssets separately
        aa = Path.home() / 'mnt/StreamingAssets/aa/StandaloneWindows64'
    original = aa / NAME
    if sha(original) != ORIGINAL_SHA:  # another tannoy probe is installed; build from the saved original
        original = ROOT / 'local/backups/tannoy-thai-001' / NAME  # pristine original saved by the first probe
    assert sha(original) == ORIGINAL_SHA, 'pristine original bundle not found'
    env = UnityPy.load(str(original))
    before = {o.path_id: o.get_raw_data() for o in env.objects}
    bf = env.assets[0].parent
    res_key = next(k for k in bf.files if k.endswith('.resource'))
    old_res = bytes(bf.files[res_key].bytes)
    clips = [(o, o.read()) for o in env.objects if o.type.name == 'AudioClip']
    assert len(clips) == 467
    by_name = {d.m_Name: d for _, d in clips}
    assert len(REPLACE) == 467 and all(n in by_name for n in REPLACE)
    # Rebuild resource in original offset order.
    order = sorted(clips, key=lambda t: t[1].m_Resource.m_Offset)
    new_res = bytearray()
    changed = {}
    for obj, d in order:
        r = d.m_Resource
        assert r.m_Source.endswith(res_key)
        blob = old_res[r.m_Offset:r.m_Offset + r.m_Size]
        assert blob[:4] == b'FSB5'
        if d.m_Name in REPLACE:
            pcm, frames = read_wav(clip_path(d.m_Name))
            blob = fsb5_pcm16(pcm, frames, blob)
            changed[d.m_Name] = {'old_seconds': d.m_Length, 'new_seconds': frames / 48000,
                                 'old_format': d.m_CompressionFormat, 'new_format': 0, 'path_id': obj.path_id}
            d.m_CompressionFormat = 0
            d.m_Length = frames / 48000
            d.m_Frequency = 48000
            d.m_Channels = 2
            d.m_BitsPerSample = 16
        new_res += b'\0' * ((-len(new_res)) % 16)
        r.m_Offset = len(new_res)
        r.m_Size = len(blob)
        new_res += blob
        d.save()
    reader = EndianBinaryReader(bytes(new_res))
    reader.flags = bf.files[res_key].flags
    bf.files[res_key] = reader
    target = OUT / NAME
    target.write_bytes(bf.save(packer='lz4'))

    # Verify: reload, structure + decode.
    loaded = UnityPy.load(str(target))
    after = {o.path_id: o.get_raw_data() for o in loaded.objects}
    assert before.keys() == after.keys()
    diff = {k for k in before if before[k] != after[k]}
    audio_ids = {o.path_id for o in loaded.objects if o.type.name == 'AudioClip'}
    assert diff <= audio_ids, 'non-AudioClip object changed'
    decoded_ok = {}
    control_ok = {}
    orig_env = UnityPy.load(str(original))
    orig_clips = {o.read().m_Name: o.read() for o in orig_env.objects if o.type.name == 'AudioClip'}
    for o in loaded.objects:
        if o.type.name != 'AudioClip':
            continue
        d = o.read()
        if d.m_Name in REPLACE and d.m_Name in SPOT:
            wav = next(iter(d.samples.values()))
            with wave.open(str(clip_path(d.m_Name)), 'rb') as w:
                src = w.readframes(w.getnframes())
            # FMOD decode of PCM16 returns a WAV; compare raw PCM payload.
            decoded_ok[d.m_Name] = src in wav
    assert all(decoded_ok.values()), decoded_ok
    report = {'candidate': PROBE, 'runtime': 'NOT_TESTED', 'replaced_count': len(changed),
              'seconds_total_new': round(sum(c['new_seconds'] for c in changed.values()), 1),
              'sources_sha256_of_list': hashlib.sha256(''.join(sha(clip_path(n)) for n in REPLACE).encode()).hexdigest(),
              'overridden_clips': sorted(p.stem for p in OVER.glob('*.wav')),
              'decoded_matches_source': decoded_ok, 'unchanged_controls_identical': control_ok,
              'audioclip_objects_rewritten': len(diff), 'non_audioclip_objects_identical': True,
              'files': [{'name': NAME, 'original_sha256': sha(original), 'probe_sha256': sha(target),
                         'original_size': original.stat().st_size, 'probe_size': target.stat().st_size}]}
    (OUT / 'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'reports' / f'{PROBE}-build.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True, indent=2))


if __name__ == '__main__':
    main()
