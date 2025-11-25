from dataclasses import dataclass

@dataclass
class Student:
    name: str
    family: str
    national_id: str
    major: str
    student_id: str
    phone: str
    address: str
    
    def to_dict(self) -> dict:
        """تبدیل به دیکشنری"""
        return {
            "name": self.name,
            "family": self.family,
            "national_id": self.national_id,
            "major": self.major,
            "student_id": self.student_id,
            "phone": self.phone,
            "address": self.address
        }