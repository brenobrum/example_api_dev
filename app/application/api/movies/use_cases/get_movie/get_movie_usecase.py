from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.movie.movie import Movie
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class GetMovieUseCaseRequest(BaseModel):
    id: str


class GetMovieUseCaseResponse(BaseModel):
    movie: Movie


class GetMovieUseCase:
    def __init__(self, repository: BaseDbRepository[Movie]) -> None:
        self.repository = repository

    def execute(self, request: GetMovieUseCaseRequest) -> GetMovieUseCaseResponse:
        try:
            movie: Movie = self.repository.get(request.id)
            return GetMovieUseCaseResponse(movie=movie)
        except KeyError:
            raise HTTPException(status_code=404, detail="Movie not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
