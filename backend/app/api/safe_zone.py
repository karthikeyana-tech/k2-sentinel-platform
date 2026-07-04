"""
Safe Zone API Routes

Handles geospatial safety zone operations.
"""

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.services.safe_zone_service import SafeZoneService

router = APIRouter(prefix="/safe-zones", tags=["Safe Zones"])


# -----------------------------
# DB Dependency
# -----------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# Get All Safe Zones
# -----------------------------
@router.get("/")
def get_all_safe_zones(db: Session = Depends(get_db)):
    return SafeZoneService.get_all_safe_zones(db)


# -----------------------------
# Find Nearest Safe Zone
# -----------------------------
@router.get("/nearest")
def find_nearest_safe_zone(
    latitude: float = Query(...),
    longitude: float = Query(...),
    db: Session = Depends(get_db),
):
    return SafeZoneService.find_nearest_safe_zone(db, latitude, longitude)