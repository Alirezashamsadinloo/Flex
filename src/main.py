import os
import tkinter as tk
from tkinter import filedialog, messagebox
from installer import create_installer_batch, auto_install_exes, run_with_admin_privileges
from backup_and_logging import copy_exe_files_with_backup, view_logs

def select_folder(title="Select Folder"):
    """ نمایش پنجره انتخاب پوشه """
    folder = filedialog.askdirectory(title=title)
    if not folder:
        messagebox.showerror("Error", "No folder selected. Exiting...")
    return folder

def main():
    """ منوی اصلی برنامه """
    while True:
        print("\n========= INSTALLER TOOL =========")
        print("1. Create Installer.bat with advanced options")
        print("2. Create Installer.bat and Install Automatically")
        print("3. Auto Install .exe files")
        print("4. Install EXE Files with Backup & Logging")  # گزینه جدید
        print("5. View Installation Logs")  # گزینه جدید
        print("6. Run with Admin Privileges")
        print("7. Exit")
        print("==================================")

        choice = input("Select an option: ")

        if choice == "1":
            create_installer_batch(auto_install=False, parallel_install=False)
        elif choice == "2":
            create_installer_batch(auto_install=True, parallel_install=False)
        elif choice == "3":
            auto_install_exes()
        elif choice == "4":
            exe_folder = select_folder("Select Folder containing .exe files")
            install_path = select_folder("Select Installation Path")
            copy_exe_files_with_backup(exe_folder, install_path)
        elif choice == "5":
            view_logs()
        elif choice == "6":
            run_with_admin_privileges()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # مخفی کردن پنجره اصلی
    main()
