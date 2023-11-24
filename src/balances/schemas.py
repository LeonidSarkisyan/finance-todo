from datetime import datetime

from pydantic import BaseModel


class BalanceBase(BaseModel):
    title: str
    type: str
    value: float
    currency: str


class BalanceCreate(BalanceBase):
    pass


class BalanceUpdate(BaseModel):
    title: str | None = None
    type: str | None = None
    value: float | None = None
    currency: str | None = None
