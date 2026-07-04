from sqlalchemy import Column, String, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(String, primary_key=True, index=True)
    incident_id = Column(String, ForeignKey("incidents.id"), nullable=False)

    message = Column(String, nullable=False)
    severity = Column(String, default="HIGH")

    created_at = Column(DateTime, default=datetime.utcnow)