from typing import Optional, List

from fastapi import APIRouter
from starlette import status

from src.application.command import create_workout_command_handler, add_exercise_set_command_handler, \
    add_exercise_history_command_handler
from src.application.command.add_exercise_history_command_handler import AddExerciseHistoryCommand
from src.application.command.add_exercise_set_command_handler import AddExerciseSetCommand
from src.application.command.create_workout_command_handler import CreateExerciseWorkoutCommand
from src.application.external.response.video_repetition_response import VideoRepetitionResponse
from src.application.query import get_exercise_workout_query_handler, get_workout_exercise_sets_query_handler
from src.application.query.get_exercise_workout_query_handler import GetExerciseWorkoutQuery
from src.application.query.get_workout_exercise_sets_query_handler import GetWorkoutExerciseSetsQuery
from src.domain.model.exercise_set import ExerciseSet
from src.domain.model.exercise_workout import ExerciseWorkout
from src.infrastucture.controller.request.add_exercise_history_request import AddExerciseHistoryRequest
from src.infrastucture.controller.request.add_exercise_set_request import AddExerciseSetRequest
from src.infrastucture.controller.request.create_workout_request import CreateWorkoutRequest

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: CreateWorkoutRequest):
    await create_workout_command_handler.handle(CreateExerciseWorkoutCommand(name=request.name,
                                                                            assigneeId=request.assigneeId,
                                                                            assignerId=request.assignerId,
                                                                            startDate=request.startDate,
                                                                            endDate=request.endDate))

@router.get("", status_code=status.HTTP_200_OK)
async def get_all(assigneeId: Optional[str] = None, assignerId: Optional[str] = None) -> List[ExerciseWorkout]:
    return await get_exercise_workout_query_handler.handle(GetExerciseWorkoutQuery(assigneeId=assigneeId,
                                                                                   assignerId=assignerId))


@router.post("/{workoutId}:addExerciseSet", status_code=status.HTTP_201_CREATED)
async def add_exercise_set(workoutId: str, request: AddExerciseSetRequest):
    await add_exercise_set_command_handler.handle(AddExerciseSetCommand(workoutId=workoutId,
                                                                        setCount=request.setCount,
                                                                        repetitionCount=request.repetitionCount,
                                                                        recurrentDays=request.recurrentDays,
                                                                        exerciseId=request.exerciseId))

@router.get("/{workoutId}/exerciseSets", status_code=status.HTTP_200_OK)
async def get_workout_exercise_sets(workoutId: str) -> List[ExerciseSet]:
    return await get_workout_exercise_sets_query_handler.handle(GetWorkoutExerciseSetsQuery(workoutId=workoutId))

@router.post("/{workoutId}/exerciseSets/{exerciseSetId}:addHistory", status_code=status.HTTP_201_CREATED)
async def add_exercise_history(workoutId: str, exerciseSetId: str, request: AddExerciseHistoryRequest) -> VideoRepetitionResponse:
    return await add_exercise_history_command_handler.handle(AddExerciseHistoryCommand(workoutId=workoutId,
                                                                        exerciseSetId=exerciseSetId,
                                                                        width=request.width,
                                                                        height=request.height,
                                                                        frames=request.frames))