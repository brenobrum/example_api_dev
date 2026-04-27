from app.application.api.authors.use_cases.create_author.create_author_usecase import CreateAuthorUseCase
from app.infra.repositories.db.local.author import LocalAuthorRepository


class CreateAuthorUseCaseFactory:
    def create(self) -> CreateAuthorUseCase:
        return CreateAuthorUseCase(repository=LocalAuthorRepository())


class CreateAuthorUseCaseTestFactory:
    def create(self) -> CreateAuthorUseCase:
        return CreateAuthorUseCase(repository=LocalAuthorRepository())


create_author_use_case_factory: CreateAuthorUseCaseFactory = CreateAuthorUseCaseFactory()
