from datetime import datetime

from app.application.api.movies.use_cases.get_movie.get_movie_factory import GetMovieUseCaseTestFactory
from app.application.api.movies.use_cases.get_movie.get_movie_usecase import GetMovieUseCase, GetMovieUseCaseRequest, GetMovieUseCaseResponse
from app.domain.models.movie.movie import Movie


def test_get_movie_returns_response() -> None:
    use_case: GetMovieUseCase = GetMovieUseCaseTestFactory().create()
    use_case.repository.create(
        Movie(
            id="movie-id-1",
            name="Movie 1",
            description="Description 1",
            author_id="author-1",
            genre_id="genre-1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: GetMovieUseCaseRequest = GetMovieUseCaseRequest(id="movie-id-1")
    response: GetMovieUseCaseResponse = use_case.execute(request)
    assert response.movie.name == "Movie 1"
