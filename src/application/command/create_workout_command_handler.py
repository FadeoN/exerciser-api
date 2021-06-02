from datetime import datetime

from odmantic import ObjectId

from src.application.repository import repository
from pydantic import BaseModel

from src.domain.model.exercise_workout import ExerciseWorkout


class CreateExerciseWorkoutCommand(BaseModel):
    name: str
    assigneeId: str
    assignerId: str
    startDate: datetime
    endDate: datetime


async def handle(command: CreateExerciseWorkoutCommand):
    await repository.engine.save(ExerciseWorkout(name=command.name,
                                      assigneeId=ObjectId(command.assigneeId),
                                      assignerId=ObjectId(command.assignerId),
                                      startDate=command.startDate,
                                      endDate=command.endDate))