from datetime import datetime

from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.genre.genre import Genre
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class UpdateGenreUseCaseRequest(BaseModel):
    id: str
    name: str
    description: str


class UpdateGenreUseCaseResponse(BaseModel):
    genre: Genre


class UpdateGenreUseCase:
    def __init__(self, repository: BaseDbRepository[Genre]) -> None:
        self.repository = repository

    def execute(self, request: UpdateGenreUseCaseRequest) -> UpdateGenreUseCaseResponse:
        try:
            existing_genre: Genre = self.repository.get(request.id)
            updated_genre: Genre = Genre(
                id=existing_genre.id,
                name=request.name,
                description=request.description,
                created_at=existing_genre.created_at,
                updated_at=datetime.now(),
            )
            genre: Genre = self.repository.update(updated_genre)
            return UpdateGenreUseCaseResponse(genre=genre)
        except KeyError:
            raise HTTPException(status_code=404, detail="Genre not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
