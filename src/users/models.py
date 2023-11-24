from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.balances.models import Balance


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    phone: Mapped[str] = mapped_column(nullable=False, unique=True)
    username: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=False)
    created_datetime: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_datetime: Mapped[datetime] = mapped_column(onupdate=func.now(), nullable=True)

    balances: Mapped[list[Balance]] = relationship(back_populates="user")
