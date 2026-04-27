from datetime import datetime

from app.application.api.movies.use_cases.list_movies.list_movies_factory import ListMoviesUseCaseTestFactory
from app.application.api.movies.use_cases.list_movies.list_movies_usecase import ListMoviesUseCase, ListMoviesUseCaseRequest, ListMoviesUseCaseResponse
from app.domain.models.movie.movie import Movie


def test_list_movies_returns_response() -> None:
    use_case: ListMoviesUseCase = ListMoviesUseCaseTestFactory().create()
    use_case.repository.create(
        Movie(
            id="movie-list-1",
            name="Movie 1",
            description="Description 1",
            author_id="author-1",
            genre_id="genre-1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    use_case.repository.create(
        Movie(
            id="movie-list-2",
            name="Movie 2",
            description="Description 2",
            author_id="author-2",
            genre_id="genre-2",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: ListMoviesUseCaseRequest = ListMoviesUseCaseRequest()
    response: ListMoviesUseCaseResponse = use_case.execute(request)
    assert len(response.movies) >= 2
