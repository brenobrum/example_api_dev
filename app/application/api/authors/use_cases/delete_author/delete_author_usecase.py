from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.repositories.db.base_db_repository import BaseDbRepository
from app.domain.models.author.author import Author


class DeleteAuthorUseCaseRequest(BaseModel):
    id: str


class DeleteAuthorUseCaseResponse(BaseModel):
    message: str


class DeleteAuthorUseCase:
    def __init__(self, repository: BaseDbRepository[Author]) -> None:
        self.repository = repository

    def execute(self, request: DeleteAuthorUseCaseRequest) -> DeleteAuthorUseCaseResponse:
        try:
            self.repository.delete(request.id)
            return DeleteAuthorUseCaseResponse(message="Author deleted")
        except KeyError:
            raise HTTPException(status_code=404, detail="Author not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
