import tkinter as tk
from tkinter import ttk, messagebox

class StudentsTab:
    def __init__(self, parent, app):
        self.parent = parent
        self.app = app
        self.create_tab()
        self.load_students_list()

    def create_tab(self):
        """ایجاد تب لیست دانشجویان"""
        self.list_frame = tk.Frame(self.parent)
        self.parent.add(self.list_frame, text="👥 لیست دانشجویان")

        # کارت لیست
        list_card = tk.Frame(self.list_frame, bg='white', relief='raised', bd=1)
        list_card.pack(fill='both', expand=True, padx=10, pady=10)

        title = tk.Label(list_card, text="لیست تمام دانشجویان ثبت‌شده",
                         font=self.app.subtitle_font, bg='white', fg='#2c3e50')
        title.pack(pady=15)

        # دکمه بارگذاری مجدد
        btn_frame = tk.Frame(list_card, bg='white')
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="🔄 بارگذاری مجدد",
                  command=self.load_students_list,
                  bg='#3498db', fg='white', font=self.app.normal_font,
                  relief='flat', padx=15, pady=5).pack()

        # جدول دانشجویان
        table_frame = tk.Frame(list_card, bg='white')
        table_frame.pack(fill='both', expand=True, padx=20, pady=10)

        # ایجاد Treeview برای نمایش جدولی
        columns = ('name', 'family', 'national_id', 'student_id', 'major')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', height=15)

        # تعریف هدرها
        self.tree.heading('name', text='نام')
        self.tree.heading('family', text='نام خانوادگی')
        self.tree.heading('national_id', text='کد ملی')
        self.tree.heading('student_id', text='شماره دانشجویی')
        self.tree.heading('major', text='رشته')

        # تنظیم عرض ستون‌ها
        self.tree.column('name', width=100)
        self.tree.column('family', width=120)
        self.tree.column('national_id', width=100)
        self.tree.column('student_id', width=120)
        self.tree.column('major', width=150)

        self.tree.pack(fill='both', expand=True)

        # اسکرول بار برای Treeview
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side='right', fill='y')

    def load_students_list(self):
        """بارگذاری لیست دانشجویان"""
        # پاک کردن جدول موجود
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            students = self.app.data_manager.load_students()
            
            for student in students:
                self.tree.insert('', tk.END, values=(
                    student.name,
                    student.family,
                    student.national_id,
                    student.student_id,
                    student.major
                ))

            self.app.update_status(f"تعداد دانشجویان: {len(students)}")
        except Exception as e:
            messagebox.showerror("خطا", f"خطا در بارگذاری لیست: {str(e)}")
