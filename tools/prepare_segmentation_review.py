"""Prepare opt-in experimental cut maps without changing translations or game assets."""
import hashlib
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'local/prototype/probe-013/tooltip-map.json'
OUT = ROOT / 'local/segmentation/SEGMENTATION-001'
sha = lambda data: hashlib.sha256(data).hexdigest()
records = {r['key'].split('/')[-1]: r for r in json.loads(SOURCE.read_text(encoding='utf-8'))}
# Controller proposals only; independent language review is required before building.
units = {
    'MSAASamples': [['เพิ่ม', 'จำนวน ', 'MSAA Samples', ' เพื่อ', 'ลด', 'รอยหยัก ',
                     'หรือ', 'ลด', 'จำนวน', 'ลง', 'เพื่อ', 'เพิ่ม', 'ประสิทธิภาพ', 'กราฟิก']],
    'WorldDetail': [['เลือก', 'ระดับ', 'รายละเอียด', 'โดยรวม', 'ของ', 'ฉาก'],
                    ['ระดับ', 'รายละเอียด', 'ฉาก', 'ที่', 'สูงขึ้น', 'จะ', 'คง', 'รายละเอียด', 'ไว้', 'ใน', 'ระยะมอง', 'ที่', 'ไกลขึ้น'],
                    ['เลือก', 'การตั้งค่า', 'ที่', 'ต่ำลง', 'เพื่อ', 'เพิ่ม', 'ประสิทธิภาพ', ' CPU ', 'และ', 'กราฟิก']],
}
protected = re.compile(r'\{[^{}]*\}|<[^<>]*>|\[i2[^\]]*\]|[A-Za-z0-9]+(?:[ /-][A-Za-z0-9]+)*')

def validate(text, cuts, expected_hash):
    if sha(text.encode()) != expected_hash:
        raise ValueError('Underlying source hash changed')
    if '\u200b' in text or cuts != sorted(set(cuts)):
        raise ValueError('Source already marked or cuts duplicate/unsorted')
    spans = [(m.start(), m.end()) for m in protected.finditer(text)]
    for cut in cuts:
        if type(cut) is not int or not 0 < cut < len(text):
            raise ValueError('Invalid Unicode-codepoint cut')
        if text[cut - 1].isspace() or text[cut].isspace():
            raise ValueError('Redundant or formatting-adjacent cut')
        if text[cut - 1] in 'เแโใไ' or unicodedata.category(text[cut]).startswith('M'):
            raise ValueError('Cut separates leading vowel or combining sequence')
        if any(start < cut < end for start, end in spans):
            raise ValueError('Cut inside token/tag/Latin-number run')
    marked = ''.join(('\u200b' if i in set(cuts) else '') + c for i, c in enumerate(text))
    if marked.replace('\u200b', '') != text:
        raise ValueError('Underlying equality failed')
    if re.findall(r'\{[^{}]*\}|<[^<>]*>|\[i2[^\]]*\]', marked) != re.findall(r'\{[^{}]*\}|<[^<>]*>|\[i2[^\]]*\]', text):
        raise ValueError('Token/tag sequence changed')
    return marked

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    proposals = []
    for key, lines in units.items():
        source = records[key]['thai']
        assert '\n'.join(''.join(line) for line in lines) == source
        cuts, offset = [], 0
        for line in lines:
            for unit in line[:-1]:
                offset += len(unit)
                if not source[offset - 1].isspace() and not source[offset].isspace():
                    cuts.append(offset)
            offset += len(line[-1]) + 1
        source_hash = sha(source.encode())
        marked = validate(source, cuts, source_hash)
        proposals.append({'key': records[key]['key'], 'text': source, 'source_sha256': source_hash,
                          'proposed_units_by_source_line': lines, 'cut_offsets_codepoints': cuts,
                          'marked_text': marked, 'linguistic_review': 'PENDING', 'runtime_status': 'NOT_RUN'})
    # Executed negative controls verify rejection, rather than only mirroring valid inputs.
    rejects = []
    fixtures = [('token', '{STAFF_COUNT_LIMIT}', [4]), ('rich_tag', '<color=red>คำ</color>', [4]),
                ('combining_mark', 'กี่', [1]), ('leading_vowel', 'เรียน', [1]),
                ('Latin_run', 'MSAA Samples', [2]), ('source_LF', 'ก\nข', [1]),
                ('duplicate_cut', 'กขค', [1, 1])]
    for name, text, cuts in fixtures:
        try:
            validate(text, cuts, sha(text.encode()))
        except ValueError:
            rejects.append(name)
        else:
            raise AssertionError('Unsafe cut accepted: ' + name)
    try:
        validate('กขค', [1], sha('กขง'.encode()))
    except ValueError:
        rejects.append('source_hash_mismatch')
    else:
        raise AssertionError('Source mutation accepted')
    token_text = records['CharacterLimits']['thai']
    assert validate(token_text, [], sha(token_text.encode())) == token_text
    package = {'batch': 'SEGMENTATION-001', 'source_map_sha256': sha(SOURCE.read_bytes()),
               'status': 'PROPOSAL_PENDING_INDEPENDENT_REVIEW', 'records': proposals,
               'limits': 'Experimental explicit maps only. No automatic tokenizer, game build, translation edit or production ZWSP.'}
    package_path = OUT / 'proposals.json'
    package_path.write_text(json.dumps(package, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    report = {'batch': package['batch'], 'records': len(proposals), 'proposal_sha256': sha(package_path.read_bytes()),
              'source_map_sha256': package['source_map_sha256'],
              'proposed_cut_counts': {p['key']: len(p['cut_offsets_codepoints']) for p in proposals},
              'negative_controls_rejected': rejects, 'CharacterLimits_identity_control': True,
              'linguistic_review': 'PENDING', 'runtime_status': 'NOT_RUN',
              'limits': 'Structural protection is not Thai word/compound segmentation approval; original translations untouched.'}
    (ROOT / 'reports/segmentation-001-preparation.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report))

if __name__ == '__main__':
    main()
