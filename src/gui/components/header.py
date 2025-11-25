import tkinter as tk

class Header:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.create_header()

    def create_header(self):
        """ایجاد هدر"""
        self.header_frame = tk.Frame(self.parent, bg='#3498db', height=80)
        self.header_frame.pack(fill='x', padx=0, pady=0)
        self.header_frame.pack_propagate(False)

        # عنوان
        title_label = tk.Label(self.header_frame, text="🎓 سیستم مدیریت دانشجویان",
                             font=self.app.title_font, bg='#3498db', fg='white')
        title_label.pack(side='left', padx=20, pady=20)

        # دکمه تغییر تم
        self.theme_btn = tk.Button(self.header_frame, text=self.get_theme_button_text(),
                                 command=self.app.toggle_theme,
                                 font=self.app.normal_font, bg='#2980b9', fg='white',
                                 relief='flat', padx=10)
        self.theme_btn.pack(side='right', padx=20, pady=20)

    def get_theme_button_text(self):
        """دریافت متن دکمه تم"""
        theme_mode = self.app.theme_manager.get_theme_mode()
        return "☀️ تم روشن" if theme_mode == "dark" else "🌙 تم تاریک"

    def update_theme_button(self):
        """به‌روزرسانی دکمه تم"""
        self.theme_btn.config(text=self.get_theme_button_text())