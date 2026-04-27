from app.application.api.authors.use_cases.get_author.get_author_usecase import GetAuthorUseCase, GetAuthorUseCaseRequest


from fastapi import APIRouter
from pydantic import BaseModel

from app.application.api.authors.use_cases.create_author import CreateAuthorUseCase, CreateAuthorUseCaseFactory, CreateAuthorUseCaseRequest, CreateAuthorUseCaseResponse
from app.application.api.authors.use_cases.delete_author import DeleteAuthorUseCase, DeleteAuthorUseCaseFactory, DeleteAuthorUseCaseRequest, DeleteAuthorUseCaseResponse
from app.application.api.authors.use_cases.get_author import GetAuthorUseCase, GetAuthorUseCaseFactory, GetAuthorUseCaseRequest, GetAuthorUseCaseResponse
from app.application.api.authors.use_cases.list_authors import ListAuthorsUseCase, ListAuthorsUseCaseFactory, ListAuthorsUseCaseRequest, ListAuthorsUseCaseResponse
from app.application.api.authors.use_cases.update_author import UpdateAuthorUseCase, UpdateAuthorUseCaseFactory, UpdateAuthorUseCaseRequest, UpdateAuthorUseCaseResponse

router: APIRouter = APIRouter(
    prefix="/api/authors",
    tags=["authors"],
)


class UpdateAuthorBody(BaseModel):
    name: str
    description: str


@router.post("")
def create_author(request: CreateAuthorUseCaseRequest) -> CreateAuthorUseCaseResponse:
    use_case: CreateAuthorUseCase = CreateAuthorUseCaseFactory().create()
    return use_case.execute(request)

@router.get("/{id}")
def get_author(id: str) -> GetAuthorUseCaseResponse:
    use_case: GetAuthorUseCase = GetAuthorUseCaseFactory().create()
    request: GetAuthorUseCaseRequest = GetAuthorUseCaseRequest(id=id)
    return use_case.execute(request)

@router.get("")
def list_authors() -> ListAuthorsUseCaseResponse:
    use_case: ListAuthorsUseCase = ListAuthorsUseCaseFactory().create()
    request: ListAuthorsUseCaseRequest = ListAuthorsUseCaseRequest()
    return use_case.execute(request)

@router.put("/{id}")
def update_author(id: str, request: UpdateAuthorBody) -> UpdateAuthorUseCaseResponse:
    use_case: UpdateAuthorUseCase = UpdateAuthorUseCaseFactory().create()
    use_case_request: UpdateAuthorUseCaseRequest = UpdateAuthorUseCaseRequest(
        id=id,
        name=request.name,
        description=request.description,
    )
    return use_case.execute(use_case_request)

@router.delete("/{id}")
def delete_author(id: str) -> DeleteAuthorUseCaseResponse:
    use_case: DeleteAuthorUseCase = DeleteAuthorUseCaseFactory().create()
    request: DeleteAuthorUseCaseRequest = DeleteAuthorUseCaseRequest(id=id)
    return use_case.execute(request)
