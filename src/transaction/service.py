from src.repository import RepositoryInterface, IntegrityException
from src.exceptions import Forbidden, CategoryNotExist, NotFound, BalanceNotExist

from src.users.schemas import UserRead
from src.balances.repository import balance_repository
from src.transaction.repository import transaction_repository
from src.transaction.schemas import TransactionCreate


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

    async def get_transactions(self, user: UserRead, balance_id: int = 0):
        filters = [self.repository.model.user_id == user.id]
        if balance_id:
            filters.append(self.repository.model.balance_id == balance_id)
        try:
            transactions = await self.repository.get_list(*filters)
        except IntegrityException:
            raise
        return transactions


transaction_service = TransactionService(transaction_repository, balance_repository)
