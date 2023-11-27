from src.repository import SQLAlchemyRepository
from src.category.models import Category, SubCategory


category_repository = SQLAlchemyRepository(Category)
sub_category_repository = SQLAlchemyRepository(SubCategory)
