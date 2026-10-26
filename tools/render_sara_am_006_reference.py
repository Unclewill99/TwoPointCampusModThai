"""WO006 offline browser reference only. Inputs: new local reference.html.
Outputs: new reference.png, DOM/log/metadata in local/review/sara-am-006.
Isolated Chrome profile, exclusive outputs; no game/install/candidate mutation.
"""
from pathlib import Path
import subprocess,json,hashlib
from PIL import Image
R=Path(__file__).resolve().parents[1];D=R/'local/review/sara-am-006'
outputs=[D/n for n in ['reference.png','reference-dom.html','chrome-stderr.txt','browser-reference.json']]
assert not any(p.exists() for p in outputs)
profile=D/'chrome-profile';profile.mkdir(exist_ok=False)
chrome=Path('C:/Program Files/Google/Chrome/Application/chrome.exe')
args=[str(chrome),'--headless=new','--disable-gpu','--disable-background-networking','--disable-component-update','--disable-default-apps','--disable-sync','--metrics-recording-only','--no-first-run','--no-default-browser-check','--hide-scrollbars','--force-device-scale-factor=1','--window-size=1400,1250','--virtual-time-budget=2000','--user-data-dir='+str(profile.resolve()),'--screenshot='+str(outputs[0].resolve()),'--dump-dom',(D/'reference.html').resolve().as_uri()]
result=subprocess.run(args,capture_output=True,timeout=55)
outputs[1].open('xb').write(result.stdout);outputs[2].open('xb').write(result.stderr)
assert result.returncode==0 and outputs[0].exists()
dom=result.stdout.decode('utf-8');assert 'Font loaded: baseline=true, probe=true' in dom and '<title>WO006_REFERENCE_READY</title>' in dom
assert Image.open(outputs[0]).size==(1400,1250)
meta={'label':'VERIFIED','browser':'Chrome155.0.8059.86 (executable ProductVersion checked separately)','css_font_px':64,'device_scale_factor':1,'image_dimensions':[1400,1250],'baseline_font_loaded':True,'probe_font_loaded':True,'new_glyph_outline_svg_rendered':True,'new_glyph_selected_by_browser_shaper':False,'text_context_shaped_by_browser':True,'returncode':result.returncode,'command':args,'reference_png_sha256':hashlib.sha256(outputs[0].read_bytes()).hexdigest(),'reference_dom_sha256':hashlib.sha256(result.stdout).hexdigest(),'limits':'SVG direct drawing of exact new glyph, because no cmap/browser GSUB alias is permitted; original text uses browser shaping. Neither route proves game FontEngine loading of glyph459.'}
outputs[3].open('x',encoding='utf-8').write(json.dumps(meta,indent=2));print(json.dumps(meta))
