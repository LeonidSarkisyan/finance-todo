from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column(nullable=False)
    created_datetime: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_datetime: Mapped[datetime] = mapped_column(onupdate=func.now(), nullable=True)
