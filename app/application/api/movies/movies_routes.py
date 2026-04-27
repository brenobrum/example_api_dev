from app.application.api.movies.use_cases.delete_movie.delete_movie_usecase import DeleteMovieUseCase, DeleteMovieUseCaseRequest


from app.application.api.movies.use_cases.update_movie.update_movie_usecase import UpdateMovieUseCase, UpdateMovieUseCaseRequest


from app.application.api.movies.use_cases.list_movies.list_movies_usecase import ListMoviesUseCase, ListMoviesUseCaseRequest


from app.application.api.movies.use_cases.get_movie.get_movie_usecase import GetMovieUseCase, GetMovieUseCaseRequest


from app.application.api.movies.use_cases.create_movie.create_movie_usecase import CreateMovieUseCase


from fastapi import APIRouter
from pydantic import BaseModel

from app.application.api.movies.use_cases.create_movie import CreateMovieUseCase, CreateMovieUseCaseFactory, CreateMovieUseCaseRequest, CreateMovieUseCaseResponse
from app.application.api.movies.use_cases.delete_movie import DeleteMovieUseCase, DeleteMovieUseCaseFactory, DeleteMovieUseCaseRequest, DeleteMovieUseCaseResponse
from app.application.api.movies.use_cases.get_movie import GetMovieUseCase, GetMovieUseCaseFactory, GetMovieUseCaseRequest, GetMovieUseCaseResponse
from app.application.api.movies.use_cases.list_movies import ListMoviesUseCase, ListMoviesUseCaseFactory, ListMoviesUseCaseRequest, ListMoviesUseCaseResponse
from app.application.api.movies.use_cases.update_movie import UpdateMovieUseCase, UpdateMovieUseCaseFactory, UpdateMovieUseCaseRequest, UpdateMovieUseCaseResponse

router: APIRouter = APIRouter(
    prefix="/api/movies",
    tags=["movies"],
)


class UpdateMovieBody(BaseModel):
    name: str
    description: str
    author_id: str
    genre_id: str


@router.post("")
def create_movie(request: CreateMovieUseCaseRequest) -> CreateMovieUseCaseResponse:
    use_case: CreateMovieUseCase = CreateMovieUseCaseFactory().create()
    return use_case.execute(request)

@router.get("/{id}")
def get_movie(id: str) -> GetMovieUseCaseResponse:
    use_case: GetMovieUseCase = GetMovieUseCaseFactory().create()
    request: GetMovieUseCaseRequest = GetMovieUseCaseRequest(id=id)
    return use_case.execute(request)

@router.get("")
def list_movies() -> ListMoviesUseCaseResponse:
    use_case: ListMoviesUseCase = ListMoviesUseCaseFactory().create()
    request: ListMoviesUseCaseRequest = ListMoviesUseCaseRequest()
    return use_case.execute(request)

@router.put("/{id}")
def update_movie(id: str, request: UpdateMovieBody) -> UpdateMovieUseCaseResponse:
    use_case: UpdateMovieUseCase = UpdateMovieUseCaseFactory().create()
    use_case_request: UpdateMovieUseCaseRequest = UpdateMovieUseCaseRequest(
        id=id,
        name=request.name,
        description=request.description,
        author_id=request.author_id,
        genre_id=request.genre_id,
    )
    return use_case.execute(use_case_request)

@router.delete("/{id}")
def delete_movie(id: str) -> DeleteMovieUseCaseResponse:
    use_case: DeleteMovieUseCase = DeleteMovieUseCaseFactory().create()
    request: DeleteMovieUseCaseRequest = DeleteMovieUseCaseRequest(id=id)
    return use_case.execute(request)
