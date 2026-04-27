from app.application.api.genres.use_cases.get_genre.get_genre_usecase import GetGenreUseCase
from app.infra.repositories.db.local.genre import LocalGenreRepository


class GetGenreUseCaseFactory:
    def create(self) -> GetGenreUseCase:
        return GetGenreUseCase(repository=LocalGenreRepository())


class GetGenreUseCaseTestFactory:
    def create(self) -> GetGenreUseCase:
        return GetGenreUseCase(repository=LocalGenreRepository())


get_genre_use_case_factory: GetGenreUseCaseFactory = GetGenreUseCaseFactory()
