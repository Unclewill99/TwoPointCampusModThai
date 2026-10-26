"""WO-004 read-only binary inspection. Inputs: GameAssembly.dll, existing symbol map,
Capstone DLL and decoder setup. Outputs: NEW local/review/sara-am-004/native only.
Does not launch, load executable code from the game, patch assets or build candidates.
"""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
# Reuse only the existing PE reader / validated Capstone setup, before its write loop.
source = (ROOT / 'tools/disassemble_tooltip_methods.py').read_text(encoding='utf-8')
sys.argv = [sys.argv[0]]
exec(compile(source.split('summary = []')[0], str(ROOT / 'tools/disassemble_tooltip_methods.py'), 'exec'))
destination = ROOT / 'local/review/sara-am-004/native'
destination.mkdir(exist_ok=False)
selected = ['TMPro.TMP_Settings::get_version', 'TMPro.TMP_TextParsingUtilities::IsBaseGlyph',
            'TMPro.TMP_FontAsset::InitializeDictionaryLookupTables',
            'TMPro.TMP_FontAsset::InitializeLigatureSubstitutionLookupDictionary',
            'TMPro.TMP_FontAsset::InitializeMarkToBaseAdjustmentRecordsLookupDictionary',
            'TMPro.TMP_FontAsset::InitializeMarkToMarkAdjustmentRecordsLookupDictionary']
result=[]
for address,file_offset,token,name in methods:
    if name not in selected: continue
    bound=next(((s,e) for s,e,_ in unwind if base+s==address),None)
    if not bound:
        result.append(dict(name=name,status='UNKNOWN_NO_EXACT_UNWIND_BOUND'));continue
    start,end=bound
    ranges=sorted(groups.get(start,[]))
    assert ranges and all(ranges[i][1]==ranges[i+1][0] for i in range(len(ranges)-1))
    end=ranges[-1][1]
    assert raw(start)==file_offset
    code=binary[file_offset:file_offset+end-start]
    array=ctypes.POINTER(Instruction)()
    n=capstone.cs_disasm(handle.value,code,len(code),address,0,ctypes.byref(array))
    assert sum(array[i].size for i in range(n))==len(code)
    lines=[];refs=[]
    for i in range(n):
        ins=array[i];op=ins.op_str.decode();mn=ins.mnemonic.decode();note=''
        rip=re.search(r'\[rip ([+-]) (0x[0-9a-f]+)\]',op)
        if rip:
            target=ins.address+ins.size+int(rip[2],16)*(1 if rip[1]=='+' else -1)
            refs.append(hex(target));note=' | RIP='+hex(target)
        if mn in ('call','jmp') and op.startswith('0x'):
            note=' | '+', '.join(symbols.get(int(op,16),[]))
        lines.append(f'{ins.address:016X} {mn:8} {op}{note}')
    capstone.cs_free(array,n)
    filename=name.replace('::','.')+'.asm.txt'
    (destination/filename).open('x',encoding='utf-8').write('\n'.join(lines)+'\n')
    result.append(dict(name=name,status='VERIFIED_STATIC_DISASSEMBLY',address=hex(address),end=hex(base+end),rip_references=refs,file=filename))
(destination/'index.json').open('x',encoding='utf-8').write(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
