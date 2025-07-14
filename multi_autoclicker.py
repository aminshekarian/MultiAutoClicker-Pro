import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import pyautogui
import keyboard
import json
import os

class MultiAutoClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multi AutoClicker - بورس")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # متغیرها
        self.clicking = False
        self.click_positions = []  # لیست موقعیت‌های کلیک
        self.click_speeds = []     # سرعت هر موقعیت
        self.click_counts = []     # تعداد کلیک هر موقعیت
        self.current_position = 0  # موقعیت فعلی برای تنظیم
        
        self.setup_ui()
        self.setup_hotkeys()
        self.load_positions()
        
    def setup_ui(self):
        # عنوان
        title_label = tk.Label(self.root, text="🎯 Multi AutoClicker Pro", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # فریم کنترل
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        # انتخاب موقعیت
        tk.Label(control_frame, text="موقعیت فعال:").pack(side=tk.LEFT)
        self.position_var = tk.StringVar(value="1")
        position_combo = ttk.Combobox(control_frame, textvariable=self.position_var, 
                                     values=["1", "2", "3", "4", "5"], width=5)
        position_combo.pack(side=tk.LEFT, padx=5)
        position_combo.bind('<<ComboboxSelected>>', self.on_position_change)
        
        # سرعت کلیک
        tk.Label(control_frame, text="سرعت:").pack(side=tk.LEFT, padx=(20,0))
        self.speed_var = tk.StringVar(value="0.1")
        speed_entry = tk.Entry(control_frame, textvariable=self.speed_var, width=8)
        speed_entry.pack(side=tk.LEFT, padx=5)
        
        # دکمه به‌روزرسانی سرعت
        update_speed_btn = tk.Button(control_frame, text="✓", 
                                    command=self.update_current_speed,
                                    bg="lightgreen", font=("Arial", 10))
        update_speed_btn.pack(side=tk.LEFT, padx=2)
        
        # دکمه‌های کنترل
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=20)
        
        self.start_btn = tk.Button(btn_frame, text="▶️ شروع همه", 
                                  command=self.toggle_clicking,
                                  bg="green", fg="white", font=("Arial", 12))
        self.start_btn.pack(side=tk.LEFT, padx=5)
        
        self.set_pos_btn = tk.Button(btn_frame, text="🎯 تنظیم موقعیت", 
                                    command=self.set_current_position,
                                    bg="blue", fg="white", font=("Arial", 12))
        self.set_pos_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = tk.Button(btn_frame, text="🗑️ پاک کردن", 
                                  command=self.clear_current_position,
                                  bg="orange", fg="white", font=("Arial", 12))
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # جدول موقعیت‌ها
        self.setup_positions_table()
        
        # وضعیت
        status_frame = tk.Frame(self.root)
        status_frame.pack(pady=10)
        
        self.status_label = tk.Label(status_frame, text="⏹️ متوقف", 
                                    font=("Arial", 12, "bold"))
        self.status_label.pack()
        
        # راهنمای کلیدها
        help_frame = tk.Frame(self.root)
        help_frame.pack(pady=10)
        
        help_text = """
🎮 کلیدهای میانبر:
Z: تنظیم موقعیت فعال
X: شروع/توقف همه
C: ریست شمارنده همه
F1-F5: انتخاب موقعیت (F1=موقعیت1, F2=موقعیت2, ...)
ESC: توقف اضطراری
        """
        help_label = tk.Label(help_frame, text=help_text, 
                             font=("Arial", 9), justify=tk.LEFT)
        help_label.pack()
        
        # بروزرسانی موقعیت ماوس
        self.update_mouse_position()
        
    def setup_positions_table(self):
        """جدول موقعیت‌ها"""
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10)
        
        # عنوان جدول
        tk.Label(table_frame, text="📊 موقعیت‌های کلیک", 
                font=("Arial", 12, "bold")).pack()
        
        # جدول
        columns = ("موقعیت", "مختصات", "سرعت", "تعداد کلیک")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=6)
        
        # عنوان ستون‌ها
        self.tree.heading("موقعیت", text="موقعیت")
        self.tree.heading("مختصات", text="مختصات (X, Y)")
        self.tree.heading("سرعت", text="سرعت (ثانیه)")
        self.tree.heading("تعداد کلیک", text="تعداد کلیک")
        
        # عرض ستون‌ها
        self.tree.column("موقعیت", width=80)
        self.tree.column("مختصات", width=150)
        self.tree.column("سرعت", width=100)
        self.tree.column("تعداد کلیک", width=100)
        
        self.tree.pack()
        
        # اضافه کردن 5 موقعیت خالی
        for i in range(5):
            self.tree.insert("", "end", values=(f"موقعیت {i+1}", "تنظیم نشده", "0.1", "0"))
            
    def setup_hotkeys(self):
        """تنظیم کلیدهای میانبر"""
        try:
            keyboard.add_hotkey('z', self.set_current_position)
            keyboard.add_hotkey('x', self.toggle_clicking)
            keyboard.add_hotkey('c', self.reset_all_counters)
            keyboard.add_hotkey('esc', self.emergency_stop)
            
            # کلیدهای انتخاب موقعیت - F1 تا F5
            keyboard.add_hotkey('f1', lambda: self.select_position(1))
            keyboard.add_hotkey('f2', lambda: self.select_position(2))
            keyboard.add_hotkey('f3', lambda: self.select_position(3))
            keyboard.add_hotkey('f4', lambda: self.select_position(4))
            keyboard.add_hotkey('f5', lambda: self.select_position(5))
            
        except Exception as e:
            print(f"Error setting up hotkeys: {e}")
            
    def select_position(self, pos):
        """انتخاب موقعیت"""
        self.position_var.set(str(pos))
        self.current_position = pos - 1
        self.update_speed_display()
        print(f"موقعیت {pos} انتخاب شد")
        
    def on_position_change(self, event=None):
        """تغییر موقعیت فعال"""
        self.current_position = int(self.position_var.get()) - 1
        self.update_speed_display()
        
    def update_speed_display(self):
        """بروزرسانی نمایش سرعت"""
        if self.current_position < len(self.click_speeds):
            self.speed_var.set(str(self.click_speeds[self.current_position]))
        else:
            self.speed_var.set("0.1")
            
    def update_current_speed(self):
        """به‌روزرسانی سرعت موقعیت فعال"""
        try:
            new_speed = float(self.speed_var.get())
            
            # گسترش لیست در صورت نیاز
            while len(self.click_speeds) <= self.current_position:
                self.click_speeds.append(0.1)
                
            self.click_speeds[self.current_position] = new_speed
            self.update_table()
            self.save_positions()
            print(f"سرعت موقعیت {self.current_position + 1} به {new_speed} تغییر کرد")
            
        except ValueError:
            messagebox.showerror("خطا", "لطفاً یک عدد معتبر وارد کنید")
            
    def update_mouse_position(self):
        """بروزرسانی موقعیت ماوس"""
        try:
            if not self.clicking:
                x, y = pyautogui.position()
                self.status_label.config(text=f"موقعیت ماوس: ({x}, {y}) | فعال: موقعیت {self.current_position + 1}")
        except Exception as e:
            print(f"Error updating mouse position: {e}")
        finally:
            self.root.after(100, self.update_mouse_position)
            
    def set_current_position(self):
        """تنظیم موقعیت فعال"""
        if self.clicking:
            return
            
        pos_num = self.current_position + 1
        messagebox.showinfo("تنظیم موقعیت", 
                           f"ماوس را برای موقعیت {pos_num} در جای مناسب قرار دهید و 3 ثانیه صبر کنید...")
        
        def capture_position():
            time.sleep(3)
            x, y = pyautogui.position()
            
            # گسترش لیست‌ها در صورت نیاز
            while len(self.click_positions) <= self.current_position:
                self.click_positions.append((0, 0))
                self.click_speeds.append(0.1)
                self.click_counts.append(0)
            
            # تنظیم موقعیت و سرعت
            self.click_positions[self.current_position] = (x, y)
            try:
                self.click_speeds[self.current_position] = float(self.speed_var.get())
            except ValueError:
                self.click_speeds[self.current_position] = 0.1
            
            # بروزرسانی جدول
            self.update_table()
            self.save_positions()
            print(f"موقعیت {pos_num} در ({x}, {y}) تنظیم شد")
            
        threading.Thread(target=capture_position, daemon=True).start()
        
    def clear_current_position(self):
        """پاک کردن موقعیت فعال"""
        if self.current_position < len(self.click_positions):
            self.click_positions[self.current_position] = (0, 0)
            self.click_counts[self.current_position] = 0
            self.update_table()
            self.save_positions()
            print(f"موقعیت {self.current_position + 1} پاک شد")
            
    def update_table(self):
        """بروزرسانی جدول"""
        for i in range(5):
            if i < len(self.click_positions) and self.click_positions[i] != (0, 0):
                x, y = self.click_positions[i]
                speed = self.click_speeds[i] if i < len(self.click_speeds) else 0.1
                count = self.click_counts[i] if i < len(self.click_counts) else 0
                
                self.tree.item(self.tree.get_children()[i], 
                              values=(f"موقعیت {i+1}", f"({x}, {y})", f"{speed}", f"{count}"))
            else:
                self.tree.item(self.tree.get_children()[i], 
                              values=(f"موقعیت {i+1}", "تنظیم نشده", "0.1", "0"))
                
    def toggle_clicking(self):
        """شروع/توقف کلیک"""
        if self.clicking:
            self.stop_clicking()
        else:
            self.start_clicking()
            
    def start_clicking(self):
        """شروع کلیک همه موقعیت‌ها"""
        # بررسی وجود موقعیت‌های تنظیم شده
        active_positions = [(i, pos) for i, pos in enumerate(self.click_positions) if pos != (0, 0)]
        
        if not active_positions:
            messagebox.showwarning("هشدار", "ابتدا حداقل یک موقعیت تنظیم کنید!")
            return
        
        self.clicking = True
        self.status_label.config(text="▶️ همه موقعیت‌ها در حال اجرا", fg="green")
        self.start_btn.config(text="⏸️ توقف همه", bg="red")
        
        # شروع کلیک برای هر موقعیت در thread جداگانه
        for i, (x, y) in active_positions:
            threading.Thread(target=self.click_loop, args=(i, x, y), daemon=True).start()
            
    def stop_clicking(self):
        """توقف کلیک همه موقعیت‌ها"""
        self.clicking = False
        self.status_label.config(text="⏹️ متوقف", fg="red")
        self.start_btn.config(text="▶️ شروع همه", bg="green")
        
    def emergency_stop(self):
        """توقف اضطراری"""
        self.clicking = False
        self.status_label.config(text="🚨 توقف اضطراری", fg="red")
        self.start_btn.config(text="▶️ شروع همه", bg="green")
        
    def reset_all_counters(self):
        """ریست همه شمارنده‌ها"""
        for i in range(len(self.click_counts)):
            self.click_counts[i] = 0
        self.update_table()
        print("همه شمارنده‌ها ریست شدند")
        
    def click_loop(self, position_index, x, y):
        """حلقه کلیک برای یک موقعیت"""
        speed = self.click_speeds[position_index] if position_index < len(self.click_speeds) else 0.1
        
        while self.clicking:
            try:
                pyautogui.click(x, y)
                if position_index < len(self.click_counts):
                    self.click_counts[position_index] += 1
                    self.update_table()
                time.sleep(speed)
            except Exception as e:
                print(f"خطا در کلیک موقعیت {position_index + 1}: {e}")
                break
                
    def save_positions(self):
        """ذخیره موقعیت‌ها"""
        data = {
            'positions': self.click_positions,
            'speeds': self.click_speeds,
            'counts': self.click_counts
        }
        try:
            with open('positions.json', 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"خطا در ذخیره: {e}")
            
    def load_positions(self):
        """بارگذاری موقعیت‌ها"""
        try:
            if os.path.exists('positions.json'):
                with open('positions.json', 'r') as f:
                    data = json.load(f)
                    self.click_positions = data.get('positions', [])
                    self.click_speeds = data.get('speeds', [])
                    self.click_counts = data.get('counts', [])
                    self.update_table()
        except Exception as e:
            print(f"خطا در بارگذاری: {e}")
            
    def run(self):
        """اجرای برنامه"""
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.emergency_stop()
            
if __name__ == "__main__":
    print("🚀 Multi AutoClicker Pro در حال شروع...")
    print("📌 کلیدهای میانبر:")
    print("   Z: تنظیم موقعیت فعال")
    print("   X: شروع/توقف همه")
    print("   C: ریست شمارنده همه")
    print("   F1-F5: انتخاب موقعیت")
    print("   ESC: توقف اضطراری")
    
    try:
        app = MultiAutoClicker()
        app.run()
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")
