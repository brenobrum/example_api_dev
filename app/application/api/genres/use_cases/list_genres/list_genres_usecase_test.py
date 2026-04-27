from datetime import datetime

from app.application.api.genres.use_cases.list_genres.list_genres_factory import ListGenresUseCaseTestFactory
from app.application.api.genres.use_cases.list_genres.list_genres_usecase import ListGenresUseCaseRequest, ListGenresUseCaseResponse
from app.domain.models.genre.genre import Genre


def test_list_genres_returns_response() -> None:
    use_case = ListGenresUseCaseTestFactory().create()
    use_case.repository.create(
        Genre(
            id="genre-list-1",
            name="Genre 1",
            description="Description 1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    use_case.repository.create(
        Genre(
            id="genre-list-2",
            name="Genre 2",
            description="Description 2",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )

    request = ListGenresUseCaseRequest()
    response: ListGenresUseCaseResponse = use_case.execute(request)
    assert len(response.genres) >= 2
