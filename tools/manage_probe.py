"""Guarded local probe installation. Default/check is read-only; restore checks hashes."""
import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
parser=argparse.ArgumentParser()
parser.add_argument('action',choices=['check','install','restore'],default='check',nargs='?')
parser.add_argument('--probe', choices=['probe-001','probe-002','probe-003','probe-004','probe-005-control','probe-005a','probe-005b','probe-007-short','probe-007-long','probe-008'], default='probe-001')
args=parser.parse_args()
probe=ROOT/'local/prototype'/args.probe
backup=ROOT/'local/backups'/args.probe
manifest=json.loads((probe/'manifest.json').read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
if args.action!='check':
    running=subprocess.run(['tasklist','/FI','IMAGENAME eq TPC.exe','/FO','CSV','/NH'],capture_output=True,text=True,check=True)
    if 'tpc.exe' in running.stdout.lower(): raise SystemExit('Close Campus before modifying files.')
plans=[]
for f in manifest['files']:
    name=f['name']
    if Path(name).name!=name: raise SystemExit('Unsafe manifest path')
    target=game/name; staged=probe/name; saved=backup/name
    if sha(staged)!=f['probe_sha256']: raise SystemExit('Staged hash mismatch: '+name)
    current=sha(target)
    if current not in [f['original_sha256'],f['probe_sha256']]: raise SystemExit('Unknown installed file; refusing overwrite: '+name)
    if saved.exists() and sha(saved)!=f['original_sha256']: raise SystemExit('Backup hash mismatch: '+name)
    if args.action=='install' and current==f['probe_sha256'] and not saved.exists(): raise SystemExit('Probe installed but original backup missing')
    if args.action=='restore' and current==f['probe_sha256'] and not saved.exists(): raise SystemExit('Original backup missing')
    plans.append((f,target,staged,saved,current))
if args.action=='install':
    backup.mkdir(parents=True,exist_ok=True)
    # Complete and verify every backup before changing either installed bundle.
    for f,target,staged,saved,current in plans:
        if not saved.exists(): shutil.copy2(target,saved)
        assert sha(saved)==f['original_sha256']
    try:
        for f,target,staged,saved,current in plans:
            shutil.copy2(staged,target)
            assert sha(target)==f['probe_sha256']
    except BaseException:
        for f,target,staged,saved,current in plans: shutil.copy2(saved,target)
        raise
elif args.action=='restore':
    for f,target,staged,saved,current in plans:
        if current==f['probe_sha256']:
            shutil.copy2(saved,target)
            assert sha(target)==f['original_sha256']
print(json.dumps({'action':args.action,'files':[{'name':f['name'],'state':'original' if sha(target)==f['original_sha256'] else 'probe'} for f,target,*_ in plans]}))
