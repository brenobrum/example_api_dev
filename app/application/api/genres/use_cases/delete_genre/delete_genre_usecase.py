from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.repositories.db.base_db_repository import BaseDbRepository
from app.domain.models.genre.genre import Genre


class DeleteGenreUseCaseRequest(BaseModel):
    id: str


class DeleteGenreUseCaseResponse(BaseModel):
    message: str


class DeleteGenreUseCase:
    def __init__(self, repository: BaseDbRepository[Genre]) -> None:
        self.repository = repository

    def execute(self, request: DeleteGenreUseCaseRequest) -> DeleteGenreUseCaseResponse:
        try:
            self.repository.delete(request.id)
            return DeleteGenreUseCaseResponse(message="Genre deleted")
        except KeyError:
            raise HTTPException(status_code=404, detail="Genre not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
