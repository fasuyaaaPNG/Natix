@echo off
SET PYTHON_COMMAND=python
SET PYTHON_CHECK=%PYTHON_COMMAND% --version

%PYTHON_CHECK% >nul 2>&1
IF ERRORLEVEL 1 (
    echo Python 3 is not installed. Installing Python 3...

    SET PYTHON_INSTALLER=https://www.python.org/ftp/python/3.10.9/python-3.11.9-amd64.exe

    curl -o python_installer.exe %PYTHON_INSTALLER%
    start /wait python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

    del python_installer.exe
)

%PYTHON_COMMAND% ./system_program/main.py

pause
