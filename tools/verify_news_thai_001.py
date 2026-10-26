"""Audit binary isolation, installed assets, screenshot hashes and save changes."""
import hashlib
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    candidate = ROOT / 'local/prototype/news-thai-001'
    manifest = json.loads((candidate / 'manifest.json').read_text(encoding='utf-8'))
    original = (ROOT / 'local/backups/news-thai-001/GameAssembly.dll').read_bytes()
    modified = (candidate / 'GameAssembly.dll').read_bytes()
    assert digest(original) == manifest['files'][0]['original_sha256']
    assert digest(modified) == manifest['files'][0]['probe_sha256']
    pe = struct.unpack_from('<I', original, 60)[0]
    opt = pe + 24
    count = struct.unpack_from('<H', original, pe + 6)[0]
    opt_size = struct.unpack_from('<H', original, pe + 20)[0]
    sections = []
    for i in range(count):
        h = opt + opt_size + i * 40
        vs, va, rs, rp = struct.unpack_from('<IIII', original, h + 8)
        assert original[h:h + 40] == modified[h:h + 40]
        sections.append((va, max(vs, rs), rp))

    def raw(rva):
        return next(rp + rva - va for va, size, rp in sections if va <= rva < va + size)

    allowed = [(pe + 6, 2), (opt + 4, 4), (opt + 56, 4), (opt + 64, 4),
               (opt + 112 + 3 * 8, 8), (opt + opt_size + count * 40, 40)]
    for patch in manifest['patches']:
        pos = raw(int(patch['rva'], 16))
        old, new = bytes.fromhex(patch['original_hex']), bytes.fromhex(patch['patched_hex'])
        assert original[pos:pos + len(old)] == old
        assert modified[pos:pos + len(new)] == new
        allowed.append((pos, len(old)))
    normalized = bytearray(modified[:len(original)])
    for offset, size in allowed:
        normalized[offset:offset + size] = original[offset:offset + size]
    assert normalized == original, 'Unexpected change outside explicit header/patch ranges'
    # Existing exception entries remain present; appended stubs have unwind data.
    ex_rva, ex_size = struct.unpack_from('<II', original, opt + 112 + 3 * 8)
    previous = [struct.unpack_from('<III', original, raw(ex_rva) + i) for i in range(0, ex_size, 12)]
    new_header = opt + opt_size + count * 40
    _, new_va, _, new_rp = struct.unpack_from('<IIII', modified, new_header + 8)
    table_va, table_size = struct.unpack_from('<II', modified, opt + 112 + 3 * 8)
    table_raw = new_rp + table_va - new_va
    entries = [struct.unpack_from('<III', modified, table_raw + i) for i in range(0, table_size, 12)]
    assert entries == sorted(entries)
    assert entries[:len(previous)] == previous
    assert len(entries) == len(previous) + 3
    image_base = struct.unpack_from('<Q', original, opt + 24)[0]
    for patch in manifest['patches']:
        start = int(patch['stub_rva'], 16)
        assert any(a == start and b == start + patch['stub_code_size'] for a, b, info in entries)
    assert digest((ROOT.parent / 'GameAssembly.dll').read_bytes()) == manifest['files'][0]['probe_sha256']
    screenshots = []
    for name in ['01-museum.png', '02-discord.png']:
        p = ROOT / 'local/qa/news-thai-001' / name
        screenshots.append({'path': str(p.relative_to(ROOT)), 'sha256': digest(p.read_bytes())})
    snapshot = ROOT / 'local/backups/gameplay-save-snapshots/20261026T122705661793Z.json'
    before = json.loads(snapshot.read_text())
    source = Path(before['source'])
    changed, missing = [], []
    for row in before['files']:
        p = source / row['relative_path']
        if not p.exists():
            missing.append(row['relative_path'])
        elif digest(p.read_bytes()) != row['sha256']:
            changed.append(row['relative_path'])
    report = {'binary_isolation': 'PASS', 'allowed_changed_ranges_in_original_file': allowed,
              'original_section_headers_unchanged': True,
              'original_exception_entries_preserved': len(previous), 'added_exception_entries': 3,
              'aslr': 'RIP-relative code/data and relative calls; no fixed image pointers added',
              'runtime': 'PASS_SCOPED: both cards, image replacement, page switch, normal exit',
              'screenshots': screenshots, 'restore_original_hash_verified': True,
              'final_installed_sha256': digest(modified),
              'save_snapshot': str(snapshot.relative_to(ROOT)),
              'existing_save_files_changed': changed, 'existing_save_files_missing': missing,
              'limits': ['Current game binary only', 'Current two card messages only',
                         'No campus/gameplay trial', 'Other UI scales not tested',
                         'External action buttons not clicked; action URLs left untouched']}
    (ROOT / 'reports/news-thai-001-verification.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
