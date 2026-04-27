from app.domain.repositories.db.base_db_repository import BaseDbRepository
from typing import Protocol, TypeVar, cast

class HasId(Protocol):
    id: str

T = TypeVar('T', bound=HasId)

class LocalBaseDbRepository(BaseDbRepository[T]):
    _storage: dict[str, HasId] = {}

    def __init__(self) -> None:
        if "_storage" not in self.__class__.__dict__:
            self.__class__._storage = {}
        self.db: dict[str, T] = cast(dict[str, T], self.__class__._storage)

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