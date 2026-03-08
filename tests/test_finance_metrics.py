from finance.metrics import summarize_series


def test_summarize_series_uptrend() -> None:
    result = summarize_series([100.0, 101.0, 104.0])
    assert result["average"] == 101.6667
    assert result["trend"] == "up"


def test_summarize_series_downtrend() -> None:
    result = summarize_series([10.0, 8.0, 7.0])
    assert result["trend"] == "down"
