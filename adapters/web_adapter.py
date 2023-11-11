
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from core.application import UserService
from adapters.database_adapter import DatabaseUserRepository
from pydantic import BaseModel
from PIL import Image
from io import BytesIO
from bson import ObjectId
from core.domain.entities import User, Clothes


app = FastAPI()

# Define allowed origins
origins = [
    "http://localhost:3001",
    "http://localhost:3000"
]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the clothing app API."}


@app.post("/register/")
async def register_user(user: User):
    user_repository = DatabaseUserRepository()
    user_service = UserService(user_repository)

    # Check if the email already exists
    existing_user = await user_repository.find_by_email(user.email)

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    # Insert user into the database
    await user_service.register_user(user.email, user.password)

    return {"message": "User registered successfully"}


@app.post("/token")
async def login_for_access_token(user: User):
    user_repository = DatabaseUserRepository()
    user_service = UserService(user_repository)

    if await user_service.authenticate_user(user.email, user.password):
        # Generate JWT token
        token = await user_service.generate_jwt_token(user.email)
        return {"access_token": token, "token_type": "bearer"}

    raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/options")
def get_options():
    return ["top", "bottom", "shoes", "accessories"]


@app.post("/clothes")
async def upload_image(clothes: Clothes, imageUpload: UploadFile):

    user_repository = DatabaseUserRepository()
    user_service = UserService(user_repository)

    image_data = await imageUpload.read()
    image = Image.open(BytesIO(image_data))

    await user_service.insert_clothes(clothes.color, clothes.type, clothes.description, clothes.userId, image)

    return {"message": "User registered successfully"}
