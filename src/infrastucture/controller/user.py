from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status

from src.application.command import create_user_command_handler
from src.application.command.create_user_command_handler import CreateUserCommand
from src.application.query import get_user_query_handler
from src.application.query.get_user_query_handler import GetUserQuery
from src.application.query.model.user_response import UserResponse
from src.domain.model.user import User
from src.infrastucture.controller.request.create_user_request import CreateUserRequest
from src.infrastucture.security.authentication import authenticate_user, create_access_token, get_current_user
from src.infrastucture.security.model.token import Token

router = APIRouter()


@router.post("", status_code=status.HTTP_201_CREATED)
async def create(request: CreateUserRequest):
    await create_user_command_handler.handle(CreateUserCommand(
        username=request.username,
        password=request.password,
        roles=request.roles
    ))


@router.get("/{username}", status_code=status.HTTP_200_OK)
async def get(username: str, current_user: User = Security(get_current_user, scopes=["Patient"])) -> UserResponse:
    return await get_user_query_handler.handle(GetUserQuery(
        username=username
    ))


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    access_token = create_access_token(data={"userId":user.id, "sub": user.username, "scopes": user.roles})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
