#!/bin/bash

if ! command -v brew &> /dev/null
then
    echo "Homebrew is not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    if ! command -v brew &> /dev/null
    then
        echo "Homebrew installation failed. Please try installing it manually from https://brew.sh/"
        exit 1
    fi
fi

if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Installing Python3 with Homebrew..."
    brew install python
fi

python3 ./system_program/main.py
