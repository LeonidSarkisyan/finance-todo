from src.repository import SQLAlchemyRepository
from src.balances.models import Balance


balance_repository = SQLAlchemyRepository(Balance)
