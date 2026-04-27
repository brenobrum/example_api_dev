from datetime import datetime

from app.application.api.genres.use_cases.update_genre.update_genre_factory import UpdateGenreUseCaseTestFactory
from app.application.api.genres.use_cases.update_genre.update_genre_usecase import UpdateGenreUseCaseRequest, UpdateGenreUseCaseResponse
from app.domain.models.genre.genre import Genre


def test_update_genre_returns_response() -> None:
    use_case = UpdateGenreUseCaseTestFactory().create()
    use_case.repository.create(
        Genre(
            id="genre-update-1",
            name="Old Genre",
            description="Old Description",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request = UpdateGenreUseCaseRequest(id="genre-update-1", name="Genre 1", description="Description 1")
    response: UpdateGenreUseCaseResponse = use_case.execute(request)
    assert response.genre.name == "Genre 1"
