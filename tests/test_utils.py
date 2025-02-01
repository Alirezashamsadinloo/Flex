import unittest
import os
import tempfile
from unittest.mock import patch, MagicMock
import src.utils # فرض می‌کنیم که کد اصلی شما به نام utils.py است

class TestUtils(unittest.TestCase):

    @patch('utils.filedialog.askdirectory')
    def test_select_folder(self, mock_askdirectory):
        # شبیه‌سازی انتخاب پوشه
        mock_askdirectory.return_value = '/test/folder'
        
        folder = src.utils.select_folder("Select Folder")
        
        # اطمینان از اینکه پوشه انتخاب شده درست است
        self.assertEqual(folder, '/test/folder')
    
    @patch('utils.filedialog.askopenfilename')
    def test_select_file(self, mock_askopenfilename):
        # شبیه‌سازی انتخاب فایل
        mock_askopenfilename.return_value = '/test/file.txt'
        
        file = src.utils.select_file("Select File")
        
        # اطمینان از اینکه فایل انتخاب شده درست است
        self.assertEqual(file, '/test/file.txt')

    @patch('utils.shutil.copy')
    def test_copy_file(self, mock_copy):
        # شبیه‌سازی کپی کردن فایل
        src = '/test/source/file.txt'
        dest = '/test/destination/file.txt'

        # فراخوانی تابع کپی
        src.utils.copy_file(src, dest)
        
        # اطمینان از اینکه تابع کپی به درستی فراخوانی شده است
        mock_copy.assert_called_with(src, dest)

    @patch('utils.shutil.rmtree')
    def test_remove_folder(self, mock_rmtree):
        # شبیه‌سازی حذف پوشه
        folder_path = '/test/folder_to_remove'
        
        # فراخوانی تابع حذف پوشه
        src.utils.remove_folder(folder_path)
        
        # اطمینان از اینکه تابع rmtree برای حذف پوشه فراخوانی شده است
        mock_rmtree.assert_called_with(folder_path)
    
    @patch('utils.os.makedirs')
    def test_create_directory(self, mock_makedirs):
        # شبیه‌سازی ایجاد پوشه
        dir_path = '/test/new_folder'
        
        # فراخوانی تابع ایجاد پوشه
        src.utils.create_directory(dir_path)
        
        # اطمینان از اینکه تابع makedirs برای ایجاد پوشه فراخوانی شده است
        mock_makedirs.assert_called_with(dir_path)

    def test_format_path(self):
        # تست فرمت کردن مسیر به فرمت صحیح
        raw_path = 'test/folder//file.txt'
        formatted_path = src.utils.format_path(raw_path)
        
        # اطمینان از اینکه مسیر به درستی فرمت شده است
        self.assertEqual(formatted_path, 'test/folder/file.txt')

if __name__ == "__main__":
    unittest.main()
