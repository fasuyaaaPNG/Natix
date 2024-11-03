from library.imports import platform
from library.imports import subprocess
from library.imports import sys

def install_nativefier():
    try:
        subprocess.run(['npm', 'install', '-g', 'nativefier'], check=True, shell=True)
        print("Nativefier has been installed successfully.")
    except FileNotFoundError:
        print("Error: npm was not found. Please ensure Node.js and npm are installed and added to the system PATH.")
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to install Nativefier:", e)