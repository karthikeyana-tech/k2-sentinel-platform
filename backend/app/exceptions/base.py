"""
Base exception classes for K² Sentinel.

All custom exceptions should inherit from AppException.
"""


class AppException(Exception):
    """
    Base application exception.

    Attributes:
        message:
            Human-readable error message.

        status_code:
            HTTP status code returned to the client.

        error_code:
            Internal application error code.
    """

    def __init__(
        self,
        message: str,
        status_code: int = 500,
        error_code: str = "APP_ERROR",
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code

        super().__init__(message)