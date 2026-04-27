from app.domain.models.movie.movie import Movie
from app.domain.repositories.movie.movie_repository import MovieRepository
from app.infra.repositories.db.local.local_base_db_repository import LocalBaseDbRepository


class LocalMovieRepository(MovieRepository, LocalBaseDbRepository[Movie]):
    def create(self, entity: Movie) -> Movie:
        return super().create(entity)

    def get(self, id: str) -> Movie:
        return super().get(id)

    def update(self, entity: Movie) -> Movie:
        return super().update(entity)

    def delete(self, id: str) -> None:
        return super().delete(id)

    def list(self) -> list[Movie]:
        return super().list()
