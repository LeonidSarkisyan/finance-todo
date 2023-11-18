from src.exceptions import HTTPExceptionBase
from src.repository import RepositoryInterface, IntegrityException

from src.users.schemas import UserCreate
from src.users.repository import user_repository
from src.users.hashing import Hash


class UserService:

    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    async def create_user(self, user: UserCreate):
        data = user.model_dump()
        data["password"] = Hash.bcrypt(user.password)
        try:
            user = await self.repository.create(data)
        except IntegrityException:
            raise UserExist
        return user

    async def get_user(self, user_id: int):
        user = await self.repository.get_by_id(user_id)
        return user


UserExist = HTTPExceptionBase(409, "Пользователь c таким username, email или phone уже зарегестрирован")
user_service = UserService(user_repository)
