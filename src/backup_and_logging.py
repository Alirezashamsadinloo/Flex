import os
import shutil
import logging
from datetime import datetime

# تنظیمات مربوط به لاگ‌گیری
LOG_FILE = "install_log.txt"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_backup(file_path, backup_dir="backup"):
    """ ایجاد نسخه پشتیبان از فایل‌های موجود """
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    file_name = os.path.basename(file_path)
    backup_path = os.path.join(backup_dir, f"{file_name}.bak_{datetime.now().strftime('%Y%m%d%H%M%S')}")
    
    try:
        shutil.copy(file_path, backup_path)
        logging.info(f"Backup created: {backup_path}")
        print(f"[BACKUP] پشتیبان‌گیری انجام شد: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup for {file_path}: {e}")
        print(f"[ERROR] خطا در ایجاد نسخه پشتیبان: {e}")

def copy_exe_files_with_backup(exe_folder, install_path):
    """ نصب فایل‌های exe با پشتیبان‌گیری """
    exe_files = [f for f in os.listdir(exe_folder) if f.endswith('.exe')]
    if not exe_files:
        logging.warning("No .exe files found in the selected folder.")
        print("[WARNING] هیچ فایل .exe یافت نشد.")
        return
    
    for exe in exe_files:
        exe_path = os.path.join(exe_folder, exe)
        install_path_exe = os.path.join(install_path, exe)
        
        if os.path.exists(install_path_exe):
            create_backup(install_path_exe)
        
        try:
            shutil.copy(exe_path, install_path_exe)
            logging.info(f"Installed {exe} to {install_path_exe}")
            print(f"[INSTALL] {exe} با موفقیت نصب شد.")
        except Exception as e:
            logging.error(f"Failed to install {exe}: {e}")
            print(f"[ERROR] خطا در نصب {exe}: {e}")

def view_logs():
    """ نمایش لاگ‌ها """
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as log_file:
            print("\n========= Installation Logs =========")
            print(log_file.read())
            print("====================================\n")
    else:
        print("[INFO] هنوز هیچ لاگی ثبت نشده است.")

if __name__ == "__main__":
    print("[INFO] اجرای فرآیند نصب با لاگ و پشتیبان‌گیری...")
    exe_folder = input("مسیر پوشه حاوی فایل‌های exe: ")
    install_path = input("مسیر نصب: ")
    copy_exe_files_with_backup(exe_folder, install_path)
    print("[INFO] فرآیند نصب به پایان رسید.")
    view_logs()
