# core/domain/repositories.py

from abc import ABC, abstractmethod
from core.domain.entities import User, Clothes


class UserRepository(ABC):
    @abstractmethod
    async def find_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    async def insert_user(self, user: User) -> None:
        pass

    @abstractmethod
    async def insert_clothes(self, clothes: Clothes, image) -> None:
        pass
