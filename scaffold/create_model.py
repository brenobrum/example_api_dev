from __future__ import annotations

import argparse
from pathlib import Path

from scaffold.utils import APP_DIR, ensure_init, singularize, snake_to_pascal, write_or_update


def create_model(module_name: str, entity_name: str | None = None) -> Path:
    module_snake: str = module_name.strip().lower()
    entity_snake: str = (entity_name or singularize(module_snake)).strip().lower()
    entity_pascal: str = snake_to_pascal(entity_snake)

    model_dir: Path = APP_DIR / "domain" / "models" / entity_snake
    ensure_init(model_dir)

    model_file: Path = model_dir / f"{entity_snake}.py"
    model_content: str = f"""from datetime import datetime
from pydantic import BaseModel


class {entity_pascal}(BaseModel):
    id: str
    name: str
    description: str
    created_at: datetime
    updated_at: datetime
"""
    write_or_update(model_file, model_content)

    init_content: str = f"""from app.domain.models.{entity_snake}.{entity_snake} import {entity_pascal}

__all__ = ["{entity_pascal}"]
"""
    write_or_update(model_dir / "__init__.py", init_content)
    return model_file


def main() -> None:
    parser = argparse.ArgumentParser(description="Create or update domain model scaffold.")
    parser.add_argument("--module", required=True, help="API module name, e.g. genres")
    parser.add_argument("--entity", help="Entity name in snake_case, e.g. genre")
    args = parser.parse_args()
    create_model(args.module, args.entity)


if __name__ == "__main__":
    main()
