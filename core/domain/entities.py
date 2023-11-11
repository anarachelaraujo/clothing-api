from pydantic import BaseModel
from fastapi import UploadFile


class User(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    is_valid: bool


class Clothes(BaseModel):
    type: str
    color: str
    description: str
    userId: int
