from typing import List

from pydantic import BaseModel

from src.application.repository import repository
from src.domain.model.exercise import Exercise


class GetAllExercisesQuery(BaseModel):
    pass


async def handle(query: GetAllExercisesQuery) -> List[Exercise]:
    return await repository.engine.find(Exercise)