"""API routing configuration."""

from fastapi import APIRouter

from agent.orchestrator import FinanceAgent
from api.models import AnalyzeRequest, AnalyzeResponse

router = APIRouter(prefix="/api", tags=["finance-agent"])
finance_agent = FinanceAgent()


@router.get("/health")
def health() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    """Analyze a list of values for a symbol using the finance agent."""
    result = finance_agent.analyze(symbol=request.symbol, values=request.values)
    return AnalyzeResponse(**result)
