
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

