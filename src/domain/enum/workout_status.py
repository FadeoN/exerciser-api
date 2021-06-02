from enum import Enum


class WorkoutStatus(str, Enum):
    ACTIVE = "Active"
    COMPLETED = "Completed"