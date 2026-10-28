"""Process ElevenLabs mp3 (local/review/radio-eleven-raw/<Character>/*.mp3) into game-ready WAV for the
radio bundle: trim leading/trailing silence, light "radio" tone (HPF 80 Hz, LPF 14 kHz, gentle compression),
loudness normalised to the original radio level (-14 LUFS integrated, -1 dBTP), PCM16 48 kHz,
mono for DJ speech clips (as in the original bundle) / stereo for music clips.

  python tools/radio_process.py --probe radio-thai-002 --character Felicity [--clips Host_Intro_1 ...]
      -> local/review/radio-thai-002/src/<clip>.wav  + loudness.json   (then fsbankcl -> fsb, then build)
Needs ffmpeg (VM or Windows). Multi-segment clips (<clip>__s<N>.mp3) are not joined here (R3).
"""
import argparse, json, re, subprocess, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURVEY = ROOT / 'local/audio/radio-survey-001/radio_survey.json'
TARGET_I, TARGET_TP = -14.0, -1.0
CHAIN = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.15,'
         'areverse,silenceremove=start_periods=1:start_threshold=-50dB:start_silence=0.25,areverse,'
         'adelay=120|120,apad=pad_dur=0.35,'
         'highpass=f=80,lowpass=f=14000,'
         'acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=2')


def measure(path):
    out = subprocess.run(['ffmpeg', '-nostats', '-i', str(path), '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                         capture_output=True, text=True).stderr
    tail = out[out.rfind('Summary:'):]
    g = lambda pat: float(re.search(pat, tail).group(1))
    return g(r'I:\s+(-?[\d.]+) LUFS'), g(r'Peak:\s+(-?[\d.]+) dBFS')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--probe', required=True)
    ap.add_argument('--character', required=True)
    ap.add_argument('--clips', nargs='*', default=None)
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    survey = json.loads(SURVEY.read_text(encoding='utf-8'))['clips']
    raw = ROOT / 'local/review/radio-eleven-raw' / a.character
    out = ROOT / 'local/review' / a.probe / 'src'
    out.mkdir(parents=True, exist_ok=True)
    files = sorted(raw.glob('*.mp3'))
    if a.clips:
        files = [f for f in files if f.stem in a.clips]
    report_path = out / 'loudness.json'
    report = json.loads(report_path.read_text(encoding='utf-8')) if report_path.exists() else {}
    for f in files:
        clip = f.stem
        if '__s' in clip or survey.get(clip, {}).get('kind') in ('voice_over_music', 'music_only'):
            print('skip (multi-segment / music bed -> R3):', clip); continue
        dst = out / f'{clip}.wav'
        if dst.exists() and not a.force:
            continue
        ch = survey.get(clip, {}).get('channels', 1)
        tmp = Path(tempfile.gettempdir()) / f'radio_{clip}.tmp.wav'
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(f), '-af', CHAIN, '-ar', '48000', '-ac', str(ch), str(tmp)], check=True)
        i, pk = measure(tmp)
        gain = TARGET_I - i
        if pk + gain > TARGET_TP:  # limiter handles the rest
            pass
        subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', str(tmp), '-af',
                        f'volume={gain:.2f}dB,alimiter=limit={10**(TARGET_TP/20):.4f}:attack=5:release=50:level=false',
                        '-ar', '48000', '-ac', str(ch), '-c:a', 'pcm_s16le', str(dst)], check=True)
        try:
            tmp.unlink()
        except OSError:
            pass
        i2, pk2 = measure(dst)
        dur = float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(dst)], capture_output=True, text=True).stdout.strip())
        report[clip] = {'lufs': i2, 'peak': pk2, 'seconds': round(dur, 2), 'orig_seconds': survey.get(clip, {}).get('seconds'),
                        'channels': ch, 'gain_db': round(gain, 2), 'character': a.character}
        print(f'{clip}: {i2:.1f} LUFS peak {pk2:.1f} dB  {dur:.1f}s (orig {survey.get(clip, {}).get("seconds")}s) ch={ch}')
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding='utf-8')
    print('->', out)


if __name__ == '__main__':
    main()
