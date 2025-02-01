import os
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import shutil
import threading
from colorama import Fore, init
import config
import utils

# فعال‌سازی رنگ‌ها برای کنسول
init(autoreset=True)

def run_installer(bat_file_path):
    """ اجرای فایل installer.bat به صورت خودکار """
    try:
        print(config.COLORS["success"] + "Running installer.bat...")
        subprocess.run([bat_file_path], check=True)
        print(config.COLORS["success"] + "Installer ran successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to run installer.bat: {e}")

def copy_exe_files(exe_folder, install_path):
    """ کپی کردن فایل‌های exe به مسیر نصب """
    exe_files = [f for f in os.listdir(exe_folder) if f.endswith('.exe')]
    if not exe_files:
        messagebox.showerror("Error", "No .exe files found in the selected folder.")
        return
    
    for exe in exe_files:
        exe_path = os.path.join(exe_folder, exe)
        install_path_exe = os.path.join(install_path, exe)
        
        try:
            shutil.copy(exe_path, install_path_exe)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to install {exe}: {e}")
            return

def install_multiple_files_in_parallel(exe_folder, install_path):
    """ نصب همزمان چندین فایل exe """
    exe_files = [f for f in os.listdir(exe_folder) if f.endswith('.exe')]
    threads = []
    
    for exe in exe_files:
        thread = threading.Thread(target=copy_exe_files, args=(exe_folder, install_path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(config.COLORS["success"] + "All installations completed.")

def create_installer_batch(auto_install=False, parallel_install=False):
    """ ایجاد فایل installer.bat و امکان نصب خودکار """
    folder_path = utils.select_folder("Select Folder containing .exe files")
    if not folder_path or not os.path.isdir(folder_path):
        return

    exe_files = [f for f in os.listdir(folder_path) if f.endswith('.exe')]
    if not exe_files:
        messagebox.showerror("Error", "No .exe files found in the selected folder.")
        return

    print(config.COLORS["info"] + "\nAvailable .exe files:")
    for idx, exe in enumerate(exe_files, 1):
        print(f"{idx}. {exe}")

    try:
        choice = int(input(config.COLORS["info"] + "\nEnter the number of the file you want to create installer.bat for: "))
        if choice < 1 or choice > len(exe_files):
            messagebox.showerror("Error", "Invalid choice. Exiting...")
            return

        selected_exe = exe_files[choice - 1]

        save_path = utils.select_folder("Select folder to save installer.bat")
        if not save_path:
            return

        icon_path = utils.select_file("Select an icon for the installer", [("Icon Files", "*.ico")])
        if not icon_path:
            return

        bat_file_path = os.path.join(save_path, 'installer.bat')
        try:
            with open(bat_file_path, 'w') as bat_file:
                bat_file.write(f'echo Installing {selected_exe}\n')
                bat_file.write(f'start {os.path.join(folder_path, selected_exe)}\n')
            print(config.COLORS["success"] + f"installer.bat created successfully at {bat_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create installer.bat: {e}")
            return

        if auto_install:
            run_installer(bat_file_path)
        elif parallel_install:
            install_multiple_files_in_parallel(folder_path, save_path)
        else:
            print(config.COLORS["info"] + "Installer.bat has been created successfully.")
            print(f"You can run it manually from {bat_file_path}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Exiting...")

def auto_install_exes():
    """ نصب خودکار فایل‌های exe """
    exe_folder = utils.select_folder("Select Folder containing .exe files")
    if not exe_folder or not os.path.isdir(exe_folder):
        return

    install_path = utils.select_folder("Select the installation path")
    if not install_path:
        return

    # نصب خودکار فایل‌ها
    utils.copy_exe_files(exe_folder, install_path)

def run_with_admin_privileges():
    """ اجرای فایل با دسترسی مدیر """
    try:
        subprocess.run("runas /user:Administrator", check=True)
        print(config.COLORS["success"] + "Running as administrator...")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to gain admin privileges: {e}")

def main():
    """ منوی اصلی برنامه """
    while True:
        print(config.COLORS["info"] + "\n1. Create Installer.bat with advanced options")
        print("2. Create Installer.bat and Install Automatically")
        print("3. Auto Install .exe files")
        print("4. Exit")
        print("5. Run with Admin Privileges (For system-level apps)")
        choice = input(config.COLORS["warning"] + "Select an option: ")

        if choice == "1":
            create_installer_batch(auto_install=False, parallel_install=False)
        elif choice == "2":
            create_installer_batch(auto_install=True, parallel_install=False)
        elif choice == "3":
            auto_install_exes()
        elif choice == "4":
            print(config.COLORS["error"] + "Exiting...")
            break
        elif choice == "5":
            run_with_admin_privileges()
        else:
            messagebox.showerror("Error", "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
