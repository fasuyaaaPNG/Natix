from library.imports import streamlit as st
from library.imports import subprocess
from library.imports import urlparse
from library.imports import platform
from library.imports import os
from library.imports import re
from system_check.pip import check_pip_installed
from system_install.pip import install_pip
from system_check.node import check_node_installed
from system_install.node import install_node
from system_check.nativefier import check_nativefier_installed
from system_install.nativefier import install_nativefier


def validate_url(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        url = "http://" + url
    try:
        parsed_url = urlparse(url)
        if not parsed_url.netloc:
            raise ValueError("Invalid URL")
        return url
    except Exception as e:
        raise ValueError(f"Invalid URL: {e}")


def generate_app(url, app_name, icon_path=None, arch=None):
    try:
        valid_url = validate_url(url)
        is_windows = platform.system() == 'Windows'
        is_mac = platform.system() == 'Darwin'
        is_linux = platform.system() == 'Linux'
        shell_flag = is_windows

        # Validate icon based on OS
        if icon_path:
            if is_linux and not icon_path.endswith('.png'):
                st.error("For Linux, only PNG files are allowed.")
                return
            elif is_windows and not icon_path.endswith('.ico'):
                st.error("For Windows, only ICO files are allowed.")
                return
            elif is_mac and not (icon_path.endswith('.icns') or icon_path.endswith('.png')):
                st.error("For macOS, only ICNS or PNG files are allowed.")
                return

        # Advanced options for architecture
        valid_arch = None
        if arch:
            if arch not in ['x64', 'armv7l', 'arm64', 'universal']:
                st.error("Invalid architecture option. Choose from 'x64', 'armv7l', 'arm64', or 'universal'.")
                return
            valid_arch = arch

        # Preparing the command arguments
        command = ['nativefier', valid_url, '--name', app_name, '--overwrite']

        if icon_path:
            command.extend(['--icon', icon_path])
        if valid_arch:
            command.extend(['-a', valid_arch])

        with st.spinner("Please wait, generating your app..."):
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=shell_flag  
            )

        st.text("Nativefier Output:")
        st.text(result.stdout.decode())
        st.text(result.stderr.decode())

        output_text = result.stdout.decode()
        match = re.search(r"App built to (.*?)(,|$)", output_text)
        
        if match:
            app_path = match.group(1).strip()
            st.success(f"App successfully generated and saved at: {app_path}")
        else:
            st.error("Failed to extract app build path. Please check the logs for details.")
    except ValueError as e:
        st.error(f"Error: {e}")


@st.cache_resource
def check_install():
    if not check_pip_installed():
        install_pip()
    if not check_node_installed():
        install_node()
    if not check_nativefier_installed():
        install_nativefier()


check_install()

st.title("Natix - Nativefier Xperience")

url = st.text_input("Enter the URL of the website you want to convert to a desktop app:", "")
app_name = st.text_input("Enter the name for your app:", "")

with st.expander("Advanced Options"):
    icon_file = st.file_uploader("Upload an icon (for Linux: PNG, for Windows: ICO, for macOS: ICNS or PNG)", type=["png", "ico", "icns"])
    if icon_file:
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        icon_folder = os.path.join(project_root, 'Source', 'image_icon')
        os.makedirs(icon_folder, exist_ok=True)

        icon_file_name = icon_file.name
        icon_path = os.path.join(icon_folder, icon_file_name)

        try:
            with open(icon_path, "wb") as f:
                f.write(icon_file.getbuffer())
            st.write(f"Icon file saved at: {icon_path}")
        except Exception as e:
            st.error(f"Failed to save icon file: {e}")
    else:
        icon_path = None
    
    arch = st.selectbox("Select Architecture (Optional)", ['x64', 'armv7l', 'arm64', 'universal', None])

if st.button("Generate App"):
    if url and app_name:
        generate_app(url, app_name, icon_path, arch)
    else:
        st.warning("Please provide both a valid URL and an app name.")
