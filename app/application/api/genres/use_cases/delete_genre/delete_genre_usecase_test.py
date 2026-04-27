from datetime import datetime

from fastapi import HTTPException

from app.application.api.genres.use_cases.delete_genre.delete_genre_factory import DeleteGenreUseCaseTestFactory
from app.application.api.genres.use_cases.delete_genre.delete_genre_usecase import DeleteGenreUseCaseRequest, DeleteGenreUseCaseResponse
from app.application.api.genres.use_cases.get_genre.get_genre_usecase import GetGenreUseCase, GetGenreUseCaseRequest
from app.domain.models.genre.genre import Genre


def test_delete_genre_returns_response() -> None:
    use_case = DeleteGenreUseCaseTestFactory().create()
    use_case.repository.create(
        Genre(
            id="genre-delete-1",
            name="Genre 1",
            description="Description 1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request = DeleteGenreUseCaseRequest(id="genre-delete-1")
    response: DeleteGenreUseCaseResponse = use_case.execute(request)
    assert response.message == "Genre deleted"

    get_use_case = GetGenreUseCase(repository=use_case.repository)
    try:
        get_use_case.execute(GetGenreUseCaseRequest(id="genre-delete-1"))
        assert False, "Deleted genre should not be found"
    except HTTPException as e:
        assert e.status_code == 404
