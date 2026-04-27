from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.author.author import Author
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class GetAuthorUseCaseRequest(BaseModel):
    id: str


class GetAuthorUseCaseResponse(BaseModel):
    author: Author


class GetAuthorUseCase:
    def __init__(self, repository: BaseDbRepository[Author]) -> None:
        self.repository = repository

    def execute(self, request: GetAuthorUseCaseRequest) -> GetAuthorUseCaseResponse:
        try:
            author: Author = self.repository.get(request.id)
            return GetAuthorUseCaseResponse(author=author)
        except KeyError:
            raise HTTPException(status_code=404, detail="Author not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
