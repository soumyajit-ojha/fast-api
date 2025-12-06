"""
Router file for the project.
"""

from fastapi import APIRouter
from fastapi import Depends
from typing import Annotated
from app.core.database import get_session
from app.schemas.schemas import UserBase, UserRead
from app.models.services import create_user
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/users", tags=["User"])

@router.post("/create", response_model=UserRead)
async def user_create(session:Annotated[AsyncSession, Depends(get_session)], user: UserBase):
    """
    create a user 
    """

    return await create_user(session, user)
