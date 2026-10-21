import ctypes
from ctypes import wintypes
import time
import sys
from pathlib import Path
from PIL import Image, ImageGrab

u = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

u.SetProcessDPIAware()

class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ('dx', wintypes.LONG),
        ('dy', wintypes.LONG),
        ('mouseData', wintypes.DWORD),
        ('dwFlags', wintypes.DWORD),
        ('time', wintypes.DWORD),
        ('dwExtraInfo', ctypes.c_size_t)
    ]

class INPUT(ctypes.Structure):
    class _I(ctypes.Union):
        _fields_ = [('mi', MOUSEINPUT)]
    _anonymous_ = ('_i',)
    _fields_ = [('type', wintypes.DWORD), ('_i', _I)]

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_WHEEL = 0x0800
MOUSEEVENTF_ABSOLUTE = 0x8000

def set_desktop():
    hdesk_default = u.OpenDesktopW('Default', 0, False, 0x01FF)
    if hdesk_default:
        u.SetThreadDesktop(hdesk_default)

def to_phys(x, y):
    sw = u.GetSystemMetrics(0)
    sh = u.GetSystemMetrics(1)
    scale_x = sw / 1920.0
    scale_y = sh / 1080.0
    return int(round(x * scale_x)), int(round(y * scale_y))

def send_mouse_event(flags, dx=0, dy=0, data=0):
    inp = INPUT()
    inp.type = 0
    inp.mi.dx = int(dx)
    inp.mi.dy = int(dy)
    inp.mi.mouseData = int(data)
    inp.mi.dwFlags = flags
    u.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

def move_mouse(x, y):
    set_desktop()
    px, py = to_phys(x, y)
    u.SetCursorPos(px, py)
    dx = int(round(px * 65535.0 / 3839.0))
    dy = int(round(py * 65535.0 / 2159.0))
    send_mouse_event(MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_MOVE, dx, dy)
    time.sleep(0.05)

def click(x, y):
    set_desktop()
    move_mouse(x, y)
    time.sleep(0.15)
    send_mouse_event(MOUSEEVENTF_LEFTDOWN)
    time.sleep(0.08)
    send_mouse_event(MOUSEEVENTF_LEFTUP)
    time.sleep(0.2)

def scroll_wheel(x, y, amount):
    set_desktop()
    move_mouse(x, y)
    time.sleep(0.15)
    send_mouse_event(MOUSEEVENTF_WHEEL, data=amount)
    time.sleep(0.5)

def grab_screen(save_path):
    set_desktop()
    img = ImageGrab.grab()
    if img.size != (1920, 1080):
        img_resized = img.resize((1920, 1080), Image.Resampling.LANCZOS)
    else:
        img_resized = img
    Path(save_path).parent.mkdir(parents=True, exist_ok=True)
    img_resized.save(save_path, 'JPEG', quality=92)
    return img_resized

def hover_and_capture(x, y, save_path, hold_sec=1.8):
    set_desktop()
    move_mouse(x, y)
    time.sleep(hold_sec)
    return grab_screen(save_path)

def find_tpc_window():
    set_desktop()
    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_int, wintypes.HWND, wintypes.LPARAM)
    found_hwnd = []
    def cb(hwnd, lparam):
        if u.IsWindowVisible(hwnd):
            length = u.GetWindowTextLengthW(hwnd)
            if length > 0:
                b = ctypes.create_unicode_buffer(length + 1)
                u.GetWindowTextW(hwnd, b, length + 1)
                t = b.value.lower()
                if 'campus' in t or 'two point' in t:
                    found_hwnd.append((hwnd, b.value))
        return 1
    proc = WNDENUMPROC(cb)
    u.EnumWindows(proc, 0)
    return found_hwnd

def activate_tpc():
    hwnds = find_tpc_window()
    if hwnds:
        hwnd = hwnds[0][0]
        u.ShowWindow(hwnd, 9)
        u.SetForegroundWindow(hwnd)
        time.sleep(0.5)
        return True
    return False
