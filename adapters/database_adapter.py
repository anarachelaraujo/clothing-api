from motor.motor_asyncio import AsyncIOMotorClient
from core.domain.entities import UserEntity
from core.domain.repositories import UserRepository


class DatabaseUserRepository:
    def __init__(self):
        self.client = AsyncIOMotorClient(
            "mongodb+srv://myMac:clothingApp@cluster0.l19f373.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["clothing_app"]
        self.users_collection = self.db["user_data"]

    async def find_by_email(self, email: str) -> UserEntity:
        user = await self.users_collection.find_one({"email": email})
        return UserEntity(**user) if user else None

    async def insert_user(self, user: UserEntity) -> None:
        user_data = user.dict()  # Convert UserEntity to a dictionary
        await self.users_collection.insert_one(user_data)
