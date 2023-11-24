from fastapi import HTTPException
from datetime import datetime

from pydantic import BaseModel, field_validator


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

    @field_validator('title')
    def check_home_country(cls, v: str, context):
        if len(v) > 16:
            raise HTTPException(422, "Название баланса не может быть больше 16 символов!")
        return v
