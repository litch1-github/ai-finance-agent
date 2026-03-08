"""Coordinator for finance analysis and retrieval context."""

from finance.metrics import summarize_series
from rag.retriever import LocalRetriever


class FinanceAgent:
    """Simple orchestration agent for finance analytics."""

    def __init__(self) -> None:
        self.retriever = LocalRetriever()

    def analyze(self, symbol: str, values: list[float]) -> dict[str, float | str]:
        """Produce analytical output plus lightweight narrative context."""
        metrics = summarize_series(values)
        context = self.retriever.get_context(symbol)

        return {
            "symbol": symbol.upper(),
            "average": metrics["average"],
            "trend": metrics["trend"],
            "agent_summary": f"{symbol.upper()} trend is {metrics['trend']}. Context: {context}",
        }
