"""Guarded install/check/restore of the independently reversible news shim."""
import argparse
import ast
import ctypes
from ctypes import wintypes
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', nargs='?', choices=['check', 'install', 'restore'], default='check')
    args = parser.parse_args()
    tree = ast.parse((ROOT / 'tools/manage_probe.py').read_text())
    guard = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'campus_running')
    exec(compile(ast.Module(body=[guard], type_ignores=[]), '<process-guard>', 'exec'), globals())
    if args.action != 'check' and campus_running():
        raise SystemExit('Close Campus before modifying files.')
    staged = ROOT / 'local/prototype/news-thai-001'
    manifest = json.loads((staged / 'manifest.json').read_text(encoding='utf-8'))
    row = manifest['files'][0]
    assert row['name'] == 'GameAssembly.dll'
    target = ROOT.parent / row['name']
    candidate = staged / row['name']
    backup = ROOT / 'local/backups/news-thai-001' / row['name']
    current = sha(target)
    assert sha(candidate) == row['probe_sha256'], 'Candidate hash mismatch'
    assert current in [row['original_sha256'], row['probe_sha256']], 'Unknown installed binary; refusing overwrite'
    if backup.exists():
        assert sha(backup) == row['original_sha256'], 'Backup hash mismatch'
    elif current == row['probe_sha256']:
        raise SystemExit('Patched binary installed but original backup missing')
    if args.action == 'install':
        assert sha(Path(manifest['banner'])) == manifest['banner_sha256'], 'Banner missing or changed'
        if not backup.exists():
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, backup)
            assert sha(backup) == row['original_sha256']
        if current != row['probe_sha256']:
            try:
                shutil.copy2(candidate, target)
                assert sha(target) == row['probe_sha256']
            except BaseException:
                shutil.copy2(backup, target)
                raise
    elif args.action == 'restore' and current == row['probe_sha256']:
        shutil.copy2(backup, target)
        assert sha(target) == row['original_sha256']
    result = {'action': args.action, 'candidate': 'news-thai-001',
              'state': 'original' if sha(target) == row['original_sha256'] else 'installed',
              'sha256': sha(target), 'utc': datetime.now(timezone.utc).isoformat()}
    if args.action != 'check':
        (ROOT / 'reports/news-thai-001-last-action.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
