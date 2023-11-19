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

    @abstractmethod
    async def get_by_field(self, field_name: str, value):
        raise NotImplemented

    @abstractmethod
    async def update(self, data: dict, entity_id: int):
        raise NotImplemented

    @abstractmethod
    async def get_list(self, *filters):
        raise NotImplemented


class SQLAlchemyRepository(RepositoryInterface):

    def __init__(self, model: Base):
        self.model = model

    async def create(self, data: dict):
        async with async_session_maker() as session:
            stmt = insert(self.model).returning(self.model).values(**data)
            try:
                result = await session.execute(stmt)
            except IntegrityError:
                raise IntegrityException
            else:
                await session.commit()
                return result.scalar()

    async def get_list(self, *filters):
        async with async_session_maker() as session:
            stmt = select(self.model).filter(*filters)
            result = await session.execute(stmt)
            return result.scalars().all()

    async def get_by_id(self, entity_id):
        async with async_session_maker() as session:
            query = select(self.model).where(self.model.id == entity_id)
            result = await session.execute(query)
            entity = result.scalar()
            if not entity:
                raise NotFound
            return entity

    async def get_by_field(self, field_name: str, value):
        async with async_session_maker() as session:
            search_field = getattr(self.model, field_name)
            query = select(self.model).where(search_field == value)
            result = await session.execute(query)
            entity = result.scalar()
            return entity

    async def update(self, data: dict, entity_id: int):
        async with async_session_maker() as session:
            stmt = (
                update(self.model)
                .returning(self.model)
                .values(**data)
                .where(self.model.id == entity_id)
            )
            result = await session.execute(stmt)
            await session.commit()
            return result.scalar()


class IntegrityException(Exception):
    pass
