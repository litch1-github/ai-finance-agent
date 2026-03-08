# AI Finance Agent

A local-first Python project scaffold for an **AI Finance Agent**.

## Features

- FastAPI service layer for health checks and future endpoints.
- Agent orchestration layer that coordinates retrieval and finance analysis.
- Retrieval Augmented Generation (RAG) placeholder for document context.
- Finance utilities for KPI summaries and simple trend analysis.
- SQLite-backed persistence helper for local deployments.
- Pytest test suite for basic integration and unit coverage.

## Project layout

```text
ai-finance-agent/
├── app/
├── api/
├── agent/
├── rag/
├── finance/
├── database/
├── tests/
├── docs/
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Run tests:

```bash
pytest -q
```

## Container usage

```bash
docker compose up --build
```

The API will be available on `http://localhost:8000`.
