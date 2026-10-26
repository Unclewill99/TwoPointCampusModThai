"""WO007 local font-evidence browser sheet; no game. Reads new reference.html;
creates new1700px PNG,DOM,stderr,metadata and isolated profile exclusively.
"""
from pathlib import Path
import subprocess,json,hashlib
from PIL import Image
R=Path(__file__).resolve().parents[1];D=R/'local/review/sara-am-007'
outputs=[D/n for n in ['reference.png','reference-dom.html','chrome-stderr.txt','browser-reference.json']];assert not any(p.exists() for p in outputs)
profile=D/'chrome-profile';profile.mkdir(exist_ok=False)
args=['C:/Program Files/Google/Chrome/Application/chrome.exe','--headless=new','--disable-gpu','--disable-background-networking','--disable-component-update','--disable-default-apps','--disable-sync','--metrics-recording-only','--no-first-run','--no-default-browser-check','--hide-scrollbars','--force-device-scale-factor=1','--window-size=1400,1700','--virtual-time-budget=2000','--user-data-dir='+str(profile.resolve()),'--screenshot='+str(outputs[0].resolve()),'--dump-dom',(D/'reference.html').resolve().as_uri()]
r=subprocess.run(args,capture_output=True,timeout=55);outputs[1].open('xb').write(r.stdout);outputs[2].open('xb').write(r.stderr)
assert r.returncode==0 and outputs[0].exists();dom=r.stdout.decode('utf-8');assert 'Font loaded: baseline=true, probe=true' in dom and '<title>WO007_REFERENCE_READY</title>' in dom;assert Image.open(outputs[0]).size==(1400,1700)
m={'label':'VERIFIED_BROWSER_RENDER','browser':'Chrome155.0.8059.86 (local ProductVersion)','css_px':64,'device_scale_factor':1,'dimensions':[1400,1700],'baseline_loaded':True,'probe_loaded':True,'new_glyph_svg_count':dom.count('<svg '),'no_browser_glyph_selection_claim':True,'png_sha256':hashlib.sha256(outputs[0].read_bytes()).hexdigest(),'dom_sha256':hashlib.sha256(r.stdout).hexdigest(),'command':args,'limits':'Direct candidate outline drawing, original Unicode browser shaping, not game execution/packing/fit evidence.'};assert m['new_glyph_svg_count']==15
outputs[3].open('x',encoding='utf-8').write(json.dumps(m,indent=2));print(json.dumps(m))
