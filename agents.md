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

