from app.application.api.movies.use_cases.delete_movie.delete_movie_usecase import DeleteMovieUseCase
from app.infra.repositories.db.local.movie import LocalMovieRepository


class DeleteMovieUseCaseFactory:
    def create(self) -> DeleteMovieUseCase:
        return DeleteMovieUseCase(repository=LocalMovieRepository())


class DeleteMovieUseCaseTestFactory:
    def create(self) -> DeleteMovieUseCase:
        return DeleteMovieUseCase(repository=LocalMovieRepository())


delete_movie_use_case_factory: DeleteMovieUseCaseFactory = DeleteMovieUseCaseFactory()
