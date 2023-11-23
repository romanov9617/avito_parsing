from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config import settings

class Base(DeclarativeBase):
    pass


engine = create_async_engine(settings.DATABASE_URL())

async_session_factory = async_sessionmaker(engine, expire_on_commit=False)



