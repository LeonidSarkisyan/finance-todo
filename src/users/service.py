from src.exceptions import HTTPExceptionBase
from src.repository import RepositoryInterface, IntegrityException

from src.users.schemas import UserCreate, UserLogin, UserUpdate
from src.users.repository import user_repository
from src.users.hashing import Hash
from src.users.auth import create_jwt_token, decode_jwt_token


class UserService:

    def __init__(self, repository: RepositoryInterface, hash_service: Hash):
        self.hash = hash_service
        self.repository = repository

    async def login(self, login: UserLogin) -> dict[str, str]:
        user = await self.repository.get_by_field("phone", login.phone)
        if not user:
            raise BadLoginOrPassword.get_http_exception()
        if not self.hash.verify(user.password, login.password):
            raise BadLoginOrPassword.get_http_exception()
        data_for_token = {"user_id": user.id}
        access_token = create_jwt_token(data_for_token)
        return {"access_token": access_token, "token_type": "bearer"}

    async def create_user(self, user: UserCreate):
        data = user.model_dump()
        data["password"] = self.hash.bcrypt(user.password)
        try:
            user = await self.repository.create(data)
        except IntegrityException:
            raise UserExist.get_http_exception()
        return user

    async def get_list_users(self, *filters):
        users = await self.repository.get_list(*filters)
        return users

    async def get_user(self, user_id: int):
        user = await self.repository.get_by_id(user_id)
        return user

    async def update_user(self, user_update: UserUpdate, user_id: int):
        data = {key: value for key, value in user_update.model_dump().items() if value is not None}
        updated_user = await self.repository.update(data, user_id)
        return updated_user


BadLoginOrPassword = HTTPExceptionBase(401, "Неверный логин или пароль")
UserExist = HTTPExceptionBase(409, "Пользователь c таким username, email или phone уже зарегестрирован")
user_service = UserService(user_repository, Hash())
