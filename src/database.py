from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

connection_string = URL.create(
  'postgresql+asyncpg',
  username='LeonidSarkisyan',
  password='aUqdbEP1TeR0',
  host='ep-tiny-poetry-24411871-pooler.eu-central-1.aws.neon.tech',
  database='FinanceTodoDB',
  query={"async_fallback": "True"}
)

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()

engine = create_async_engine(connection_string)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
