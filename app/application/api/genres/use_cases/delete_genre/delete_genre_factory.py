from app.application.api.genres.use_cases.delete_genre.delete_genre_usecase import DeleteGenreUseCase
from app.infra.repositories.db.local.genre import LocalGenreRepository


class DeleteGenreUseCaseFactory:
    def create(self) -> DeleteGenreUseCase:
        return DeleteGenreUseCase(repository=LocalGenreRepository())


class DeleteGenreUseCaseTestFactory:
    def create(self) -> DeleteGenreUseCase:
        return DeleteGenreUseCase(repository=LocalGenreRepository())


delete_genre_use_case_factory: DeleteGenreUseCaseFactory = DeleteGenreUseCaseFactory()
