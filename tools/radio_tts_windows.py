r"""ElevenLabs TTS for the radio phase (run on Windows; key in local\secrets\elevenlabs.key).

    py -3 tools\radio_tts_windows.py --list-voices
    py -3 tools\radio_tts_windows.py --cast-samples                 # 1 short sample per candidate voice per character
    py -3 tools\radio_tts_windows.py --cast-samples --characters Felicity Hugh
    py -3 tools\radio_tts_windows.py --character Felicity --clips Host_Intro_1 Host_Intro_2
    py -3 tools\radio_tts_windows.py --character Felicity --all      # every clip whose speech is only that character
    py -3 tools\radio_tts_windows.py --character Felicity --all --dry-run   # count characters/credits, no API calls

Scripts: local/review/radio-lines-thai.json (segments per clip). Cast: local/review/radio-cast.json
(characters[].voice_id or voice_name, tag, settings; candidates[] = names or ids for --cast-samples).
Pronunciation respelling: local/review/tannoy-pronounce.json (shared with the PA set).
Output: local/review/radio-eleven-raw/<Character>/<clip>.mp3 (multi-segment clips: <clip>__s<N>.mp3 per
speech segment of that character). Samples: local/review/radio-cast-samples/<Character>/<voice name>.mp3
"""
import argparse, json, os, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINES = ROOT / 'local/review/radio-lines-thai.json'
CAST = ROOT / 'local/review/radio-cast.json'
PRONOUNCE = ROOT / 'local/review/tannoy-pronounce.json'
KEYFILE = ROOT / 'local/secrets/elevenlabs.key'
API = 'https://api.elevenlabs.io/v1'
CREDIT_PER_CHAR = 0.45  # measured on the PA set (eleven_v4)


def respell(text, table):
    for word, said in sorted(table.items(), key=lambda kv: -len(kv[0])):
        if not word.startswith('_'):
            text = text.replace(word, said)
    return text


def api_key():
    key = os.environ.get('ELEVENLABS_API_KEY') or (KEYFILE.read_text(encoding='utf-8').strip() if KEYFILE.exists() else '')
    if not key:
        sys.exit(f'No API key: put it in {KEYFILE} (one line) or set ELEVENLABS_API_KEY')
    return key


def request(path, key, data=None, headers=None):
    h = {'xi-api-key': key, 'accept': 'application/json'}
    if headers:
        h.update(headers)
    body = json.dumps(data).encode('utf-8') if data is not None else None
    if body is not None:
        h['content-type'] = 'application/json'
    req = urllib.request.Request(API + path, data=body, headers=h, method='POST' if body is not None else 'GET')
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f'HTTP {e.code} on {path}: {e.read()[:500].decode("utf-8", "replace")}')


def voices_by_name(key):
    out = {}
    for v in json.loads(request('/voices', key))['voices']:
        out[v['name'].lower()] = v
        out.setdefault(v['name'].split(' - ')[0].strip().lower(), v)  # "Sarah - Mature, ..." -> "sarah"
    return out


def resolve(ref, byname):
    """ref = voice id or voice name -> (id, name)"""
    if ref.lower() in byname:
        v = byname[ref.lower()]
        return v['voice_id'], v['name']
    for v in byname.values():
        if v['voice_id'] == ref:
            return v['voice_id'], v['name']
    sys.exit(f'voice not found in your account: {ref} (see --list-voices)')


def tts(key, voice_id, text, settings, model, out_path):
    payload = {'text': text, 'model_id': model, 'language_code': 'th',
               'voice_settings': {'stability': settings['stability'], 'similarity_boost': settings['similarity'],
                                  'style': settings.get('style', 0.0), 'use_speaker_boost': True,
                                  'speed': settings.get('speed', 1.0)}}
    if settings.get('seed') is not None:
        payload['seed'] = settings['seed']
    audio = request(f'/text-to-speech/{voice_id}?output_format=mp3_44100_128', key, payload, {'accept': 'audio/mpeg'})
    out_path.write_bytes(audio)


def sample_text(lines, character, max_chars=90, prefer=None):
    """First speech segment of this character (from the preferred clip if given), cut at a space near max_chars."""
    items = ([(prefer, lines[prefer])] if prefer in lines else []) + list(lines.items())
    for clip, v in items:
        for s in v['segments'] or []:
            if s['type'] == 'speech' and s['speaker'] == character and len(s['text']) > 30:
                t = s['text']
                if len(t) > max_chars:
                    cut = t.rfind(' ', 0, max_chars)
                    t = t[:cut if cut > 40 else max_chars]
                return t
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--list-voices', action='store_true')
    ap.add_argument('--cast-samples', action='store_true')
    ap.add_argument('--characters', nargs='*', default=None)
    ap.add_argument('--character', default=None)
    ap.add_argument('--clips', nargs='*', default=[])
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--model', default=None, help='override cast defaults.model')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    cast = json.loads(CAST.read_text(encoding='utf-8'))
    defaults = cast['defaults']
    lines = json.loads(LINES.read_text(encoding='utf-8'))['lines']
    table = json.loads(PRONOUNCE.read_text(encoding='utf-8')) if PRONOUNCE.exists() else {}
    model = a.model or defaults.get('model', 'eleven_v4')
    key = None if a.dry_run else api_key()
    if a.list_voices:
        for v in json.loads(request('/voices', key))['voices']:
            lab = v.get('labels') or {}
            print(f"{v['voice_id']}  {v['name']:<22} {lab.get('gender','')}/{lab.get('accent','')}/{lab.get('age','')}/{lab.get('description','')}  {v.get('category','')}")
        return
    byname = {} if a.dry_run else voices_by_name(key)
    if a.cast_samples:
        chars = a.characters or [c for c, v in cast['characters'].items() if not c.startswith('_') and v.get('candidates')]
        total = 0
        for c in chars:
            ch = cast['characters'][c]
            text = sample_text(lines, c, prefer=ch.get('sample_clip'))
            if not text:
                print(f'{c}: no sample line found'); continue
            text = ch.get('tag', '') + respell(text, table)
            out = ROOT / 'local/review/radio-cast-samples' / c
            out.mkdir(parents=True, exist_ok=True)
            for ref in ch.get('candidates', []):
                total += len(text)
                if a.dry_run:
                    print(f'{c:12s} {ref:14s} {len(text):4d} chars | {text}'); continue
                vid, vname = resolve(ref, byname)
                p = out / f"{vname.split(' - ')[0].strip()}.mp3"
                if p.exists() and not a.force:
                    print('skip', p); continue
                settings = dict(defaults, **ch.get('settings', {}))
                tts(key, vid, text, settings, model, p)
                print(f'{c:12s} {vname:14s} -> {p.name} | {text}')
                time.sleep(0.3)
        print(f'total chars {total} ≈ {total*CREDIT_PER_CHAR:.0f} credits')
        return
    if not a.character:
        sys.exit('give --character NAME with --clips/--all, or --cast-samples')
    ch = cast['characters'][a.character]
    ref = ch.get('voice_id') or ch.get('voice_name')
    if not ref:
        sys.exit(f'{a.character}: voice_id/voice_name not set in {CAST}')
    if a.all:
        names = [n for n, v in lines.items() if v['segments'] and any(s['type'] == 'speech' and s['speaker'] == a.character for s in v['segments'])]
    else:
        names = a.clips
    if not names:
        sys.exit('no clips')
    out = ROOT / 'local/review/radio-eleven-raw' / a.character
    out.mkdir(parents=True, exist_ok=True)
    settings = dict(defaults, **ch.get('settings', {}))
    total = 0; jobs = []
    for n in names:
        segs = [(i, s) for i, s in enumerate(lines[n]['segments']) if s['type'] == 'speech' and s['speaker'] == a.character]
        multi = len([s for s in lines[n]['segments'] if s['type'] == 'speech']) > 1
        for i, s in segs:
            p = out / (f'{n}__s{i}.mp3' if multi else f'{n}.mp3')
            text = ch.get('tag', '') + respell(s['text'], table)
            total += len(text); jobs.append((n, p, text))
    print(f'{len(jobs)} segments, {total} chars ≈ {total*CREDIT_PER_CHAR:.0f} credits, voice {ref}, model {model}')
    if a.dry_run:
        for n, p, text in jobs[:5]: print(' ', p.name, '|', text[:100])
        return
    vid, vname = resolve(ref, byname)
    done = 0
    for n, p, text in jobs:
        if p.exists() and not a.force:
            continue
        tts(key, vid, text, settings, model, p)
        done += 1
        print(f'{done}/{len(jobs)} {p.name} ({len(text)} chars)')
        time.sleep(0.3)
    print('done ->', out)


if __name__ == '__main__':
    main()
