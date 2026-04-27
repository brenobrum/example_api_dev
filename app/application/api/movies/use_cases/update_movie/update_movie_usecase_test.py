from datetime import datetime

from app.application.api.movies.use_cases.update_movie.update_movie_factory import UpdateMovieUseCaseTestFactory
from app.application.api.movies.use_cases.update_movie.update_movie_usecase import UpdateMovieUseCase, UpdateMovieUseCaseRequest, UpdateMovieUseCaseResponse
from app.domain.models.movie.movie import Movie


def test_update_movie_returns_response() -> None:
    use_case: UpdateMovieUseCase = UpdateMovieUseCaseTestFactory().create()
    use_case.repository.create(
        Movie(
            id="movie-update-1",
            name="Old Movie",
            description="Old Description",
            author_id="author-1",
            genre_id="genre-1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: UpdateMovieUseCaseRequest = UpdateMovieUseCaseRequest(
        id="movie-update-1",
        name="Movie 1",
        description="Description 1",
        author_id="author-2",
        genre_id="genre-2",
    )
    response: UpdateMovieUseCaseResponse = use_case.execute(request)
    assert response.movie.name == "Movie 1"
