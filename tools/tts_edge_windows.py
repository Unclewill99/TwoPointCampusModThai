"""Generate Thai PA clips with Microsoft Edge neural TTS (free, online). Run on Windows:

    py -3 -m pip install edge-tts
    py -3 tools\tts_edge_windows.py --clips Tannoy_Calling_Janitor_BlockedToilets_1
    py -3 tools\tts_edge_windows.py --all

Output: local/review/tannoy-edge-raw/<voice>/<clip>.mp3 (24 kHz). Claude post-processes (PA effect,
loudness to -15 LUFS, 48 kHz stereo PCM) and builds the bundle. Voices: th-TH-NiwatNeural (male),
th-TH-PremwadeeNeural (female). --rate/--pitch e.g. "-5%" / "-10Hz".
"""
import argparse, asyncio, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINES = ROOT / 'local/review/tannoy-lines-thai.json'
PRONOUNCE = ROOT / 'local/review/tannoy-pronounce.json'  # word -> phonetic respelling (audio only)


def respell(text, table):
    for word, said in sorted(table.items(), key=lambda kv: -len(kv[0])):
        if not word.startswith('_'):
            text = text.replace(word, said)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--clips', nargs='*', default=[])
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--voice', default='th-TH-NiwatNeural')
    ap.add_argument('--rate', default='+0%')
    ap.add_argument('--pitch', default='+0Hz')
    ap.add_argument('--out', default=None)
    ap.add_argument('--force', action='store_true', help='regenerate even if the file exists')
    a = ap.parse_args()
    # Tolerate bare numbers: --rate -20 -> -20%, --pitch -15 -> -15Hz
    if not a.rate.endswith('%'):
        a.rate = a.rate + '%'
    if not a.pitch.endswith('Hz'):
        a.pitch = a.pitch + 'Hz'
    a.rate = a.rate if a.rate[0] in '+-' else '+' + a.rate
    a.pitch = a.pitch if a.pitch[0] in '+-' else '+' + a.pitch
    try:
        import edge_tts
    except ImportError:
        sys.exit('edge-tts not installed: py -3 -m pip install edge-tts')
    data = json.loads(LINES.read_text(encoding='utf-8'))['lines']
    table = json.loads(PRONOUNCE.read_text(encoding='utf-8')) if PRONOUNCE.exists() else {}
    names = list(data) if a.all else a.clips
    if not names:
        sys.exit('give --clips NAME... or --all')
    out = Path(a.out) if a.out else ROOT / 'local/review/tannoy-edge-raw' / a.voice
    out.mkdir(parents=True, exist_ok=True)

    async def run():
        done = 0
        for n in names:
            text = respell(data[n], table)
            path = out / f'{n}.mp3'
            if path.exists() and not a.force:
                continue
            await edge_tts.Communicate(text, a.voice, rate=a.rate, pitch=a.pitch).save(str(path))
            done += 1
            print(f'{done}/{len(names)} {n}: {text}')
    asyncio.run(run())
    print('done ->', out)


if __name__ == '__main__':
    main()
