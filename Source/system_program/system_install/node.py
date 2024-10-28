import urllib.request
import subprocess
import platform
import sys
import os
from system_check.mac.brew import check_homebrew_installed
from system_install.mac.brew import install_homebrew

def install_node():
    os_type = platform.system()
    
    if os_type == "Windows":
        print("Mengunduh installer Node.js untuk Windows...")
        nodejs_url = 'https://nodejs.org/dist/v18.16.0/node-v18.16.0-x64.msi'

        try:
            subprocess.run(['curl', nodejs_url, '-o', "node.msi"], check=True)
            print("File installer berhasil diunduh.")
        except subprocess.CalledProcessError as e:
            print(f"Gagal mengunduh file: {e}")
            sys.exit(1)
        
        print("Menginstal Node.js di Windows...")
        try:
            subprocess.run(['msiexec', '/i', "node.msi"], check=True)
            print("Node.js berhasil diinstal.")
        except subprocess.CalledProcessError as e:
            print(f"Gagal menginstal Node.js: {e}")
            sys.exit(1)

    elif os_type == "Darwin":
        print("Menginstal Node.js di macOS...")
        subprocess.run(['brew', 'install', 'node'], check=True)
        print("Node.js berhasil diinstal di macOS.")

    elif os_type == "Linux":
        print("Menginstal Node.js di Linux...")
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nodejs'], check=True)
        print("Node.js berhasil diinstal di Linux.")

    else:
        print("Sistem operasi tidak didukung.")
        sys.exit(1)

