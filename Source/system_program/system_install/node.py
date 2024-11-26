import platform
import shutil
import subprocess
import sys

def install_node():
    os_type = platform.system()

    if os_type == "Windows":
        print("Mengunduh installer Node.js untuk Windows...")
        nodejs_url = 'https://nodejs.org/dist/v18.16.0/node-v18.16.0-x64.msi'

        try:
            subprocess.run(['curl', nodejs_url, '-o', "node.msi"], check=True)
            print("File installer berhasil diunduh.")
        except subprocess.CalledProcessError as e:
            print(f"Gagal mengunduh file: {e}")
            sys.exit(1)
        
        print("Menginstal Node.js di Windows...")
        try:
            subprocess.run(['msiexec', '/i', "node.msi"], check=True)
            print("Node.js berhasil diinstal.")
        except subprocess.CalledProcessError as e:
            print(f"Gagal menginstal Node.js: {e}")
            sys.exit(1)

    elif os_type == "Darwin":
        print("Menginstal Node.js di macOS...")
        if shutil.which("brew") is None:
            print("Homebrew tidak ditemukan. Harap instal Homebrew terlebih dahulu.")
            sys.exit(1)
        try:
            subprocess.run(['brew', 'install', 'node'], check=True)
            print("Node.js berhasil diinstal di macOS.")
        except subprocess.CalledProcessError as e:
            print(f"Gagal menginstal Node.js: {e}")
            sys.exit(1)

    elif os_type == "Linux":
        print("Menginstal Node.js di Linux...")
        try:
            if shutil.which("pacman"):
                print("Menggunakan pacman di Arch Linux...")
                subprocess.run(['sudo', 'pacman', '-Sy', '--noconfirm', 'nodejs', 'npm'], check=True)
                print("Node.js berhasil diinstal di Arch Linux.")
            elif shutil.which("apt-get"):
                print("Menggunakan apt-get di Debian/Ubuntu...")
                # Tambahkan repository NodeSource untuk versi terbaru
                subprocess.run(['sudo', 'apt-get', 'update'], check=True)
                subprocess.run(
                    "curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -",
                    shell=True,
                    check=True
                )
                subprocess.run(['sudo', 'apt-get', 'install', '-y', 'nodejs'], check=True)
                print("Node.js versi terbaru berhasil diinstal di Debian/Ubuntu.")
            else:
                print("Manajer paket tidak dikenali. Harap instal Node.js secara manual.")
                sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"Gagal menginstal Node.js: {e}")
            sys.exit(1)

    else:
        print("Sistem operasi tidak didukung.")
        sys.exit(1)

# Contoh pemanggilan fungsi
if __name__ == "__main__":
    install_node()
