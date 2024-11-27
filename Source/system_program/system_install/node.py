import platform
import shutil
import subprocess
import sys

def install_node():
    os_type = platform.system()

    if os_type == "Windows":
        print("Downloading Node.js installer for Windows...")
        nodejs_url = 'https://nodejs.org/dist/v20.18.1/node-v20.18.1-x64.msi'

        try:
            subprocess.run(['curl', nodejs_url, '-o', "node.msi"], check=True)
            print("Installer file downloaded successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to download the file: {e}")
            sys.exit(1)
        
        print("Installing Node.js on Windows...")
        try:
            subprocess.run(['msiexec', '/i', "node.msi"], check=True)
            print("Node.js installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Node.js: {e}")
            sys.exit(1)

    elif os_type == "Darwin":
        print("Installing Node.js on macOS...")
        if shutil.which("brew") is None:
            print("Homebrew not found. Please install Homebrew first.")
            sys.exit(1)
        try:
            subprocess.run(['brew', 'install', 'node'], check=True)
            print("Node.js installed successfully on macOS.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Node.js: {e}")
            sys.exit(1)

    elif os_type == "Linux":
        print("Installing Node.js on Linux...")
        try:
            if shutil.which("pacman"):
                print("Using pacman on Arch Linux...")
                subprocess.run(['sudo', 'pacman', '-Sy', '--noconfirm', 'nodejs', 'npm'], check=True)
                print("Node.js installed successfully on Arch Linux.")
            elif shutil.which("apt-get"):
                print("Using apt-get on Debian/Ubuntu...")
                subprocess.run(['sudo', 'apt-get', 'update'], check=True)
                subprocess.run(
                    "curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -",
                    shell=True,
                    check=True
                )
                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nodejs'], check=True)
                print("Latest version of Node.js installed successfully on Debian/Ubuntu.")
            else:
                print("Package manager not recognized. Please install Node.js manually.")
                sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Failed to install Node.js: {e}")
            sys.exit(1)

    else:
        print("Operating system not supported.")
        sys.exit(1)

if __name__ == "__main__":
    install_node()
