from app.application.api.movies.use_cases.update_movie.update_movie_usecase import UpdateMovieUseCase
from app.infra.repositories.db.local.movie import LocalMovieRepository


class UpdateMovieUseCaseFactory:
    def create(self) -> UpdateMovieUseCase:
        return UpdateMovieUseCase(repository=LocalMovieRepository())


class UpdateMovieUseCaseTestFactory:
    def create(self) -> UpdateMovieUseCase:
        return UpdateMovieUseCase(repository=LocalMovieRepository())


update_movie_use_case_factory: UpdateMovieUseCaseFactory = UpdateMovieUseCaseFactory()
