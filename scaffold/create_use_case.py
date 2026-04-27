from __future__ import annotations

import argparse
from pathlib import Path

from scaffold.create_route import create_route
from scaffold.utils import APP_DIR, singularize, snake_to_pascal, write_or_update


def create_use_case(module_name: str, use_case_name: str, entity_name: str | None = None) -> Path:
    module_snake: str = module_name.strip().lower()
    entity_snake: str = (entity_name or singularize(module_snake)).strip().lower()
    entity_pascal: str = snake_to_pascal(entity_snake)
    use_case_snake: str = use_case_name.strip().lower()
    use_case_pascal: str = snake_to_pascal(use_case_snake)

    use_case_dir: Path = APP_DIR / "application" / "api" / module_snake / "use_cases" / use_case_snake
    use_case_dir.mkdir(parents=True, exist_ok=True)

    use_case_file: Path = use_case_dir / f"{use_case_snake}_usecase.py"
    use_case_content: str = f"""from datetime import datetime
import uuid

from fastapi import HTTPException
from pydantic import BaseModel

from app.domain.models.{entity_snake}.{entity_snake} import {entity_pascal}
from app.domain.repositories.db.base_db_repository import BaseDbRepository


class {use_case_pascal}UseCaseRequest(BaseModel):
    name: str
    description: str


class {use_case_pascal}UseCaseResponse(BaseModel):
    {entity_snake}: {entity_pascal}


class {use_case_pascal}UseCase:
    def __init__(self, repository: BaseDbRepository[{entity_pascal}]) -> None:
        self.repository = repository

    def execute(self, request: {use_case_pascal}UseCaseRequest) -> {use_case_pascal}UseCaseResponse:
        try:
            temp_{entity_snake}: {entity_pascal} = {entity_pascal}(
                id=str(uuid.uuid4()),
                name=request.name,
                description=request.description,
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            saved_{entity_snake}: {entity_pascal} = self.repository.create(temp_{entity_snake})
            return {use_case_pascal}UseCaseResponse({entity_snake}=saved_{entity_snake})
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
"""
    write_or_update(use_case_file, use_case_content)

    factory_file: Path = use_case_dir / f"{use_case_snake}_factory.py"
    factory_content: str = f"""from app.application.api.{module_snake}.use_cases.{use_case_snake}.{use_case_snake}_usecase import {use_case_pascal}UseCase
from app.infra.repositories.db.local.{entity_snake} import Local{entity_pascal}Repository


class {use_case_pascal}UseCaseFactory:
    def create(self) -> {use_case_pascal}UseCase:
        return {use_case_pascal}UseCase(repository=Local{entity_pascal}Repository())


class {use_case_pascal}UseCaseTestFactory:
    def create(self) -> {use_case_pascal}UseCase:
        return {use_case_pascal}UseCase(repository=Local{entity_pascal}Repository())


{use_case_snake}_use_case_factory: {use_case_pascal}UseCaseFactory = {use_case_pascal}UseCaseFactory()
"""
    write_or_update(factory_file, factory_content)

    test_file: Path = use_case_dir / f"{use_case_snake}_usecase_test.py"
    test_content: str = f"""from app.application.api.{module_snake}.use_cases.{use_case_snake}.{use_case_snake}_factory import {use_case_pascal}UseCaseTestFactory
from app.application.api.{module_snake}.use_cases.{use_case_snake}.{use_case_snake}_usecase import {use_case_pascal}UseCaseRequest, {use_case_pascal}UseCaseResponse


def test_{use_case_snake}_returns_response() -> None:
    use_case = {use_case_pascal}UseCaseTestFactory().create()
    request = {use_case_pascal}UseCaseRequest(name="{entity_pascal} 1", description="Description 1")
    response: {use_case_pascal}UseCaseResponse = use_case.execute(request)
    assert response.{entity_snake}.name == "{entity_pascal} 1"
"""
    write_or_update(test_file, test_content)

    init_file: Path = use_case_dir / "__init__.py"
    init_content: str = f"""from app.application.api.{module_snake}.use_cases.{use_case_snake}.{use_case_snake}_factory import {use_case_pascal}UseCaseFactory
from app.application.api.{module_snake}.use_cases.{use_case_snake}.{use_case_snake}_usecase import {use_case_pascal}UseCase
from app.application.api.{module_snake}.use_cases.{use_case_snake}.{use_case_snake}_usecase import {use_case_pascal}UseCaseRequest, {use_case_pascal}UseCaseResponse

__all__ = ["{use_case_pascal}UseCaseFactory", "{use_case_pascal}UseCase", "{use_case_pascal}UseCaseRequest", "{use_case_pascal}UseCaseResponse"]
"""
    write_or_update(init_file, init_content)

    create_route(module_snake, use_case_snake, entity_snake)
    return use_case_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Create or update use case scaffold.")
    parser.add_argument("--module", required=True, help="API module name, e.g. genres")
    parser.add_argument("--use-case", required=True, help="Use case name in snake_case, e.g. create_genre")
    parser.add_argument("--entity", help="Entity name in snake_case, e.g. genre")
    args = parser.parse_args()
    create_use_case(args.module, args.use_case, args.entity)


if __name__ == "__main__":
    main()
