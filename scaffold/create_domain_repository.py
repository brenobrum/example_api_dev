from __future__ import annotations

import argparse
from pathlib import Path

from scaffold.utils import APP_DIR, ensure_init, singularize, snake_to_pascal, write_if_missing, write_or_update


BASE_REPOSITORY_CONTENT: str = """from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseDbRepository(ABC, Generic[T]):
    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def get(self, id: str) -> T:
        pass

    @abstractmethod
    def update(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self, id: str) -> None:
        pass

    @abstractmethod
    def list(self) -> list[T]:
        pass
"""


def create_domain_repository(module_name: str, entity_name: str | None = None) -> Path:
    module_snake: str = module_name.strip().lower()
    entity_snake: str = (entity_name or singularize(module_snake)).strip().lower()
    entity_pascal: str = snake_to_pascal(entity_snake)

    db_repo_dir: Path = APP_DIR / "domain" / "repositories" / "db"
    ensure_init(db_repo_dir)
    write_if_missing(db_repo_dir / "base_db_repository.py", BASE_REPOSITORY_CONTENT)
    write_or_update(
        db_repo_dir / "__init__.py",
        """from app.domain.repositories.db.base_db_repository import BaseDbRepository

__all__ = ["BaseDbRepository"]
""",
    )

    repo_dir: Path = APP_DIR / "domain" / "repositories" / entity_snake
    ensure_init(repo_dir)
    repo_file: Path = repo_dir / f"{entity_snake}_repository.py"
    repo_content: str = f"""from app.domain.models.{entity_snake}.{entity_snake} import {entity_pascal}
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class {entity_pascal}Repository(BaseDbRepository[{entity_pascal}]):
    pass
"""
    write_or_update(repo_file, repo_content)
    write_or_update(
        repo_dir / "__init__.py",
        f"""from app.domain.repositories.{entity_snake}.{entity_snake}_repository import {entity_pascal}Repository

__all__ = ["{entity_pascal}Repository"]
""",
    )
    return repo_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Create or update domain repository scaffold.")
    parser.add_argument("--module", required=True, help="API module name, e.g. genres")
    parser.add_argument("--entity", help="Entity name in snake_case, e.g. genre")
    args = parser.parse_args()
    create_domain_repository(args.module, args.entity)


if __name__ == "__main__":
    main()
