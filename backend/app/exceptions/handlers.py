"""
Global exception handlers for K² Sentinel.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.schemas.response import ApiResponse


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    """
    Handle all unexpected exceptions.
    """

    return JSONResponse(
        status_code=500,
        content=ApiResponse(
            success=False,
            message="Internal Server Error",
            data=None,
        ).model_dump(),
    )


def register_exception_handlers(app: FastAPI):
    """
    Register all global exception handlers.
    """

    app.add_exception_handler(
        Exception,
        generic_exception_handler,
    )