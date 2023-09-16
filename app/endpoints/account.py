from fastapi import APIRouter

from app.usecase.user import register_user, delete_user
from app.schemas.user import UserCreate, DeleteUser


api = APIRouter(prefix="/account", tags=["Account"])


@api.post("/signup")
async def signup_user(user: UserCreate):
    await register_user(user)


@api.delete("/delete_user")
async def user_account_delete(user: DeleteUser):
    await delete_user(user)