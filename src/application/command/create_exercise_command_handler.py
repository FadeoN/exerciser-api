from datetime import datetime

from pydantic import BaseModel

from src.application.repository import repository
from src.domain.enum.exercise_difficulty import ExerciseDifficulty
from src.domain.model.exercise import Exercise


class CreateExerciseCommand(BaseModel):
    name: str
    difficulty: ExerciseDifficulty
    imageUrl: str
    videoUrl: str


async def handle(command: CreateExerciseCommand):
    await repository.engine.save(Exercise(name=command.name,
                               difficulty=command.difficulty,
                               imageUrl=command.imageUrl,
                               videoUrl=command.videoUrl,
                               creationDate=datetime.utcnow()))
