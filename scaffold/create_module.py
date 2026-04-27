from __future__ import annotations

import argparse

from scaffold.create_domain_repository import create_domain_repository
from scaffold.create_infra_repository import create_infra_repository
from scaffold.create_model import create_model
from scaffold.create_use_case import create_use_case
from scaffold.utils import singularize


def create_module(module_name: str, entity_name: str | None = None, use_cases: list[str] | None = None) -> None:
    module_snake: str = module_name.strip().lower()
    entity_snake: str = (entity_name or singularize(module_snake)).strip().lower()
    selected_use_cases: list[str] = use_cases or [f"create_{entity_snake}"]

    create_model(module_snake, entity_snake)
    create_domain_repository(module_snake, entity_snake)
    create_infra_repository(module_snake, entity_snake)

    for use_case in selected_use_cases:
        create_use_case(module_snake, use_case, entity_snake)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a full API module.")
    parser.add_argument("--module", required=True, help="API module name, e.g. genres")
    parser.add_argument("--entity", help="Entity name in snake_case, e.g. genre")
    parser.add_argument(
        "--use-cases",
        nargs="*",
        help="Use case names in snake_case, e.g. create_genre get_genre list_genres",
    )
    args = parser.parse_args()
    create_module(args.module, args.entity, args.use_cases)


if __name__ == "__main__":
    main()
