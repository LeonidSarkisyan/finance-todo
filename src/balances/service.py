from src.exceptions import Forbidden
from src.repository import RepositoryInterface
from src.users.schemas import UserRead
from src.balances.schemas import BalanceCreate, BalanceUpdate
from src.balances.repository import balance_repository


class BalanceService:

    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    async def create_balance(self, balance: BalanceCreate, user: UserRead):
        balance_data = balance.model_dump()
        balance_data["user_id"] = user.id
        new_balance = await self.repository.create(balance_data)
        return new_balance

    async def get_balances(self, user: UserRead):
        balances = await self.repository.get_list(self.repository.model.user_id == user.id)
        return balances

    async def get_balance(self, balance_id: int, user: UserRead):
        balance = await self.repository.get_by_id(balance_id)
        if balance.user_id != user.id:
            raise Forbidden
        return balance

    async def update_balance(self, balance_id: int, balance: BalanceUpdate, user: UserRead):
        updated_balance = await self.repository.update(
            balance.model_dump(), balance_id, self.repository.model.user_id == user.id
        )
        if not updated_balance:
            raise Forbidden
        return updated_balance

    async def delete_balance(self, balance_id: int, user: UserRead):
        deleted_balance = await self.repository.delete(
            balance_id, self.repository.model.id == balance_id, self.repository.model.user_id == user.id
        )
        if not deleted_balance:
            raise Forbidden
        return deleted_balance


balance_service = BalanceService(balance_repository)
