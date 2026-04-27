from app.application.api.movies.use_cases.list_movies.list_movies_usecase import ListMoviesUseCase
from app.infra.repositories.db.local.movie import LocalMovieRepository


class ListMoviesUseCaseFactory:
    def create(self) -> ListMoviesUseCase:
        return ListMoviesUseCase(repository=LocalMovieRepository())


class ListMoviesUseCaseTestFactory:
    def create(self) -> ListMoviesUseCase:
        return ListMoviesUseCase(repository=LocalMovieRepository())


list_movies_use_case_factory: ListMoviesUseCaseFactory = ListMoviesUseCaseFactory()
