from datetime import datetime

from app.application.api.authors.use_cases.update_author.update_author_factory import UpdateAuthorUseCaseTestFactory
from app.application.api.authors.use_cases.update_author.update_author_usecase import UpdateAuthorUseCase, UpdateAuthorUseCaseRequest, UpdateAuthorUseCaseResponse
from app.domain.models.author.author import Author


def test_update_author_returns_response() -> None:
    use_case: UpdateAuthorUseCase = UpdateAuthorUseCaseTestFactory().create()
    use_case.repository.create(
        Author(
            id="author-update-1",
            name="Old Author",
            description="Old Description",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: UpdateAuthorUseCaseRequest = UpdateAuthorUseCaseRequest(id="author-update-1", name="Author 1", description="Description 1")
    response: UpdateAuthorUseCaseResponse = use_case.execute(request)
    assert response.author.name == "Author 1"
