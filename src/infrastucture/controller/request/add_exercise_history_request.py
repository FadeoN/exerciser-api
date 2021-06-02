from typing import List

from pydantic import BaseModel


class KeypointDTO(BaseModel):
    name: str
    score: float
    x: float
    y: float


class FrameKeypointDTO(BaseModel):
    keypoints: List[KeypointDTO]


class AddExerciseHistoryRequest(BaseModel):
    width: int
    height: int
    frames: List[FrameKeypointDTO]
