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

def menu(commands):
    command_string = f"nativefier {commands[1]} --target='{commands[0]}' " + " ".join(commands[2:] + ["./output_app/"])
    print(f"""
Options:
1. Arch: the CPU architecture to build [choices: "x64", "armv7l", "arm64", "universal"]      
2. Conceal: package the app source code into an asar archive [boolean: true or false]
3. Electron version:
4. Icon:
5. Platform: default platform operating system [linux, windows, osx or mas]

Your command right now: {command_string}

0. Generate app
              """)
    answer = int(get_input(": "))
    return answer

def main():
    check_install()
    
    url = get_input("Url: ")
    domain = parse_domain(url)
    
    app_name = get_input("Name: ")
    commands = [domain, app_name]

    while True:
        answer = menu(commands)
        
        if answer == 1:
            arch = get_input("Architecture: ")
            commands.append(f'--arch \'{arch}\'') 
        elif answer == 2:
            conceal_input = get_input("Conceal app source code into an asar archive (true/false): ")
            commands.append(f'--conceal \'{conceal_input}\'')  
        elif answer == 3:
            electron_version = get_input("Electron version: ")
            commands.append(f'--electron-version \'{electron_version}\'')
        elif answer == 4:
            icon = get_input("Icon path: ")
            commands.append(f'--icon \'{icon}\'')
        elif answer == 5:
            platform = get_input("Platform: ")
            commands.append(f'--platform \'{platform}\'')
        elif answer == 0:
            output_dir = '../output_app'
            temp_dir = f"{output_dir}/{app_name}-temp"
            
            print("Generating app...")
            result = subprocess.run(
                ['nativefier', '--name', app_name, '--overwrite', domain, temp_dir] + commands[2:],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(result.stdout.decode())
            print(result.stderr.decode())
        
            final_output_path = f"{output_dir}/{app_name}"
            if os.path.exists(final_output_path):
                shutil.rmtree(final_output_path) 
            os.rename(temp_dir, final_output_path)
            
            print(f"App saved at: {final_output_path}")
            print(" ")
            break

if __name__ == "__main__":
    main()
