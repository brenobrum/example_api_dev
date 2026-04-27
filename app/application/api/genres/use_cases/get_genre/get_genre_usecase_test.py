from datetime import datetime

from app.application.api.genres.use_cases.get_genre.get_genre_factory import GetGenreUseCaseTestFactory
from app.application.api.genres.use_cases.get_genre.get_genre_usecase import GetGenreUseCaseRequest, GetGenreUseCaseResponse
from app.domain.models.genre.genre import Genre


def test_get_genre_returns_response() -> None:
    use_case = GetGenreUseCaseTestFactory().create()
    genre: Genre = Genre(
        id="genre-id-1",
        name="Genre 1",
        description="Description 1",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    use_case.repository.create(genre)

    request = GetGenreUseCaseRequest(id="genre-id-1")
    response: GetGenreUseCaseResponse = use_case.execute(request)
    assert response.genre.name == "Genre 1"
