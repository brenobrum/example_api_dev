from app.application.api.genres.use_cases.create_genre.create_genre_usecase import CreateGenreUseCase
from app.infra.repositories.db.local.genre import LocalGenreRepository

class CreateGenreUseCaseFactory:
    def create(self) -> CreateGenreUseCase:
        return CreateGenreUseCase(genre_repository=LocalGenreRepository())

class CreateGenreUseCaseTestFactory:
    def create(self) -> CreateGenreUseCase:
        return CreateGenreUseCase(genre_repository=LocalGenreRepository())

create_genre_use_case_factory: CreateGenreUseCaseFactory = CreateGenreUseCaseFactory()