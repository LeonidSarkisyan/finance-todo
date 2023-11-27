from src.repository import SQLAlchemyRepository
from src.transaction.models import Transaction


transaction_repository = SQLAlchemyRepository(Transaction)
