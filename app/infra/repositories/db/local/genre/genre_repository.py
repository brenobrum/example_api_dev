from app.infra.repositories.db.local.local_base_db_repository import LocalBaseDbRepository
from app.domain.repositories.genre.genre_repository import GenreRepository
from app.domain.models.genre.genre import Genre
    
class LocalGenreRepository(GenreRepository, LocalBaseDbRepository[Genre]):
    def create(self, entity: Genre) -> Genre:
        return super().create(entity)

    def get(self, id: str) -> Genre:
        return super().get(id)

    def update(self, entity: Genre) -> Genre:
        return super().update(entity)

    def delete(self, id: str) -> None:
        return super().delete(id)

    def list(self) -> list[Genre]:
        return super().list()