from odmantic import ObjectId
from pydantic import BaseModel

from src.application.repository import repository
from src.domain.model.exercise import Exercise


class DeleteExerciseCommand(BaseModel):
    id: str


async def handle(command: DeleteExerciseCommand):
    exercise = await repository.engine.find_one(Exercise, Exercise.id == ObjectId(command.id))
    await repository.engine.delete(exercise)
