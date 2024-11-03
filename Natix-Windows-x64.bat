@echo off
REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Python sudah terinstal di sistem.
) ELSE (
    echo Python tidak ditemukan. Mengunduh dan membuka installer Python 3.11...
    REM Download Python 3.11 from the Microsoft Store
    start /wait ms-windows-store://pdp/?productid=9NRWMJP3717K
    echo Silakan lanjutkan instalasi Python 3.11 dari Microsoft Store, lalu tekan sembarang tombol untuk melanjutkan.
    pause
)

REM Ensure pip is installed and upgrade pip
@REM ensurepip --default-pip
@REM pip3 install --upgrade pip

REM Install Streamlit
echo Menginstal Streamlit...
pip install streamlit

REM Run Streamlit
echo Menjalankan Streamlit...
set SCRIPT_PATH=%~dp0\Source\system_program\main.py
python -m streamlit run "%SCRIPT_PATH%"
pause
