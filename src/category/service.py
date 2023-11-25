from src.exceptions import Forbidden
from src.repository import RepositoryInterface
from src.users.schemas import UserRead
from src.category.schemas import CategoryCreate, CategoryUpdate
from src.category.repository import category_repository


class CategoryService:

    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    async def create_category(self, category: CategoryCreate, user: UserRead):
        category_data = category.model_dump()
        category_data["user_id"] = user.id
        new_category = await self.repository.create(category_data)
        return new_category

    async def get_categories(self, user: UserRead):
        categories = await self.repository.get_list(self.repository.model.user_id == user.id)
        return categories

    async def get_category(self, category_id: int, user: UserRead):
        category = await self.repository.get_by_id(category_id)
        if category.user_id != user.id:
            raise Forbidden
        return category

    async def update_category(self, category_id: int, category: CategoryUpdate, user: UserRead):
        data = {key: value for key, value in category.model_dump().items() if value is not None}
        updated_category = await self.repository.update(
            data, category_id, self.repository.model.user_id == user.id
        )
        if not updated_category:
            raise Forbidden
        return updated_category

    async def delete_category(self, category_id: int, user: UserRead):
        deleted_category = await self.repository.delete(
            category_id, self.repository.model.id == category_id, self.repository.model.user_id == user.id
        )
        if not deleted_category:
            raise Forbidden
        return deleted_category


category_service = CategoryService(category_repository)
