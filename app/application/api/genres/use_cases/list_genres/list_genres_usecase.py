from pydantic import BaseModel

from app.domain.models.genre.genre import Genre
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class ListGenresUseCaseRequest(BaseModel):
    pass


class ListGenresUseCaseResponse(BaseModel):
    genres: list[Genre]


class ListGenresUseCase:
    def __init__(self, repository: BaseDbRepository[Genre]) -> None:
        self.repository = repository

    def execute(self, request: ListGenresUseCaseRequest) -> ListGenresUseCaseResponse:
        _ = request
        return ListGenresUseCaseResponse(genres=self.repository.list())
