from typing import Optional, List

from odmantic import ObjectId
from pydantic import BaseModel

from src.application.query.model.exercise_workout_response import ExerciseWorkoutResponse
from src.application.repository import repository
from src.domain.model.exercise_workout import ExerciseWorkout


class GetExerciseWorkoutQuery(BaseModel):
    assigneeId: Optional[str]
    assignerId: Optional[str]


async def handle(query: GetExerciseWorkoutQuery) -> List[ExerciseWorkoutResponse]:
    exerciseWorkouts = await getExerciseWorkouts(query.assigneeId, query.assignerId)
    return [convertToExerciseWorkoutResponse(exerciseWorkout) for exerciseWorkout in exerciseWorkouts]


async def getExerciseWorkouts(assigneeId: str, assignerId: str) -> List[ExerciseWorkout]:
    if assigneeId and assignerId:
        return await repository.engine.find(ExerciseWorkout, (ExerciseWorkout.assigneeId == ObjectId(assigneeId)) &
                                                             (ExerciseWorkout.assignerId == ObjectId(assignerId)))
    elif assigneeId:
        return await repository.engine.find(ExerciseWorkout, ExerciseWorkout.assigneeId == ObjectId(assigneeId))
    elif assignerId:
        return await repository.engine.find(ExerciseWorkout, ExerciseWorkout.assignerId == ObjectId(assignerId))

    return await repository.engine.find(ExerciseWorkout)


def convertToExerciseWorkoutResponse(exerciseWorkout: ExerciseWorkout) -> ExerciseWorkoutResponse:
    return ExerciseWorkoutResponse(id=str(exerciseWorkout.id),
                                   name=exerciseWorkout.name,
                                   assigneeId=str(exerciseWorkout.assigneeId),
                                   assignerId=str(exerciseWorkout.assignerId),
                                   startDate=exerciseWorkout.startDate,
                                   endDate=exerciseWorkout.endDate,
                                   status=exerciseWorkout.status,
                                   creationDate=exerciseWorkout.creationDate)