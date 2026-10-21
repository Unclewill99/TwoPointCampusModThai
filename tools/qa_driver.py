import ctypes
from ctypes import wintypes
import time
import sys
from pathlib import Path
from PIL import Image, ImageGrab

u = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

# Explicit pointer signatures avoid HWND/HANDLE truncation on 64-bit Windows.
u.GetForegroundWindow.restype = wintypes.HWND
u.IsWindowVisible.argtypes = [wintypes.HWND]
u.GetWindowThreadProcessId.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
u.GetWindowThreadProcessId.restype = wintypes.DWORD
u.ShowWindow.argtypes = [wintypes.HWND, ctypes.c_int]
u.SetForegroundWindow.argtypes = [wintypes.HWND]
u.GetWindowTextLengthW.argtypes = [wintypes.HWND]
u.GetWindowTextW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
kernel32.OpenProcess.argtypes = [wintypes.DWORD, wintypes.BOOL, wintypes.DWORD]
kernel32.OpenProcess.restype = wintypes.HANDLE
kernel32.QueryFullProcessImageNameW.argtypes = [wintypes.HANDLE, wintypes.DWORD, wintypes.LPWSTR, ctypes.POINTER(wintypes.DWORD)]
kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
EXPECTED_GAME_EXE = Path(__file__).resolve().parents[2] / 'TPC.exe'

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
    require_game_foreground()
    inp = INPUT()
    inp.type = 0
    inp.mi.dx = int(dx)
    inp.mi.dy = int(dy)
    inp.mi.mouseData = int(data)
    inp.mi.dwFlags = flags
    u.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))

def move_mouse(x, y):
    set_desktop()
    require_game_foreground()
    px, py = to_phys(x, y)
    sw, sh = u.GetSystemMetrics(0), u.GetSystemMetrics(1)
    if sw <= 1 or sh <= 1 or not (0 <= px < sw and 0 <= py < sh):
        raise RuntimeError('Pointer outside current primary display; refresh capture mapping')
    u.SetCursorPos(px, py)
    dx = int(round(px * 65535.0 / (sw - 1)))
    dy = int(round(py * 65535.0 / (sh - 1)))
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
    require_game_foreground()
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

def window_is_game_process(hwnd):
    """Match owning executable path, never a title substring; fail closed."""
    if not hwnd or not u.IsWindowVisible(hwnd):
        return False
    pid = wintypes.DWORD()
    if not u.GetWindowThreadProcessId(hwnd, ctypes.byref(pid)) or not pid.value:
        return False
    handle = kernel32.OpenProcess(0x1000, False, pid.value)
    if not handle:
        return False
    try:
        buffer = ctypes.create_unicode_buffer(32768)
        size = wintypes.DWORD(len(buffer))
        if not kernel32.QueryFullProcessImageNameW(handle, 0, buffer, ctypes.byref(size)):
            return False
        return str(Path(buffer.value).resolve()).casefold() == str(EXPECTED_GAME_EXE.resolve()).casefold()
    finally:
        kernel32.CloseHandle(handle)


def require_game_foreground():
    """Reject browser/report/screenshot overlays before pointer input/capture."""
    if not window_is_game_process(u.GetForegroundWindow()):
        raise RuntimeError('Foreground is not the verified TPC.exe window; no input sent')


def find_tpc_window():
    set_desktop()
    callback_type = ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    found_hwnd = []
    def cb(hwnd, lparam):
        if window_is_game_process(hwnd):
            length = u.GetWindowTextLengthW(hwnd)
            buffer = ctypes.create_unicode_buffer(length + 1)
            u.GetWindowTextW(hwnd, buffer, length + 1)
            found_hwnd.append((hwnd, buffer.value))
        return True
    callback = callback_type(cb)
    if not u.EnumWindows(callback, 0):
        raise ctypes.WinError()
    return found_hwnd


def activate_tpc():
    hwnds = find_tpc_window()
    if len(hwnds) != 1:
        return False
    hwnd = hwnds[0][0]
    u.ShowWindow(hwnd, 9)
    u.SetForegroundWindow(hwnd)
    time.sleep(0.5)
    return u.GetForegroundWindow() == hwnd and window_is_game_process(hwnd)
