"""Finance metric helpers."""


def summarize_series(values: list[float]) -> dict[str, float | str]:
    """Compute average and simple trend direction for a series."""
    average = sum(values) / len(values)
    trend = "up" if values[-1] >= values[0] else "down"
    return {"average": round(average, 4), "trend": trend}
