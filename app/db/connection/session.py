from app.config import DefaultSettings

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker


class SessionManager:

    def __init__(self) -> None:
        self.refresh()


    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(SessionManager, cls).__new__(cls)
        return cls.instance
    

    def get_session_maker(self) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(bind= self.engine, expire_on_commit=False)
    

    def refresh(self) -> None:
        self.engine = create_async_engine(DefaultSettings().database_uri, echo=True, future=True)



async def get_session() -> AsyncSession:
    session_maker = SessionManager().get_session_maker()
    async with session_maker() as session:
        return session