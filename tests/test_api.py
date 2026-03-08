from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze() -> None:
    response = client.post(
        "/api/analyze",
        json={"symbol": "AAPL", "values": [190.0, 195.0, 198.0]},
    )
    body = response.json()

    assert response.status_code == 200
    assert body["symbol"] == "AAPL"
    assert body["trend"] == "up"
    assert "Context" in body["agent_summary"]
