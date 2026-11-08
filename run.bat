@echo off
title StreamGuard - Video Streaming & Security Platform
cd /d "%~dp0"
echo ====================================================================
echo Starting StreamGuard Video Platform from: %cd%
echo ====================================================================
python run.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo An error occurred while launching. Press any key to exit.
    pause
)
