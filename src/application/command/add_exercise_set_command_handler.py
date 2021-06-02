from typing import List

from odmantic import ObjectId
from pydantic import BaseModel

from src.application.repository import repository
from src.domain.enum.days_of_week import DaysOfWeek
from src.domain.model.exercise import Exercise
from src.domain.model.exercise_set import ExerciseSet
from src.domain.model.exercise_workout import ExerciseWorkout


class AddExerciseSetCommand(BaseModel):
    workoutId: str
    setCount: int
    repetitionCount: int
    recurrentDays: List[DaysOfWeek]
    exerciseId: str


async def handle(command: AddExerciseSetCommand):
    exerciseWorkout = await repository.engine.find_one(ExerciseWorkout, ExerciseWorkout.id == ObjectId(command.workoutId))
    if exerciseWorkout is None:
        raise NotFoundException("exerciseWorkout.not.found")

    exercise = await repository.engine.find_one(Exercise, Exercise.id == ObjectId(command.exerciseId))
    if exercise is None:
        raise NotFoundException("exercise.not.found")

    exerciseWorkout.addExerciseSet(ExerciseSet(setCount=command.setCount,
                                               repetitionCount=command.repetitionCount,
                                               recurrentDays=command.recurrentDays,
                                               exercise=exercise))
    await repository.engine.save(exerciseWorkout)
