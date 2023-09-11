from sqlalchemy import Column, VARCHAR, UUID, func, TIMESTAMP, Date, Boolean
import uuid

from app.db import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, name="id", index=True, default=uuid.uuid4)
    username = Column(VARCHAR(15), nullable=False)
    email = Column(VARCHAR(40), nullable=False)
    password = Column(VARCHAR(64), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())
    is_active = Column(Boolean, nullable=False, default=False)
    birthdate = Column(Date, nullable=False)