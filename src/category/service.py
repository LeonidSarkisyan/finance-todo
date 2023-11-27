from dataclasses import asdict

from src.exceptions import Forbidden, NotFound
from src.repository import RepositoryInterface, IntegrityException

from src.users.schemas import UserRead

from src.category.default import DEFAULT_CATEGORIES
from src.category.schemas import SubCategoryCreate, SubCategoryUpdate
from src.category.repository import category_repository, sub_category_repository


class CategoryService:

    def __init__(self, repository: RepositoryInterface, repository_sub: RepositoryInterface):
        self.repository = repository
        self.repository_sub = repository_sub
    async def get_categories(self):
        categories = await self.repository.get_list()
        return categories

    async def get_category(self, category_id: int, user: UserRead):
        category = await self.repository.get_by_id(category_id)
        if not category:
            raise NotFound.get_http_exception()
        if category.is_deleted:
            raise NotFound.get_http_exception()
        if category.user_id != user.id:
            raise Forbidden.get_http_exception()
        return category

    async def delete_category(self, category_id: int, user: UserRead):
        data = {"is_deleted": True}
        deleted_category = await self.repository.update(
            data, category_id, self.repository.model.user_id == user.id
        )
        if not deleted_category:
            raise Forbidden.get_http_exception()
        return deleted_category

    async def create_default_categories(self):
        default_categories = [asdict(category) for category in DEFAULT_CATEGORIES]
        categories = []
        sub_categories = []
        for default_category in default_categories:
            categories.append({"title": default_category["title"]})
            sub_categories_one = []
            for sub_category in default_category["sub_categories"]:
                sub_categories_one.append({"title": sub_category["title"]})
            sub_categories.append(sub_categories_one)

        try:
            categories_ids = await self.repository.bulk_insert(categories)
            for category_id, sub_categories_list in zip(categories_ids, sub_categories):
                for sub_categories_list_item in sub_categories_list:
                    sub_categories_list_item["category_id"] = category_id
                await self.repository_sub.bulk_insert(sub_categories_list)
        except IntegrityException:
            pass


class SubCategoryService:

    def __init__(self, repository: RepositoryInterface, repository_category: RepositoryInterface):
        self.repository = repository
        self.repository_category = repository_category
        self.category_owner_id = 0

    @property
    async def category_owner_id_property(self):
        if not self.category_owner_id:
            personal_category = await self.repository_category.get_by_field("title", "Личные")
            self.category_owner_id = personal_category.id
            return personal_category.id
        else:
            return self.category_owner_id

    async def create_sub_category(self, title: str, user: UserRead):
        data = {
            "title": title,
            "user_id": user.id,
            "category_id": await self.category_owner_id_property
        }
        return await self.repository.create(data)

    async def get_my_subcategories(self, user: UserRead):
        sub_categories = await self.repository.get_list(
            self.repository.model.user_id == user.id,
            self.repository.model.is_deleted == False
        )
        return sub_categories

    async def update_subcategory(self, subcategory_id: int, subcategory: SubCategoryUpdate, user: UserRead):
        subcategory_updated = await self.repository.update(
            subcategory.model_dump(),
            subcategory_id,
            self.repository.model.user_id == user.id,
            self.repository.model.is_deleted == False
        )
        if not subcategory_updated:
            raise Forbidden.get_http_exception()
        return subcategory_updated

    async def delete_subcategory(self, subcategory_id: int, user: UserRead):
        data = {"is_deleted": True}
        subcategory_deleted = await self.repository.update(
            data,
            subcategory_id,
            self.repository.model.user_id == user.id,
            self.repository.model.is_deleted == False
        )
        if not subcategory_deleted:
            raise NotFound.get_http_exception()
        return subcategory_deleted


category_service = CategoryService(category_repository, sub_category_repository)
sub_category_service = SubCategoryService(sub_category_repository, category_repository)
