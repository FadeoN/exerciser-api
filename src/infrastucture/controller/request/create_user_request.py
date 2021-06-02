from typing import List

from pydantic import BaseModel

from src.domain.enum.user_role import UserRole


class CreateUserRequest(BaseModel):
    username: str
    password: str
    roles: List[UserRole] = [UserRole.PATIENT]
