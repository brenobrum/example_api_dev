from __future__ import annotations

import argparse
from pathlib import Path

from scaffold.utils import APP_DIR, ensure_init, singularize, snake_to_pascal, write_if_missing, write_or_update


LOCAL_BASE_REPOSITORY_CONTENT: str = """from typing import Protocol, TypeVar

from app.domain.repositories.db.base_db_repository import BaseDbRepository


class HasId(Protocol):
    id: str


T = TypeVar("T", bound=HasId)


class LocalBaseDbRepository(BaseDbRepository[T]):
    def __init__(self) -> None:
        self.db: dict[str, T] = {}

    def create(self, entity: T) -> T:
        self.db[entity.id] = entity
        return entity

    def get(self, id: str) -> T:
        return self.db[id]

    def update(self, entity: T) -> T:
        self.db[entity.id] = entity
        return entity

    def delete(self, id: str) -> None:
        del self.db[id]

    def list(self) -> list[T]:
        return list(self.db.values())
"""


def create_infra_repository(module_name: str, entity_name: str | None = None) -> Path:
    module_snake: str = module_name.strip().lower()
    entity_snake: str = (entity_name or singularize(module_snake)).strip().lower()
    entity_pascal: str = snake_to_pascal(entity_snake)

    local_dir: Path = APP_DIR / "infra" / "repositories" / "db" / "local"
    ensure_init(local_dir)
    write_if_missing(local_dir / "local_base_db_repository.py", LOCAL_BASE_REPOSITORY_CONTENT)
    write_or_update(
        local_dir / "__init__.py",
        """from app.infra.repositories.db.local.local_base_db_repository import LocalBaseDbRepository

__all__ = ["LocalBaseDbRepository"]
""",
    )

    entity_local_dir: Path = local_dir / entity_snake
    ensure_init(entity_local_dir)
    repo_file: Path = entity_local_dir / f"{entity_snake}_repository.py"
    repo_content: str = f"""from app.domain.models.{entity_snake}.{entity_snake} import {entity_pascal}
from app.domain.repositories.{entity_snake}.{entity_snake}_repository import {entity_pascal}Repository
from app.infra.repositories.db.local.local_base_db_repository import LocalBaseDbRepository


class Local{entity_pascal}Repository({entity_pascal}Repository, LocalBaseDbRepository[{entity_pascal}]):
    def create(self, entity: {entity_pascal}) -> {entity_pascal}:
        return super().create(entity)

    def get(self, id: str) -> {entity_pascal}:
        return super().get(id)

    def update(self, entity: {entity_pascal}) -> {entity_pascal}:
        return super().update(entity)

    def delete(self, id: str) -> None:
        return super().delete(id)

    def list(self) -> list[{entity_pascal}]:
        return super().list()
"""
    write_or_update(repo_file, repo_content)
    write_or_update(
        entity_local_dir / "__init__.py",
        f"""from app.infra.repositories.db.local.{entity_snake}.{entity_snake}_repository import Local{entity_pascal}Repository

__all__ = ["Local{entity_pascal}Repository"]
""",
    )
    return repo_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Create or update infra repository scaffold.")
    parser.add_argument("--module", required=True, help="API module name, e.g. genres")
    parser.add_argument("--entity", help="Entity name in snake_case, e.g. genre")
    args = parser.parse_args()
    create_infra_repository(args.module, args.entity)


if __name__ == "__main__":
    main()
