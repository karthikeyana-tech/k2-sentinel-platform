from fastapi import APIRouter

from app.exceptions.custom import ResourceNotFoundException
from app.schemas.response import ApiResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "",
    response_model=ApiResponse,
    summary="Health Check",
)
def health_check():
    return ApiResponse(
        success=True,
        message="Health check successful",
        data={
            "status": "healthy",
            "service": "K² Sentinel API",
        },
    )


@router.get(
    "/error",
    summary="Test Global Exception Handler",
)
def test_exception():
    """
    Temporary endpoint to test custom exception handling.
    """
    raise ResourceNotFoundException(
        message="Tourist not found."
    )