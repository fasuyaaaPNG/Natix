from library.imports import platform
from library.imports import subprocess
from library.imports import sys

def install_nativefier():
    subprocess.run(['npm', 'install', '-g', 'nativefier'], check=True)