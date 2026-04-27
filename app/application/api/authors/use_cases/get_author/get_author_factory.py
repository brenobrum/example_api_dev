from app.application.api.authors.use_cases.get_author.get_author_usecase import GetAuthorUseCase
from app.infra.repositories.db.local.author import LocalAuthorRepository


class GetAuthorUseCaseFactory:
    def create(self) -> GetAuthorUseCase:
        return GetAuthorUseCase(repository=LocalAuthorRepository())


class GetAuthorUseCaseTestFactory:
    def create(self) -> GetAuthorUseCase:
        return GetAuthorUseCase(repository=LocalAuthorRepository())


get_author_use_case_factory: GetAuthorUseCaseFactory = GetAuthorUseCaseFactory()
