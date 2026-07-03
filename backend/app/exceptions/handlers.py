"""
Global exception handlers for K² Sentinel.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.base import AppException
from app.schemas.response import ApiResponse


async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    """
    Handle all custom application exceptions.
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            success=False,
            message=exc.message,
            data={
                "error_code": exc.error_code,
            },
        ).model_dump(),
    )


async def generic_exception_handler(
    request: Request,
    exc: Exception,
):
    """
    Handle unexpected exceptions.
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
    Register all exception handlers.
    """

    app.add_exception_handler(
        AppException,
        app_exception_handler,
    )

    app.add_exception_handler(
        Exception,
        generic_exception_handler,
    )