# core/domain/entities.py

from pydantic import BaseModel


class UserEntity(BaseModel):
    email: str
    password: str
