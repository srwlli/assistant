@echo off
REM CodeRef Explorer Web Launcher
REM Starts Python server and opens browser

cd /d "%~dp0"

echo Starting CodeRef Explorer (Web Version)...

REM Kill any existing Python servers on port 8080
taskkill /F /IM python.exe >nul 2>&1

REM Start Python server in background
start /B python server.py

REM Wait 2 seconds for server to start
timeout /t 2 /nobreak >nul

REM Open browser
start http://localhost:8080/src/pages/coderef-explorer.html

echo CodeRef Explorer is running at http://localhost:8080
echo Press any key to stop the server...

REM Keep window open (server runs in background)
pause >nul

REM Kill server when user presses key
taskkill /F /IM python.exe >nul 2>&1
