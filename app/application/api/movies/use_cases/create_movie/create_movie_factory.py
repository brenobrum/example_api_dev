from app.application.api.movies.use_cases.create_movie.create_movie_usecase import CreateMovieUseCase
from app.infra.repositories.db.local.movie import LocalMovieRepository


class CreateMovieUseCaseFactory:
    def create(self) -> CreateMovieUseCase:
        return CreateMovieUseCase(repository=LocalMovieRepository())


class CreateMovieUseCaseTestFactory:
    def create(self) -> CreateMovieUseCase:
        return CreateMovieUseCase(repository=LocalMovieRepository())


create_movie_use_case_factory: CreateMovieUseCaseFactory = CreateMovieUseCaseFactory()
