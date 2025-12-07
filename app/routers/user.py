"""
This module contains routers for user model.
"""

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.schemas.user import UserCreate, UserResponse
from app.services import user_services

router = APIRouter()

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    """
    endpoint function for user register.
    """
    user = await user_services.get_user_by_email(db=db, email=user.email)
    if user:
        HTTPException(status_code=400, detail="User already exist")
    await user_services.create_user(user=user, db=db)

