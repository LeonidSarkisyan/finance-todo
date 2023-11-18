from fastapi import APIRouter

from src.users.schemas import UserCreate, UserRead


router = APIRouter(tags=['User'], prefix='/users')


@router.post('/')
async def create_user(user: UserCreate):
    return user
