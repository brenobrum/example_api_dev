from app.domain.models.author.author import Author
from app.domain.repositories.author.author_repository import AuthorRepository
from app.infra.repositories.db.local.local_base_db_repository import LocalBaseDbRepository


class LocalAuthorRepository(AuthorRepository, LocalBaseDbRepository[Author]):
    def create(self, entity: Author) -> Author:
        return super().create(entity)

    def get(self, id: str) -> Author:
        return super().get(id)

    def update(self, entity: Author) -> Author:
        return super().update(entity)

    def delete(self, id: str) -> None:
        return super().delete(id)

    def list(self) -> list[Author]:
        return super().list()
