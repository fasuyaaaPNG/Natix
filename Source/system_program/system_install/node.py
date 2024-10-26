from library.imports import platform
from library.imports import subprocess
from library.imports import sys
from system_check.mac.brew import check_homebrew_installed
from system_install.mac.brew import install_homebrew

def install_node():
    os_type = platform.system()
    if os_type == "Windows":
        print("Installing Node.js on Windows...")
        subprocess.run(['choco', 'install', 'nodejs'], check=True)
    elif os_type == "Darwin":
        if not check_homebrew_installed():
            install_homebrew()
        print("Installing Node.js on macOS...")
        subprocess.run(['brew', 'install', 'node'], check=True)  
    elif os_type == "Linux":
        print("Installing Node.js on Linux...")
        subprocess.run(['sudo','apt-get', 'install', '-y', 'nodejs'], check=True)
    else:
        print("Unsupported operating system.")
        sys.exit(1)