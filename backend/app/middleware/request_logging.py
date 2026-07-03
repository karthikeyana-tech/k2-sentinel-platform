"""
Request Logging Middleware for K² Sentinel.

Logs every incoming HTTP request including:
- HTTP Method
- Request Path
- Client IP
- Response Status Code
- Processing Time
- Unhandled Exceptions

This middleware helps monitor API traffic and diagnose issues.
"""

import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.logging import get_logger

logger = get_logger(__name__)


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that logs every HTTP request and response.
    """

    async def dispatch(self, request: Request, call_next):
        """
        Process each incoming request, log request details,
        measure execution time, and log the response.
        """

        # Record request start time
        start_time = time.perf_counter()

        # Client IP Address
        client_ip = (
            request.client.host
            if request.client
            else "Unknown"
        )

        # Log incoming request
        logger.info(
            "Request Started | %s %s | Client: %s",
            request.method,
            request.url.path,
            client_ip,
        )

        try:
            # Continue request processing
            response = await call_next(request)

        except Exception as exc:
            # Calculate execution time
            duration_ms = (time.perf_counter() - start_time) * 1000

            # Log exception with traceback
            logger.exception(
                "Request Failed | %s %s | Duration: %.2f ms | Error: %s",
                request.method,
                request.url.path,
                duration_ms,
                str(exc),
            )

            # Re-raise exception so FastAPI handles it
            raise

        # Calculate total processing time
        duration_ms = (time.perf_counter() - start_time) * 1000

        # Log successful response
        logger.info(
            "Request Completed | %s %s | Status: %s | Duration: %.2f ms",
            request.method,
            request.url.path,
            response.status_code,
            duration_ms,
        )

        return response