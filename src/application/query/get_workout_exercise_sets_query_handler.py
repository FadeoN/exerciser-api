from typing import List

from odmantic import ObjectId
from pydantic import BaseModel

from src.application.exception.not_found_exception import NotFoundException
from src.application.repository import repository
from src.domain.model.exercise_set import ExerciseSet
from src.domain.model.exercise_workout import ExerciseWorkout


class GetWorkoutExerciseSetsQuery(BaseModel):
    workoutId: str


async def handle(query: GetWorkoutExerciseSetsQuery) -> List[ExerciseSet]:
    exerciseWorkout = await repository.engine.find_one(ExerciseWorkout, ExerciseWorkout.id == ObjectId(query.workoutId))
    if exerciseWorkout is None:
        raise NotFoundException("exerciseWorkout.not.found")
    return exerciseWorkout.exerciseSets