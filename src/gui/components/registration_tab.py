import tkinter as tk
from tkinter import messagebox
from src.utils.validators import validate_required_fields

class RegistrationTab:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.create_tab()

    def create_tab(self):
        """ایجاد تب ثبت نام"""
        self.reg_frame = tk.Frame(self.parent)
        self.parent.add(self.reg_frame, text="📝 ثبت نام جدید")

        # کارت فرم
        form_card = tk.Frame(self.reg_frame, bg='white', relief='raised', bd=1)
        form_card.pack(fill='both', expand=True, padx=10, pady=10)

        title = tk.Label(form_card, text="فرم ثبت اطلاعات دانشجو",
                         font=self.app.subtitle_font, bg='white', fg='#2c3e50')
        title.pack(pady=15)

        # فریم برای فیلدها
        fields_frame = tk.Frame(form_card, bg='white')
        fields_frame.pack(padx=20, pady=10)

        # فیلدهای ورودی
        fields = [
            ("نام", "name"),
            ("نام خانوادگی", "family"),
            ("کد ملی", "national_id"),
            ("رشته تحصیلی", "major"),
            ("شماره دانشجویی", "student_id"),
            ("شماره تماس", "phone"),
            ("آدرس (استان و شهر)", "address")
        ]

        self.entries = {}

        for i, (label_text, field_name) in enumerate(fields):
            row_frame = tk.Frame(fields_frame, bg='white')
            row_frame.grid(row=i, column=0, columnspan=2, sticky='ew', pady=8)

            tk.Label(row_frame, text=label_text, bg='white',
                     font=self.app.normal_font, width=15, anchor='e').pack(side='left', padx=(0, 10))

            entry = tk.Entry(row_frame, font=self.app.normal_font, width=30,
                             relief='solid', bd=1, fg='black', insertbackground='black')
            entry.pack(side='left', fill='x', expand=True)
            self.entries[field_name] = entry

        # دکمه‌ها
        button_frame = tk.Frame(form_card, bg='white')
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="💾 ثبت اطلاعات",
                  command=self.register_student,
                  bg='#27ae60', fg='white', font=self.app.normal_font,
                  relief='flat', padx=20, pady=8).pack(side='left', padx=10)

        tk.Button(button_frame, text="🧹 پاک کردن فرم",
                  command=self.clear_form,
                  bg='#e67e22', fg='white', font=self.app.normal_font,
                  relief='flat', padx=20, pady=8).pack(side='left', padx=10)

    def register_student(self):
        """ثبت دانشجوی جدید"""
        # جمع‌آوری داده‌ها از فرم
        student_data = {}
        for field, entry in self.entries.items():
            value = entry.get().strip()
            if not value:
                messagebox.showerror("خطا", f"لطفا فیلد {field} را پر کنید!")
                return
            student_data[field] = value

        try:
            # ذخیره در فایل JSON
            success = self.app.data_manager.save_student(student_data)
            if success:
                messagebox.showinfo("موفقیت", "✅ اطلاعات دانشجو با موفقیت ثبت شد!")
                self.clear_form()
                self.app.update_status("آخرین عملیات: ثبت دانشجوی جدید")
                # به‌روزرسانی لیست دانشجویان
                if hasattr(self.app, 'students_tab'):
                    self.app.students_tab.load_students_list()
            else:
                messagebox.showerror("خطا", "❌ کد ملی یا شماره دانشجویی تکراری است!")
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در ثبت اطلاعات: {str(e)}")

    def clear_form(self):
        """پاک کردن فرم"""
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.app.update_status("فرم پاک شد")
