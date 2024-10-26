from library.imports import subprocess

def check_pip_installed():
    try:
        result = subprocess.run(['pip', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print("pip is installed. Version:", result.stdout.decode().strip())
            return True
        else:
            print("pip is not installed.")
            return False
    except FileNotFoundError:
        print("pip is not installed.")
        return False
