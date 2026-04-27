from app.application.api.genres.use_cases.update_genre.update_genre_usecase import UpdateGenreUseCase
from app.infra.repositories.db.local.genre import LocalGenreRepository


class UpdateGenreUseCaseFactory:
    def create(self) -> UpdateGenreUseCase:
        return UpdateGenreUseCase(repository=LocalGenreRepository())


class UpdateGenreUseCaseTestFactory:
    def create(self) -> UpdateGenreUseCase:
        return UpdateGenreUseCase(repository=LocalGenreRepository())


update_genre_use_case_factory: UpdateGenreUseCaseFactory = UpdateGenreUseCaseFactory()
