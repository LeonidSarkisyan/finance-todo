from src.repository import SQLAlchemyRepository
from src.users.models import User


user_repository = SQLAlchemyRepository(User)
