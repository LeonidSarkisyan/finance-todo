from src.repository import SQLAlchemyRepository
from src.category.models import Category


category_repository = SQLAlchemyRepository(Category)
