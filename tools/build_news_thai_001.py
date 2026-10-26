"""Version-guarded, ASLR-safe local news text shim for two approved cards.

Only two TMP set_text call sites and the AddNews image argument are redirected.
No network, action URLs, account state, gameplay or source news records are changed.
"""
import hashlib
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'local/prototype/news-thai-001'
ORIGINAL = ROOT.parent / 'GameAssembly.dll'
BANNER = ROOT / 'local/review/news-thai-001/discord-banner-thai.png'
DISCORD = "Join our Discord community to share screenshots, stories, and more. There's even the occasional cheeky game leak..."
MUSEUM = ('Curate and manage incredible museums! Explore to discover amazing artifacts. '
          'Design and refine the layout, keep staff happy, guests entertained, '
          'donations plentiful... and children off the exhibits.')
THAI_DISCORD = 'มาร่วมชุมชน Discord ของเรา เพื่อแบ่งปันภาพหน้าจอ เรื่องราว และอีกมากมาย บางครั้งอาจมีแอบหลุดข้อมูลเกมให้รู้ก่อนใครด้วย…'
THAI_MUSEUM = 'จัดแสดงและบริหารพิพิธภัณฑ์สุดน่าทึ่ง! ออกสำรวจค้นหาวัตถุจัดแสดง ออกแบบและปรับผังให้ลงตัว ดูแลพนักงานให้มีความสุข ผู้เข้าชมให้สนุก เงินบริจาคให้ไหลมา… และอย่าให้เด็ก ๆ ปีนของจัดแสดง!'


def segmented(text):
    # Explicitly reviewed word boundaries for these two short, fixed messages.
    boundaries = {
        THAI_DISCORD: 'มา|ร่วม|ชุมชน Discord ของ|เรา เพื่อ|แบ่งปัน|ภาพ|หน้าจอ เรื่องราว และ|อีก|มากมาย บางครั้ง|อาจ|มี|แอบ|หลุด|ข้อมูล|เกม|ให้|รู้|ก่อน|ใคร|ด้วย…',
        THAI_MUSEUM: 'จัดแสดง|และ|บริหาร|พิพิธภัณฑ์|สุด|น่า|ทึ่ง! ออก|สำรวจ|ค้นหา|วัตถุ|จัดแสดง ออกแบบ|และ|ปรับ|ผัง|ให้|ลงตัว ดูแล|พนักงาน|ให้|มี|ความสุข ผู้|เข้าชม|ให้|สนุก เงิน|บริจาค|ให้|ไหล|มา… และ|อย่า|ให้|เด็ก ๆ ปีน|ของ|จัดแสดง!',
    }
    result = boundaries[text].replace('|', '\u200b')
    assert result.replace('\u200b', '') == text
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def align(n, a):
    return (n + a - 1) // a * a


class Asm:
    def __init__(self, rva):
        self.rva, self.code, self.labels, self.fixups = rva, bytearray(), {}, []

    def emit(self, hexcode):
        self.code += bytes.fromhex(hexcode)

    def label(self, name):
        assert name not in self.labels
        self.labels[name] = len(self.code)

    def rel(self, opcode, target):
        self.emit(opcode)
        self.fixups.append((len(self.code), target))
        self.code += b'\0' * 4

    def string_equals(self, text, failure):
        # Input RDX is a managed string, with length at 0x10 and UTF16 at 0x14.
        self.emit('48 85 d2')
        self.rel('0f 84', failure)
        self.emit('81 7a 10')
        self.code += struct.pack('<I', len(text.encode('utf-16le')) // 2)
        self.rel('0f 85', failure)
        data = text.encode('utf-16le')
        for i in range(0, len(data), 4):
            part = data[i:i + 4]
            if len(part) == 2:
                self.emit('66')
            self.emit('81 ba')
            self.code += struct.pack('<I', 0x14 + i) + part
            self.rel('0f 85', failure)

    def finish(self):
        for offset, target in self.fixups:
            dest = self.rva + self.labels[target] if isinstance(target, str) else target
            struct.pack_into('<i', self.code, offset, dest - (self.rva + offset + 4))
        return bytes(self.code)


def make_stub(rva, string_new, replacements, mode):
    a = Asm(rva)
    a.emit('48 83 ec 58')  # shadow space, saved parameters; stack aligned to 16
    # All nonvolatile registers are untouched. Volatile XMM values may be
    # clobbered at the original call sites already (set_text / AddImageRef).
    a.emit('48 89 4c 24 20 48 89 54 24 28 4c 89 44 24 30')
    a.emit('4c 89 4c 24 38 48 89 44 24 40')
    strings = []
    for i, (source, replacement) in enumerate(replacements):
        next_label = f'next{i}'
        if mode == 'image':
            a.emit('48 8b 53 28')  # News (value type), Title offset 0x28
        elif mode == 'button':
            a.emit('48 8b 53 38')  # NewsData (object), Title offset 0x38
        else:
            a.emit('48 8b 54 24 28')
        a.string_equals(source, next_label)
        if mode == 'button':
            a.emit('48 8b 54 24 28')
            a.string_equals('Learn More', next_label)
        a.rel('48 8d 0d', f'string{i}')
        a.rel('e8', string_new)
        a.emit('48 89 44 24 28')
        a.rel('e9', 'done')
        a.label(next_label)
        strings.append((f'string{i}', replacement.encode('utf-8') + b'\0'))
    a.label('done')
    a.emit('48 8b 4c 24 20 48 8b 54 24 28 4c 8b 44 24 30')
    a.emit('4c 8b 4c 24 38 48 8b 44 24 40 48 83 c4 58')
    if mode == 'image':
        a.emit('45 31 c0 c3')  # AddImageRef MethodInfo = null, return
    else:
        a.emit('ff a0 18 05 00 00')  # tailcall original TMP virtual setter
    code_end = len(a.code)
    for label, data in strings:
        a.label(label)
        a.code += data
    return a.finish(), code_end


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if (OUT / 'manifest.json').exists():
        raise SystemExit('Candidate already exists; refusing overwrite.')
    image = bytearray(ORIGINAL.read_bytes())
    assert hashlib.sha256(image).hexdigest() == 'e4276817dac20d34cd8b6d5a2b5dbc1f55b47575ee27c421a3130695cbd9b957', 'Unsupported game binary'
    pe = struct.unpack_from('<I', image, 60)[0]
    assert image[pe:pe + 4] == b'PE\0\0'
    count = struct.unpack_from('<H', image, pe + 6)[0]
    opt = pe + 24
    opt_size = struct.unpack_from('<H', image, pe + 20)[0]
    assert struct.unpack_from('<H', image, opt)[0] == 0x20b
    section_align, file_align = struct.unpack_from('<II', image, opt + 32)
    sections = []
    for i in range(count):
        h = opt + opt_size + i * 40
        vs, va, rs, rp = struct.unpack_from('<IIII', image, h + 8)
        sections.append((va, max(vs, rs), rp))

    def raw(rva):
        return next(rp + rva - va for va, size, rp in sections if va <= rva < va + size)

    export_rva, _ = struct.unpack_from('<II', image, opt + 112)
    e = raw(export_rva)
    names_count, funcs, names, ordinals = struct.unpack_from('<IIII', image, e + 24)
    exports = {}
    for i in range(names_count):
        name = struct.unpack_from('<I', image, raw(names) + i * 4)[0]
        pos = raw(name)
        name = image[pos:image.index(0, pos)].decode('ascii')
        ordinal = struct.unpack_from('<H', image, raw(ordinals) + i * 2)[0]
        exports[name] = struct.unpack_from('<I', image, raw(funcs) + ordinal * 4)[0]
    string_new = exports['il2cpp_string_new']
    new_rva = align(max(va + size for va, size, rp in sections), section_align)
    new_raw = align(len(image), file_align)
    content = bytearray()
    ranges, patches = [], []
    body_maps = []
    # Accept typographic punctuation variants, otherwise leave changed news alone.
    for source, translation in [(DISCORD, THAI_DISCORD), (MUSEUM, THAI_MUSEUM)]:
        for text in dict.fromkeys([source, source.replace("'", '’'), source.replace('...', '…'), source.replace("'", '’').replace('...', '…')]):
            body_maps.append((text, segmented(translation)))
    specs = [
        ('body', 0xAA5BED, bytes.fromhex('ff 90 18 05 00 00'), body_maps),
        ('button', 0xAA5C4B, bytes.fromhex('ff 90 18 05 00 00'),
         [('Discord', 'ดูเพิ่มเติม'), ('Two Point Museum', 'ดูเพิ่มเติม')]),
        ('image', 0xAA63C5, bytes.fromhex('48 8b 53 58 45 33 c0'),
         [('Discord', BANNER.resolve().as_uri())]),
    ]
    for mode, site, expected, replacements in specs:
        pos = raw(site)
        assert image[pos:pos + len(expected)] == expected, (mode, image[pos:pos + len(expected)].hex())
        content += b'\x90' * (align(len(content), 16) - len(content))
        start = new_rva + len(content)
        # Image hook replaces an argument load, so reproduce it before saving RDX.
        prefix = bytes.fromhex('48 8b 53 58') if mode == 'image' else b''
        code, end = make_stub(start + len(prefix), string_new, replacements, mode)
        content += prefix + code
        ranges.append((start, start + len(prefix) + end, len(prefix)))
        patched = b'\xe8' + struct.pack('<i', start - (site + 5)) + b'\x90' * (len(expected) - 5)
        image[pos:pos + len(expected)] = patched
        patches.append({'kind': mode, 'rva': hex(site), 'original_hex': expected.hex(),
                        'patched_hex': patched.hex(), 'stub_rva': hex(start),
                        'stub_code_size': len(prefix) + end})
    content += b'\0' * (align(len(content), 4) - len(content))
    entries = []
    for start, end, prefix_size in ranges:
        unwind_rva = new_rva + len(content)
        # Version 1, prolog size (optional mov + sub rsp), one ALLOC_SMALL(88).
        content += bytes([1, prefix_size + 4, 1, 0, prefix_size + 4, 0xA2, 0, 0])
        entries.append((start, end, unwind_rva))
    ex_rva, ex_size = struct.unpack_from('<II', image, opt + 112 + 3 * 8)
    assert ex_size % 12 == 0
    previous = [struct.unpack_from('<III', image, raw(ex_rva) + i) for i in range(0, ex_size, 12)]
    entries = sorted(previous + entries)
    table_rva = new_rva + len(content)
    content += b''.join(struct.pack('<III', *entry) for entry in entries)
    header = opt + opt_size + count * 40
    assert header + 40 <= min(rp for va, size, rp in sections if rp)
    assert not any(image[header:header + 40])
    header_data = struct.pack('<8sIIIIIIHHI', b'.thnews\0', len(content), new_rva,
                              align(len(content), file_align), new_raw, 0, 0, 0, 0, 0x60000020)
    image[header:header + 40] = header_data
    struct.pack_into('<H', image, pe + 6, count + 1)
    struct.pack_into('<I', image, opt + 4, struct.unpack_from('<I', image, opt + 4)[0] + align(len(content), file_align))
    struct.pack_into('<I', image, opt + 56, align(new_rva + len(content), section_align))
    struct.pack_into('<I', image, opt + 64, 0)  # PE checksum (not used for user DLLs)
    struct.pack_into('<II', image, opt + 112 + 3 * 8, table_rva, len(entries) * 12)
    image += b'\0' * (new_raw - len(image)) + content
    image += b'\0' * (align(len(image), file_align) - len(image))
    target = OUT / 'GameAssembly.dll'
    target.write_bytes(image)
    report = {'candidate': 'news-thai-001', 'files': [{'name': 'GameAssembly.dll',
               'original_sha256': sha(ORIGINAL), 'probe_sha256': sha(target)}],
              'banner': str(BANNER.resolve()), 'banner_sha256': sha(BANNER),
              'patches': patches, 'new_section_rva': hex(new_rva),
              'il2cpp_string_new_rva': hex(string_new), 'exception_entries_added': 3,
              'original_exception_entries_preserved': len(previous),
              'match_policy': 'Exact full body or exact card title; unmatched content passes through',
              'action_urls': 'UNCHANGED', 'runtime': 'NOT_TESTED',
              'translations': {'discord': THAI_DISCORD, 'museum': THAI_MUSEUM, 'button': 'ดูเพิ่มเติม'}}
    (OUT / 'manifest.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    (ROOT / 'reports/news-thai-001-build.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps({k: report[k] for k in ['candidate', 'files', 'patches']}, indent=2))


if __name__ == '__main__':
    main()
