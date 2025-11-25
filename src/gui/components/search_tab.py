import tkinter as tk
from tkinter import scrolledtext, messagebox

class SearchTab:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.create_tab()

    def create_tab(self):
        """ایجاد تب جستجو"""
        self.search_frame = tk.Frame(self.parent)
        self.parent.add(self.search_frame, text="🔍 جستجوی دانشجو")

        # کارت جستجو
        search_card = tk.Frame(self.search_frame, bg='white', relief='raised', bd=1)
        search_card.pack(fill='both', expand=True, padx=10, pady=10)

        title = tk.Label(search_card, text="جستجوی دانشجو",
                         font=self.app.subtitle_font, bg='white', fg='#2c3e50')
        title.pack(pady=15)

        # فریم جستجو
        search_input_frame = tk.Frame(search_card, bg='white')
        search_input_frame.pack(padx=20, pady=20, fill='x')

        tk.Label(search_input_frame, text="نوع جستجو:", bg='white',
                 font=self.app.normal_font).pack(side='left', padx=(0, 10))

        self.search_type = tk.StringVar(value="national_id")

        tk.Radiobutton(search_input_frame, text="کد ملی",
                       variable=self.search_type, value="national_id",
                       bg='white', font=self.app.normal_font).pack(side='left', padx=10)

        tk.Radiobutton(search_input_frame, text="شماره دانشجویی",
                       variable=self.search_type, value="student_id",
                       bg='white', font=self.app.normal_font).pack(side='left', padx=10)

        search_entry_frame = tk.Frame(search_card, bg='white')
        search_entry_frame.pack(padx=20, pady=10, fill='x')

        tk.Label(search_entry_frame, text="مقدار جستجو:", bg='white',
                 font=self.app.normal_font, width=15, anchor='e').pack(side='left', padx=(0, 10))

        self.search_entry = tk.Entry(search_entry_frame, font=self.app.normal_font,
                                     width=30, relief='solid', bd=1,
                                     fg='black', insertbackground='black')
        self.search_entry.pack(side='left', fill='x', expand=True)

        tk.Button(search_entry_frame, text="🔍 انجام جستجو",
                  command=self.search_student,
                  bg='#3498db', fg='white', font=self.app.normal_font,
                  relief='flat', padx=15, pady=5).pack(side='left', padx=10)

        # ناحیه نتایج
        results_frame = tk.Frame(search_card, bg='white')
        results_frame.pack(fill='both', expand=True, padx=20, pady=20)

        tk.Label(results_frame, text="نتایج جستجو:", bg='white',
                 font=self.app.subtitle_font).pack(anchor='w')

        self.result_text = scrolledtext.ScrolledText(results_frame,
                                                     height=15,
                                                     font=self.app.normal_font,
                                                     relief='solid', bd=1,
                                                     fg='black', insertbackground='black')
        self.result_text.pack(fill='both', expand=True, pady=10)

    def search_student(self):
        """جستجوی دانشجو"""
        search_value = self.search_entry.get().strip()
        if not search_value:
            messagebox.showerror("خطا", "لطفا مقدار جستجو را وارد کنید!")
            return

        try:
            result = self.app.data_manager.search_student(self.search_type.get(), search_value)
            self.display_search_result(result)
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در جستجو: {str(e)}")

    def display_search_result(self, student):
        """نمایش نتیجه جستجو"""
        self.result_text.delete(1.0, tk.END)

        if student:
            result_str = f"""
╔══════════════════════════════════════╗
║            نتایج جستجو              ║
╠══════════════════════════════════════╣
║ 📝 نام: {student.name}
║ 📝 نام خانوادگی: {student.family}
║ 🆔 کد ملی: {student.national_id}
║ 🎓 رشته تحصیلی: {student.major}
║ 🎫 شماره دانشجویی: {student.student_id}
║ 📞 شماره تماس: {student.phone}
║ 📍 آدرس: {student.address}
╚══════════════════════════════════════╝
"""
            self.result_text.insert(tk.END, result_str)
            self.app.update_status("آخرین عملیات: جستجوی موفق")
        else:
            self.result_text.insert(tk.END, "❌ دانشجوی مورد نظر یافت نشد!")
            self.app.update_status("آخرین عملیات: جستجوی ناموفق")
