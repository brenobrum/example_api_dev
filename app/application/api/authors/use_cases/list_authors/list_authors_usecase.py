from pydantic import BaseModel

from app.domain.models.author.author import Author
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class ListAuthorsUseCaseRequest(BaseModel):
    pass


class ListAuthorsUseCaseResponse(BaseModel):
    authors: list[Author]


class ListAuthorsUseCase:
    def __init__(self, repository: BaseDbRepository[Author]) -> None:
        self.repository = repository

    def execute(self, request: ListAuthorsUseCaseRequest) -> ListAuthorsUseCaseResponse:
        _ = request
        return ListAuthorsUseCaseResponse(authors=self.repository.list())
