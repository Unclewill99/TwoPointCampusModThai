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
echo  Uninstall Thai mod (restore original game files)
echo ============================================================
if "%HASPROBE%"=="0" (
  echo The original game files are already in place. Nothing to restore.
  goto :end
)
echo.
echo This will restore the original English bundle files from the local backup.
echo Your save files are not touched.
choice /c YN /m "Continue"
if errorlevel 2 (
  echo Cancelled. Nothing was changed.
  goto :end
)
echo.
echo Restoring...
%PY% tools\manage_probe.py restore --probe %PROBE%
if errorlevel 1 (
  echo [ERROR] Restore failed. See the message above. Do not start the game; ask for help.
  goto :end
)
echo.
echo Verifying...
%PY% tools\manage_probe.py check --probe %PROBE%
echo.
echo Done. All 3 files should show "original".
:end
echo.
pause
endlocal
