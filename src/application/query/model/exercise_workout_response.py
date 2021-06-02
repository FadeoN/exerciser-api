from datetime import datetime

from pydantic import BaseModel

from src.domain.enum.workout_status import WorkoutStatus


class ExerciseWorkoutResponse(BaseModel):
    id: str
    name: str
    assigneeId: str
    assignerId: str
    startDate: datetime
    endDate: datetime
    status: WorkoutStatus
    creationDate: datetime
