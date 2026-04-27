from fastapi import APIRouter
from pydantic import BaseModel

from app.application.api.genres.use_cases.create_genre import CreateGenreUseCase, CreateGenreUseCaseFactory, CreateGenreUseCaseRequest, CreateGenreUseCaseResponse
from app.application.api.genres.use_cases.delete_genre import DeleteGenreUseCase, DeleteGenreUseCaseFactory, DeleteGenreUseCaseRequest, DeleteGenreUseCaseResponse
from app.application.api.genres.use_cases.get_genre import GetGenreUseCase, GetGenreUseCaseFactory, GetGenreUseCaseRequest, GetGenreUseCaseResponse
from app.application.api.genres.use_cases.list_genres import ListGenresUseCase, ListGenresUseCaseFactory, ListGenresUseCaseRequest, ListGenresUseCaseResponse
from app.application.api.genres.use_cases.update_genre import UpdateGenreUseCase, UpdateGenreUseCaseFactory, UpdateGenreUseCaseRequest, UpdateGenreUseCaseResponse


router: APIRouter = APIRouter(
    prefix="/api/genres",
    tags=["genres"]
)


class UpdateGenreBody(BaseModel):
    name: str
    description: str


@router.post("")
def create_genre(request: CreateGenreUseCaseRequest) -> CreateGenreUseCaseResponse:
    """
    Create a new genre
    """
    create_genre_use_case: CreateGenreUseCase = CreateGenreUseCaseFactory().create()
    return create_genre_use_case.execute(request)

@router.get("/{id}")
def get_genre(id: str) -> GetGenreUseCaseResponse:
    use_case: GetGenreUseCase = GetGenreUseCaseFactory().create()
    request: GetGenreUseCaseRequest = GetGenreUseCaseRequest(id=id)
    return use_case.execute(request)

@router.get("")
def list_genres() -> ListGenresUseCaseResponse:
    use_case: ListGenresUseCase = ListGenresUseCaseFactory().create()
    request: ListGenresUseCaseRequest = ListGenresUseCaseRequest()
    return use_case.execute(request)

@router.put("/{id}")
def update_genre(id: str, request: UpdateGenreBody) -> UpdateGenreUseCaseResponse:
    use_case: UpdateGenreUseCase = UpdateGenreUseCaseFactory().create()
    use_case_request: UpdateGenreUseCaseRequest = UpdateGenreUseCaseRequest(
        id=id,
        name=request.name,
        description=request.description,
    )
    return use_case.execute(use_case_request)

@router.delete("/{id}")
def delete_genre(id: str) -> DeleteGenreUseCaseResponse:
    use_case: DeleteGenreUseCase = DeleteGenreUseCaseFactory().create()
    request: DeleteGenreUseCaseRequest = DeleteGenreUseCaseRequest(id=id)
    return use_case.execute(request)
