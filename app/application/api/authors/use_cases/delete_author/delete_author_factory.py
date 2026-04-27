from app.application.api.authors.use_cases.delete_author.delete_author_usecase import DeleteAuthorUseCase
from app.infra.repositories.db.local.author import LocalAuthorRepository


class DeleteAuthorUseCaseFactory:
    def create(self) -> DeleteAuthorUseCase:
        return DeleteAuthorUseCase(repository=LocalAuthorRepository())


class DeleteAuthorUseCaseTestFactory:
    def create(self) -> DeleteAuthorUseCase:
        return DeleteAuthorUseCase(repository=LocalAuthorRepository())


delete_author_use_case_factory: DeleteAuthorUseCaseFactory = DeleteAuthorUseCaseFactory()
