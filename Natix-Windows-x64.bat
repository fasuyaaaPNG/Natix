@echo off

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    powershell -Command "Start-Process msiexec.exe -ArgumentList '/i https://www.python.org/ftp/python/3.9.7/python-3.11.7-amd64.exe /quiet InstallAllUsers=1 PrependPath=1' -NoNewWindow -Wait"
    if %errorlevel% neq 0 (
        echo Failed to install Python. Please install manually.
        exit /b
    )
) else (
    echo Python is installed.
)

:: Install Streamlit
echo Installing Streamlit...
pip install streamlit --upgrade

:: Run Streamlit app
echo Running Streamlit app...
streamlit run ./Source/system_program/main.py
