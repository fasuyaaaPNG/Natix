@echo off
REM Cek apakah Python sudah terinstal
python --version >nul 2>&1
IF %ERRORLEVEL% EQU 0 (
    echo Python sudah terinstal di sistem.
) ELSE (
    echo Python tidak ditemukan. Mengunduh dan membuka installer Python 3.11...
    REM Mengunduh Python 3.11 dari Microsoft Store
    start /wait ms-windows-store://pdp/?productid=9NRWMJP3717K
    echo Silakan lanjutkan instalasi Python 3.11 dari Microsoft Store, lalu tekan sembarang tombol untuk melanjutkan.
    pause
)

REM Memastikan pip terinstal dan upgrade pip
@REM ensurepip --default-pip
@REM pip3 install --upgrade pip

REM Menginstal Streamlit
echo Menginstal Streamlit...
pip3 install streamlit

REM Menjalankan Streamlit
echo Menjalankan Streamlit...
streamlit run ./Source/system_program/main.py
pause
