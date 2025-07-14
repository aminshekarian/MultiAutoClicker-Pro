# 🎯 Multi AutoClicker Pro

یک ابزار قدرتمند برای کلیک خودکار روی موقعیت‌های مختلف صفحه با قابلیت کنترل کامل

## ✨ ویژگی‌ها

- 🎮 **5 موقعیت مختلف** برای کلیک خودکار
- ⚡ **تنظیم سرعت جداگانه** برای هر موقعیت
- 🎯 **کنترل دقیق** با کلیدهای میانبر
- 📊 **شمارنده کلیک** برای هر موقعیت
- 💾 **ذخیره خودکار** تنظیمات
- 🖥️ **رابط کاربری ساده** و کاربردی

## 🎮 کلیدهای میانبر

| کلید | عملکرد |
|------|---------|
| `F1-F5` | انتخاب سریع موقعیت‌ها |
| `Z` | تنظیم موقعیت فعال |
| `X` | شروع/توقف همه |
| `C` | ریست همه شمارنده‌ها |
| `ESC` | توقف اضطراری |

## 🚀 نصب سریع

### روش 1: نصب خودکار
```bash
git clone https://github.com/[username]/Multi-AutoClicker-Pro.git
cd Multi-AutoClicker-Pro
./setup.bat

### روش 2: نصب دستی
bash
pip install -r requirements.txt
python multi_autoclicker.py

## 📖 نحوه استفاده

1. **نصب و راه‌اندازی:**
   - `setup.bat` را اجرا کنید
   - یا مستقیماً `python multi_autoclicker.py`

2. **تنظیم موقعیت‌ها:**
   - موقعیت مورد نظر را انتخاب کنید
   - سرعت کلیک را تنظیم کنید
   - "تنظیم موقعیت" را بزنید

3. **شروع کلیک:**
   - موقعیت‌های بیشتری اضافه کنید
   - "شروع همه" را بزنید

## 🛠️ پیش‌نیازها

- Python 3.6 یا بالاتر
- Windows 10/11
- کتابخانه‌های مورد نیاز (نصب خودکار)

## 📦 کتابخانه‌های مورد نیاز

- `pyautogui` - کنترل ماوس و کیبورد
- `keyboard` - گرفتن کلیدهای میانبر
- `tkinter` - رابط کاربری
- `pillow` - پردازش تصویر

## 🧪 تست

bash
python test_requirements.py

## 🔧 فایل‌های پروژه

- `multi_autoclicker.py` - کد اصلی
- `setup.bat` - نصب خودکار
- `run_autoclicker.bat` - راه‌انداز سریع
- `positions.json` - ذخیره تنظیمات

## 🚨 نکات مهم

- برنامه را با دسترسی مدیر اجرا کنید
- Windows Defender ممکن است هشدار دهد (طبیعی است)
- ESC برای توقف اضطراری استفاده کنید

## 🤝 مشارکت

1. Fork کنید
2. Branch جدید بسازید
3. تغییرات را commit کنید
4. Pull request بفرستید

## 📄 مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## 🐛 گزارش مشکل

مشکلات را در [Issues](https://github.com/[username]/Multi-AutoClicker-Pro/issues) گزارش دهید.

---

⭐ **اگر مفید بود، یه ستاره بدید!** ⭐


## 📄 **.gitignore**:

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Settings
positions.json
settings.json
config.json

# Logs
*.log
logs/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
desktop.ini

# Temporary files
*.tmp
*.temp
~$*
