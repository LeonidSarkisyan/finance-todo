from typing import Annotated

from fastapi import APIRouter, Depends

from src.depends import get_current_user
from src.users.schemas import UserRead
from src.transaction.schemas import TransactionCreate, TransactionUpdate
from src.transaction.service import transaction_service


router = APIRouter(tags=['Transaction'], prefix='/transactions')


@router.post("/")
async def create_transaction(
    transaction: TransactionCreate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await transaction_service.create_transaction(transaction, current_user)


@router.get("/")
async def get_my_transactions(
    balance_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await transaction_service.get_transactions(current_user, balance_id)


@router.get("/{transaction_id}")
async def get_transaction(
    transaction_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await transaction_service.get_transaction(transaction_id, current_user)


@router.patch("/{transaction_id}")
async def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await transaction_service.update_transaction(transaction_id, transaction, current_user)


@router.delete("/{transaction_id}")
async def delete_transaction(
    transaction_id: int,
    current_user: Annotated[UserRead, Depends(get_current_user)]
):
    return await transaction_service.delete_transaction(transaction_id, current_user)
