@echo off
chcp 65001 >nul
title Multi AutoClicker Pro - نصب و راه‌اندازی

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                🎯 Multi AutoClicker Pro Setup 🎯               ║
echo ║                   نصب خودکار کتابخانه‌ها                        ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

echo 🔍 بررسی وجود Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python یافت نشد!
    echo 📥 لطفاً Python را از python.org دانلود و نصب کنید
    echo 🔗 https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python موجود است
echo.

echo 📦 نصب کتابخانه‌های مورد نیاز...
echo.

echo 🔧 نصب pyautogui...
pip install pyautogui
if %errorlevel% neq 0 (
    echo ❌ خطا در نصب pyautogui
    goto error
)

echo 🔧 نصب keyboard...
pip install keyboard
if %errorlevel% neq 0 (
    echo ❌ خطا در نصب keyboard
    goto error
)

echo 🔧 نصب pillow (برای screenshot)...
pip install pillow
if %errorlevel% neq 0 (
    echo ❌ خطا در نصب pillow
    goto error
)

echo 🔧 بررسی tkinter (معمولاً با Python نصب می‌شود)...
python -c "import tkinter; print('✅ tkinter موجود است')" 2>nul
if %errorlevel% neq 0 (
    echo ⚠️  tkinter موجود نیست - ممکن است نیاز به نصب python-tk باشد
)

echo.
echo ✅ نصب کتابخانه‌ها تکمیل شد!
echo.

echo 🎮 ایجاد فایل راه‌انداز...
echo @echo off > run_autoclicker.bat
echo chcp 65001 ^>nul >> run_autoclicker.bat
echo title Multi AutoClicker Pro >> run_autoclicker.bat
echo echo 🚀 شروع Multi AutoClicker Pro... >> run_autoclicker.bat
echo echo. >> run_autoclicker.bat
echo echo 📌 کلیدهای میانبر: >> run_autoclicker.bat
echo echo    Z: تنظیم موقعیت فعال >> run_autoclicker.bat
echo echo    X: شروع/توقف همه >> run_autoclicker.bat
echo echo    C: ریست شمارنده همه >> run_autoclicker.bat
echo echo    F1-F5: انتخاب موقعیت >> run_autoclicker.bat
echo echo    ESC: توقف اضطراری >> run_autoclicker.bat
echo echo. >> run_autoclicker.bat
echo python multi_autoclicker.py >> run_autoclicker.bat
echo pause >> run_autoclicker.bat

echo 📋 ایجاد فایل راهنما...
echo # Multi AutoClicker Pro - راهنمای استفاده > README.md
echo. >> README.md
echo ## 🎯 ویژگی‌ها >> README.md
echo - کلیک خودکار روی 5 موقعیت مختلف >> README.md
echo - تنظیم سرعت جداگانه برای هر موقعیت >> README.md
echo - کنترل کامل با کلیدهای میانبر >> README.md
echo - شمارنده کلیک برای هر موقعیت >> README.md
echo - ذخیره و بارگذاری خودکار تنظیمات >> README.md
echo. >> README.md
echo ## 🎮 کلیدهای میانبر >> README.md
echo - **Z**: تنظیم موقعیت فعال >> README.md
echo - **X**: شروع/توقف همه موقعیت‌ها >> README.md
echo - **C**: ریست همه شمارنده‌ها >> README.md
echo - **F1-F5**: انتخاب سریع موقعیت‌ها >> README.md
echo - **ESC**: توقف اضطراری >> README.md
echo. >> README.md
echo ## 📖 نحوه استفاده >> README.md
echo 1. برنامه را اجرا کنید >> README.md
echo 2. موقعیت مورد نظر را انتخاب کنید >> README.md
echo 3. سرعت کلیک را تنظیم کنید >> README.md
echo 4. دکمه "تنظیم موقعیت" را بزنید >> README.md
echo 5. موقعیت‌های بیشتری اضافه کنید >> README.md
echo 6. "شروع همه" را بزنید >> README.md

echo 🔧 ایجاد فایل تست...
echo import sys > test_requirements.py
echo import importlib >> test_requirements.py
echo. >> test_requirements.py
echo print("🧪 تست کتابخانه‌ها...") >> test_requirements.py
echo print() >> test_requirements.py
echo. >> test_requirements.py
echo modules = ['tkinter', 'threading', 'time', 'json', 'os'] >> test_requirements.py
echo external_modules = ['pyautogui', 'keyboard'] >> test_requirements.py
echo. >> test_requirements.py
echo print("📦 کتابخانه‌های داخلی Python:") >> test_requirements.py
echo for module in modules: >> test_requirements.py
echo     try: >> test_requirements.py
echo         importlib.import_module(module) >> test_requirements.py
echo         print(f"   ✅ {module}") >> test_requirements.py
echo     except ImportError: >> test_requirements.py
echo         print(f"   ❌ {module}") >> test_requirements.py
echo. >> test_requirements.py
echo print() >> test_requirements.py
echo print("🔧 کتابخانه‌های خارجی:") >> test_requirements.py
echo for module in external_modules: >> test_requirements.py
echo     try: >> test_requirements.py
echo         importlib.import_module(module) >> test_requirements.py
echo         print(f"   ✅ {module}") >> test_requirements.py
echo     except ImportError: >> test_requirements.py
echo         print(f"   ❌ {module} - نیاز به نصب") >> test_requirements.py
echo. >> test_requirements.py
echo print() >> test_requirements.py
echo print("✅ تست تکمیل شد!") >> test_requirements.py

echo 📄 ایجاد فایل requirements.txt...
echo pyautogui==0.9.54 > requirements.txt
echo keyboard==0.13.5 >> requirements.txt
echo pillow>=8.0.0 >> requirements.txt

echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                        ✅ نصب موفقیت‌آمیز!                      ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.
echo 🎯 فایل‌های ایجاد شده:
echo    📁 run_autoclicker.bat - راه‌انداز سریع
echo    📁 test_requirements.py - تست کتابخانه‌ها
echo    📁 requirements.txt - لیست کتابخانه‌ها
echo    📁 README.md - راهنمای کامل
echo.
echo 🚀 برای اجرا:
echo    1️⃣  دوبار کلیک روی run_autoclicker.bat
echo    2️⃣  یا python multi_autoclicker.py
echo.
echo 🧪 برای تست کتابخانه‌ها:
echo    python test_requirements.py
echo.
echo 🎮 کلیدهای میانبر جدید:
echo    F1-F5: انتخاب سریع موقعیت‌ها
echo    Z: تنظیم موقعیت
echo    X: شروع/توقف
echo    C: ریست شمارنده‌ها
echo    ESC: توقف اضطراری
echo.

python test_requirements.py

echo.
echo 📌 نکات مهم:
echo    - برنامه را با دسترسی مدیر اجرا کنید
echo    - Windows Defender ممکن است هشدار دهد (طبیعی است)
echo    - فایل positions.json تنظیمات را ذخیره می‌کند
echo.

goto end

:error
echo.
echo ❌ خطا در نصب!
echo 🔧 راه‌حل‌های ممکن:
echo    1. اینترنت را بررسی کنید
echo    2. Python را به‌روزرسانی کنید
echo    3. CMD را با دسترسی مدیر اجرا کنید
echo    4. از pip install --user استفاده کنید
echo.
pause
exit /b 1

:end
echo 🎉 آماده استفاده! موفق باشید!
echo.
pause
