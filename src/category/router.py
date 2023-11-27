from typing import Annotated

from fastapi import APIRouter, Depends

from src.depends import get_current_user
from src.users.schemas import UserRead
from src.category.schemas import SubCategoryUpdate, SubCategoryCreate, CategoryRead, SubCategoryRead
from src.category.service import category_service, sub_category_service


router = APIRouter(tags=["Category"], prefix="/categories")
router_sub = APIRouter(tags=["Sub Category"], prefix="/categories/sub")


@router.get("/")
async def get_categories(
    current_user: Annotated[UserRead, Depends(get_current_user)]
) -> list[CategoryRead]:
    return await category_service.get_categories()


@router_sub.post("/")
async def create_subcategory(
    sub_category: SubCategoryCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await sub_category_service.create_sub_category(sub_category.title, current_user)


@router_sub.get("/")
async def get_my_subcategories(
    current_user: Annotated[UserRead, Depends(get_current_user)]
) -> list[SubCategoryRead]:
    return await sub_category_service.get_my_subcategories(current_user)


@router_sub.patch("/{subcategory_id}")
async def update_subcategory(
    subcategory_id: int,
    subcategory: SubCategoryUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
) -> SubCategoryRead:
    return await sub_category_service.update_subcategory(subcategory_id, subcategory, current_user)


@router_sub.delete("/{subcategory_id}")
async def delete_subcategory(
    subcategory_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
) -> SubCategoryRead:
    return await sub_category_service.delete_subcategory(subcategory_id, current_user)
