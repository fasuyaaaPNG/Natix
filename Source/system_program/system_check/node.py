from library.imports import subprocess

def check_node_installed():
    try:
        result = subprocess.run(['node', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.returncode == 0, result.stdout.decode().strip()
    except FileNotFoundError:
        return False