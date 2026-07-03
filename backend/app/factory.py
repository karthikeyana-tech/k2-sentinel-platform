from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.middleware.request_logging import RequestLoggingMiddleware


def create_app() -> FastAPI:
    """
    Application Factory.
    Creates and configures the FastAPI application.
    """
    # Configure application logging
    setup_logging()
    
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="Cloud-Native Intelligent Tourist Safety Platform",
        version=settings.VERSION,
    )

    # Register middleware
    app.add_middleware(RequestLoggingMiddleware)

    # Register API routers
    app.include_router(
        health_router,
        prefix=settings.API_PREFIX,
    )

    # Root endpoint
    @app.get("/", tags=["Root"])
    def root():
        return {
            "message": f"Welcome to {settings.PROJECT_NAME} 🚀",
            "version": settings.VERSION,
            "environment": settings.ENVIRONMENT,
        }

    return app