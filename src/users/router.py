from fastapi import APIRouter, Depends

from src.users.schemas import UserCreate, UserRead
from src.users.service import user_service


router = APIRouter(tags=['User'], prefix='/users')


@router.post('/')
async def create_user(user: UserCreate):
    result = await user_service.create_user(user)
    return result


@router.get('/{user_id}')
async def get_user(user_id: int) -> UserRead:
    user = await user_service.get_user(user_id)
    return user
