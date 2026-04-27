from app.domain.models.author.author import Author
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class AuthorRepository(BaseDbRepository[Author]):
    pass
