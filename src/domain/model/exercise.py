from datetime import datetime

from odmantic import Model

from src.domain.enum.exercise_difficulty import ExerciseDifficulty


class Exercise(Model):
    name: str
    difficulty: ExerciseDifficulty
    imageUrl: str
    videoUrl: str
    creationDate: datetime = datetime.utcnow()