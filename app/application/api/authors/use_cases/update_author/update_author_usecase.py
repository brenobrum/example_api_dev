from datetime import datetime

from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.author.author import Author
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class UpdateAuthorUseCaseRequest(BaseModel):
    id: str
    name: str
    description: str


class UpdateAuthorUseCaseResponse(BaseModel):
    author: Author


class UpdateAuthorUseCase:
    def __init__(self, repository: BaseDbRepository[Author]) -> None:
        self.repository = repository

    def execute(self, request: UpdateAuthorUseCaseRequest) -> UpdateAuthorUseCaseResponse:
        try:
            existing_author: Author = self.repository.get(request.id)
            updated_author: Author = Author(
                id=existing_author.id,
                name=request.name,
                description=request.description,
                created_at=existing_author.created_at,
                updated_at=datetime.now(),
            )
            author: Author = self.repository.update(updated_author)
            return UpdateAuthorUseCaseResponse(author=author)
        except KeyError:
            raise HTTPException(status_code=404, detail="Author not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
