from typing import List

from fastapi import APIRouter
from starlette import status

from src.application.command import create_exercise_command_handler, delete_exercise_command_handler
from src.application.command.create_exercise_command_handler import CreateExerciseCommand
from src.application.command.delete_exercise_command_handler import DeleteExerciseCommand
from src.application.query import  get_all_exercises_query_handler
from src.application.query.get_all_exercises_query_handler import GetAllExercisesQuery
from src.domain.model.exercise import Exercise
from src.infrastucture.controller.request.create_exercise_request import CreateExerciseRequest

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: CreateExerciseRequest):
    await create_exercise_command_handler.handle(CreateExerciseCommand(
        name=request.name,
        difficulty=request.difficulty,
        imageUrl=request.imageUrl,
        videoUrl=request.videoUrl
    ))


@router.get("", status_code=status.HTTP_200_OK)
async def get_all() -> List[Exercise]:
    return await get_all_exercises_query_handler.handle(GetAllExercisesQuery())


@router.delete("/<id>", status_code=status.HTTP_200_OK)
async def delete(id: str):
    return await delete_exercise_command_handler.handle(DeleteExerciseCommand(id=id))