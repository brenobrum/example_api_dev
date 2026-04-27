from datetime import datetime

from app.application.api.authors.use_cases.get_author.get_author_factory import GetAuthorUseCaseTestFactory
from app.application.api.authors.use_cases.get_author.get_author_usecase import GetAuthorUseCase, GetAuthorUseCaseRequest, GetAuthorUseCaseResponse
from app.domain.models.author.author import Author


def test_get_author_returns_response() -> None:
    use_case: GetAuthorUseCase = GetAuthorUseCaseTestFactory().create()
    use_case.repository.create(
        Author(
            id="author-id-1",
            name="Author 1",
            description="Description 1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: GetAuthorUseCaseRequest = GetAuthorUseCaseRequest(id="author-id-1")
    response: GetAuthorUseCaseResponse = use_case.execute(request)
    assert response.author.name == "Author 1"
