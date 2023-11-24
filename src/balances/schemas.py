from datetime import datetime

from pydantic import BaseModel


class BalanceBase(BaseModel):
    title: str
    type: str
    value: float
    currency: str


class BalanceCreate(BalanceBase):
    pass


class BalanceUpdate(BalanceBase):
    pass
