# Modules Connections (`app/`)

This document explains how modules in `app/` are organized, how they connect, and what to create when adding a new feature.

## 1) High-level architecture

The project follows a DDD-style layering:

- `app/application`: API entrypoints, request/response DTOs, use cases, and factories.
- `app/domain`: business models and repository contracts (interfaces/abstractions).
- `app/infra`: concrete implementations for external concerns (local DB repo, env/config).

Dependency direction (must stay one-way):

- `application` -> `domain`
- `application` -> `infra` only in factories/composition
- `infra` -> `domain`
- `domain` must not depend on `application` or `infra`

## 2) File-by-file connections

### Application layer

- `app/application/api/genres/genres_routes.py`
  - Defines HTTP route (`POST /api/genres`).
  - Depends on use case exports from `create_genre/__init__.py`.
  - Receives `CreateGenreUseCaseRequest`, returns `CreateGenreUseCaseResponse`.
  - Calls factory to build use case with concrete dependencies.

- `app/application/api/genres/use_cases/create_genre/create_genre_usecase.py`
  - Defines:
    - `CreateGenreUseCaseRequest` (input DTO)
    - `CreateGenreUseCaseResponse` (output DTO)
    - `CreateGenreUseCase` (business flow orchestration)
  - Depends on:
    - `Genre` domain model
    - `BaseDbRepository[Genre]` domain repository contract
  - Creates a `Genre` and persists it through repository abstraction.

- `app/application/api/genres/use_cases/create_genre/create_genre_factory.py`
  - Composition root for this use case.
  - Chooses concrete infra implementation (`LocalGenreRepository`) and injects it into use case.
  - This is where infra is wired to application.

- `app/application/api/genres/use_cases/create_genre/create_genre_usecase_test.py`
  - Tests use case behavior through `CreateGenreUseCaseTestFactory`.
  - Verifies the use case returns a response and includes a genre.

- `app/application/api/genres/use_cases/create_genre/__init__.py`
  - Re-exports use case/factory/DTO symbols for cleaner imports.

- `app/application/api/genres/__init__.py`
  - Re-exports `genres_routes` router.

### Domain layer

- `app/domain/models/genre/genre.py`
  - Core domain entity model (`Genre`) with `id`, `name`, `description`, timestamps.

- `app/domain/repositories/db/base_db_repository.py`
  - Generic repository contract (create/get/update/delete/list).
  - Defines behavior expected by use cases.

- `app/domain/repositories/genre/genre_repository.py`
  - Genre-specific repository contract, based on `BaseDbRepository`.
  - Used as domain-level specialization point.

- `app/domain/*/__init__.py`
  - Re-export domain symbols to keep import paths stable/clean.

### Infra layer

- `app/infra/repositories/db/local/local_base_db_repository.py`
  - In-memory concrete repository implementation.
  - Implements domain contract methods using internal dict storage.

- `app/infra/repositories/db/local/genre/genre_repository.py`
  - Concrete genre repository (`LocalGenreRepository`).
  - Combines domain `GenreRepository` contract + local base implementation.

- `app/infra/repositories/db/local/**/*.py` `__init__.py`
  - Re-export concrete classes for clean factory imports.

- `app/infra/config/env.py`
  - Environment settings holder (`Env`).

## 3) Runtime flow (request -> persistence -> response)

1. HTTP request hits `POST /api/genres` in `genres_routes.py`.
2. Route validates body into `CreateGenreUseCaseRequest`.
3. Route asks `CreateGenreUseCaseFactory` to build use case.
4. Factory injects `LocalGenreRepository` (infra) into `CreateGenreUseCase`.
5. Use case creates `Genre` domain object.
6. Use case persists via `BaseDbRepository[Genre]` abstraction.
7. Concrete infra repository stores entity.
8. Use case returns `CreateGenreUseCaseResponse`.
9. FastAPI serializes and sends response.

## 4) Change impact guide

- Change `Genre` fields (`domain/models/genre.py`)
  - Likely update request/response DTOs, use case mapping, tests, and route contracts.

- Change repository contract (`domain/repositories/db/base_db_repository.py`)
  - Must update all concrete implementations in infra and any use cases relying on signatures.

- Change infra implementation (`infra/repositories/...`)
  - Usually no route/use-case signature change if contract remains the same.
  - Factory may change if class names/paths change.

- Change route signature (`genres_routes.py`)
  - Must align use case request/response DTOs and API tests/clients.

- Change factory wiring (`create_genre_factory.py`)
  - Affects runtime dependency selection (local DB, SQL DB, mock, etc).

## 5) How to create files for a new module (recommended pattern)

For a new module (example: `movies`):

1. Domain first
   - Create entity model in `app/domain/models/<module>/<entity>.py`.
   - Create/update repository contract in `app/domain/repositories/<module>/`.
2. Infra implementation
   - Add concrete repo in `app/infra/repositories/db/local/<module>/`.
   - Implement all methods required by domain contract.
3. Application use case
   - Create `request` and `response` DTOs as Pydantic models.
   - Implement use case depending on domain contract, not concrete infra class.
4. Factory
   - Inject concrete infra implementation in factory.
5. Route
   - Expose endpoint in `app/application/api/<module>/<module>_routes.py`.
   - Route only coordinates HTTP concerns and use case invocation.
6. Exports
   - Update `__init__.py` files for stable import surface.
7. Tests
   - Add use case tests in the module use-case folder.

## 6) Best practices

- Keep dependency rule strict: domain independent, infra behind abstractions.
- Keep route thin: validation + call use case + return response.
- Keep use case focused on business flow, not framework/infrastructure details.
- Use factories as composition root for dependency injection.
- Keep DTOs explicit (`Request`/`Response`) to avoid leaking internals.
- Prefer symbol re-exports in `__init__.py` for clean imports and easier refactors.
- If repository key type is `str`, enforce it consistently in model + contracts + infra.
- Update tests whenever contracts or DTOs change.
