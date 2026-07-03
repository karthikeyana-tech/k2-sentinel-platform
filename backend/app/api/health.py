from fastapi import APIRouter

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
    Temporary endpoint to test the global exception handler.
    This endpoint will be removed before production.
    """
    raise Exception("This is a test exception.")