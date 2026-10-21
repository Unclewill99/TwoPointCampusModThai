"""Read-only input/reference and evidence audit; never assigns a shaping PASS."""
import base64
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from PIL import Image
import UnityPy

ROOT = Path(__file__).resolve().parents[1]
sha = lambda path: hashlib.sha256(path.read_bytes()).hexdigest()
prototype = ROOT / 'local/prototype/probe-004'
manifest = json.loads((prototype / 'manifest.json').read_text(encoding='utf-8'))
map_path = prototype / 'diagnostic-map.json'
assert sha(map_path) == manifest['diagnostic_map_sha256']
mapping = json.loads(map_path.read_text(encoding='utf-8'))
case = next(row for row in mapping if row['case_id'] == 'CRP-VOWEL-02')
corpus = json.loads((ROOT / 'docs/qa/rendering-corpus.json').read_text(encoding='utf-8'))
full = next(row for row in corpus['items'] if row['id'] == case['case_id'])
groups = case['text'].split(' ')
assert groups == full['target_elements'] and len(groups) == 8
assert case['codepoints'] == [f'U+{ord(c):04X}' for c in case['text']]
assert case['text'] != full['text']
assert not any(c in case['text'] for c in ('\u200b', '\n', '\r', '\t'))

class ReferenceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.samples = []
    def handle_starttag(self, tag, attrs):
        if tag == 'p' and dict(attrs).get('class') == 'sample':
            self.inside = True
            self.samples.append('')
    def handle_endtag(self, tag):
        if tag == 'p':
            self.inside = False
    def handle_data(self, data):
        if self.inside:
            self.samples[-1] += data

reference = ROOT / 'local/qa/references/WO-VISUAL-005/exact-reference.html'
html = reference.read_text(encoding='utf-8')
parser = ReferenceParser()
parser.feed(html)
assert parser.samples[0] == case['text']
font_bytes = base64.b64decode(re.search(r'data:font/ttf;base64,([A-Za-z0-9+/=]+)', html)[1], validate=True)
font_hash = hashlib.sha256(font_bytes).hexdigest()
baseline = json.loads((ROOT / 'local/prototype/probe-003/manifest.json').read_text(encoding='utf-8'))
assert font_hash == baseline['matching_font_sha256']
font_file = next(item for item in manifest['files'] if item['name'] == 'fonts_assets_all.bundle')
assert sha(prototype / font_file['name']) == font_file['probe_sha256']
assert font_file['probe_sha256'] == next(item['probe_sha256'] for item in baseline['files'] if item['name'] == font_file['name'])
UnityPy.config.FALLBACK_UNITY_VERSION = '2020.3.47f1'
font_env = UnityPy.load(str(prototype / font_file['name']))
embedded = []
for obj in font_env.objects:
    if obj.type.name == 'Font':
        tree = obj.read_typetree()
        if hashlib.sha256(bytes(tree['m_FontData'])).hexdigest() == font_hash:
            embedded.append({'path_id': obj.path_id, 'name': tree['m_Name']})
assert embedded
localisation = next(item for item in manifest['files'] if item['name'].startswith('localisation_'))
assert sha(prototype / localisation['name']) == localisation['probe_sha256']
env = UnityPy.load(str(prototype / localisation['name']))
asset = next(obj.read() for obj in env.objects if obj.type.name == 'TextAsset' and obj.read().m_Name == case['asset'])
key, value = asset.m_Script.split('[i2t]')[case['segment_index']].split('=', 1)
assert key == case['key'] and value == case['text']

images = []
for relative in ['local/qa/WO-VISUAL-004/06-game-medium.jpg',
                 'local/qa/WO-VISUAL-004/07-controls-medium.jpg',
                 'local/qa/WO-VISUAL-004/08-controls-unclipped.jpg',
                 'local/qa/WO-VISUAL-004/16-controls-small.jpg',
                 'local/qa/WO-VISUAL-004/18-controls-large.jpg',
                 'local/qa/WO-VISUAL-004/31-restart-controls.jpg',
                 'local/qa/WO-VISUAL-005/03-exact-both.jpg']:
    path = ROOT / relative
    with Image.open(path) as img:
        images.append({'path': relative, 'width': img.width, 'height': img.height,
                       'format': img.format, 'sha256': sha(path)})
report = {'case': case['case_id'], 'date': '2026-10-18', 'key': key,
          'input_text': case['text'], 'groups': [{'text': text, 'codepoints': [f'U+{ord(c):04X}' for c in text]} for text in groups],
          'scope': 'Exact injected target-pair subset, not full lexical corpus sentences',
          'diagnostic_map_sha256': sha(map_path), 'reference_html_sha256': sha(reference),
          'embedded_font_sha256': font_hash, 'matching_game_font_objects': embedded,
          'source_reference_font_checks': 'PASS', 'existing_images': images,
          'runtime_shaping_status': 'PARTIAL; detailed ascender/upper-vowel evidence unresolved',
          'capture_feasibility': 'Current documented sky API has no raw/native-size, lossless, crop or quality option. Steam capture verified after activation, JPEG 1137x675; not evidence of current game capture resolution. Earlier game originals are JPEG 1920x1080.',
          'limits': 'No new game session, installation, image enlargement or shaping inference from font identity. Browser font bytes matching does not prove runtime font loading or identical shaping.'}
(ROOT / 'reports/vowel-02-evidence-audit.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps({'groups': len(groups), 'input_reference_font': 'PASS', 'matching_game_font_objects': len(embedded), 'shaping': 'PARTIAL'}))
