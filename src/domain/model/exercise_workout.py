from datetime import datetime
from typing import List

from bson import ObjectId
from odmantic import Model

from src.domain.enum.days_of_week import DaysOfWeek
from src.domain.enum.workout_status import WorkoutStatus
from src.domain.model.exercise import Exercise
from src.domain.model.exercise_set import ExerciseSet


class ExerciseWorkout(Model):
    name: str
    assigneeId: ObjectId
    assignerId: ObjectId
    startDate: datetime
    endDate: datetime
    status: WorkoutStatus = WorkoutStatus.ACTIVE
    creationDate: datetime = datetime.utcnow()
    exerciseSets: List[ExerciseSet] = list()

    def addExerciseSet(self, setCount: int, repetitionCount: int, recurrentDays: List[DaysOfWeek], exercise: Exercise):
        self.exerciseSets.append(ExerciseSet(id=ObjectId(),
                                             creationDate=datetime.utcnow(),
                                             setCount=setCount,
                                             repetitionCount=repetitionCount,
                                             recurrentDays=recurrentDays,
                                             exercise=exercise))

    def getExerciseSet(self, exerciseSetId: str):
        for exerciseSet in self.exerciseSets:
            if exerciseSet.id == ObjectId(exerciseSetId):
                return exerciseSet
        return None
