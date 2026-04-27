from datetime import datetime

from fastapi import HTTPException

from app.application.api.authors.use_cases.delete_author.delete_author_factory import DeleteAuthorUseCaseTestFactory
from app.application.api.authors.use_cases.delete_author.delete_author_usecase import DeleteAuthorUseCase, DeleteAuthorUseCaseRequest, DeleteAuthorUseCaseResponse
from app.application.api.authors.use_cases.get_author.get_author_usecase import GetAuthorUseCase, GetAuthorUseCaseRequest
from app.domain.models.author.author import Author


def test_delete_author_returns_response() -> None:
    use_case: DeleteAuthorUseCase = DeleteAuthorUseCaseTestFactory().create()
    use_case.repository.create(
        Author(
            id="author-delete-1",
            name="Author 1",
            description="Description 1",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
    )
    request: DeleteAuthorUseCaseRequest = DeleteAuthorUseCaseRequest(id="author-delete-1")
    response: DeleteAuthorUseCaseResponse = use_case.execute(request)
    assert response.message == "Author deleted"

    get_use_case: GetAuthorUseCase = GetAuthorUseCase(repository=use_case.repository)
    try:
        get_use_case.execute(GetAuthorUseCaseRequest(id="author-delete-1"))
        assert False, "Deleted author should not be found"
    except HTTPException as e:
        assert e.status_code == 404
