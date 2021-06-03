# TODO: exerciseId: int to string
from typing import List

import httpx

from src.application.external.request.index_exercise_video_request import IndexExerciseVideoRequest
from src.application.external.request.video_similarity_request import VideoSimilarityRequest
from src.application.external.response.video_repetition_response import VideoRepetitionResponse
from src.infrastucture.configuration import APP_OPTIONS
from src.infrastucture.controller.request.add_exercise_history_request import FrameKeypointDTO


async def index_exercise_video_request(exerciseId: str, exerciseName: str, url: str, tag: str, index: str):
    async with httpx.AsyncClient() as client:
        request = IndexExerciseVideoRequest(exerciseId=exerciseId,
                                            exerciseName=exerciseName,
                                            url=url,
                                            tag=tag,
                                            index=index)
        endpoint = f"{APP_OPTIONS.video_embedding_api_options.url}/index/exercise"
        await client.post(endpoint, data=request.json())


async def count_video_exercise_repetition(exerciseId: str, width: int, height: int, frames: List[FrameKeypointDTO], index: str) -> VideoRepetitionResponse:
    async with httpx.AsyncClient(timeout=APP_OPTIONS.video_embedding_api_options.timeout) as client:
    
         request = VideoSimilarityRequest(exerciseId=exerciseId,
                                         width=width,
                                          height=height,
                                          frames=frames,
                                          index=index)
    
         endpoint = f"{APP_OPTIONS.video_embedding_api_options.url}/similarities/video"
         response = await client.post(endpoint, data=request.json())
    
    return VideoRepetitionResponse.parse_raw(response.content)
