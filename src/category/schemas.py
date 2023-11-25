from fastapi import HTTPException
from pydantic import BaseModel, field_validator


class CategoryBase(BaseModel):
    title: str

    @field_validator("title")
    def check_title(cls, v: str, context):
        if len(v) > 16:
            raise HTTPException(422, "Название категории не может быть больше 16 символов!")
        return v


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryCreate):
    pass
