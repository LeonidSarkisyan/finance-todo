from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.depends import get_current_user
from src.users.schemas import UserCreate, UserRead, UserLogin, Token, UserUpdate
from src.users.service import user_service


router = APIRouter(tags=['User'], prefix='/users')


@router.post('/login')
async def login(user_login: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user_login = UserLogin(phone=user_login.username, password=user_login.password)
    token = await user_service.login(user_login)
    return token


@router.get("/me")
async def get_me(current_user: Annotated[UserRead, Depends(get_current_user)]) -> UserRead:
    return current_user


@router.post('/')
async def create_user(user: UserCreate) -> UserRead:
    result = await user_service.create_user(user)
    return result


@router.get('/')
async def get_list_users(current_user: Annotated[UserRead, Depends(get_current_user)]) -> list[UserRead]:
    users = await user_service.get_list_users()
    return users


@router.get('/{user_id}')
async def get_user(user_id: int, current_user: Annotated[UserRead, Depends(get_current_user)]) -> UserRead:
    user = await user_service.get_user(user_id)
    return user


@router.patch('/')
async def update_user(
    user_update: UserUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
) -> UserRead:
    updated_user = await user_service.update_user(user_update, current_user.id)
    return updated_user
