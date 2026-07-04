"""
Safe Zone Service Layer

Handles location-based safety zone operations.
"""

from sqlalchemy.orm import Session
from app.models.safe_zone import SafeZoneModel
from app.schemas.response import ApiResponse
import math


class SafeZoneService:
    """
    Service class for Safe Zone operations.
    """

    @staticmethod
    def get_all_safe_zones(db: Session):
        """
        Fetch all active safe zones.
        """

        zones = db.query(SafeZoneModel).filter(
            SafeZoneModel.is_active == True
        ).all()

        return ApiResponse(
            success=True,
            message="Safe zones fetched successfully",
            data=[
                {
                    "id": str(zone.id),
                    "name": zone.name,
                    "zone_type": zone.zone_type,
                    "latitude": zone.latitude,
                    "longitude": zone.longitude,
                    "contact_number": zone.contact_number,
                }
                for zone in zones
            ],
        )

    @staticmethod
    def find_nearest_safe_zone(db: Session, latitude: float, longitude: float):
        """
        Find nearest safe zone using basic distance calculation.
        """

        zones = db.query(SafeZoneModel).filter(
            SafeZoneModel.is_active == True
        ).all()

        def calculate_distance(lat1, lon1, lat2, lon2):
            return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

        nearest_zone = None
        min_distance = float("inf")

        for zone in zones:
            distance = calculate_distance(
                latitude,
                longitude,
                zone.latitude,
                zone.longitude
            )

            if distance < min_distance:
                min_distance = distance
                nearest_zone = zone

        if not nearest_zone:
            return ApiResponse(
                success=False,
                message="No safe zones found",
                data=None,
            )

        return ApiResponse(
            success=True,
            message="Nearest safe zone found",
            data={
                "id": str(nearest_zone.id),
                "name": nearest_zone.name,
                "zone_type": nearest_zone.zone_type,
                "latitude": nearest_zone.latitude,
                "longitude": nearest_zone.longitude,
                "contact_number": nearest_zone.contact_number,
                "distance": min_distance,
            },
        )