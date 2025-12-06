"""
This modules contains the database connection.
"""

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base
from decouple import config


DB_HOST = config("DB_HOST")
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
DB_PORT = config("DB_PORT")

# DATABASE_URL = dialect+driver://user:pass@host:port/dbname$$
DATABASE_URL = f"mysql+aiomysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 1. The async-engine-creaion
async_engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# 2. Async Session Creation
async_session = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False, autoflush=False
)


# 3. Base class declaration for all models
Base = declarative_base()


# Database session
async def get_session():
    """
    Create a session by connecting to the database.
    which help to quering data.
    """
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()
