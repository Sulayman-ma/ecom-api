from typing import Any

from sqlalchemy.ext.declarative import declared_attr, as_declarative
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from ecomapi.core.config import settings


# Async Database engine
engine = create_async_engine(
    # check same thread to be removed during production
    settings.SQLALCHEMY_DATABASE_URI, connect_args={'check_same_thread': True}
)


# Async Session Local instance
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)
# AsyncScopedSession = async_scoped_session(async_session_factory, scopefunc=current_task)
# SessionLocal = AsyncScopedSession()


# Base SQLAlchemy class for the application's database models
# Base = declarative_base()
@as_declarative()
class Base:
    id: Any
    __name__: str   
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'
