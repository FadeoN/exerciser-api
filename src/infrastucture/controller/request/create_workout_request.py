from datetime import datetime

from pydantic import BaseModel


class CreateWorkoutRequest(BaseModel):
    name: str
    assigneeId: str
    assignerId: str
    startDate: datetime
    endDate: datetime