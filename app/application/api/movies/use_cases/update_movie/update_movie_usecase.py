from datetime import datetime

from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.movie.movie import Movie
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class UpdateMovieUseCaseRequest(BaseModel):
    id: str
    name: str
    description: str
    author_id: str
    genre_id: str


class UpdateMovieUseCaseResponse(BaseModel):
    movie: Movie


class UpdateMovieUseCase:
    def __init__(self, repository: BaseDbRepository[Movie]) -> None:
        self.repository = repository

    def execute(self, request: UpdateMovieUseCaseRequest) -> UpdateMovieUseCaseResponse:
        try:
            existing_movie: Movie = self.repository.get(request.id)
            updated_movie: Movie = Movie(
                id=existing_movie.id,
                name=request.name,
                description=request.description,
                author_id=request.author_id,
                genre_id=request.genre_id,
                created_at=existing_movie.created_at,
                updated_at=datetime.now(),
            )
            movie: Movie = self.repository.update(updated_movie)
            return UpdateMovieUseCaseResponse(movie=movie)
        except KeyError:
            raise HTTPException(status_code=404, detail="Movie not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
