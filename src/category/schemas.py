from fastapi import HTTPException
from pydantic import BaseModel, field_validator


class SubCategoryBase(BaseModel):
    title: str

    @field_validator("title")
    def check_title(cls, v: str, context):
        if len(v) > 40:
            raise HTTPException(422, "Название под-категории не может быть больше 40 символов!")
        return v


class SubCategoryCreate(SubCategoryBase):
    pass


class SubCategoryUpdate(SubCategoryCreate):
    pass


class CategoryRead(BaseModel):
    id: int
    title: str


class SubCategoryRead(CategoryRead):
    user_id: int | None = None
