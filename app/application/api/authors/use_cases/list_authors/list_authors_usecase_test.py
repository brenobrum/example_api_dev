from datetime import datetime

from app.application.api.authors.use_cases.list_authors.list_authors_factory import ListAuthorsUseCaseTestFactory
from app.application.api.authors.use_cases.list_authors.list_authors_usecase import ListAuthorsUseCase, ListAuthorsUseCaseRequest, ListAuthorsUseCaseResponse
from app.domain.models.author.author import Author


def test_list_authors_returns_response() -> None:
    use_case: ListAuthorsUseCase = ListAuthorsUseCaseTestFactory().create()
    use_case.repository.create(
        Author(
            id="author-list-1",
            name="Author 1",
            description="Description 1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    use_case.repository.create(
        Author(
            id="author-list-2",
            name="Author 2",
            description="Description 2",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: ListAuthorsUseCaseRequest = ListAuthorsUseCaseRequest()
    response: ListAuthorsUseCaseResponse = use_case.execute(request)
    assert len(response.authors) >= 2
