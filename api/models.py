"""Pydantic models for API contracts."""

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    """Input payload for finance analysis."""

    symbol: str = Field(..., description="Asset symbol, e.g. AAPL or BTC")
    values: list[float] = Field(..., min_length=2, description="Time-series values")


class AnalyzeResponse(BaseModel):
    """Output payload for finance analysis."""

    symbol: str
    average: float
    trend: str
    agent_summary: str
