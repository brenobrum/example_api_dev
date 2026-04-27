from datetime import datetime
import uuid

from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.movie.movie import Movie
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class CreateMovieUseCaseRequest(BaseModel):
    name: str
    description: str
    author_id: str
    genre_id: str


class CreateMovieUseCaseResponse(BaseModel):
    movie: Movie


class CreateMovieUseCase:
    def __init__(self, repository: BaseDbRepository[Movie]) -> None:
        self.repository = repository

    def execute(self, request: CreateMovieUseCaseRequest) -> CreateMovieUseCaseResponse:
        try:
            temp_movie: Movie = Movie(
                id=str(uuid.uuid4()),
                name=request.name,
                description=request.description,
                author_id=request.author_id,
                genre_id=request.genre_id,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            saved_movie: Movie = self.repository.create(temp_movie)
            return CreateMovieUseCaseResponse(movie=saved_movie)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
