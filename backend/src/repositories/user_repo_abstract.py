from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Optional


class UserRepoAbstract(ABC):
    @classmethod
    @abstractmethod
    async def read_all(cls) -> List[dict]:
        pass

    @classmethod
    @abstractmethod
    async def save_user(cls, user_data: dict) -> dict:
        pass

    @classmethod
    @abstractmethod
    async def get_by_username(cls, username: str) -> Optional[dict]:
        pass

    @classmethod
    @abstractmethod
    async def update_by_username(cls, username: str, updates: dict) -> Optional[dict]:
        pass
