from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import motor
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel  # Import Pydantic's BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
import datetime
import config

app = FastAPI()

# MongoDB connection settings
MONGO_DB_URL = "mongodb+srv://myMac:clothingApp@cluster0.l19f373.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB_NAME = "clothing_app"

client = AsyncIOMotorClient(MONGO_DB_URL)
db = client[MONGO_DB_NAME]

# Collection name for user data
USERS_COLLECTION = "user_data"

# Define allowed origins
origins = [
    "http://localhost:3001", 
    "http://localhost:3000"
]

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Welcome to the options API."}

@app.get("/options")
def get_options():
        return {"top", "bottom", "shoes", "accessories"}


# User model
class User(BaseModel):
        email: str
        password: str

# Pydantic model for the response
class RegistrationResponse(BaseModel):
    message: str

@app.post("/register/", response_model=RegistrationResponse)  # Use the response_model parameter
async def register_user(user: User):
    # Check if the email already exists
    user_collection = db[USERS_COLLECTION]
    existing_user = await user_collection.find_one({"email": user.email})

    if existing_user:
        raise HTTPException(status_code=400, detail="email already exists")

    # Insert user into the database
    print(user)
    await user_collection.insert_one(user.__dict__)
    
    # Respond with a JSON response
    return RegistrationResponse(message="User registered successfully")

# Function to verify user credentials
async def authenticate_user(user_data: User):
    user_collection = db[USERS_COLLECTION]
    user = await user_collection.find_one({"email": user_data.email, "password": user_data.password})
    print(user)
    if user:
        return True
    else:
        return False

# Route to generate a JWT token upon successful login
@app.post("/token")
async def login_for_access_token(user: User):
    email = user.email
    password = user.password

    if not await authenticate_user(user):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Generate JWT token
    token_data = {"sub": email, "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)}
    token = jwt.encode(token_data, config.SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)