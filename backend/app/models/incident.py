from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(String, primary_key=True, index=True)
    tourist_id = Column(String, ForeignKey("tourists.id"), nullable=False)

    incident_type = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, nullable=False)

    status = Column(String, default="OPEN")

    created_at = Column(DateTime, default=datetime.utcnow)