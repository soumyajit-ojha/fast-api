"""
This module has schemas for authentication table
"""

from pydantic import BaseModel


class Token(BaseModel):
    """
    Token field datatype config.
    """

    access_token: str
    token_type: str


class TokenData(BaseExceptionGroup):
    """
    TokenData configuration of field
    """

    username: str | None = None
