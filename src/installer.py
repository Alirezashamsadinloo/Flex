import os
import subprocess
import time
import shutil
from tkinter import filedialog, messagebox
import config
import utils

def run_installer(bat_file_path):
    """ اجرای فایل installer.bat """
    try:
        print(config.COLORS["success"] + "Running installer.bat...")
        subprocess.run([bat_file_path], check=True)
        print(config.COLORS["success"] + "Installer ran successfully.")
    except subprocess.CalledProcessError as e:
        print(config.COLORS["error"] + f"Failed to run installer.bat: {e}")
        messagebox.showerror("Error", f"Failed to run installer.bat: {e}")
    except Exception as e:
        print(config.COLORS["error"] + f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")

def copy_files_to_installation_folder(exe_folder, install_folder):
    """ کپی کردن فایل‌های exe به پوشه نصب """
    exe_files = [f for f in os.listdir(exe_folder) if f.endswith('.exe')]
    
    if not exe_files:
        messagebox.showerror("Error", "No .exe files found in the selected folder.")
        return
    
    for exe in exe_files:
        source_path = os.path.join(exe_folder, exe)
        destination_path = os.path.join(install_folder, exe)
        
        try:
            shutil.copy(source_path, destination_path)
            print(config.COLORS["success"] + f"{exe} installed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to copy {exe}: {e}")
            return

def create_installer_bat(exe_folder, save_path, selected_exe):
    """ ایجاد فایل installer.bat """
    bat_file_path = os.path.join(save_path, 'installer.bat')
    try:
        with open(bat_file_path, 'w') as bat_file:
            bat_file.write(f'echo Installing {selected_exe}\n')
            bat_file.write(f'start {os.path.join(exe_folder, selected_exe)}\n')
        print(config.COLORS["success"] + f"Installer.bat created at {bat_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create installer.bat: {e}")
        return None
    return bat_file_path

def create_iconified_installer(exe_folder, save_path, selected_exe, icon_path=None):
    """ ایجاد نصب‌کننده با آیکن """
    bat_file_path = create_installer_bat(exe_folder, save_path, selected_exe)
    if not bat_file_path:
        return
    
    if icon_path:
        try:
            # تبدیل فایل bat به یک فایل نصب با آیکن مشخص شده
            # این بخش می‌تواند به طور پیشرفته‌تر با استفاده از ابزارهای دیگر انجام شود
            print(config.COLORS["info"] + f"Adding icon {icon_path} to installer...")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add icon: {e}")
    else:
        print(config.COLORS["info"] + "No icon provided for installer.")
    
    return bat_file_path

def main():
    """ اجرای منوی اصلی و تعامل با کاربر """
    print(config.COLORS["info"] + "Welcome to the Installer Script!")
    while True:
        print(config.COLORS["info"] + "\n1. Create Installer.bat with advanced options")
        print("2. Create Installer.bat and Install Automatically")
        print("3. Auto Install .exe files")
        print("4. Exit")
        print("5. Run with Admin Privileges (For system-level apps)")
        choice = input(config.COLORS["warning"] + "Select an option: ")

        if choice == "1":
            exe_folder = utils.select_folder("Select Folder containing .exe files")
            save_path = utils.select_folder("Select folder to save installer.bat")
            if not exe_folder or not save_path:
                continue
            exe_files = [f for f in os.listdir(exe_folder) if f.endswith('.exe')]
            if not exe_files:
                messagebox.showerror("Error", "No .exe files found in the selected folder.")
                continue

            print(config.COLORS["info"] + "Available .exe files:")
            for idx, exe in enumerate(exe_files, 1):
                print(f"{idx}. {exe}")
            
            try:
                choice = int(input(config.COLORS["info"] + "\nEnter the number of the file to create installer for: "))
                if choice < 1 or choice > len(exe_files):
                    messagebox.showerror("Error", "Invalid choice. Please try again.")
                    continue

                selected_exe = exe_files[choice - 1]
                icon_path = utils.select_file("Select an icon for the installer", [("Icon Files", "*.ico")])

                bat_file_path = create_iconified_installer(exe_folder, save_path, selected_exe, icon_path)

                if bat_file_path:
                    print(config.COLORS["success"] + f"Installer.bat created successfully: {bat_file_path}")
                    run_installer(bat_file_path)
                
            except ValueError:
                messagebox.showerror("Error", "Invalid input. Please try again.")

        elif choice == "2":
            exe_folder = utils.select_folder("Select Folder containing .exe files")
            install_folder = utils.select_folder("Select Folder to Install Files")
            if not exe_folder or not install_folder:
                continue
            copy_files_to_installation_folder(exe_folder, install_folder)
            print(config.COLORS["success"] + "Files installed automatically.")
        
        elif choice == "3":
            exe_folder = utils.select_folder("Select Folder containing .exe files")
            install_folder = utils.select_folder("Select Folder to Install Files")
            if not exe_folder or not install_folder:
                continue
            utils.install_multiple_files_in_parallel(exe_folder, install_folder)
            print(config.COLORS["success"] + "All files installed successfully.")
        
        elif choice == "4":
            print(config.COLORS["error"] + "Exiting...")
            break
        
        elif choice == "5":
            utils.run_with_admin_privileges()

        else:
            messagebox.showerror("Error", "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
