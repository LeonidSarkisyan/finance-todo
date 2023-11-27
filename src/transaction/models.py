from datetime import datetime

from sqlalchemy import func, DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(60))
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    value: Mapped[float] = mapped_column()
    created_date_time: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_date_time: Mapped[datetime] = mapped_column(DateTime, onupdate=func.now(), nullable=True)
    balance_id: Mapped[int] = mapped_column(ForeignKey("balances.id", ondelete='CASCADE'))
    sub_category_id: Mapped[int] = mapped_column(ForeignKey("sub_categories.id"), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship(back_populates="transactions")
    balance: Mapped["Balance"] = relationship(back_populates="transactions")
    sub_category: Mapped["SubCategory"] = relationship(back_populates="transactions")
