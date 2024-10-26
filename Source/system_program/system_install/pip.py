from library.imports import subprocess
from library.imports import os

def install_pip():
    print("Downloading get-pip.py...")
    subprocess.run(['curl', 'https://bootstrap.pypa.io/get-pip.py', '-o', 'get-pip.py'])
    print("Installing pip...")
    subprocess.run(['python3', 'get-pip.py'])
    os.remove('get-pip.py') 
    print("pip installed successfully.")