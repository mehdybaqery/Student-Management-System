import tkinter as tk
from tkinter import ttk
from .components.header import Header
from .components.registration_tab import RegistrationTab
from .components.search_tab import SearchTab
from .components.students_tab import StudentsTab
from .themes import ThemeManager
from src.data.data_manager import DataManager


class ModernStudentRegistrationSystem:
    def __init__(self, root):
        self.root = root
        self.setup_window()

        # Initialize managers
        self.theme_manager = ThemeManager()
        self.data_manager = DataManager()

        self.setup_fonts()
        self.create_widgets()
        self.apply_theme()

    def setup_window(self):
        """تنظیمات پنجره اصلی"""
        self.root.title("🎓 سیستم مدیریت دانشجویان")
        self.root.geometry("800x700")
        self.root.configure(bg='#f0f2f5')

    def setup_fonts(self):
        """تنظیم فونت‌ها"""
        self.title_font = ("Helvetica", 16, "bold")
        self.subtitle_font = ("Helvetica", 12, "bold")
        self.normal_font = ("Helvetica", 10)

    def create_widgets(self):
        """ایجاد ویجت‌های اصلی"""
        # هدر
        self.header = Header(self.root, self)

        # نوت‌بوک
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=20, pady=10)

        # ایجاد تب‌ها
        self.registration_tab = RegistrationTab(self.notebook, self)
        self.search_tab = SearchTab(self.notebook, self)
        self.students_tab = StudentsTab(self.notebook, self)

        # نوار وضعیت
        self.create_status_bar()

    def create_status_bar(self):
        """ایجاد نوار وضعیت"""
        self.status_frame = tk.Frame(self.root, bg='#bdc3c7', height=25)
        self.status_frame.pack(fill='x', side='bottom')
        self.status_frame.pack_propagate(False)

        self.status_label = tk.Label(self.status_frame, text="آماده",
                                     bg='#bdc3c7', fg='#2c3e50', font=self.normal_font)
        self.status_label.pack(side='left', padx=10)

    def apply_theme(self):
        """اعمال تم فعلی"""
        self.theme_manager.apply_theme(self.root)

    def toggle_theme(self):
        """تغییر تم"""
        self.theme_manager.toggle_theme()
        self.apply_theme()
        self.header.update_theme_button()
        self.status_label.config(text="تم برنامه تغییر کرد")

    def update_status(self, message):
        """به‌روزرسانی نوار وضعیت"""
        self.status_label.config(text=message)