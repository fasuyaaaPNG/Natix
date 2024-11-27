#!/bin/bash

if ! command -v python3 &> /dev/null; then
    echo "Python not found. Installing Python..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v pacman &> /dev/null; then
            sudo pacman -Sy --noconfirm python python-pip
        elif command -v apt &> /dev/null; then
            sudo apt update
            sudo apt install -y python3 python3-pip
        else
            echo "Package manager not recognized. Please install Python manually."
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "Homebrew not found. Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
            eval "$(/opt/homebrew/bin/brew shellenv)"
        fi
        brew install python
    else
        echo "OS not supported. Please install Python manually."
        exit 1
    fi
else
    echo "Python is already installed."
fi

if ! command -v pip3 &> /dev/null; then
    echo "pip3 not found. Installing pip3..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v pacman &> /dev/null; then
            sudo pacman -Sy --noconfirm python-pip
        elif command -v apt &> /dev/null; then
            sudo apt update
            sudo apt install -y python3-pip
        else
            echo "Package manager not recognized. Please install pip3 manually."
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Installing pip3 using ensurepip..."
        python3 -m ensurepip --upgrade
    else
        echo "OS not supported. Please install pip3 manually."
        exit 1
    fi
else
    echo "pip3 is already installed."
fi

echo "Installing Streamlit..."

os_type=$(uname -s)

if [[ "$os_type" == "Linux" ]]; then
    if command -v pacman &> /dev/null; then
        echo "pacman package manager found. Installing Streamlit with --break-system-packages..."
        pip3 install --user streamlit --break-system-packages
    elif command -v apt &> /dev/null; then
        echo "apt package manager found. Installing Streamlit..."
        pip3 install --user streamlit --break-system-packages
    else
        echo "Package manager not recognized. Installing Streamlit manually..."
        pip3 install --user streamlit
    fi
else
    echo "OS detected: $os_type"
    pip3 install --user streamlit
fi

if ! echo "$PATH" | grep -q "$(python3 -m site --user-base)/bin"; then
    echo "Adding pip user bin directory to PATH..."
    export PATH="$(python3 -m site --user-base)/bin:$PATH"
    echo 'export PATH="$(python3 -m site --user-base)/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
fi

echo "Running the Streamlit application..."
python3 -m streamlit run ./Source/system_program/main.py
