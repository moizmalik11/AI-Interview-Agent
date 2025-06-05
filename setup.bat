@echo off
echo Checking for Python...

where python >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed or not in PATH. Please install Python 3.
    exit /b
)

for /f "delims=" %%i in ('python --version') do set PYVERSION=%%i
echo ✅ Found %PYVERSION%

echo.
echo 📦 Creating virtual environment...
python -m venv venv

echo.
echo 🚀 Activating virtual environment...
call venv\Scripts\activate

echo.
IF EXIST requirements.txt (
    echo 📥 Installing packages from requirements.txt...
    pip install -r requirements.txt
) ELSE (
    echo ⚠️ requirements.txt not found. Skipping package install.
)

echo.
echo 🛑 Deactivating virtual environment...
deactivate

echo.
echo ✅ Setup complete!
echo 👉 To run the app:
echo    venv\Scripts\activate
echo    python app.py
