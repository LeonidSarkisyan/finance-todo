from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

connection_string = URL.create(
  'postgresql',
  username='LeonidSarkisyan',
  password='yr8jq5VEsZPl',
  host='ep-sparkling-tooth-34814142.eu-central-1.aws.neon.tech',
  database='FrilanceTodoDB'
)

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base = declarative_base()

engine = create_async_engine(connection_string)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
