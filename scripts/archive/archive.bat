@echo off
REM Archive Files - Batch Wrapper
REM Usage: archive.bat "path1" "path2" "path3" ...

powershell -ExecutionPolicy Bypass -File "%~dp0archive-files.ps1" %*
