from pydantic import BaseModel, Field, validator
from datetime import date


class BaseUser(BaseModel):
    username: str = Field(max_length=30, min_length=5)
    password: str = Field(max_length=30, min_length=8)


class UserCreate(BaseUser):
    email: str
    birthdate: date


class DeleteUser(BaseUser):
    pass




