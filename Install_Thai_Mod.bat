@echo off
setlocal
cd /d "%~dp0"
set "PROBE=fresh-translation-006"
set "TMPF=%TEMP%\tpc_thai_mod_check.txt"

where py >nul 2>nul
if %errorlevel%==0 (set "PY=py -3") else (
  where python >nul 2>nul
  if errorlevel 1 (
    echo [ERROR] Python 3 was not found. Install Python 3 first.
    goto :end
  )
  set "PY=python"
)
if not exist "tools\manage_probe.py" (
  echo [ERROR] tools\manage_probe.py not found. Run this file from the ThaiCampusMod folder.
  goto :end
)
if not exist "local\prototype\%PROBE%\manifest.json" (
  echo [ERROR] local\prototype\%PROBE%\manifest.json not found.
  goto :end
)
tasklist /fi "imagename eq TPC.exe" 2>nul | find /i "TPC.exe" >nul
if %errorlevel%==0 (
  echo [ERROR] Two Point Campus is running. Close the game completely, then run this file again.
  goto :end
)

echo Checking current game files...
%PY% tools\manage_probe.py check --probe %PROBE% > "%TMPF%" 2>&1
if errorlevel 1 (
  echo [ERROR] Check failed. Nothing was changed. Details:
  type "%TMPF%"
  echo.
  echo If the game was updated or verified by Steam, the original files may have changed.
  goto :end
)
set "HASPROBE=0"
set "HASORIG=0"
findstr /c:"probe" "%TMPF%" >nul && set "HASPROBE=1"
findstr /c:"original" "%TMPF%" >nul && set "HASORIG=1"

echo ============================================================
echo  Install Thai mod (%PROBE%)
echo ============================================================
if "%HASPROBE%"=="1" if "%HASORIG%"=="0" (
  echo The Thai mod is already installed. Nothing to do.
  goto :end
)
if "%HASPROBE%"=="1" (
  echo [ERROR] Game files are in a mixed state. Run Uninstall_Thai_Mod.bat first.
  goto :end
)
echo.
echo This will back up your save files, then replace 3 game bundle files.
echo The original files are backed up and can be restored with Uninstall_Thai_Mod.bat.
choice /c YN /m "Continue"
if errorlevel 2 (
  echo Cancelled. Nothing was changed.
  goto :end
)

echo.
echo [1/3] Backing up saves...
%PY% tools\backup_gameplay_saves.py
if errorlevel 1 (
  echo [ERROR] Save backup failed. Nothing was installed.
  goto :end
)
echo.
echo [2/3] Installing...
%PY% tools\manage_probe.py install --probe %PROBE%
if errorlevel 1 (
  echo [ERROR] Install failed. The tool restores the originals on copy failure; run Uninstall_Thai_Mod.bat to verify.
  goto :end
)
echo.
echo [3/3] Verifying...
%PY% tools\manage_probe.py check --probe %PROBE%
echo.
echo Done. All 3 files should show "probe". You can start the game now.
:end
echo.
pause
endlocal
