@echo off
setlocal
cd /d "%~dp0"
rem Restores every component of the Thai mod, in reverse install order:
rem   news-thai-001          GameAssembly.dll        (manage_news_thai.py)
rem   county-logo-001        TWO POINT COUNTY Thai logo  (manage_probe.py)
rem   thai-logo-001          TWO POINT CAMPUS Thai logo   (manage_probe.py)
rem   fresh-translation-007  Thai text + fonts + UI  (manage_probe.py)
rem   fresh-translation-006  older translation, restored only if still present
set "TRANSLATIONS=fresh-translation-007 fresh-translation-006"
set "LOGOS=county-logo-001 thai-logo-001"
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

if "%ANY%"=="0" (
  echo The original game files are already in place. Nothing to restore.
  goto :end
)
echo.
echo This will restore the original English bundle files and GameAssembly.dll from the local backups.
echo Your save files are not touched.
choice /c YN /m "Continue"
if errorlevel 2 (
  echo Cancelled. Nothing was changed.
  goto :end
)

echo.
echo [1/3] Restoring news cards ^(news-thai-001^)...
if exist "local\prototype\news-thai-001\manifest.json" (
  %PY% tools\manage_news_thai.py restore
  if errorlevel 1 (
    echo [ERROR] Restore failed for news-thai-001. Do not start the game; ask for help.
    goto :end
  )
)

echo.
echo [2/3] Restoring logos...
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
echo [3/3] Restoring translation...
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
