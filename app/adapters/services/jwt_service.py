import jwt
import datetime
from app.core.entities.user import User
from decouple import config as decouple_config

SECRET_KEY = decouple_config("SECRET_KEY")

def generate_token(user: User):
    token_data = {
        "sub": user.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm="HS256")
    return {"access_token": token}

def authenticate_user(user_data: User, user_collection):
    user = user_collection.find_one({"email": user_data.email, "password": user_data.password})
    return user is not None

