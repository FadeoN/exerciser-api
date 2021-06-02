from typing import List

from pydantic import BaseModel, Field

from src.infrastucture.controller.request.add_exercise_history_request import FrameKeypointDTO


class VideoSimilarityRequest(BaseModel):
    exerciseId: str
    width: int = Field(default=1, ge=1, description="Width must be more than zero")
    height: int = Field(default=1, ge=1, description="Height must be more than zero")
    frames: List[FrameKeypointDTO]
    index: str
