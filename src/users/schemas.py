from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    phone: str | None = None
    email: EmailStr | None = None


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    created_datetime: datetime
    updated_datetime: datetime

    class Config:
        orm_mode = True
