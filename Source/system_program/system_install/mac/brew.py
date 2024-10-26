from library.imports import subprocess

def install_homebrew():
    print("Installing Homebrew...")
    subprocess.run(['/bin/bash', '-c', '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)'], check=True)