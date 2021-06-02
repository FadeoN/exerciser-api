from pydantic.main import BaseModel


class IndexExerciseVideoRequest(BaseModel):
    exerciseId: str
    exerciseName: str
    url: str
    tag: str
    index: str
