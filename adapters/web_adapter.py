
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from core.application import UserService
from adapters.database_adapter import DatabaseUserRepository
from pydantic import BaseModel


app = FastAPI()

# Define allowed origins
origins = [
    "http://localhost:3001",
    "http://localhost:3000"
]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


class User(BaseModel):
    email: str
    password: str


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
