from datetime import datetime
from typing import List

from odmantic import EmbeddedModel, Reference, ObjectId

from src.domain.enum.days_of_week import DaysOfWeek
from src.domain.enum.exercise_history_status import ExerciseHistoryStatus
from src.domain.model.exercise import Exercise


class ExerciseHistory(EmbeddedModel):
    id: ObjectId = ObjectId()
    status: ExerciseHistoryStatus
    repetitionCount: int
    creationDate: datetime = datetime.utcnow()


class ExerciseSet(EmbeddedModel):
    id: ObjectId = ObjectId()
    setCount: int
    repetitionCount: int
    recurrentDays: List[DaysOfWeek]
    history: List[ExerciseHistory] = list()
    exercise: Exercise = Reference()
    creationDate: datetime = datetime.utcnow()

    def addExerciseHistory(self, status: ExerciseHistoryStatus, repetitionCount: int):
        self.history.append(ExerciseHistory(status=status,
                                            repetitionCount=repetitionCount))

