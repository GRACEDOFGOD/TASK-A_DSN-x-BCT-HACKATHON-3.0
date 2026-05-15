@echo off
REM ============================================================
REM install.bat — Installation script for Windows
REM Nigerian AI Review Generator — Task A
REM ============================================================

setlocal enabledelayedexpansion

echo.
echo 🇳🇬 Installing Nigerian AI Review Generator...
echo.

REM Check Python version
echo ✓ Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from https://www.python.org/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo   Found Python !PYTHON_VERSION!
echo.

REM Create virtual environment
echo ✓ Creating virtual environment...
if exist "venv\" (
    echo   Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo   Virtual environment created
)
echo.

REM Activate virtual environment
echo ✓ Activating virtual environment...
call venv\Scripts\activate.bat
echo   Virtual environment activated
echo.

REM Upgrade pip
echo ✓ Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo   pip upgraded
echo.

REM Install dependencies
echo ✓ Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)
echo   Dependencies installed
echo.

REM Create .env file
echo ✓ Setting up environment variables...
if not exist ".env" (
    copy .env.example .env >nul
    echo   .env file created from .env.example
    echo.
    echo ⚠️  IMPORTANT: Edit .env and add your Groq API key:
    echo    Open .env in a text editor
    echo.
    echo    Replace: GROQ_API_KEY=gsk_your_actual_api_key_here_do_not_expose
    echo    With:    GROQ_API_KEY=gsk_YOUR_ACTUAL_KEY_HERE
) else (
    echo   .env file already exists
)
echo.

REM Verify installation
echo ✓ Verifying installation...
python -c "from agent import run_pipeline; from personas import NIGERIAN_USERS; print('  ✓ All imports successful!')" 2>nul
if errorlevel 1 (
    echo   ❌ Import verification failed
    echo   Make sure you've installed all dependencies
    pause
    exit /b 1
)
echo.

echo ✅ Installation complete!
echo.
echo Next steps:
echo 1. Edit .env file with your Groq API key
echo 2. Run: python app.py
echo 3. Open browser: http://127.0.0.1:7860
echo.
echo For help, see SETUP.md or TROUBLESHOOTING.md
echo.
pause
