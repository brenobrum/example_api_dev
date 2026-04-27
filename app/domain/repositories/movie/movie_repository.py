from app.domain.models.movie.movie import Movie
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class MovieRepository(BaseDbRepository[Movie]):
    pass
