from sqlalchemy import insert, delete
from sqlalchemy.exc import IntegrityError

from app.db.connection.session import get_session
from app.db.models.users import User
# from app.exceptions import UserExists
from app.schemas.user import UserCreate, DeleteUser
from app.tools.crypto import get_hash


async def register_user(credentials: UserCreate):
    credentials.password = get_hash(credentials.password)
    try:
            session = await get_session()
            await session.execute(insert(User), [credentials.__dict__])
            await session.commit()
    except IntegrityError:
        raise ValueError("User exists!")
    

async def delete_user(credentials: DeleteUser):
    credentials.password = get_hash(credentials.password)
    try:
            session = await get_session()
            await session.execute(delete(User).where(User.username==credentials.username))
            await session.commit()
    except IntegrityError:
        raise ValueError("User isn't deleted!")