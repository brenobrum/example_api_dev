from app.application.api.movies.use_cases.create_movie.create_movie_factory import CreateMovieUseCaseTestFactory
from app.application.api.movies.use_cases.create_movie.create_movie_usecase import CreateMovieUseCase, CreateMovieUseCaseRequest, CreateMovieUseCaseResponse


def test_create_movie_returns_response() -> None:
    use_case: CreateMovieUseCase = CreateMovieUseCaseTestFactory().create()
    request: CreateMovieUseCaseRequest = CreateMovieUseCaseRequest(
        name="Movie 1",
        description="Description 1",
        author_id="author-1",
        genre_id="genre-1",
    )
    response: CreateMovieUseCaseResponse = use_case.execute(request)
    assert response.movie.name == "Movie 1"
