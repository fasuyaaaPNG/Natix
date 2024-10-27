from library.imports import subprocess
from library.imports import urlparse
from library.imports import shutil
from library.imports import os
from system_check.pip import check_pip_installed
from system_install.pip import install_pip
from system_check.node import check_node_installed
from system_install.node import install_node
from system_check.nativefier import check_nativefier_installed
from system_install.nativefier import install_nativefier

def check_install():
    if not check_pip_installed():
        install_pip()
    if not check_node_installed():
        install_node()
    if not check_nativefier_installed():
        install_nativefier()

def parse_domain(domain):
    if not (domain.startswith("http://") or domain.startswith("https://")):
        domain = "http://" + domain
    parsed_url = urlparse(domain)
    return parsed_url.netloc

def get_input(prompt):
    return input(prompt).strip()

def main():
    check_install()
    
    url = get_input("Url: ")
    domain = parse_domain(url)
    
    app_name = get_input("Name: ")
    commands = [domain, app_name]

    user_home = os.path.expanduser("~")
    output_dir = os.path.join(user_home, 'output_natix')

    os.makedirs(output_dir, exist_ok=True)

    final_output_path = os.path.join(output_dir, app_name)

    print("Generating app...")
    result = subprocess.run(
        ['nativefier', '--name', app_name, '--overwrite', domain, final_output_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    print(result.stdout.decode())
    print(result.stderr.decode())

    if os.path.exists(final_output_path):
        print(f"App saved at: {final_output_path}")
    else:
        print("Failed to generate app.")

if __name__ == "__main__":
    main()
