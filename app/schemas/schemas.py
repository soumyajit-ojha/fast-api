"""
This module contains schemas for models on tables.py
"""

from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    """
    Basic User model fields and their types
    """

    email: str
    username: str
    hashed_password: str


class UserRead(UserBase):
    """
    Data validation class for user creation or retrieve.
    """

    id: int
    is_active: bool | None
