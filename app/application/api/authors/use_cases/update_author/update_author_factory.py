from app.application.api.authors.use_cases.update_author.update_author_usecase import UpdateAuthorUseCase
from app.infra.repositories.db.local.author import LocalAuthorRepository


class UpdateAuthorUseCaseFactory:
    def create(self) -> UpdateAuthorUseCase:
        return UpdateAuthorUseCase(repository=LocalAuthorRepository())


class UpdateAuthorUseCaseTestFactory:
    def create(self) -> UpdateAuthorUseCase:
        return UpdateAuthorUseCase(repository=LocalAuthorRepository())


update_author_use_case_factory: UpdateAuthorUseCaseFactory = UpdateAuthorUseCaseFactory()
