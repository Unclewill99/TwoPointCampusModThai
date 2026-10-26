"""WO-004 inputs: saved official Unity registry; HTTPS Unity package tarballs.
Outputs: new local/review/sara-am-004/official-packages and package evidence JSON.
Read-only to game/project inputs; no candidate build, game load, asset editing or installation.
Extracts only selected C# source and package.json to validated new paths; verifies registry SHA1.
"""
from pathlib import Path
import json, urllib.request, tarfile, io, hashlib
R=Path(__file__).resolve().parents[1]
base=R/'local/review/sara-am-004'
registry=json.loads((base/'unity-registry.json').read_bytes())
out=base/'official-packages';out.mkdir(exist_ok=False)
names={'package.json','TMP_FontAsset.cs','TMP_FontFeatureTable.cs','TMP_TextParsingUtilities.cs','TMPro_UGUI_Private.cs','TMP_Text.cs','TMP_Settings.cs','FontFeatureCommonGSUB.cs'}
report={'source':'https://packages.unity.com/com.unity.textmeshpro','packages':[],'shipped_package_version':{'label':'UNKNOWN','reason':'No shipped project packages-lock.json/package manifest binding found; package metadata verifies fetched sources only.'}}
for version in ['3.2.0-pre.4','3.2.0-pre.10']:
    meta=registry['versions'][version];dist=meta['dist']
    blob=urllib.request.urlopen(dist['tarball'],timeout=45).read()
    assert hashlib.sha1(blob).hexdigest()==dist['shasum']
    directory=out/version;directory.mkdir(exist_ok=False)
    files=[]
    with tarfile.open(fileobj=io.BytesIO(blob),mode='r:gz') as tar:
        for member in tar.getmembers():
            if not member.isfile() or Path(member.name).name not in names:continue
            name=Path(member.name).name;data=tar.extractfile(member).read()
            (directory/name).open('xb').write(data)
            files.append({'name':name,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)})
    package=json.loads((directory/'package.json').read_bytes())
    assert package['name']=='com.unity.textmeshpro' and package['version']==version
    report['packages'].append({'label':'VERIFIED','version':version,'tarball':dist['tarball'],'registry_sha1':dist['shasum'],'download_sha256':hashlib.sha256(blob).hexdigest(),'package_repository':package.get('repository'),'files':files})
(R/'reports/sara-am-004-package-evidence.json').open('x',encoding='utf-8').write(json.dumps(report,indent=2))
print(json.dumps({'verified_source_packages':[p['version'] for p in report['packages']],'shipped_package_version':'UNKNOWN'}))
