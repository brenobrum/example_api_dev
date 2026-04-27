from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.genre.genre import Genre
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class GetGenreUseCaseRequest(BaseModel):
    id: str


class GetGenreUseCaseResponse(BaseModel):
    genre: Genre


class GetGenreUseCase:
    def __init__(self, repository: BaseDbRepository[Genre]) -> None:
        self.repository = repository

    def execute(self, request: GetGenreUseCaseRequest) -> GetGenreUseCaseResponse:
        try:
            genre: Genre = self.repository.get(request.id)
            return GetGenreUseCaseResponse(genre=genre)
        except KeyError:
            raise HTTPException(status_code=404, detail="Genre not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
