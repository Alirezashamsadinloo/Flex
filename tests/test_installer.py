import unittest
import os
import subprocess
import tempfile
from unittest.mock import patch, MagicMock
import shutil
import src.installer  # فرض می‌کنیم که کد اصلی شما به نام installer.py است
import utils
import src.config
import src.utils

class TestInstaller(unittest.TestCase):

    @patch('installer.subprocess.run')
    def test_run_installer(self, mock_run):
        # تست اجرای فایل installer.bat
        bat_file_path = "test_installer.bat"
        
        # شبیه‌سازی اجرای subprocess
        mock_run.return_value = None
        src.installer.run_installer(bat_file_path)
        
        # اطمینان از اینکه subprocess.run با مسیر صحیح فراخوانی شده است
        mock_run.assert_called_with([bat_file_path], check=True)

    @patch('installer.shutil.copy')
    def test_copy_files_to_installation_folder(self, mock_copy):
        # تست کپی کردن فایل‌ها به پوشه نصب
        exe_folder = tempfile.mkdtemp()
        install_folder = tempfile.mkdtemp()
        
        # ایجاد فایل تست
        test_exe_file = os.path.join(exe_folder, 'test_program.exe')
        with open(test_exe_file, 'w') as f:
            f.write("This is a test EXE file.")

        src.installer.copy_files_to_installation_folder(exe_folder, install_folder)
        
        # اطمینان از اینکه فایل‌ها کپی شده‌اند
        mock_copy.assert_called_with(test_exe_file, os.path.join(install_folder, 'test_program.exe'))

    @patch('installer.utils.select_folder')
    @patch('installer.utils.select_file')
    def test_create_installer_bat(self, mock_select_file, mock_select_folder):
        # شبیه‌سازی انتخاب پوشه و فایل از طریق GUI
        mock_select_folder.return_value = tempfile.mkdtemp()
        mock_select_file.return_value = "test_icon.ico"
        
        exe_folder = tempfile.mkdtemp()
        save_path = tempfile.mkdtemp()
        selected_exe = 'test_program.exe'
        
        # ایجاد فایل .bat
        bat_file_path = src.installer.create_iconified_installer(exe_folder, save_path, selected_exe, icon_path="test_icon.ico")
        
        # اطمینان از اینکه فایل bat ایجاد شده است
        self.assertTrue(os.path.exists(bat_file_path))

    @patch('installer.shutil.copy')
    def test_create_installer_bat_with_error(self, mock_copy):
        # شبیه‌سازی خطا در هنگام کپی فایل
        exe_folder = tempfile.mkdtemp()
        install_folder = tempfile.mkdtemp()

        # ایجاد یک فایل اشتباه برای کپی کردن
        test_exe_file = os.path.join(exe_folder, 'test_program.exe')
        
        # شبیه‌سازی خطا
        mock_copy.side_effect = Exception("Error copying file")
        
        with self.assertRaises(Exception):
            src.installer.copy_files_to_installation_folder(exe_folder, install_folder)

    @patch('installer.utils.select_folder')
    def test_create_installer_with_invalid_folder(self, mock_select_folder):
        # شبیه‌سازی انتخاب پوشه اشتباه
        mock_select_folder.return_value = None  # هیچ پوشه‌ای انتخاب نشده است
        
        exe_folder = tempfile.mkdtemp()
        save_path = tempfile.mkdtemp()
        selected_exe = 'test_program.exe'
        
        # تست ایجاد installer.bat با پوشه اشتباه
        bat_file_path = src.installer.create_iconified_installer(exe_folder, save_path, selected_exe)
        
        self.assertIsNone(bat_file_path)

if __name__ == "__main__":
    unittest.main()
