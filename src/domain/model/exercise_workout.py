from datetime import datetime
from typing import List

from bson import ObjectId
from odmantic import Model

from src.domain.enum.workout_status import WorkoutStatus
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

    def addExerciseSet(self, exerciseSet: ExerciseSet):
        self.exerciseSets.append(exerciseSet)

    def getExerciseSet(self, exerciseSetId: str):
        for exerciseSet in self.exerciseSets:
            if exerciseSet.id == ObjectId(exerciseSetId):
                return exerciseSet
        return None
