from typing import Annotated

from fastapi import APIRouter, Depends

from src.depends import get_current_user
from src.users.schemas import UserRead
from src.category.schemas import CategoryCreate, CategoryUpdate
from src.category.service import category_service


router = APIRouter(tags=['Category'], prefix='/categories')


@router.post("/")
async def create_category(
    category: CategoryCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await category_service.create_category(category, current_user)


@router.get("/")
async def get_my_categories(
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await category_service.get_categories(current_user)


@router.get("/{category_id}")
async def get_my_category(
    category_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await category_service.get_category(category_id, current_user)


@router.patch("/{category_id}")
async def update_category(
    category_id: int,
    category_update: CategoryUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await category_service.update_category(category_id, category_update, current_user)


@router.delete("/{category_id}")
async def delete_balance(
    category_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await category_service.delete_category(category_id, current_user)
