from pydantic import BaseModel

from app.domain.models.movie.movie import Movie
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class ListMoviesUseCaseRequest(BaseModel):
    pass


class ListMoviesUseCaseResponse(BaseModel):
    movies: list[Movie]


class ListMoviesUseCase:
    def __init__(self, repository: BaseDbRepository[Movie]) -> None:
        self.repository = repository

    def execute(self, request: ListMoviesUseCaseRequest) -> ListMoviesUseCaseResponse:
        _ = request
        return ListMoviesUseCaseResponse(movies=self.repository.list())
