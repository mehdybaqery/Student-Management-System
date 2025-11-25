import json
import os
from typing import List, Dict, Optional
from .models import Student

class DataManager:
    def __init__(self, data_file: str = "students_data.json"):
        self.data_file = data_file
        self._initialize_data_file()

    def _initialize_data_file(self):
        """ایجاد فایل داده اگر وجود ندارد"""
        if not os.path.exists(self.data_file):
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump({"students": []}, f, ensure_ascii=False, indent=4)

    def load_students(self) -> List[Student]:
        """بارگذاری تمام دانشجویان"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return [Student(**student) for student in data.get("students", [])]
        except Exception as e:
            raise Exception(f"خطا در بارگذاری داده‌ها: {str(e)}")

    def save_student(self, student_data: Dict) -> bool:
        """ذخیره دانشجوی جدید"""
        try:
            data = self._load_raw_data()
            
            # بررسی یکتایی
            if self._is_duplicate(student_data, data["students"]):
                return False
                
            data["students"].append(student_data)
            self._save_raw_data(data)
            return True
        except Exception as e:
            raise Exception(f"خطا در ذخیره‌سازی: {str(e)}")

    def search_student(self, search_type: str, search_value: str) -> Optional[Student]:
        """جستجوی دانشجو"""
        students = self.load_students()
        for student in students:
            if getattr(student, search_type) == search_value:
                return student
        return None

    def _load_raw_data(self) -> Dict:
        """بارگذاری داده خام"""
        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_raw_data(self, data: Dict):
        """ذخیره داده خام"""
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def _is_duplicate(self, new_student: Dict, existing_students: List) -> bool:
        """بررسی تکراری نبودن داده‌ها"""
        for student in existing_students:
            if student["national_id"] == new_student["national_id"]:
                return True
            if student["student_id"] == new_student["student_id"]:
                return True
        return False