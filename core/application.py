# core/application.py

import jwt
import datetime
from core.domain.entities import User, Clothes
from core.domain.repositories import UserRepository
from fastapi import UploadFile


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def register_user(self, email: str, password: str) -> None:
        user = User(email=email, password=password)
        await self.user_repository.insert_user(user)

    async def authenticate_user(self, email: str, password: str) -> bool:
        user = await self.user_repository.find_by_email(email)
        return user and user.password == password

    async def generate_jwt_token(self, email: str) -> str:
        token_data = {
            "sub": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
        token = jwt.encode(
            token_data, "gwZbGHlt28VoI-NXbc06nX6z5ybqfvW9-KpLAHk1IDQ", algorithm="HS256")
        return token

    async def find_user_by_email(self, email: str) -> User:
        return await self.user_repository.find_by_email(email)

    async def add_new_clothes(self, clothes: Clothes, image: UploadFile) -> None:
        return await self.user_repository.insert_clothes(clothes, image)
