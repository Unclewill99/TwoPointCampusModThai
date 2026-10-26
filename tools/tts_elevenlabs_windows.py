r"""Generate Thai PA clips with ElevenLabs (online, paid/free tier). Run on Windows:

    (put your API key, one line, in local\secrets\elevenlabs.key  — never commit it)
    py -3 tools\tts_elevenlabs_windows.py --list-voices
    py -3 tools\tts_elevenlabs_windows.py --clips Tannoy_Calling_Janitor_BlockedToilets_1 --voice-id <id>
    py -3 tools\tts_elevenlabs_windows.py --all --voice-id <id>

Uses the same script file (local/review/tannoy-lines-thai.json) and pronunciation table
(local/review/tannoy-pronounce.json) as the Edge script. Optional per-clip emotion tags for v3-class
models live in local/review/tannoy-tags.json: {"Tannoy_X": "[sarcastic] "} is prepended to the text.
Output: local/review/tannoy-eleven-raw/<voice-id>/<clip>.mp3. Only urllib is used (no SDK needed).
"""
import argparse, json, os, sys, time, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINES = ROOT / 'local/review/tannoy-lines-thai.json'
PRONOUNCE = ROOT / 'local/review/tannoy-pronounce.json'
TAGS = ROOT / 'local/review/tannoy-tags.json'
KEYFILE = ROOT / 'local/secrets/elevenlabs.key'
API = 'https://api.elevenlabs.io/v1'


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
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        sys.exit(f'HTTP {e.code} on {path}: {e.read()[:500].decode("utf-8", "replace")}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--list-voices', action='store_true')
    ap.add_argument('--list-models', action='store_true')
    ap.add_argument('--clips', nargs='*', default=[])
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--voice-id', default=None)
    ap.add_argument('--model', default='eleven_v3')
    ap.add_argument('--stability', type=float, default=0.5)
    ap.add_argument('--similarity', type=float, default=0.75)
    ap.add_argument('--style', type=float, default=0.0)
    ap.add_argument('--speed', type=float, default=1.0)
    ap.add_argument('--tag', default='', help='text prepended to every line, e.g. "[sarcastic] "')
    ap.add_argument('--out', default=None)
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    key = api_key()
    if a.list_voices:
        for v in json.loads(request('/voices', key))['voices']:
            lab = v.get('labels') or {}
            print(f"{v['voice_id']}  {v['name']:<22} {lab.get('gender','')}/{lab.get('accent','')}/{lab.get('age','')}  {v.get('category','')}")
        return
    if a.list_models:
        for m in json.loads(request('/models', key)):
            langs = [l['language_id'] for l in m.get('languages', [])]
            print(f"{m['model_id']:<28} thai={'th' in langs}  {m.get('name','')}")
        return
    if not a.voice_id:
        sys.exit('--voice-id required (see --list-voices)')
    data = json.loads(LINES.read_text(encoding='utf-8'))['lines']
    table = json.loads(PRONOUNCE.read_text(encoding='utf-8')) if PRONOUNCE.exists() else {}
    tags = json.loads(TAGS.read_text(encoding='utf-8')) if TAGS.exists() else {}
    names = list(data) if a.all else a.clips
    if not names:
        sys.exit('give --clips NAME... or --all')
    out = Path(a.out) if a.out else ROOT / 'local/review/tannoy-eleven-raw' / a.voice_id
    out.mkdir(parents=True, exist_ok=True)
    done = 0
    for n in names:
        path = out / f'{n}.mp3'
        if path.exists() and not a.force:
            continue
        text = a.tag + tags.get(n, '') + respell(data[n], table)
        payload = {'text': text, 'model_id': a.model, 'language_code': 'th',
                   'voice_settings': {'stability': a.stability, 'similarity_boost': a.similarity,
                                      'style': a.style, 'use_speaker_boost': True, 'speed': a.speed}}
        audio = request(f'/text-to-speech/{a.voice_id}?output_format=mp3_44100_128', key, payload,
                        {'accept': 'audio/mpeg'})
        path.write_bytes(audio)
        done += 1
        print(f'{done}/{len(names)} {n}: {text}')
        time.sleep(0.3)
    print('done ->', out)


if __name__ == '__main__':
    main()
