@echo off
REM CodeRef Explorer Launcher - Electron Edition
REM Launches the Electron desktop app

cd /d "%~dp0"

echo Starting CodeRef Explorer (Electron)...

REM Check if node_modules exists
if not exist "node_modules\" (
    echo ERROR: Dependencies not installed!
    echo Please run: npm install
    echo.
    pause
    exit /b 1
)

REM Launch Electron app
npm start
