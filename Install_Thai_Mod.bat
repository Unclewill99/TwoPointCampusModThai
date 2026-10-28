@echo off
setlocal
cd /d "%~dp0"
rem Components installed, in order. Each is independent (different game files).
rem   fresh-translation-007  Thai text + fonts + UI  (3 bundles, manage_probe.py)
rem   thai-logo-001          TWO POINT CAMPUS Thai logo  (2 bundles, manage_probe.py)
rem   county-logo-001        TWO POINT COUNTY Thai logo (1 bundle,  manage_probe.py)
rem   news-thai-001          Thai news cards        (GameAssembly.dll, manage_news_thai.py)
rem   tannoy-thai-007        Thai PA announcements  (audio-tannoy bundle, manage_probe.py)
rem   radio-thai-008         Thai radio DJs         (audio-radio bundle,  manage_probe.py)
set "TRANSLATION=fresh-translation-007"
set "OLD_TRANSLATION=fresh-translation-006"
set "LOGOS=thai-logo-001 county-logo-001"
set "TANNOY=tannoy-thai-007"
set "OLD_TANNOY=tannoy-thai-006 tannoy-thai-005 tannoy-thai-004 tannoy-thai-003 tannoy-thai-002 tannoy-thai-001"
set "RADIO=radio-thai-008"
set "OLD_RADIO=radio-thai-007 radio-thai-006 radio-thai-005 radio-thai-004 radio-thai-003 radio-thai-002 radio-thai-001"
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
if not exist "tools\manage_news_thai.py" (
  echo [ERROR] tools\manage_news_thai.py not found.
  goto :end
)
for %%P in (%TRANSLATION% %LOGOS% news-thai-001 %TANNOY% %RADIO%) do (
  if not exist "local\prototype\%%P\manifest.json" (
    echo [ERROR] local\prototype\%%P\manifest.json not found.
    goto :end
  )
)
tasklist /fi "imagename eq TPC.exe" 2>nul | find /i "TPC.exe" >nul
if %errorlevel%==0 (
  echo [ERROR] Two Point Campus is running. Close the game completely, then run this file again.
  goto :end
)

echo ============================================================
echo  Install Thai mod
echo    translation %TRANSLATION%
echo    logos       %LOGOS%
echo    news cards  news-thai-001
echo    PA audio    %TANNOY%
echo    radio audio %RADIO%
echo ============================================================
echo Checking current game files...

rem --- Translation: detect an older 006 install that must be removed first ---
set "NEED_006_RESTORE=0"
%PY% tools\manage_probe.py check --probe %TRANSLATION% > "%TMPF%" 2>&1
if not errorlevel 1 goto :translation_ok
if not exist "local\prototype\%OLD_TRANSLATION%\manifest.json" goto :translation_fail
%PY% tools\manage_probe.py check --probe %OLD_TRANSLATION% > "%TMPF%" 2>&1
if errorlevel 1 goto :translation_fail
findstr /c:"\"probe\"" "%TMPF%" >nul
if errorlevel 1 goto :translation_fail
set "NEED_006_RESTORE=1"
echo Found older translation %OLD_TRANSLATION% installed. It will be replaced by %TRANSLATION%.
goto :translation_checked

:translation_fail
%PY% tools\manage_probe.py check --probe %TRANSLATION% > "%TMPF%" 2>&1
echo [ERROR] Translation check failed. Nothing was changed. Details:
type "%TMPF%"
echo.
echo If the game was updated or verified by Steam, the original files may have changed.
goto :end

:translation_ok
findstr /c:"\"probe\"" "%TMPF%" >nul
if errorlevel 1 goto :translation_checked
findstr /c:"\"original\"" "%TMPF%" >nul
if errorlevel 1 goto :translation_checked
echo [ERROR] Translation files are in a mixed state. Run Uninstall_Thai_Mod.bat first.
goto :end

:translation_checked

rem --- Logos: fail early on unknown files ---
for %%P in (%LOGOS%) do (
  %PY% tools\manage_probe.py check --probe %%P > "%TMPF%" 2>&1
  if errorlevel 1 (
    echo [ERROR] Check failed for %%P. Nothing was changed. Details:
    type "%TMPF%"
    goto :end
  )
)
%PY% tools\manage_news_thai.py check > "%TMPF%" 2>&1
if errorlevel 1 (
  echo [ERROR] Check failed for news-thai-001 ^(GameAssembly.dll^). Nothing was changed. Details:
  type "%TMPF%"
  goto :end
)

rem --- Audio: each bundle may hold an older version that must be restored first ---
set "RESTORE_TANNOY="
set "RESTORE_RADIO="
call :detect_audio TANNOY %TANNOY% %OLD_TANNOY%
if "%AUDIO_FAIL%"=="1" goto :end
call :detect_audio RADIO %RADIO% %OLD_RADIO%
if "%AUDIO_FAIL%"=="1" goto :end

echo.
echo This will back up your save files, then replace 8 game bundle files and GameAssembly.dll.
echo Components already installed are left as they are.
echo The original files are backed up and can be restored with Uninstall_Thai_Mod.bat.
choice /c YN /m "Continue"
if errorlevel 2 (
  echo Cancelled. Nothing was changed.
  goto :end
)

echo.
echo [1/7] Backing up saves...
%PY% tools\backup_gameplay_saves.py
if errorlevel 1 (
  echo [ERROR] Save backup failed. Nothing was installed.
  goto :end
)

if "%NEED_006_RESTORE%"=="1" (
  echo.
  echo [2/7] Removing older translation %OLD_TRANSLATION%...
  %PY% tools\manage_probe.py restore --probe %OLD_TRANSLATION%
  if errorlevel 1 (
    echo [ERROR] Could not remove %OLD_TRANSLATION%. Do not start the game; ask for help.
    goto :end
  )
) else (
  echo.
  echo [2/7] No older translation to remove.
)

echo.
echo [3/7] Installing translation %TRANSLATION%...
%PY% tools\manage_probe.py install --probe %TRANSLATION%
if errorlevel 1 (
  echo [ERROR] Translation install failed. The tool restores the originals on copy failure; run Uninstall_Thai_Mod.bat to verify.
  goto :end
)

echo.
echo [4/7] Installing logos...
for %%P in (%LOGOS%) do (
  echo   - %%P
  %PY% tools\manage_probe.py install --probe %%P
  if errorlevel 1 (
    echo [ERROR] Install failed for %%P. Translation is installed; run Uninstall_Thai_Mod.bat to roll everything back.
    goto :end
  )
)

echo.
echo [5/7] Installing Thai news cards ^(news-thai-001^)...
%PY% tools\manage_news_thai.py install
if errorlevel 1 (
  echo [ERROR] News card install failed. Translation and logos are installed; run Uninstall_Thai_Mod.bat to roll everything back.
  goto :end
)

echo.
echo [6/7] Installing Thai PA announcements ^(%TANNOY%^)...
call :install_audio %TANNOY% "%RESTORE_TANNOY%"
if "%AUDIO_FAIL%"=="1" goto :end

echo.
echo [7/7] Installing Thai radio ^(%RADIO%^)...
call :install_audio %RADIO% "%RESTORE_RADIO%"
if "%AUDIO_FAIL%"=="1" goto :end

echo.
echo Verifying...
for %%P in (%TRANSLATION% %LOGOS% %TANNOY% %RADIO%) do (
  echo   %%P:
  %PY% tools\manage_probe.py check --probe %%P
)
echo   news-thai-001:
%PY% tools\manage_news_thai.py check
echo.
echo Done. All bundles should show "probe" and news-thai-001 should show "installed". You can start the game now.
goto :end

rem ---- subroutines ----------------------------------------------------------
rem :detect_audio VARNAME CURRENT OLD1 OLD2 ...
rem   Sets RESTORE_<VARNAME> to the older version found installed (empty if none),
rem   AUDIO_FAIL=1 if the game file is in an unknown state.
:detect_audio
set "AUDIO_FAIL=0"
set "_VAR=%~1"
set "_CUR=%~2"
%PY% tools\manage_probe.py check --probe %_CUR% > "%TMPF%" 2>&1
if not errorlevel 1 goto :eof
shift
shift
:detect_audio_loop
if "%~1"=="" goto :detect_audio_fail
if exist "local\prototype\%~1\manifest.json" (
  %PY% tools\manage_probe.py check --probe %~1 > "%TMPF%" 2>&1
  if not errorlevel 1 (
    findstr /c:"\"probe\"" "%TMPF%" >nul && set "RESTORE_%_VAR%=%~1" && echo Found older %~1 installed. It will be replaced by %_CUR%.&& goto :eof
  )
)
shift
goto :detect_audio_loop
:detect_audio_fail
%PY% tools\manage_probe.py check --probe %_CUR% > "%TMPF%" 2>&1
echo [ERROR] Audio check failed for %_CUR%. Nothing was changed. Details:
type "%TMPF%"
echo.
echo If the game was updated or verified by Steam, the original files may have changed.
set "AUDIO_FAIL=1"
goto :eof

rem :install_audio CURRENT "OLD-TO-RESTORE"
:install_audio
set "AUDIO_FAIL=0"
if not "%~2"=="" (
  echo   - removing older %~2
  %PY% tools\manage_probe.py restore --probe %~2
  if errorlevel 1 (
    echo [ERROR] Could not remove %~2. Do not start the game; ask for help.
    set "AUDIO_FAIL=1"
    goto :eof
  )
)
echo   - %~1
%PY% tools\manage_probe.py install --probe %~1
if errorlevel 1 (
  echo [ERROR] Install failed for %~1. Other components are installed; run Uninstall_Thai_Mod.bat to roll everything back.
  set "AUDIO_FAIL=1"
)
goto :eof

:end
echo.
pause
endlocal
