from app.adapters.repositories.user_repository import UserRepository
from app.core.entities.user import User
from app.adapters.services.jwt_service import authenticate_user, generate_token

async def register_user_usecase(user: User):
    return await UserRepository.create_user(user)

async def authenticate_user_usecase(user: User):
    return await authenticate_user(user)


