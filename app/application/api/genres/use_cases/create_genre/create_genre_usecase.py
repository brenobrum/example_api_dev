from app.domain.models.genre.genre import Genre
from app.domain.repositories.db.base_db_repository import BaseDbRepository
from datetime import datetime
from fastapi import HTTPException
from pydantic import BaseModel
import uuid

class CreateGenreUseCaseRequest(BaseModel):
    name: str
    description: str

class CreateGenreUseCaseResponse(BaseModel):
    genre: Genre

class CreateGenreUseCase:
    def __init__(self, genre_repository: BaseDbRepository[Genre]) -> None:
        self.genre_repository: BaseDbRepository[Genre] = genre_repository

    def execute(self, request: CreateGenreUseCaseRequest) -> CreateGenreUseCaseResponse:
        try:
            temp_genre: Genre = Genre(
                id=str(uuid.uuid4()),
                name=request.name,
                description=request.description,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            genre: Genre = self.genre_repository.create(temp_genre)
            
            return CreateGenreUseCaseResponse(
                genre=genre,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))