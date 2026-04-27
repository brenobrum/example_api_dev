from app.application.api.movies.use_cases.get_movie.get_movie_usecase import GetMovieUseCase
from app.infra.repositories.db.local.movie import LocalMovieRepository


class GetMovieUseCaseFactory:
    def create(self) -> GetMovieUseCase:
        return GetMovieUseCase(repository=LocalMovieRepository())


class GetMovieUseCaseTestFactory:
    def create(self) -> GetMovieUseCase:
        return GetMovieUseCase(repository=LocalMovieRepository())


get_movie_use_case_factory: GetMovieUseCaseFactory = GetMovieUseCaseFactory()
