from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base
from src.transaction.models import Transaction


class SubCategory(Base):
    __tablename__ = "sub_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(40))
    is_deleted: Mapped[bool] = mapped_column(default=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)

    category: Mapped["Category"] = relationship(back_populates="sub_categories")
    transactions: Mapped[list[Transaction]] = relationship(back_populates="sub_category")
    user: Mapped["User"] = relationship(back_populates="sub_categories")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(16), unique=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)

    sub_categories: Mapped[list[SubCategory]] = relationship(back_populates="category")
