from datetime import datetime

from sqlalchemy import func, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Balance(Base):
    __tablename__ = 'balances'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(16))
    type: Mapped[str] = mapped_column()
    value: Mapped[float] = mapped_column()
    currency: Mapped[str] = mapped_column()
    created_date_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_date_time: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now(), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="balances")
