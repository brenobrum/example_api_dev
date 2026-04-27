from __future__ import annotations

import argparse
from pathlib import Path

from scaffold.utils import APP_DIR, append_if_missing, snake_to_pascal


def _http_meta(use_case_name: str) -> tuple[str, str]:
    if use_case_name.startswith("create_"):
        return "post", ""
    if use_case_name.startswith("get_"):
        return "get", "/{id}"
    if use_case_name.startswith("list_"):
        return "get", ""
    if use_case_name.startswith("update_"):
        return "put", "/{id}"
    if use_case_name.startswith("delete_"):
        return "delete", "/{id}"
    return "post", f"/{use_case_name}"


def create_route(module_name: str, use_case_name: str, entity_name: str) -> Path:
    module_snake: str = module_name.strip().lower()
    entity_snake: str = entity_name.strip().lower()
    route_file: Path = APP_DIR / "application" / "api" / module_snake / f"{module_snake}_routes.py"
    route_file.parent.mkdir(parents=True, exist_ok=True)
    module_init: Path = route_file.parent / "__init__.py"

    use_case_pascal: str = snake_to_pascal(use_case_name)
    response_name: str = f"{use_case_pascal}UseCaseResponse"
    request_name: str = f"{use_case_pascal}UseCaseRequest"
    method, suffix = _http_meta(use_case_name)

    if not route_file.exists():
        route_file.write_text(
            f"""from fastapi import APIRouter

router: APIRouter = APIRouter(
    prefix="/api/{module_snake}",
    tags=["{module_snake}"],
)
"""
        )

    import_block: str = (
        f"from app.application.api.{module_snake}.use_cases.{use_case_name} import "
        f"{use_case_pascal}UseCase, {use_case_pascal}UseCaseFactory, {request_name}, {response_name}"
    )
    append_if_missing(route_file, import_block)

    endpoint_block: str = f"""
@router.{method}("{suffix}")
def {use_case_name}(request: {request_name}) -> {response_name}:
    use_case: {use_case_pascal}UseCase = {use_case_pascal}UseCaseFactory().create()
    return use_case.execute(request)
"""
    append_if_missing(route_file, endpoint_block)

    module_init.write_text(
        f"""from app.application.api.{module_snake}.{module_snake}_routes import router as {module_snake}_routes

__all__ = ["{module_snake}_routes"]
"""
    )
    return route_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Create or update API route scaffold.")
    parser.add_argument("--module", required=True, help="API module name, e.g. genres")
    parser.add_argument("--use-case", required=True, help="Use case name in snake_case, e.g. create_genre")
    parser.add_argument("--entity", required=True, help="Entity name in snake_case, e.g. genre")
    args = parser.parse_args()
    create_route(args.module, args.use_case, args.entity)


if __name__ == "__main__":
    main()
