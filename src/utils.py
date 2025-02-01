import os
import shutil
from tkinter import filedialog, messagebox

def select_folder(title="Select Folder"):
    """ نمایش پنجره انتخاب پوشه """
    folder = filedialog.askdirectory(title=title)
    if not folder:
        messagebox.showerror("Error", "No folder selected. Exiting...")
    return folder

def select_file(title="Select File", filetypes=None):
    """ نمایش پنجره انتخاب فایل """
    file = filedialog.askopenfilename(title=title, filetypes=filetypes)
    if not file:
        messagebox.showerror("Error", "No file selected. Exiting...")
    return file

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
