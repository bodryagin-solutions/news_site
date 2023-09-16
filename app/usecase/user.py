from sqlalchemy import insert, delete, select
from sqlalchemy.exc import IntegrityError

from app.db.connection.session import get_session
from app.db.models.users import User
# from app.exceptions import UserExists
from app.schemas.user import UserCreate, DeleteUser, BaseUser
from app.tools.crypto import get_hash, get_salt


async def register_user(credentials: UserCreate):
    credentials.password = get_hash(credentials.password, get_salt(12))
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
    


async def get_user(credentials: BaseUser) -> User:
     try:
          session = await get_session()
          res = (await session.execute(select(User.username, User.password).where(User.username == credentials.username))).first()
          if res:
               return res
          raise ValueError("Incorrect username or password")
     except:
          raise ValueError("User can't be retrived")


async def get_active_user(credetials:BaseUser) -> User:
     try:
          user = await get_user(credetials)
          if user.is_active:
               return user
          raise ValueError("User is inactivate")
     except:
          raise ValueError("User can't be retrived")