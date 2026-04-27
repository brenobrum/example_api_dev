from datetime import datetime

from fastapi import HTTPException

from app.application.api.movies.use_cases.delete_movie.delete_movie_factory import DeleteMovieUseCaseTestFactory
from app.application.api.movies.use_cases.delete_movie.delete_movie_usecase import DeleteMovieUseCase, DeleteMovieUseCaseRequest, DeleteMovieUseCaseResponse
from app.application.api.movies.use_cases.get_movie.get_movie_usecase import GetMovieUseCase, GetMovieUseCaseRequest
from app.domain.models.movie.movie import Movie


def test_delete_movie_returns_response() -> None:
    use_case: DeleteMovieUseCase = DeleteMovieUseCaseTestFactory().create()
    use_case.repository.create(
        Movie(
            id="movie-delete-1",
            name="Movie 1",
            description="Description 1",
            author_id="author-1",
            genre_id="genre-1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: DeleteMovieUseCaseRequest = DeleteMovieUseCaseRequest(id="movie-delete-1")
    response: DeleteMovieUseCaseResponse = use_case.execute(request)
    assert response.message == "Movie deleted"

    get_use_case: GetMovieUseCase = GetMovieUseCase(repository=use_case.repository)
    try:
        get_use_case.execute(GetMovieUseCaseRequest(id="movie-delete-1"))
        assert False, "Deleted movie should not be found"
    except HTTPException as e:
        assert e.status_code == 404
