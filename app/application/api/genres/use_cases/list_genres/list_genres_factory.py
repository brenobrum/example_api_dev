from app.application.api.genres.use_cases.list_genres.list_genres_usecase import ListGenresUseCase
from app.infra.repositories.db.local.genre import LocalGenreRepository


class ListGenresUseCaseFactory:
    def create(self) -> ListGenresUseCase:
        return ListGenresUseCase(repository=LocalGenreRepository())


class ListGenresUseCaseTestFactory:
    def create(self) -> ListGenresUseCase:
        return ListGenresUseCase(repository=LocalGenreRepository())


list_genres_use_case_factory: ListGenresUseCaseFactory = ListGenresUseCaseFactory()
