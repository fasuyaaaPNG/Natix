from library.imports import subprocess
from library.imports import urlparse
from library.imports import os
from system_check.pip import check_pip_installed
from system_install.pip import install_pip
from system_check.node import check_node_installed
from system_install.node import install_node
from system_check.nativefier import check_nativefier_installed
from system_install.nativefier import install_nativefier
from library.imports import streamlit as st


# Helper function to parse domain
def parse_domain(domain):
    if not (domain.startswith("http://") or domain.startswith("https://")):
        domain = "http://" + domain
    parsed_url = urlparse(domain)
    return parsed_url.netloc


# Function to generate the app
def generate_app(url, app_name):
    try:
        domain = parse_domain(url)
        user_home = os.path.expanduser("~")
        output_dir = os.path.join(user_home, 'output_natix')
        final_output_path = os.path.join(output_dir, app_name)

        os.makedirs(output_dir, exist_ok=True)

        st.write("Generating app...")

        # Pass the correct arguments to Nativefier
        result = subprocess.run(
            ['nativefier', url, '--name', app_name, '--overwrite', '--out', output_dir],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True
        )

        # Display the result of the command
        st.text(result.stdout.decode())
        st.text(result.stderr.decode())

        if os.path.exists(final_output_path):
            st.success(f"App saved at: {final_output_path}")
        else:
            st.error("Failed to generate app.")
    except ValueError as e:
        st.error(f"Error: {e}")


# Streamlit caching and installation checks
@st.cache_resource
def check_install():
    if not check_pip_installed():
        install_pip()
    if not check_node_installed():
        install_node()
    if not check_nativefier_installed():
        install_nativefier()


# Check installations
check_install()

# Streamlit UI
st.title("Natix - Nativefier Xperience")

url = st.text_input("Enter URL:", "")
app_name = st.text_input("Enter App Name:", "")

if st.button("Generate App"):
    if url and app_name:
        generate_app(url, app_name)
    else:
        st.warning("Please enter both the URL and App Name.")
