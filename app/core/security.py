"""
This module contains security codes.
"""

import time
from datetime import timedelta, datetime, timezone
from typing import Optional
import jwt
from passlib.context import CryptContext
from decouple import config


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify the plain password and hashed password.
    by pwd_context
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_hashed_password(password: str) -> str:
    """
    Hashed password by pwd_context.
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Create a acceess token for user.
    """

    encode_data = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=config("ACCESS_TOKEN_LIFE_MINUIT")
        )

    encode_data.update({"exp": expire})
    encoded_jwt = jwt.encode(
        encode_data, config("SECRET_KEY"), config("ENCODE_ALGORITHM")
    )
    return encoded_jwt
