from pydantic import BaseModel

from src.application.query.model.user_response import UserResponse
from src.application.repository import repository
from src.domain.model.user import User


class GetUserQuery(BaseModel):
    username: str


async def handle(query: GetUserQuery) -> UserResponse:
    user = await repository.engine.find_one(User, User.username == query.username)
    if user is None:
        raise NotFoundException()

    return UserResponse(id=str(user.id),
                        username=user.username,
                        password=user.password,
                        roles=user.roles)