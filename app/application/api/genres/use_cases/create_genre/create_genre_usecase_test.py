import pytest
from app.application.api.genres.use_cases.create_genre.create_genre_usecase import CreateGenreUseCase, CreateGenreUseCaseResponse
from app.application.api.genres.use_cases.create_genre.create_genre_factory import CreateGenreUseCaseTestFactory
from app.application.api.genres.use_cases.create_genre.create_genre_usecase import CreateGenreUseCaseRequest

def test_create_genre() -> None:
    create_genre_use_case: CreateGenreUseCase = CreateGenreUseCaseTestFactory().create()
    temp_genre: CreateGenreUseCaseRequest = CreateGenreUseCaseRequest(
        name="Genre 1",
        description="Description 1",
    )
    assert create_genre_use_case.execute(temp_genre) is not None

def test_create_genre_should_return_genre() -> None:
    create_genre_use_case: CreateGenreUseCase = CreateGenreUseCaseTestFactory().create()
    temp_genre: CreateGenreUseCaseRequest = CreateGenreUseCaseRequest(
        name="Genre 1",
        description="Description 1",
    )
    response: CreateGenreUseCaseResponse = create_genre_use_case.execute(temp_genre)
    assert response.genre is not None