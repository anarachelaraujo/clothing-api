from typing import Self
from motor.motor_asyncio import AsyncIOMotorClient
from core.domain.entities import User, Clothes
from fastapi import UploadFile


class DatabaseUserRepository:
    def __init__(self):
        self.client = AsyncIOMotorClient(
            "mongodb+srv://myMac:clothingApp@cluster0.l19f373.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["clothing_app"]
        self.users_collection = self.db["user_data"]
        self.clothes_collection = self.db["clothes"]

    async def find_by_email(self, email: str) -> User:
        user = await self.users_collection.find_one({"email": email})
        return User(**user) if user else None

    async def insert_user(self, user: User) -> None:
        user_data = user.dict()  # Convert User to a dictionary
        await self.users_collection.insert_one(user_data)

    async def insert_clothes(self, clothes: Clothes, file: UploadFile) -> None:
        clothes_data = clothes.dict()
        await self.clothes_collection.insert_one(clothes_data, file)
