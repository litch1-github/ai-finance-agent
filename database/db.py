"""SQLite connection helper."""

from __future__ import annotations

import os
import sqlite3
from contextlib import contextmanager
from typing import Iterator


DEFAULT_DB_PATH = "ai_finance_agent.db"


def get_db_path() -> str:
    """Read DB path from env or default local file."""
    raw_url = os.getenv("DATABASE_URL", f"sqlite:///./{DEFAULT_DB_PATH}")
    if raw_url.startswith("sqlite:///"):
        return raw_url.replace("sqlite:///", "")
    return DEFAULT_DB_PATH


@contextmanager
def get_connection() -> Iterator[sqlite3.Connection]:
    """Yield a SQLite connection for local persistence operations."""
    connection = sqlite3.connect(get_db_path())
    try:
        yield connection
    finally:
        connection.close()
