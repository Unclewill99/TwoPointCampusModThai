"""Guarded local probe installation. Default/check is read-only; restore checks hashes."""
import argparse
import hashlib
import json
import shutil
import ctypes
from ctypes import wintypes
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
game=ROOT.parent/'TPC_Data/StreamingAssets/aa/StandaloneWindows64'
parser=argparse.ArgumentParser()
parser.add_argument('action',choices=['check','install','restore'],default='check',nargs='?')
parser.add_argument('--probe', choices=['probe-001','probe-002','probe-003','probe-004','probe-005-control','probe-005a','probe-005b','probe-007-short','probe-007-long','probe-008','probe-009','probe-010','probe-011','probe-012a','probe-012b'], default='probe-001')
args=parser.parse_args()
probe=ROOT/'local/prototype'/args.probe
backup=ROOT/'local/backups'/args.probe
manifest=json.loads((probe/'manifest.json').read_text(encoding='utf-8'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def campus_running():
    """Enumerate local processes directly; errors abort instead of assuming closure."""
    class Entry(ctypes.Structure):
        _fields_=[('dwSize',wintypes.DWORD),('cntUsage',wintypes.DWORD),
                  ('th32ProcessID',wintypes.DWORD),('th32DefaultHeapID',ctypes.c_size_t),
                  ('th32ModuleID',wintypes.DWORD),('cntThreads',wintypes.DWORD),
                  ('th32ParentProcessID',wintypes.DWORD),('pcPriClassBase',wintypes.LONG),
                  ('dwFlags',wintypes.DWORD),('szExeFile',wintypes.WCHAR*260)]
    kernel=ctypes.WinDLL('kernel32',use_last_error=True)
    kernel.CreateToolhelp32Snapshot.argtypes=[wintypes.DWORD,wintypes.DWORD]
    kernel.CreateToolhelp32Snapshot.restype=wintypes.HANDLE
    for name in ['Process32FirstW','Process32NextW']:
        fn=getattr(kernel,name);fn.argtypes=[wintypes.HANDLE,ctypes.POINTER(Entry)];fn.restype=wintypes.BOOL
    kernel.CloseHandle.argtypes=[wintypes.HANDLE];kernel.CloseHandle.restype=wintypes.BOOL
    handle=kernel.CreateToolhelp32Snapshot(2,0)
    if handle==ctypes.c_void_p(-1).value:raise ctypes.WinError(ctypes.get_last_error())
    try:
        entry=Entry();entry.dwSize=ctypes.sizeof(Entry)
        ok=kernel.Process32FirstW(handle,ctypes.byref(entry))
        if not ok:raise ctypes.WinError(ctypes.get_last_error())
        while ok:
            if entry.szExeFile.casefold()=='tpc.exe':return True
            ok=kernel.Process32NextW(handle,ctypes.byref(entry))
        error=ctypes.get_last_error()
        if error!=18:raise ctypes.WinError(error)
        return False
    finally:
        kernel.CloseHandle(handle)
if args.action!='check' and campus_running():
    raise SystemExit('Close Campus before modifying files.')
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
