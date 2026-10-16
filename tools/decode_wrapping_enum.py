"""Decode this build's v27 metadata enum defaults with strict layout/name checks."""
import hashlib,json,struct
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=(ROOT.parent/'TPC_Data/il2cpp_data/Metadata/global-metadata.dat').read_bytes()
assert struct.unpack_from('<II',p)==(0xFAB11BAF,27)
def table(word):
    offset,size=struct.unpack_from('<II',p,word*4)
    assert 0<=offset<=offset+size<=len(p)
    return offset,size
strings,ss=table(6);types,ts=table(40);fields,fs=table(24);defaults,ds=table(16);data,dsz=table(18)
assert ts%88==0 and fs%12==0 and ds%12==0
def string(i):
    assert 0<=i<ss
    end=p.index(b'\0',strings+i,strings+ss)
    return p[strings+i:end].decode('utf-8')
matches=[]
for i in range(ts//88):
    off=types+i*88
    name,namespace=struct.unpack_from('<ii',p,off)
    if string(name)=='TextWrappingModes' and string(namespace)=='TMPro':matches.append((i,off))
assert len(matches)==1
index,off=matches[0]
field_start=struct.unpack_from('<i',p,off+32)[0]
field_count=struct.unpack_from('<H',p,off+68)[0]
assert field_count==5
default_map={}
for pos in range(defaults,defaults+ds,12):
    field,type_index,data_index=struct.unpack_from('<iii',p,pos)
    if field_start<=field<field_start+field_count:
        assert field not in default_map
        assert 0<=data_index<=dsz-4
        default_map[field]={'type_index':type_index,'data_index':data_index,'value':struct.unpack_from('<i',p,data+data_index)[0]}
rows=[]
for field in range(field_start,field_start+field_count):
    ni,ti,token=struct.unpack_from('<iii',p,fields+field*12)
    name=string(ni)
    if name=='value__':assert field not in default_map;continue
    rows.append({'name':name,'field_index':field,'field_type_index':ti,'token':hex(token),**default_map[field]})
values={r['name']:r['value'] for r in rows}
assert values=={'NoWrap':0,'Normal':1,'PreserveWhitespace':2,'PreserveWhitespaceNoWrap':3}
r={'metadata_sha256':hashlib.sha256(p).hexdigest(),'metadata_version':27,'type':'TMPro.TextWrappingModes','type_index':index,
   'type_definition_size':88,'field_start':field_start,'field_count':field_count,'members':rows,
   'limits':'Build-specific static metadata layout with strict name/count/default checks; does not inspect runtime property assignment or compiled renderer behavior.'}
(ROOT/'reports/wrapping-enum-decoded.json').write_text(json.dumps(r,indent=2),encoding='utf-8')
print(json.dumps(values))
