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

def generate_app(url, app_name):
    try:
        valid_url = validate_url(url)
        is_windows = platform.system() == 'Windows'
        shell_flag = is_windows

        with st.spinner("Please wait, generating your app..."):
            result = subprocess.run(
                ['nativefier', valid_url, '--name', app_name, '--overwrite'],
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

if st.button("Generate App"):
    if url and app_name:
        generate_app(url, app_name)
    else:
        st.warning("Please provide both a valid URL and an app name.")
