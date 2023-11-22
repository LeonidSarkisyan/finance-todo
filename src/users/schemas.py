from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    phone: str
    password: str


class UserBase(BaseModel):
    username: str
    phone: str | None = None
    email: EmailStr | None = None


class UserUpdate(BaseModel):
    username: str | None = None
    phone: str | None = None
    email: EmailStr | None = None


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_datetime: datetime
    updated_datetime: datetime | None

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None
