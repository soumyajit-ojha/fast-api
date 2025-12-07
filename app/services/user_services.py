"""
This module contain user services.
new user creation.
user delete,
user update
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.users import User
from app.schemas.user import UserCreate
from app.core.security import get_hashed_password


async def create_user(db: AsyncSession, user: UserCreate):
    """
    Create a new user by using sqlalchemy syntax to db instance.
    """
    try:
        hashed_password = get_hashed_password(user.password)
    
        new_user = User(
            username=user.username, email=user.email, hashed_password=hashed_password
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
    except Exception as e:
        print("HASHING ERROR", str(e))

async def get_user_by_email(db: AsyncSession, email: str):
    """
    Get user by filtering email address from all users.
    """

    res = await db.execute(select(User).filter(User.email == email))
    return res


async def get_user_by_username(db: AsyncSession, username: str):
    """
    Get users by filtering username.
    """
    res = await db.execute(select(User).filter(User.username == username))
    return res
