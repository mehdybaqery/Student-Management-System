def format_student_display(student) -> str:
    """
    فرمت‌بندی نمایش دانشجو
    """
    return f"""
╔══════════════════════════════════════╗
║            اطلاعات دانشجو           ║
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

def get_student_count() -> int:
    """
    دریافت تعداد دانشجویان
    """
    try:
        from src.data.data_manager import DataManager
        dm = DataManager()
        students = dm.load_students()
        return len(students)
    except:
        return 0