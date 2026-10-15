"""Read installed game data; emit metadata only, never modify game assets."""
import json
import re
from pathlib import Path
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
GAMES = {'campus': ROOT.parent, 'museum': ROOT.parent.parent / 'Two Point Museum'}
report = {}
for name, base in GAMES.items():
    data = base / ('TPC_Data' if name == 'campus' else 'TPM_Data')
    unity_version = re.search(rb'(?:20[12][0-9]|6000)\.[0-9]+\.[0-9]+[abfp][0-9]+', (data / 'globalgamemanagers').read_bytes()).group().decode()
    UnityPy.config.FALLBACK_UNITY_VERSION = unity_version
    meta = (data / 'il2cpp_data/Metadata/global-metadata.dat').read_bytes()
    strings = sorted(set(s.decode('ascii') for s in re.findall(rb'[ -~]{5,}', meta) if len(s) <= 200
                         if re.search(rb'thai|font|textmesh|localis|localiz|linebreak|shap', s, re.I)))
    entry = {'unity_version': unity_version, 'version': (base / 'version.txt').read_text().strip(), 'metadata_signals': strings,
             'bundles': len(list((data / 'StreamingAssets/aa/StandaloneWindows64').glob('*.bundle'))),
             'assets': {}}
    paths = [data / 'StreamingAssets/aa/catalog.bundle']
    if name == 'campus':
        paths += list((data / 'StreamingAssets/aa/StandaloneWindows64').glob('fonts*.bundle'))
        paths += list((data / 'StreamingAssets/aa/StandaloneWindows64').glob('localisation*english.bundle'))
    for path in paths:
        env = UnityPy.load(str(path))
        objects = []
        for obj in env.objects:
            record = {'path_id': obj.path_id, 'type': obj.type.name}
            try:
                parsed = obj.read()
                record['name'] = getattr(parsed, 'm_Name', '')
                if obj.type.name == 'TextAsset' and 'catalog' in path.name:
                    raw = parsed.m_Script
                    if isinstance(raw, bytes): raw = raw.decode('utf-8', errors='replace')
                    cat = json.loads(raw)
                    entry['catalog_keys'] = list(cat)
                    entry['catalog_relevant_ids'] = [s for s in cat.get('m_InternalIds', []) if re.search('thai|font|localis|localiz', s, re.I)]
            except Exception as exc:
                record['read_error'] = str(exc)[:250]
            objects.append(record)
        entry['assets'][str(path.relative_to(base))] = objects
    report[name] = entry
(ROOT / 'reports/initial-inspection.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({k: {'version': v['version'], 'bundles': v['bundles'], 'signals': len(v['metadata_signals']), 'catalog_ids': v.get('catalog_relevant_ids', [])[:25]} for k,v in report.items()}, indent=2))
