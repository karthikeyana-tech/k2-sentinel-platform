from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="K² Sentinel API",
    description="Cloud-Native Intelligent Tourist Safety Platform",
    version="0.1.0",
)

app.include_router(health_router)


@app.get("/")
async def root():
    return {
        "message": "Welcome to K² Sentinel 🚀"
    }