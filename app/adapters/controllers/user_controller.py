from fastapi import APIRouter, HTTPException, Depends
from app.core.entities.user import User
from app.adapters.services.jwt_service import generate_token, authenticate_user
from app.adapters.repositories.user_repository import UserRepository
from app.core.usecases.user_usecase import register_user

router = APIRouter()

@router.post("/register/")
async def register_user_controller(user: User, user_repository: UserRepository = Depends(UserRepository)):
    return await user_repository.create_user(user)

@router.post("/token")
async def login_for_access_token(user: User, user_repository: UserRepository = Depends(UserRepository)):
    if authenticate_user(user, user_repository):
        return await generate_token(user)
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


