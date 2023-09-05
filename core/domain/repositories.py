# core/domain/repositories.py

from abc import ABC, abstractmethod
from core.domain.entities import UserEntity


class UserRepository(ABC):
    @abstractmethod
    async def find_by_email(self, email: str) -> UserEntity:
        pass

    @abstractmethod
    async def insert_user(self, user: UserEntity) -> None:
        pass
