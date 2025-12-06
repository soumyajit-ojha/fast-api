"""
This module contains helper functions for models.
"""

from .users import User
from app.schemas.schemas import UserBase
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(sesssion: AsyncSession, user: UserBase):
    """
    User creation logic
    """
    pass
    new_user = User(
        email = user.email,
        username = user.username,
        hashed_password = user.hashed_password
    )
    sesssion.add(new_user)
    await sesssion.commit()
    await sesssion.refresh(new_user)
    return new_user

