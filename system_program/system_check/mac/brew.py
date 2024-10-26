from library.imports import subprocess

def check_homebrew_installed():
    try:
        result = subprocess.run(['brew', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0
    except FileNotFoundError:
        return False