from fastapi import APIRouter

from app.application.api.genres.use_cases.create_genre import CreateGenreUseCase, CreateGenreUseCaseFactory, CreateGenreUseCaseRequest, CreateGenreUseCaseResponse


router: APIRouter = APIRouter(
    prefix="/api/genres",
    tags=["genres"]
)

@router.post("")
def create_genre(request: CreateGenreUseCaseRequest) -> CreateGenreUseCaseResponse:
    """
    Create a new genre
    """
    create_genre_use_case: CreateGenreUseCase = CreateGenreUseCaseFactory().create()
    return create_genre_use_case.execute(request)