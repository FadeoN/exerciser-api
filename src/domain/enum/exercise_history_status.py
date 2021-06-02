from enum import Enum


class ExerciseHistoryStatus(str, Enum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    UNCOMPLETED = "COMPLETED"

    @staticmethod
    def getStatus(setRepetitionCount: int, userRepetitionCount):
        if setRepetitionCount > userRepetitionCount:
            return ExerciseHistoryStatus.FAILED

        return ExerciseHistoryStatus.COMPLETED