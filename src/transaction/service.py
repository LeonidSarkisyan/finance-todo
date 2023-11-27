from src.repository import RepositoryInterface, IntegrityException
from src.exceptions import Forbidden, CategoryNotExist, NotFound, BalanceNotExist

from src.users.schemas import UserRead
from src.balances.repository import balance_repository
from src.transaction.repository import transaction_repository
from src.transaction.schemas import TransactionCreate, TransactionUpdate


class TransactionService:

    def __init__(self, repository: RepositoryInterface, repository_balance: RepositoryInterface):
        self.repository = repository
        self.repository_balance = repository_balance

    async def create_transaction(self, transaction: TransactionCreate, user: UserRead):
        balance = await self.repository_balance.get_by_id(transaction.balance_id)

        if not balance:
            raise BalanceNotExist.get_http_exception()
        if balance.user_id != user.id:
            raise Forbidden.get_http_exception()

        transaction_data = transaction.model_dump()
        transaction_data["user_id"] = user.id

        try:
            new_transaction = await self.repository.create(transaction_data)
        except IntegrityException:
            raise CategoryNotExist.get_http_exception()

        return new_transaction

    async def get_transaction(self, transaction_id: int, user: UserRead):
        transaction_updated = await self.repository.get_by_id(transaction_id)
        if not transaction_updated:
            raise NotFound.get_http_exception()
        if transaction_updated.user_id != user.id:
            raise Forbidden.get_http_exception()
        return transaction_updated

    async def get_transactions(self, user: UserRead, balance_id: int = 0):
        filters = [self.repository.model.user_id == user.id]
        if balance_id:
            filters.append(self.repository.model.balance_id == balance_id)
        try:
            transactions = await self.repository.get_list(*filters)
        except IntegrityException:
            raise
        return transactions

    async def update_transaction(self, transaction_id: int, transaction: TransactionCreate, current_user: UserRead):
        data = {key: value for key, value in transaction.model_dump().items() if value is not None}
        transaction_updated = await self.repository.update(
            data, transaction_id, self.repository.model.user_id == current_user.id
        )
        if not transaction_updated:
            raise NotFound.get_http_exception()
        return transaction_updated

    async def delete_transaction(self, transaction_id: int, current_user: UserRead):
        transaction_deleted = await self.repository.delete(
            transaction_id, self.repository.model.user_id == current_user.id
        )
        if not transaction_deleted:
            raise NotFound.get_http_exception()
        return transaction_deleted


transaction_service = TransactionService(transaction_repository, balance_repository)
