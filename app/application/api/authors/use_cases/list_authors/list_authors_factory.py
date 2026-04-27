from app.application.api.authors.use_cases.list_authors.list_authors_usecase import ListAuthorsUseCase
from app.infra.repositories.db.local.author import LocalAuthorRepository


class ListAuthorsUseCaseFactory:
    def create(self) -> ListAuthorsUseCase:
        return ListAuthorsUseCase(repository=LocalAuthorRepository())


class ListAuthorsUseCaseTestFactory:
    def create(self) -> ListAuthorsUseCase:
        return ListAuthorsUseCase(repository=LocalAuthorRepository())


list_authors_use_case_factory: ListAuthorsUseCaseFactory = ListAuthorsUseCaseFactory()
