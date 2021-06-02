from pydantic import BaseModel


class VideoRepetitionResponse(BaseModel):
    count: int