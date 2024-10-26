from library.imports import subprocess

def check_nativefier_installed():
    try:
        result = subprocess.run(['nativefier', '--help'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0, result.stdout.decode().strip()
    except FileNotFoundError:
        return False