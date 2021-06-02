from typing import List

from pydantic import BaseModel

from src.domain.enum.user_role import UserRole


class UserResponse(BaseModel):
    id: str
    username: str
    password: str
    roles: List[UserRole]