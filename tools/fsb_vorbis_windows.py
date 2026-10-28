"""Encode WAV files to single-subsound FSB5 (Vorbis) with FMOD's fsbankcl.exe. Run on Windows.

Usage (PowerShell, from the ThaiCampusMod folder):
  python tools/fsb_vorbis_windows.py --probe radio-thai-001                 # all wav in local/review/<probe>/src -> local/review/<probe>/fsb
  python tools/fsb_vorbis_windows.py --probe radio-thai-001 --quality 60
  python tools/fsb_vorbis_windows.py --fsbankcl "C:\\Program Files\\FMOD SoundSystem\\FMOD Studio 2.03.08\\fsbankcl.exe" ...
  python tools/fsb_vorbis_windows.py --help-fsbankcl                         # just print fsbankcl's own help

fsbankcl ships with the FMOD Engine (API) package, NOT the FMOD Studio authoring app: fmod.com/download -> FMOD Engine -> Windows; it installs to "FMOD Studio API Windows/bin/fsbankcl.exe" (free download, fmod.com account required). Install it, then this script
looks in the usual install folders or takes --fsbankcl. One FSB per wav, same basename, Vorbis, source
sample rate/channels kept. Quality: original DJ clips are ~82-85 kbps mono, stings/ads ~250-280 kbps stereo;
start with --quality 60 and compare sizes (printed at the end) against local/audio/radio-survey-001/radio_survey.json.
"""
import argparse
import glob
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def find_fsbankcl(explicit):
    if explicit:
        return Path(explicit)
    pats = [r'C:\Program Files\FMOD SoundSystem\FMOD Studio *\fsbankcl.exe',
            r'C:\Program Files (x86)\FMOD SoundSystem\FMOD Studio *\fsbankcl.exe',
            r'C:\Program Files\FMOD SoundSystem\FMOD Studio API Windows\tools\fsbankcl.exe',
            r'C:\Program Files (x86)\FMOD SoundSystem\FMOD Studio API Windows\tools\fsbankcl.exe',
            r'C:\Program Files (x86)\FMOD SoundSystem\FMOD Studio API Windows\bin\fsbankcl.exe',
            r'C:\Program Files*\FMOD SoundSystem\*\tools\fsbankcl.exe',
            r'C:\Program Files*\FMOD SoundSystem\*\bin\fsbankcl.exe']
    hits = []
    for p in pats:
        hits += glob.glob(p)
    hits = sorted(hits)
    if not hits:
        sys.exit('fsbankcl.exe not found. Install the FMOD Engine (API) package for Windows from https://www.fmod.com/download (it installs ...\\FMOD Studio API Windows\\tools\\fsbankcl.exe) or pass --fsbankcl <path>.')
    return Path(hits[-1])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--probe', help='local/review/<probe>/src/*.wav -> local/review/<probe>/fsb/*.fsb')
    ap.add_argument('--src', help='explicit source folder of wav files (overrides --probe)')
    ap.add_argument('--out', help='explicit output folder (overrides --probe)')
    ap.add_argument('--quality', type=int, default=60, help='fsbankcl Vorbis quality 0-100 (default 60)')
    ap.add_argument('--fsbankcl', help='path to fsbankcl.exe')
    ap.add_argument('--help-fsbankcl', action='store_true')
    ap.add_argument('--extra', nargs=argparse.REMAINDER, help='extra args passed to fsbankcl verbatim')
    a = ap.parse_args()
    exe = find_fsbankcl(a.fsbankcl)
    print('fsbankcl:', exe)
    if a.help_fsbankcl:
        subprocess.run([str(exe), '-help'])
        return
    src = Path(a.src) if a.src else ROOT / 'local/review' / a.probe / 'src'
    out = Path(a.out) if a.out else ROOT / 'local/review' / a.probe / 'fsb'
    out.mkdir(parents=True, exist_ok=True)
    wavs = sorted(src.glob('*.wav'))
    if not wavs:
        sys.exit(f'no wav in {src}')
    report = {}
    for w in wavs:
        o = out / (w.stem + '.fsb')
        cmd = [str(exe), '-o', str(o), '-format', 'vorbis', '-quality', str(a.quality)] + (a.extra or []) + [str(w)]
        print(' '.join(cmd))
        r = subprocess.run(cmd, capture_output=True, text=True)
        print(r.stdout.strip()[-800:])
        if r.returncode != 0 or not o.exists():
            print(r.stderr.strip()[-800:])
            sys.exit(f'fsbankcl failed on {w.name} (exit {r.returncode}). Try --help-fsbankcl and adjust flags.')
        head = o.read_bytes()[:8]
        report[w.stem] = {'fsb_bytes': o.stat().st_size, 'wav_bytes': w.stat().st_size, 'magic': head[:4].decode('latin1'), 'quality': a.quality}
        print(f'  -> {o.name} {o.stat().st_size} bytes magic={head[:4]!r}')
    (out / '_encode_report.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
