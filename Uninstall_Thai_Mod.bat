@echo off
setlocal
cd /d "%~dp0"
rem Restores every component of the Thai mod, in reverse install order:
rem   radio-thai-00N         Thai radio DJs          (manage_probe.py, whichever version is installed)
rem   tannoy-thai-00N        Thai PA announcements   (manage_probe.py, whichever version is installed)
rem   news-thai-001          GameAssembly.dll        (manage_news_thai.py)
rem   county-logo-001        TWO POINT COUNTY Thai logo  (manage_probe.py)
rem   thai-logo-001          TWO POINT CAMPUS Thai logo   (manage_probe.py)
rem   fresh-translation-007  Thai text + fonts + UI  (manage_probe.py)
rem   fresh-translation-006  older translation, restored only if still present
set "TRANSLATIONS=fresh-translation-007 fresh-translation-006"
set "LOGOS=county-logo-001 thai-logo-001"
set "AUDIO=radio-thai-008 radio-thai-007 radio-thai-006 radio-thai-005 radio-thai-004 radio-thai-003 radio-thai-002 radio-thai-001 tannoy-thai-007 tannoy-thai-006 tannoy-thai-005 tannoy-thai-004 tannoy-thai-003 tannoy-thai-002 tannoy-thai-001"
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
tasklist /fi "imagename eq TPC.exe" 2>nul | find /i "TPC.exe" >nul
if %errorlevel%==0 (
  echo [ERROR] Two Point Campus is running. Close the game completely, then run this file again.
  goto :end
)

echo ============================================================
echo  Uninstall Thai mod (restore original game files)
echo ============================================================
echo Checking current game files...
set "ANY=0"
set "FAILED=0"

rem Translation: at most one of 007 / 006 can be present. A check failure for one
rem version is expected when the other is installed, so only a check that succeeds
rem and reports "probe" counts.
for %%P in (%TRANSLATIONS%) do (
  if exist "local\prototype\%%P\manifest.json" (
    %PY% tools\manage_probe.py check --probe %%P > "%TMPF%" 2>&1
    if not errorlevel 1 (
      findstr /c:"\"probe\"" "%TMPF%" >nul && call set "ANY=1" && echo   %%P: installed
    )
  )
)
for %%P in (%LOGOS%) do (
  if exist "local\prototype\%%P\manifest.json" (
    %PY% tools\manage_probe.py check --probe %%P > "%TMPF%" 2>&1
    if errorlevel 1 (
      echo [ERROR] Check failed for %%P. Nothing was changed. Details:
      type "%TMPF%"
      goto :end
    )
    findstr /c:"\"probe\"" "%TMPF%" >nul && call set "ANY=1" && echo   %%P: installed
  )
)
if exist "local\prototype\news-thai-001\manifest.json" (
  %PY% tools\manage_news_thai.py check > "%TMPF%" 2>&1
  if errorlevel 1 (
    echo [ERROR] Check failed for news-thai-001 ^(GameAssembly.dll^). Nothing was changed. Details:
    type "%TMPF%"
    goto :end
  )
  findstr /c:"\"installed\"" "%TMPF%" >nul && call set "ANY=1" && echo   news-thai-001: installed
)
rem Audio: one radio version and one PA version at most. A check failure for a
rem version is expected when another version is installed, so only a check that
rem succeeds and reports "probe" counts.
set "AUDIO_INSTALLED="
for %%P in (%AUDIO%) do (
  if exist "local\prototype\%%P\manifest.json" (
    %PY% tools\manage_probe.py check --probe %%P > "%TMPF%" 2>&1
    if not errorlevel 1 (
      findstr /c:"\"probe\"" "%TMPF%" >nul && call set "ANY=1" && call set "AUDIO_INSTALLED=%%AUDIO_INSTALLED%% %%P" && echo   %%P: installed
    )
  )
)

if "%ANY%"=="0" (
  echo The original game files are already in place. Nothing to restore.
  goto :end
)
echo.
echo This will restore the original English bundle files ^(text, logos, PA, radio^) and GameAssembly.dll from the local backups.
echo Your save files are not touched.
choice /c YN /m "Continue"
if errorlevel 2 (
  echo Cancelled. Nothing was changed.
  goto :end
)

echo.
echo [1/4] Restoring audio ^(PA + radio^)...
for %%P in (%AUDIO_INSTALLED%) do (
  echo   - %%P
  %PY% tools\manage_probe.py restore --probe %%P
  if errorlevel 1 (
    echo [ERROR] Restore failed for %%P. Do not start the game; ask for help.
    goto :end
  )
)

echo.
echo [2/4] Restoring news cards ^(news-thai-001^)...
if exist "local\prototype\news-thai-001\manifest.json" (
  %PY% tools\manage_news_thai.py restore
  if errorlevel 1 (
    echo [ERROR] Restore failed for news-thai-001. Do not start the game; ask for help.
    goto :end
  )
)

echo.
echo [3/4] Restoring logos...
for %%P in (%LOGOS%) do (
  if exist "local\prototype\%%P\manifest.json" (
    echo   - %%P
    %PY% tools\manage_probe.py restore --probe %%P
    if errorlevel 1 (
      echo [ERROR] Restore failed for %%P. Do not start the game; ask for help.
      goto :end
    )
  )
)

echo.
echo [4/4] Restoring translation...
for %%P in (%TRANSLATIONS%) do (
  if exist "local\prototype\%%P\manifest.json" (
    %PY% tools\manage_probe.py check --probe %%P > "%TMPF%" 2>&1
    if not errorlevel 1 (
      findstr /c:"\"probe\"" "%TMPF%" >nul && call :restore_translation %%P
    )
  )
)
if "%FAILED%"=="1" goto :end

echo.
echo Verifying...
for %%P in (%LOGOS%) do (
  if exist "local\prototype\%%P\manifest.json" (
    echo   %%P:
    %PY% tools\manage_probe.py check --probe %%P
  )
)
for %%P in (%TRANSLATIONS%) do (
  if exist "local\prototype\%%P\manifest.json" (
    echo   %%P:
    %PY% tools\manage_probe.py check --probe %%P 2>nul
  )
)
echo   news-thai-001:
%PY% tools\manage_news_thai.py check
echo   audio:
for %%P in (%AUDIO_INSTALLED%) do (
  echo   %%P:
  %PY% tools\manage_probe.py check --probe %%P
)
echo.
echo Done. All bundles should show "original" and news-thai-001 should show "original".
goto :end

:restore_translation
echo   - %1
%PY% tools\manage_probe.py restore --probe %1
if errorlevel 1 (
  echo [ERROR] Restore failed for %1. Do not start the game; ask for help.
  set "FAILED=1"
)
goto :eof

:end
echo.
pause
endlocal
