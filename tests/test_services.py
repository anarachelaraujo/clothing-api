import httpx
from core.application import UserService
from adapters.database_adapter import DatabaseUserRepository
from core.domain.entities import UserEntity
from main import app
from httpx import AsyncClient
import pytest
from faker import Faker

fake = Faker()


client = httpx.AsyncClient(app=app, base_url="http://testserver")
random_email = fake.email()


@pytest.mark.asyncio
async def test_register_user():
    # Mock the dependencies
    user_repository = DatabaseUserRepository()
    user_service = UserService(user_repository)

    # Create a user to register
    user_data = UserEntity(email=random_email, password="password")

    # Test the register_user method
    response = await client.post("/register/", json=user_data.dict())
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}


@pytest.mark.asyncio
async def test_login_for_access_token():
    # Mock the dependencies
    user_repository = DatabaseUserRepository()
    user_service = UserService(user_repository)

    # Create a user to authenticate
    user_data = UserEntity(email=random_email, password="password")

    # Register the user (this should be in a separate test case)
    await client.post("/register/", json=user_data.dict())

    # Test the login_for_access_token method
    response = await client.post("/token", json=user_data.dict())
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
