#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Installing Python..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo apt update
        sudo apt install -y python3 python3-pip
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "Homebrew is not installed. Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
            eval "$(/opt/homebrew/bin/brew shellenv)"
        fi
        brew install python
    else
        echo "Unsupported OS. Please install Python manually."
        exit 1
    fi
else
    echo "Python is installed."
fi

echo "Installing Streamlit..."
pip3 install streamlit --upgrade

echo "Running Streamlit app..."
python3 -m streamlit run ./Source/system_program/main.py
