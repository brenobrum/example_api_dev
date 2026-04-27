from app.application.api.authors.use_cases.create_author.create_author_factory import CreateAuthorUseCaseTestFactory
from app.application.api.authors.use_cases.create_author.create_author_usecase import CreateAuthorUseCaseRequest, CreateAuthorUseCaseResponse


def test_create_author_returns_response() -> None:
    use_case = CreateAuthorUseCaseTestFactory().create()
    request = CreateAuthorUseCaseRequest(name="Author 1", description="Description 1")
    response: CreateAuthorUseCaseResponse = use_case.execute(request)
    assert response.author.name == "Author 1"
