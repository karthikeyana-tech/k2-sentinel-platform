"""
Safe Zone Domain Entity.

Represents a safe location for tourists during emergencies.
"""

from dataclasses import dataclass
from uuid import UUID


@dataclass
class SafeZone:
    """
    Domain entity representing a safe zone for tourists.

    Includes locations like hospitals, police stations,
    embassies, and verified emergency support areas.
    """

    id: UUID
    name: str
    zone_type: str

    address: str
    latitude: float
    longitude: float

    contact_number: str

    is_active: bool

    def is_operational(self) -> bool:
        """
        Check if the safe zone is active and usable.
        """
        return self.is_active

    def is_hospital(self) -> bool:
        """
        Check if this safe zone is a hospital.
        """
        return self.zone_type.strip().upper() == "HOSPITAL"

    def is_police_station(self) -> bool:
        """
        Check if this safe zone is a police station.
        """
        return self.zone_type.strip().upper() == "POLICE_STATION"

    def is_embassy(self) -> bool:
        """
        Check if this safe zone is an embassy.
        """
        return self.zone_type.strip().upper() == "EMBASSY"

    def summary(self) -> str:
        """
        Return a human-readable summary of the safe zone.
        """
        return (
            f"{self.name} ({self.zone_type}) - "
            f"{self.address}"
        )