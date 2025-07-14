@echo off
chcp 65001 >nul
echo 🚀 نصب Multi AutoClicker Pro...
echo.

echo 📦 نصب کتابخانه‌های مورد نیاز...
pip install keyboard pyautogui pynput psutil

echo.
echo 📝 ایجاد فایل requirements.txt...
echo keyboard==1.13.27> requirements.txt
echo pyautogui==0.9.54>> requirements.txt
echo pynput==1.7.6>> requirements.txt
echo psutil==5.9.5>> requirements.txt

echo.
echo 📝 ایجاد فایل راه‌انداز...
echo @echo off> run_autoclicker.bat
echo chcp 65001 ^>nul>> run_autoclicker.bat
echo title Multi AutoClicker Pro>> run_autoclicker.bat
echo echo 🚀 شروع Multi AutoClicker Pro...>> run_autoclicker.bat
echo echo.>> run_autoclicker.bat
echo echo 📌 کلیدهای میانبر:>> run_autoclicker.bat
echo echo    Z: تنظیم موقعیت فعال>> run_autoclicker.bat
echo echo    X: شروع/توقف همه>> run_autoclicker.bat
echo echo    C: ریست شمارنده همه>> run_autoclicker.bat
echo echo    F1-F5: انتخاب موقعیت>> run_autoclicker.bat
echo echo    ESC: توقف اضطراری>> run_autoclicker.bat
echo echo.>> run_autoclicker.bat
echo python autoclicker.py>> run_autoclicker.bat
echo pause>> run_autoclicker.bat

echo.
echo ✅ نصب با موفقیت انجام شد!
echo 🎯 برای اجرا: run_autoclicker.bat
echo.
pause
