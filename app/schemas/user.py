"""
This module contains schemas for User model.
"""

from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    """
    Basic User model fields and their types
    """

    email: str
    username: str


class UserCreate(UserBase):
    """
    Data validation class for user creation or retrieve.
    """
    password: str

class UserResponse(UserBase):
    """
    Schema class for user response
    """
    id: int
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
    # below class id depricated
    # class Config:
    #     from_attributes = True
