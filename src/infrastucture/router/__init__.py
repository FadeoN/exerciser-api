from fastapi import APIRouter

from src.infrastucture.controller.exercise import router as exercise_router
from src.infrastucture.controller.user import router as user_router
from src.infrastucture.controller.workout import router as workout_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/users", tags=["user"])
api_router.include_router(exercise_router, prefix="/exercises", tags=["exercise"])
api_router.include_router(workout_router, prefix="/workouts", tags=["workout"])