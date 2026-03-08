# Architecture Overview

## Components

- **app/**: FastAPI application entrypoint and ASGI configuration.
- **api/**: HTTP routes and request/response models.
- **agent/**: Orchestration logic between retrieval and finance analysis.
- **rag/**: Retrieval helper for local domain context.
- **finance/**: Deterministic financial calculations.
- **database/**: Local database utility layer.
- **tests/**: Unit and API tests.

## Request flow

1. Client sends request to `/api/analyze`.
2. Router validates input using Pydantic.
3. `FinanceAgent` computes metrics and augments with retrieval context.
4. API returns normalized response payload.
