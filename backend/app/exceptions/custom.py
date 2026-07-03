"""
Custom application exceptions for K² Sentinel.
"""

from fastapi import status

from app.exceptions.base import AppException


class ResourceNotFoundException(AppException):
    """
    Raised when a requested resource is not found.
    """

    def __init__(
        self,
        message: str = "Resource not found",
        error_code: str = "RESOURCE_NOT_FOUND",
    ):
        super().__init__(
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,
            error_code=error_code,
        )


class ValidationException(AppException):
    """
    Raised when validation fails.
    """

    def __init__(
        self,
        message: str = "Validation failed",
        error_code: str = "VALIDATION_ERROR",
    ):
        super().__init__(
            message=message,
            status_code=status.HTTP_400_BAD_REQUEST,
            error_code=error_code,
        )


class UnauthorizedException(AppException):
    """
    Raised when authentication fails.
    """

    def __init__(
        self,
        message: str = "Unauthorized",
        error_code: str = "UNAUTHORIZED",
    ):
        super().__init__(
            message=message,
            status_code=status.HTTP_401_UNAUTHORIZED,
            error_code=error_code,
        )


class ForbiddenException(AppException):
    """
    Raised when access is forbidden.
    """

    def __init__(
        self,
        message: str = "Forbidden",
        error_code: str = "FORBIDDEN",
    ):
        super().__init__(
            message=message,
            status_code=status.HTTP_403_FORBIDDEN,
            error_code=error_code,
        )


class InternalServerException(AppException):
    """
    Raised for unexpected server errors.
    """

    def __init__(
        self,
        message: str = "Internal server error",
        error_code: str = "INTERNAL_SERVER_ERROR",
    ):
        super().__init__(
            message=message,
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            error_code=error_code,
        )