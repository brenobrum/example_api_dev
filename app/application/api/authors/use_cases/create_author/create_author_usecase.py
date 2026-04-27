from datetime import datetime
import uuid

from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.author.author import Author
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class CreateAuthorUseCaseRequest(BaseModel):
    name: str
    description: str


class CreateAuthorUseCaseResponse(BaseModel):
    author: Author


class CreateAuthorUseCase:
    def __init__(self, repository: BaseDbRepository[Author]) -> None:
        self.repository = repository

    def execute(self, request: CreateAuthorUseCaseRequest) -> CreateAuthorUseCaseResponse:
        try:
            temp_author: Author = Author(
                id=str(uuid.uuid4()),
                name=request.name,
                description=request.description,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            saved_author: Author = self.repository.create(temp_author)
            return CreateAuthorUseCaseResponse(author=saved_author)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
