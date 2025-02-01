import os

# تنظیمات پیش‌فرض پروژه
DEFAULT_INSTALLATION_PATH = os.path.expanduser("~\\Desktop\\Installation")
DEFAULT_ICON_PATH = os.path.join(os.path.dirname(__file__), "icons", "default.ico")

# رنگ‌ها برای پیام‌های کنسول
COLORS = {
    "success": "\033[92m",  # سبز
    "error": "\033[91m",    # قرمز
    "warning": "\033[93m",  # زرد
    "info": "\033[94m",     # آبی
}

# تنظیمات مربوط به نصب
INSTALL_SETTINGS = {
    "parallel_install": True,  # آیا نصب به صورت همزمان انجام شود؟
    "auto_install": False,     # آیا نصب به صورت خودکار انجام شود؟
    "create_installer_bat": True,  # آیا فایل installer.bat ایجاد شود؟
}

# مسیرهای پیش‌فرض برای استفاده در پروژه
DEFAULT_PATHS = {
    "exe_files": os.path.expanduser("~\\Desktop\\ExeFiles"),  # مسیر پیش‌فرض برای فایل‌های exe
    "installer_save": os.path.expanduser("~\\Desktop\\Installers"),  # مسیر پیش‌فرض برای ذخیره فایل‌های installer
}

# پیکربندی‌های مربوط به رابط کاربری
UI_SETTINGS = {
    "window_width": 800,
    "window_height": 600,
    "background_color": "#f0f0f0",  # رنگ پس‌زمینه
    "button_color": "#4CAF50",      # رنگ دکمه‌ها
    "button_text_color": "white",   # رنگ متن دکمه‌ها
    "highlight_color": "#ff9800",   # رنگ هایلایت
}

# فایل‌های لاگ
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "logs", "install_log.txt")

# دیگر تنظیمات مهم
TIMEOUT_LIMIT = 30  # زمان تایم‌اوت برای درخواست‌ها (ثانیه)
MAX_RETRIES = 3     # حداکثر تعداد تلاش‌های مجدد در صورت خطا
