@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (set "PY=python") else (set "PY=py -3")
%PY% tools\manage_news_thai.py install
if errorlevel 1 (echo Installation failed. See the message above.) else (echo Thai news cards installed.)
pause
endlocal
