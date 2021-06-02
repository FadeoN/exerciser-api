from enum import Enum


class UserRole(str, Enum):
    PATIENT = "Patient"
    DOCTOR = "Doctor"
    ADMIN = "Admin"

    @staticmethod
    def map():
        return {c.name: c.value for c in UserRole}