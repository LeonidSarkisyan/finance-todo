from abc import ABC, abstractmethod

from sqlalchemy import insert, select, delete, update
from sqlalchemy.exc import IntegrityError

from src.database import async_session_maker, Base
from src.exceptions import NotFound


class RepositoryInterface(ABC):
    @abstractmethod
    async def create(self, data: dict):
        raise NotImplemented

    @abstractmethod
    async def get_by_id(self, entity_id):
        raise NotImplemented


class SQLAlchemyRepository(RepositoryInterface):

    def __init__(self, model: Base):
        self.model = model

    async def create(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).returning(self.model).values(**data)
            try:
                result = await session.execute(stmt)
            except IntegrityError as error:
                raise IntegrityException
            else:
                await session.commit()
                return result.scalar()

    async def get_by_id(self, entity_id):
        async with async_session_maker() as session:
            query = select(self.model).where(self.model.id == entity_id)
            result = await session.execute(query)
            entity = result.scalar()
            if not entity:
                raise NotFound
            return entity


class IntegrityException(Exception):
    pass
