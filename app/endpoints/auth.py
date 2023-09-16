from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from typing import Annotated

from app.db.models import User
from app.schemas.user import BaseUser
from app.schemas.auth import Token
from app.usecase.user import get_active_user, get_user
from app.tools.auth import create_access_token
from app.tools.crypto import verify_password


ACCESS_TOKEN_EXPIRE_MINUTES = 30


api = APIRouter(prefix="/auth", tags=["Auth"])


async def authenticate_user(username: str, password: str) -> User:
    try:
        user = await get_user(BaseUser(username=username))
        # user = await get_active_user(credetials=BaseUser(username=username))#
        if not verify_password(password, user.password):
            return False
        return user
    except:
        raise ValueError("Server Error")


@api.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await authenticate_user(form_data.username, form_data.password)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}