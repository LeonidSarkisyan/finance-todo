from pydantic import BaseModel, field_validator


class TransactionBase(BaseModel):
    title: str
    description: str | None = None
    value: float
    balance_id: int
    sub_category_id: int


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    value: float | None = None
