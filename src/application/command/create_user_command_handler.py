from datetime import datetime
from typing import List

from pydantic import BaseModel

from src.application.exception.already_exists_exception import AlreadyExistsException
from src.application.repository import repository
from src.domain.enum.user_role import UserRole
from src.domain.model.user import User
from src.infrastucture.security.authentication import hash_password


class CreateUserCommand(BaseModel):
    username: str
    password: str
    roles: List[UserRole]


async def handle(command: CreateUserCommand):
    user = await repository.engine.find_one(User, User.username == command.username)
    if user is not None:
        raise AlreadyExistsException("user.already.exists")

    await repository.engine.save(User(username=command.username,
                           password=hash_password(command.password),
                           roles=command.roles,
                           creationDate=datetime.utcnow()))
