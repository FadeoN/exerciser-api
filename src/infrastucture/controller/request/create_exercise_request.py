from pydantic import BaseModel, HttpUrl

from src.domain.enum.exercise_difficulty import ExerciseDifficulty


class CreateExerciseRequest(BaseModel):
    name: str
    difficulty: ExerciseDifficulty
    imageUrl: HttpUrl
    videoUrl: HttpUrl
