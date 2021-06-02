from datetime import datetime
from typing import List

from odmantic import Model

from src.domain.enum.user_role import UserRole


class User(Model):
    username: str
    password: str
    roles: List[UserRole]
    creationDate: datetime = datetime.utcnow()
