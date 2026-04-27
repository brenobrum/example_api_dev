# How to create API modules

This repo uses DDD as core principle

the file tree looks like this

app/
  application/
  domain/
  infra/

# Repositories

Repositories are split into two layers:

- `domain/repositories`: define repository interfaces (contracts) only. Keep this layer pure business logic: no SQL, ORM, HTTP clients, framework code, or environment access.
- `infra/repositories`: implement those interfaces with concrete persistence details (database queries, ORM models, external APIs, cache, etc).

Implementation rule for agents:
1. Create or update the repository contract in `domain/repositories` first.
2. Implement the contract in `infra/repositories`.
3. Application use cases must depend on the domain contract, never directly on infra classes.
4. Wire the concrete infra implementation through dependency injection/composition at the module boundary.

# Scaffold guide for agents

Use scaffold scripts before manually creating files. They exist to keep module structure consistent and reduce errors.

## Mandatory instruction

When creating anything new (module, use case, route, model, domain repository, or infra repository), agents must use the scaffold system first.

After scaffolding, agents should only update the generated files with implementation-specific details.

## Available scripts

- `scaffold/create_model.py`
- `scaffold/create_domain_repository.py`
- `scaffold/create_infra_repository.py`
- `scaffold/create_use_case.py`
- `scaffold/create_route.py`
- `scaffold/create_module.py`

## Golden rules

1. Prefer `create_module.py` when creating a brand new API module.
2. Prefer `create_use_case.py` when module already exists and you only need a new use case.
3. Keep names in `snake_case`.
4. Use plural module names for API folder (`genres`, `movies`) and singular entity names (`genre`, `movie`).
5. Keep IDs as `str` across model + contracts + repositories.

## Full module creation

Command:

`uv run python -m scaffold.create_module --module genres --entity genre --use-cases create_genre get_genre list_genres`

What it creates/updates:

- Domain model in `app/domain/models/<entity>/`
- Domain repository contract in `app/domain/repositories/<entity>/`
- Infra local repository in `app/infra/repositories/db/local/<entity>/`
- Use case folders/files in `app/application/api/<module>/use_cases/`
- Route file `app/application/api/<module>/<module>_routes.py`
- Route module exports in `app/application/api/<module>/__init__.py`

Default behavior:

- If `--use-cases` is omitted, scaffold creates `create_<entity>`.

## Add only one use case to existing module

Command:

`uv run python -m scaffold.create_use_case --module genres --use-case update_genre --entity genre`

What it creates/updates:

- Creates use case folder with:
  - `<use_case>_usecase.py`
  - `<use_case>_factory.py`
  - `<use_case>_usecase_test.py`
  - `__init__.py`
- Appends corresponding import + endpoint function to `app/application/api/<module>/<module>_routes.py`

## Low-level scripts (when to use)

- `create_model.py`: only add/update domain entity model.
- `create_domain_repository.py`: only add/update domain repository contract.
- `create_infra_repository.py`: only add/update concrete infra repository.
- `create_route.py`: only add/update route binding for an existing use case.

## Recommended workflow after scaffold

1. Run scaffold command.
2. Open generated files and replace placeholder behavior with real business rules.
3. Ensure route path, request/response DTOs, and naming match product needs.
4. Run tests: `uv run pytest -v`.
5. If route was added in a new module, ensure `main.py` includes that router import/binding.

## Important caveats

- `create_use_case.py` generates a standard request shape (`name`, `description`) by default; adjust fields as needed.
- Generated endpoint HTTP verb/path is inferred by use case prefix:
  - `create_` -> `POST`
  - `get_` -> `GET /{id}`
  - `list_` -> `GET`
  - `update_` -> `PUT /{id}`
  - `delete_` -> `DELETE /{id}`
- Re-running scripts updates files to scaffold defaults; if you already customized logic, review diffs before re-running.

