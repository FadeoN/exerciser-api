from typing import List

from odmantic import ObjectId
from pydantic import BaseModel

from src.application.exception.not_found_exception import NotFoundException
from src.application.external import video_embedding_service
from src.application.external.response.video_repetition_response import VideoRepetitionResponse
from src.application.repository import repository
from src.domain.enum.exercise_history_status import ExerciseHistoryStatus
from src.domain.model.exercise_workout import ExerciseWorkout
from src.infrastucture.controller.request.add_exercise_history_request import FrameKeypointDTO


class AddExerciseHistoryCommand(BaseModel):
    workoutId: str
    exerciseSetId: str
    width: int
    height: int
    frames: List[FrameKeypointDTO]


async def handle(command: AddExerciseHistoryCommand) -> VideoRepetitionResponse:
    exerciseWorkout = await repository.engine.find_one(ExerciseWorkout, (ExerciseWorkout.id == ObjectId(command.workoutId)))
    if exerciseWorkout is None:
        raise NotFoundException("exerciseWorkout.not.found")
    exerciseSet = exerciseWorkout.getExerciseSet(command.exerciseSetId)
    if exerciseSet is None:
        raise NotFoundException("exerciseSet.not.found")
    response = await video_embedding_service.count_video_exercise_repetition(exerciseId=str(exerciseSet.exercise.id),
                                                                   width=command.width,
                                                                   height=command.height,
                                                                   frames=command.frames,
                                                                   index=str(exerciseSet.exercise.id))

    exerciseHistoryStatus = ExerciseHistoryStatus.getStatus(exerciseSet.repetitionCount, response.count)

    exerciseSet.addExerciseHistory(status=exerciseHistoryStatus,
                                   repetitionCount=response.count)

    await repository.engine.save(exerciseWorkout)

    return response