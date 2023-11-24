from typing import Annotated

from fastapi import APIRouter, Depends

from src.depends import get_current_user
from src.users.schemas import UserRead
from src.balances.schemas import BalanceCreate, BalanceUpdate
from src.balances.service import balance_service


router = APIRouter(tags=['Balance'], prefix='/balances')


@router.post("/")
async def create_balance(
    balance: BalanceCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await balance_service.create_balance(balance, current_user)


@router.get("/")
async def get_my_balances(
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await balance_service.get_balances(current_user)


@router.get("/{balance_id}")
async def get_my_balance(
    balance_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await balance_service.get_balance(balance_id, current_user)


@router.patch("/{balance_id}")
async def update_balance(
    balance_id: int,
    balance_update: BalanceUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await balance_service.update_balance(balance_id, balance_update, current_user)


@router.delete("/{balance_id}")
async def delete_balance(
    balance_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await balance_service.delete_balance(balance_id, current_user)
