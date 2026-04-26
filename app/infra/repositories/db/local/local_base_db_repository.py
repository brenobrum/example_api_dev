from app.domain.repositories.db.base_db_repository import BaseDbRepository
from typing import Protocol, TypeVar

class HasId(Protocol):
    id: str

T = TypeVar('T', bound=HasId)

class LocalBaseDbRepository(BaseDbRepository[T]):

    def __init__(self) -> None:
        self.db: dict[str, T] = {}

    def create(self, entity: T) -> T:
        self.db[entity.id] = entity
        return entity

    def get(self, id: str) -> T:
        return self.db[id]

    def update(self, entity: T) -> T:
        self.db[entity.id] = entity
        return entity

    def delete(self, id: str) -> None:
        del self.db[id]

    def list(self) -> list[T]:
        return list(self.db.values())