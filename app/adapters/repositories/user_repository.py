# import motor
# from motor.motor_asyncio import AsyncIOMotorClient
# from app.core.entities.user import User

# # MongoDB connection settings
# MONGO_DB_URL = "mongodb+srv://myMac:clothingApp@cluster0.l19f373.mongodb.net/?retryWrites=true&w=majority"
# MONGO_DB_NAME = "clothing_app"
# print("Hello", "how are you?", sep="---")
# client = AsyncIOMotorClient(MONGO_DB_URL)
# db = client[MONGO_DB_NAME]

# # Collection name for user data
# USERS_COLLECTION = "user_data"

# class UserRepository:
#     def __init__(self, db):
#         self.db = db
#         self.collection =  db[USERS_COLLECTION]

#     async def create_user(self, user: User):
#         print("Hello", "how are you?", sep="---")
#         print(user)
#         user_dict = user.dict()
#         print(user_dict)
#         result = await self.collection.insert_one(user)
#         return result.inserted_id


from app.core.entities.user import User
import pymongo

class UserRepository:
    def __init__(self, db):
            client = pymongo.MongoClient("mongodb+srv://myMac:clothingApp@cluster0.l19f373.mongodb.net/?retryWrites=true&w=majority")
            db = client.myDatabase
            my_collection = db["user_data"]


    async def create_user(self, user: User):
        result = self.my_collection.insert_many(user)
        inserted_count = len(result.inserted_ids)
        print("I inserted %x documents." %(inserted_count))