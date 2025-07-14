import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui
import time
import threading
import keyboard
import pynput
from pynput import mouse, keyboard as kb
import json
import os

class MultiAutoClicker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multi AutoClicker Pro")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # متغیرها
        self.is_running = False
        self.click_positions = []
        self.delay = 1.0
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Multi AutoClicker Pro", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Position Frame
        pos_frame = ttk.LabelFrame(main_frame, text="موقعیت‌های کلیک", padding="10")
        pos_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Position List
        self.pos_listbox = tk.Listbox(pos_frame, height=8, width=50)
        self.pos_listbox.grid(row=0, column=0, columnspan=3, pady=5)
        
        # Buttons
        ttk.Button(pos_frame, text="افزودن موقعیت", 
                  command=self.add_position).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(pos_frame, text="حذف موقعیت", 
                  command=self.remove_position).grid(row=1, column=1, padx=5, pady=5)
        ttk.Button(pos_frame, text="پاک کردن همه", 
                  command=self.clear_positions).grid(row=1, column=2, padx=5, pady=5)
        
        # Settings Frame
        settings_frame = ttk.LabelFrame(main_frame, text="تنظیمات", padding="10")
        settings_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=10)
        
        # Delay
        ttk.Label(settings_frame, text="تاخیر (ثانیه):").grid(row=0, column=0, sticky=tk.W)
        self.delay_var = tk.StringVar(value="1.0")
        ttk.Entry(settings_frame, textvariable=self.delay_var, width=10).grid(row=0, column=1, padx=10)
        
        # Control Buttons
        control_frame = ttk.Frame(main_frame)
        control_frame.grid(row=3, column=0, columnspan=3, pady=20)
        
        self.start_btn = ttk.Button(control_frame, text="شروع (F6)", 
                                   command=self.start_clicking, style="Accent.TButton")
        self.start_btn.grid(row=0, column=0, padx=10)
        
        self.stop_btn = ttk.Button(control_frame, text="توقف (F7)", 
                                  command=self.stop_clicking, state="disabled")
        self.stop_btn.grid(row=0, column=1, padx=10)
        
        # Status
        self.status_var = tk.StringVar(value="آماده")
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=4, column=0, columnspan=3, pady=10)
        
        # Hotkeys
        keyboard.add_hotkey('f6', self.start_clicking)
        keyboard.add_hotkey('f7', self.stop_clicking)
        
    def add_position(self):
        self.status_var.set("روی موقعیت مورد نظر کلیک کنید...")
        self.root.after(2000, self.capture_position)
        
    def capture_position(self):
        listener = mouse.Listener(on_click=self.on_click)
        listener.start()
        
    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_positions.append((x, y))
            self.pos_listbox.insert(tk.END, f"موقعیت {len(self.click_positions)}: ({x}, {y})")
            self.status_var.set(f"موقعیت ({x}, {y}) اضافه شد")
            return False
            
    def remove_position(self):
        selection = self.pos_listbox.curselection()
        if selection:
            index = selection[0]
            del self.click_positions[index]
            self.pos_listbox.delete(index)
            self.status_var.set("موقعیت حذف شد")
            
    def clear_positions(self):
        self.click_positions.clear()
        self.pos_listbox.delete(0, tk.END)
        self.status_var.set("تمام موقعیت‌ها پاک شد")
        
    def start_clicking(self):
        if not self.click_positions:
            messagebox.showwarning("هشدار", "لطفاً حداقل یک موقعیت اضافه کنید!")
            return
            
        try:
            self.delay = float(self.delay_var.get())
        except ValueError:
            messagebox.showerror("خطا", "تاخیر باید عدد باشد!")
            return
            
        self.is_running = True
        self.start_btn.config(state="disabled")
        self.stop_btn.config(state="normal")
        self.status_var.set("در حال کلیک کردن...")
        
        # شروع thread برای کلیک
        self.click_thread = threading.Thread(target=self.click_loop)
        self.click_thread.daemon = True
        self.click_thread.start()
        
    def stop_clicking(self):
        self.is_running = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")
        self.status_var.set("متوقف شد")
        
    def click_loop(self):
        while self.is_running:
            for x, y in self.click_positions:
                if not self.is_running:
                    break
                pyautogui.click(x, y)
                time.sleep(self.delay)
                
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MultiAutoClicker()
    app.run()
