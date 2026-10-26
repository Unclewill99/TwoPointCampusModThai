@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (set "PY=python") else (set "PY=py -3")
%PY% tools\manage_news_thai.py restore
if errorlevel 1 (echo Restore failed. See the message above.) else (echo Original news display restored. Translation and Thai logo are unchanged.)
pause
endlocal
