"""Read-only source backup of Campus Cloud and local preferences; writes only project-local zip."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from datetime import datetime,timezone
import json,hashlib,ctypes
R=Path(__file__).resolve().parents[1]
source=Path.home()/'AppData/LocalLow/Two Point Studios/Two Point Campus'
# Reuse the existing read-only Windows process guard without executing manager actions.
import ast
from ctypes import wintypes
manager=ast.parse((R/'tools/manage_probe.py').read_text())
guard=next(n for n in manager.body if isinstance(n,ast.FunctionDef) and n.name=='campus_running')
exec(compile(ast.Module(body=[guard],type_ignores=[]),'<process-guard>','exec'))
if campus_running():raise SystemExit('Close Campus normally before taking save snapshot')
paths=sorted(p for p in (source/'Cloud').rglob('*') if p.is_file())
if (source/'localpreferences.json').is_file():paths.append(source/'localpreferences.json')
assert paths and any(p.suffix=='.csav' for p in paths)
out=R/'local/backups/gameplay-save-snapshots';out.mkdir(parents=True,exist_ok=True)
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');target=out/(stamp+'.zip');entries=[]
with ZipFile(target,'x',ZIP_DEFLATED) as z:
 for p in paths:
  relative=p.relative_to(source).as_posix();data=p.read_bytes();z.writestr(relative,data)
  entries.append({'relative_path':relative,'size':len(data),'sha256':hashlib.sha256(data).hexdigest()})
with ZipFile(target) as z:
 for f in entries:assert hashlib.sha256(z.read(f['relative_path'])).hexdigest()==f['sha256']
manifest={'backup':str(target.resolve()),'source':str(source),'files':entries,'verified':True,'source_modified':False}
(target.with_suffix('.json')).write_text(json.dumps(manifest,indent=2));print(json.dumps({'backup':str(target.resolve()),'files':len(entries),'verified':True}))
