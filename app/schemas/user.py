from pydantic import BaseModel, Field, validator
from datetime import date


class BaseUser(BaseModel):
    username: str = Field(max_length=30, min_length=5)


class UserCreate(BaseUser):
    password: str = Field(max_length=30, min_length=8)
    email: str
    birthdate: date


class DeleteUser(BaseUser):
    password: str = Field(max_length=30, min_length=8)




