from datetime import datetime, timedelta
from typing import Optional, List

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import ValidationError

from src.application.query import get_user_query_handler
from src.application.query.get_user_query_handler import GetUserQuery
from src.domain.enum.user_role import UserRole
from src.infrastucture.configuration import APP_OPTIONS
from src.infrastucture.security.model.token import TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token",
                                     scopes=UserRole.map())


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str):
    return pwd_context.hash(password)


async def authenticate_user(username: str, password: str):
    user = await get_user_query_handler.handle(GetUserQuery(username=username))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=APP_OPTIONS.security_options.access_token_expire_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, APP_OPTIONS.security_options.secret_key,
                             algorithm=APP_OPTIONS.security_options.algorithm)
    return encoded_jwt


def check_user_scope(user_scopes, security_scopes, authenticate_value):
    for scope in security_scopes:
        if scope not in user_scopes:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Not enough permissions",
                headers={"WWW-Authenticate": authenticate_value},
            )


async def get_current_user(
    security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)
):

    if security_scopes.scopes:
        authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    else:
        authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": authenticate_value},
    )
    try:
        payload = jwt.decode(token, APP_OPTIONS.security_options.secret_key, algorithms=[APP_OPTIONS.security_options.algorithm])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (JWTError, ValidationError):
        raise credentials_exception

    check_user_scope(token_data.scopes, security_scopes.scopes, authenticate_value)

    user = await get_user_query_handler.handle(GetUserQuery(username=token_data.username))
    if user is None:
        raise credentials_exception

    return user