@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Python is already installed on the system.
) ELSE (
    echo Python not found. Downloading and opening Python 3.11 installer...
    REM Download Python 3.11 from the Microsoft Store
    start /wait ms-windows-store://pdp/?productid=9NRWMJP3717K
    echo Please complete the installation of Python 3.11 from the Microsoft Store, then press any key to continue.
    pause
)

REM Ensure pip is installed and upgrade pip
@REM ensurepip --default-pip
@REM pip3 install --upgrade pip

REM Install Streamlit
echo Installing Streamlit...
pip install streamlit

REM Run Streamlit
echo Running Streamlit...
set SCRIPT_PATH=%~dp0\Source\system_program\main.py
python -m streamlit run "%SCRIPT_PATH%"
pause
