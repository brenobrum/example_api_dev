from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.repositories.db.base_db_repository import BaseDbRepository
from app.domain.models.movie.movie import Movie


class DeleteMovieUseCaseRequest(BaseModel):
    id: str


class DeleteMovieUseCaseResponse(BaseModel):
    message: str


class DeleteMovieUseCase:
    def __init__(self, repository: BaseDbRepository[Movie]) -> None:
        self.repository = repository

    def execute(self, request: DeleteMovieUseCaseRequest) -> DeleteMovieUseCaseResponse:
        try:
            self.repository.delete(request.id)
            return DeleteMovieUseCaseResponse(message="Movie deleted")
        except KeyError:
            raise HTTPException(status_code=404, detail="Movie not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
