"""Local-only native listings using validated PE unwind bounds and existing Capstone 4."""
import ctypes
import json
import struct
import re
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--extra-prefix', action='append', default=[])
args = parser.parse_args()
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'local/tools/native-inspection'
binary = (ROOT.parent / 'GameAssembly.dll').read_bytes()
pe = struct.unpack_from('<I', binary, 0x3c)[0]
assert binary[pe:pe + 4] == b'PE\0\0'
assert struct.unpack_from('<H', binary, pe + 4)[0] == 0x8664
count, opt_size = struct.unpack_from('<H', binary, pe + 6)[0], struct.unpack_from('<H', binary, pe + 20)[0]
optional = pe + 24
assert struct.unpack_from('<H', binary, optional)[0] == 0x20b
base = struct.unpack_from('<Q', binary, optional + 24)[0]
sections = []
for index in range(count):
    offset = optional + opt_size + index * 40
    size, rva, raw_size, raw = struct.unpack_from('<IIII', binary, offset + 8)
    sections.append((rva, max(size, raw_size), raw))
def raw(rva):
    return next(start + rva - address for address, size, start in sections if address <= rva < address + size)
exception_rva, exception_size = struct.unpack_from('<II', binary, optional + 112 + 3 * 8)
unwind = [struct.unpack_from('<III', binary, offset) for offset in range(raw(exception_rva), raw(exception_rva) + exception_size, 12)]
def unwind_root(entry):
    start, end, info = entry
    visited = set()
    while info not in visited:
        visited.add(info)
        offset = raw(info)
        flags = binary[offset] >> 3
        if not flags & 4:
            return start
        code_count = binary[offset + 2]
        chain_offset = offset + ((4 + code_count * 2 + 3) & ~3)
        start, end, info = struct.unpack_from('<III', binary, chain_offset)
    raise ValueError('Unwind cycle')
groups = {}
for entry in unwind:
    groups.setdefault(unwind_root(entry), []).append(entry)
symbols = {}
methods = []
for line in (OUT / 'methods.tsv').read_text(encoding='utf-8-sig').splitlines():
    address, file_offset, token, name = line.split('\t')
    address = int(address, 16)
    symbols.setdefault(address, []).append(name)
    methods.append((address, int(file_offset), token, name))
module_tables = {}
for line in (OUT / 'modules.tsv').read_text(encoding='utf-8-sig').splitlines():
    type_name, module_name, table_address, table_count = line.split('\t')
    module_tables[type_name] = (int(table_address, 16), int(table_count))
validated_pointers = 0
for address, file_offset, token, name in methods:
    type_name = name.split('::')[0]
    if type_name not in module_tables:
        continue
    table_address, table_count = module_tables[type_name]
    rid = int(token, 16) & 0xffffff
    assert 0 < rid <= table_count
    independent_pointer = struct.unpack_from('<Q', binary, raw(table_address - base) + (rid - 1) * 8)[0]
    assert independent_pointer == address, name
    assert raw(address - base) == file_offset, name
    validated_pointers += 1

class Instruction(ctypes.Structure):
    _fields_ = [('id', ctypes.c_uint), ('address', ctypes.c_uint64), ('size', ctypes.c_uint16),
                ('bytes', ctypes.c_ubyte * 16), ('mnemonic', ctypes.c_char * 32),
                ('op_str', ctypes.c_char * 160), ('detail', ctypes.c_void_p)]

dll_path = Path.home() / 'AppData/Local/Programs/Python/Python313/Lib/site-packages/TypeTreeGeneratorAPI/capstone.dll'
capstone = ctypes.CDLL(str(dll_path))
major, minor = ctypes.c_int(), ctypes.c_int()
capstone.cs_version(ctypes.byref(major), ctypes.byref(minor))
assert major.value == 4
capstone.cs_open.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_size_t)]
capstone.cs_disasm.argtypes = [ctypes.c_size_t, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_uint64, ctypes.c_size_t, ctypes.POINTER(ctypes.POINTER(Instruction))]
capstone.cs_disasm.restype = ctypes.c_size_t
capstone.cs_free.argtypes = [ctypes.POINTER(Instruction), ctypes.c_size_t]
capstone.cs_close.argtypes = [ctypes.POINTER(ctypes.c_size_t)]
handle = ctypes.c_size_t()
assert capstone.cs_open(3, 8, ctypes.byref(handle)) == 0
summary = []
for address, file_offset, token, name in methods:
    if not any(key in name for key in ('TPC.PreferencesPanelVideo::', 'TPC.TooltipSpawner::', 'TPC.TooltipManager::',
                                      'TPC.FrontendUI::UpdateCursor', 'TPS.Core.Input.InputManager::Update',
                                      'TPS.Core.Input.InputManager::OnPointer', 'TPS.Core.UI.UIButton::OnPointerEnter',
                                      'TPC.NavigableDropdown::OnPointerEnter') + tuple(args.extra_prefix)):
        continue
    bound = next(((start, end) for start, end, _ in unwind if base + start == address), None)
    if bound is None:
        summary.append({'name': name, 'address': hex(address), 'status': 'NO_EXACT_UNWIND_BOUND'})
        continue
    start, end = bound
    ranges = sorted(groups.get(start, []))
    assert ranges and ranges[0][0] == start
    assert all(ranges[i][1] == ranges[i + 1][0] for i in range(len(ranges) - 1))
    end = ranges[-1][1]
    assert raw(start) == file_offset
    code = binary[file_offset:file_offset + end - start]
    array = ctypes.POINTER(Instruction)()
    size = capstone.cs_disasm(handle.value, code, len(code), address, 0, ctypes.byref(array))
    decoded_bytes = sum(array[i].size for i in range(size))
    partial_decode = decoded_bytes != len(code)
    if partial_decode:
        assert any(name.startswith(prefix) for prefix in args.extra_prefix), (name, decoded_bytes, len(code))
    lines, calls = [], []
    for index in range(size):
        instruction = array[index]
        mnemonic, operands = instruction.mnemonic.decode(), instruction.op_str.decode()
        note = ''
        rip = re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]', operands)
        if rip:
            target = instruction.address + instruction.size + int(rip[2], 16) * (1 if rip[1] == '+' else -1)
            note = ' | RIP=' + hex(target)
            try:
                offset = raw(target - base)
                text = binary[offset:offset + 220].split(b'\0', 1)[0]
                if 4 <= len(text) < 220 and all(32 <= b < 127 for b in text):
                    note += ' ' + text.decode('ascii')
            except StopIteration:
                pass
        if mnemonic in ('call', 'jmp') and operands.startswith('0x'):
            target = int(operands, 16)
            note = ' | ' + ', '.join(symbols.get(target, []))
            calls.append({'address': hex(instruction.address), 'target': hex(target), 'symbols': symbols.get(target, [])})
        lines.append(f'{instruction.address:016X} {mnemonic:8} {operands}{note}')
    capstone.cs_free(array, size)
    filename = name.replace('::', '.').replace('/', '_').replace('<', '_').replace('>', '_') + '.asm.txt'
    (OUT / filename).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    summary.append({'name': name, 'token': token, 'address': hex(address), 'end': hex(base + end),
                    'decoded_bytes': decoded_bytes, 'unwind_ranges': len(ranges), 'partial_decode': partial_decode,
                    'instructions': size, 'calls': calls, 'local_listing': filename})
capstone.cs_close(ctypes.byref(handle))
(OUT / 'native-summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
selected = [row for row in summary if row['name'] in (
    'TPC.PreferencesPanelVideo::Awake', 'TPC.PreferencesPanelVideo::Show',
    'TPC.PreferencesPanelVideo::SyncGUIToCurrentSettings', 'TPC.PreferencesPanelVideo::RefreshDropDowns',
    'TPC.TooltipManager::OnUpdate', 'TPC.TooltipSpawner::CursorOver', 'TPC.TooltipSpawner::CursorOut')]
assert len(selected) == 7 and all('local_listing' in row for row in selected)
evidence = {'game_assembly_sha256': hashlib.sha256(binary).hexdigest(),
            'metadata_sha256': hashlib.sha256((ROOT.parent / 'TPC_Data/il2cpp_data/Metadata/global-metadata.dat').read_bytes()).hexdigest(),
            'capstone_version': [major.value, minor.value], 'independently_validated_method_pointers': validated_pointers,
            'methods': [{k: v for k, v in row.items() if k != 'calls'} for row in selected],
            'limits': 'Static native analysis. Full listings and global symbol maps stay local. Chained unwind ranges followed; full byte consumption checked. Shared code addresses may have multiple managed aliases.'}
(ROOT / 'reports/tooltip-native-inspection.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'mapped_methods': len(methods), 'listings': sum('local_listing' in row for row in summary)}))
