"""Local retrieval component used by the agent."""


class LocalRetriever:
    """Basic context retriever; can be replaced by vector DB implementation."""

    _knowledge_base = {
        "AAPL": "Apple often tracks product cycles and macro rates.",
        "BTC": "Bitcoin can be highly sensitive to liquidity and risk sentiment.",
    }

    def get_context(self, symbol: str) -> str:
        """Return local context for a symbol."""
        return self._knowledge_base.get(symbol.upper(), "No local context available.")
