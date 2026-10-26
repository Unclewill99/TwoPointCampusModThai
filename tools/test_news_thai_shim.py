"""Execute isolated generated shims against fake managed strings and callbacks.
Does not load or alter the game. Windows x64 ABI regression checks.
"""
import ctypes as c
import struct
from build_news_thai_001 import Asm, make_stub, DISCORD, MUSEUM, segmented, THAI_DISCORD, THAI_MUSEUM

kernel = c.WinDLL('kernel32', use_last_error=True)
kernel.VirtualAlloc.argtypes = [c.c_void_p, c.c_size_t, c.c_uint32, c.c_uint32]
kernel.VirtualAlloc.restype = c.c_void_p
kernel.VirtualFree.argtypes = [c.c_void_p, c.c_size_t, c.c_uint32]
memory = kernel.VirtualAlloc(None, 65536, 0x3000, 0x40)
assert memory
roots, observed = [], []


def managed(text):
    data = text.encode('utf-16le')
    buf = c.create_string_buffer(20 + len(data) + 2)
    struct.pack_into('<I', buf, 16, len(data) // 2)
    c.memmove(c.addressof(buf) + 20, data, len(data))
    roots.append(buf)
    return c.addressof(buf)


def decode(ptr):
    size = c.c_uint32.from_address(ptr + 16).value
    return c.string_at(ptr + 20, size * 2).decode('utf-16le')


@c.CFUNCTYPE(c.c_void_p, c.c_void_p)
def allocate(ptr):
    return managed(c.string_at(ptr).decode('utf-8'))


@c.CFUNCTYPE(None, c.c_void_p, c.c_void_p, c.c_void_p)
def setter(ui, text, method):
    observed.append((ui, decode(text) if text else None, method))


try:
    # Local absolute tail thunk keeps generated relative calls within +/-2 GiB.
    thunk = b'\x48\xb8' + struct.pack('<Q', c.cast(allocate, c.c_void_p).value) + b'\xff\xe0'
    c.memmove(memory, thunk, len(thunk))
    vtable = c.create_string_buffer(0x530)
    struct.pack_into('<Q', vtable, 0x518, c.cast(setter, c.c_void_p).value)
    roots.append(vtable)
    total = 0
    for index, mode in enumerate(['body', 'button', 'image']):
        start = memory + 0x1000 + index * 0x4000
        prefix = bytes.fromhex('48 8b 53 58') if mode == 'image' else b''
        maps = {'body': [(DISCORD, segmented(THAI_DISCORD)), (MUSEUM, segmented(THAI_MUSEUM))],
                'button': [('Discord', 'ดูเพิ่มเติม'), ('Two Point Museum', 'ดูเพิ่มเติม')],
                'image': [('Discord', 'file:///D:/test/banner.png')]}[mode]
        code, _ = make_stub(start + len(prefix), memory, maps, mode)
        c.memmove(start, prefix + code, len(prefix) + len(code))
        a = Asm(start - 256)
        a.emit('53 48 83 ec 20')
        if mode == 'image':
            a.emit('48 89 cb')  # rbx = News value pointer
        else:
            a.emit('4c 89 cb 49 8b 01')  # rbx = NewsData, rax = fake vtable
        a.rel('e8', start)
        if mode == 'image':
            a.emit('48 89 d0')
        a.emit('48 83 c4 20 5b c3')
        wrapper = a.finish()
        c.memmove(start - 256, wrapper, len(wrapper))
        call = c.CFUNCTYPE(c.c_void_p, c.c_void_p, c.c_void_p, c.c_void_p, c.c_void_p)(start - 256)
        for title in ['Discord', 'Two Point Museum', 'Unrelated news']:
            obj = c.create_string_buffer(128)
            struct.pack_into('<Q', obj, 0, c.addressof(vtable))
            struct.pack_into('<Q', obj, 0x28 if mode == 'image' else 0x38, managed(title))
            if mode == 'body':
                cases = [(DISCORD, segmented(THAI_DISCORD)), (MUSEUM, segmented(THAI_MUSEUM)),
                         ('Changed source message', 'Changed source message'), ('', ''), (None, None)]
            elif mode == 'button':
                cases = [('Learn More', 'ดูเพิ่มเติม' if title != 'Unrelated news' else 'Learn More'),
                         ('Changed label', 'Changed label')]
            else:
                cases = [('https://original.test/banner.png', 'file:///D:/test/banner.png' if title == 'Discord' else 'https://original.test/banner.png')]
            for source, expected in cases:
                ptr = managed(source) if source is not None else 0
                if mode == 'image':
                    struct.pack_into('<Q', obj, 0x58, ptr)
                    result = call(c.addressof(obj), 0, 0, 0)
                    actual = decode(result)
                else:
                    call(123, ptr, 456, c.addressof(obj))
                    ui, actual, method = observed[-1]
                    assert (ui, method) == (123, 456)
                assert actual == expected, (mode, title, source, actual, expected)
                total += 1
    print(f'PASS: {total} native shim cases; matched, unknown, empty/null and parameter preservation.')
finally:
    kernel.VirtualFree(memory, 0, 0x8000)
