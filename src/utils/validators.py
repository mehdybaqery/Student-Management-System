def validate_required_fields(fields: dict) -> tuple:
    """
    اعتبارسنجی فیلدهای اجباری
    """
    for field_name, value in fields.items():
        if not value or not value.strip():
            return False, f"فیلد {field_name} نمی‌تواند خالی باشد"

    # اعتبارسنجی کد ملی (10 رقمی)
    national_id = fields.get('national_id', '')
    if len(national_id) != 10 or not national_id.isdigit():
        return False, "کد ملی باید 10 رقم باشد"

    # اعتبارسنجی شماره دانشجویی
    student_id = fields.get('student_id', '')
    if not student_id.isdigit():
        return False, "شماره دانشجویی باید عددی باشد"

    return True, ""


def validate_iranian_national_id(national_id: str) -> bool:
    """
    اعتبارسنجی کد ملی ایران
    """
    if len(national_id) != 10:
        return False

    if not national_id.isdigit():
        return False

    # الگوریتم بررسی کنترل کد ملی
    control_digit = int(national_id[9])
    sum = 0
    for i in range(9):
        sum += int(national_id[i]) * (10 - i)

    remainder = sum % 11
    if remainder < 2:
        return control_digit == remainder
    else:
        return control_digit == (11 - remainder)