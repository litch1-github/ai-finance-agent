"""FastAPI entrypoint."""

from fastapi import FastAPI

from api.routes import router as api_router

app = FastAPI(title="AI Finance Agent", version="0.1.0")
app.include_router(api_router)


@app.get("/")
def root() -> dict[str, str]:
    """Root endpoint with a simple status message."""
    return {"message": "AI Finance Agent is running"}
