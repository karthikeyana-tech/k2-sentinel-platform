"""
SQLAlchemy ORM model for Safe Zones.

Represents verified safety locations like hospitals,
police stations, embassies, and emergency centers.
"""

from sqlalchemy import Column, String, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.models.base import Base


class SafeZoneModel(Base):
    """
    Database model for safe zones.
    """

    __tablename__ = "safe_zones"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    name = Column(String, nullable=False)
    zone_type = Column(String, nullable=False)

    address = Column(String, nullable=False)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    contact_number = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)