from fastapi import FastAPI
import uvicorn

from typing import Optional

from app.usecase.user import register_user, delete_user
from app.schemas.user import UserCreate, DeleteUser

news = FastAPI(title="First project")

@news.post("/signup")
async def signup_user(user: UserCreate):
    await register_user(user)


@news.delete("/delete_user")
async def user_account_delete(user: DeleteUser):
    await delete_user(user)


if __name__ == "__main__":
    uvicorn.run(news, port=8000)