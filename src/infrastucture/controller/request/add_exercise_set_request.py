from typing import List

from pydantic import BaseModel, HttpUrl, Field

from src.domain.enum.days_of_week import DaysOfWeek


class AddExerciseSetRequest(BaseModel):
    setCount: int = Field(default=1, ge=1, description="Set count must be more than zero")
    repetitionCount: int = Field(default=1, ge=1, description="Repetition count must be more than zero")
    recurrentDays: List[DaysOfWeek]
    exerciseId: str
