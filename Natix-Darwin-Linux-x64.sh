#!/bin/bash

# Cek apakah Python 3 terinstal
if ! command -v python3 &> /dev/null; then
    echo "Python tidak ditemukan. Menginstal Python..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v pacman &> /dev/null; then
            sudo pacman -Sy --noconfirm python python-pip
        elif command -v apt &> /dev/null; then
            sudo apt update
            sudo apt install -y python3 python3-pip
        else
            echo "Manajer paket tidak dikenali. Harap instal Python secara manual."
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        if ! command -v brew &> /dev/null; then
            echo "Homebrew tidak ditemukan. Menginstal Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
            eval "$(/opt/homebrew/bin/brew shellenv)"
        fi
        brew install python
    else
        echo "OS tidak didukung. Harap instal Python secara manual."
        exit 1
    fi
else
    echo "Python telah terinstal."
fi

# Cek apakah pip3 terinstal
if ! command -v pip3 &> /dev/null; then
    echo "pip3 tidak ditemukan. Menginstal pip3..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v pacman &> /dev/null; then
            sudo pacman -Sy --noconfirm python-pip
        elif command -v apt &> /dev/null; then
            sudo apt update
            sudo apt install -y python3-pip
        else
            echo "Manajer paket tidak dikenali. Harap instal pip3 secara manual."
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Menginstal pip3 menggunakan ensurepip..."
        python3 -m ensurepip --upgrade
    else
        echo "OS tidak didukung. Harap instal pip3 secara manual."
        exit 1
    fi
else
    echo "pip3 telah terinstal."
fi

# Menginstal Streamlit
echo "Menginstal Streamlit..."

# Deteksi OS
os_type=$(uname -s)

# Cek apakah OS Linux
if [[ "$os_type" == "Linux" ]]; then
    # Periksa manajer paket (apt atau pacman)
    if command -v pacman &> /dev/null; then
        echo "Manajer paket pacman ditemukan. Menginstal Streamlit dengan --break-system-packages..."
        pip3 install --user streamlit --break-system-packages
    elif command -v apt &> /dev/null; then
        echo "Manajer paket apt ditemukan. Menginstal Streamlit..."
        pip3 install --user streamlit
    else
        echo "Manajer paket tidak dikenali. Menginstal Streamlit secara manual..."
        pip3 install --user streamlit
    fi
else
    echo "OS terdeteksi: $os_type"
    pip3 install --user streamlit
fi


# Menambahkan pip user bin ke PATH jika tidak ada
if ! echo "$PATH" | grep -q "$(python3 -m site --user-base)/bin"; then
    echo "Menambahkan direktori pip user bin ke PATH..."
    export PATH="$(python3 -m site --user-base)/bin:$PATH"
    echo 'export PATH="$(python3 -m site --user-base)/bin:$PATH"' >> ~/.bashrc
    source ~/.bashrc
fi

# Menjalankan aplikasi Streamlit
echo "Menjalankan aplikasi Streamlit..."
python3 -m streamlit run ./Source/system_program/main.py
