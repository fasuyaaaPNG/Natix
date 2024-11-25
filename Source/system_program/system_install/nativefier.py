from library.imports import platform
from library.imports import subprocess
from library.imports import sys
from shutil import which

def install_nativefier():
    try:
        # Periksa apakah npm tersedia
        if which("npm") is None:
            print("Error: npm was not found. Please ensure Node.js and npm are installed and added to the system PATH.")
            sys.exit(1)
        
        # Periksa manajer paket dan tambahkan `sudo` jika perlu
        if which("pacman") is not None:
            print("Detected pacman. Installing Nativefier with sudo...")
            subprocess.run(['sudo', 'npm', 'install', '-g', 'nativefier'], check=True)
        elif which("apt-get") is not None:
            print("Detected apt-get. Installing Nativefier with sudo...")
            subprocess.run(['sudo', 'npm', 'install', '-g', 'nativefier'], check=True)
        else:
            print("Package manager not detected. Attempting without sudo...")
            subprocess.run(['npm', 'install', '-g', 'nativefier'], check=True, shell=True)
        
        print("Nativefier has been installed successfully.")
    except FileNotFoundError:
        print("Error: npm was not found. Please ensure Node.js and npm are installed and added to the system PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to install Nativefier:")
        print(f"Exit code: {e.returncode}")
        print(f"Command: {e.cmd}")
        sys.exit(1)

if __name__ == "__main__":
    install_nativefier()
