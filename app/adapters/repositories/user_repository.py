import motor
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.entities.user import User

# MongoDB connection settings
MONGO_DB_URL = "mongodb+srv://myMac:clothingApp@cluster0.l19f373.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB_NAME = "clothing_app"

client = AsyncIOMotorClient(MONGO_DB_URL)
db = client[MONGO_DB_NAME]


# Collection name for user data
USERS_COLLECTION = "user_data"

class UserRepository:
    def __init__(self, db):
        self.db = db
        self.collection = db[USERS_COLLECTION]

    async def create_user(self, user: User):
        user_dict = user.dict()
        result = await self.collection.insert_one(user_dict)
        return result.inserted_id

