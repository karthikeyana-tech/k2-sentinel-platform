from sqlalchemy import Column, String, DateTime
from datetime import datetime
from app.core.database import Base


class Tourist(Base):
    __tablename__ = "tourists"

    id = Column(String, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    nationality = Column(String, nullable=False)
    passport_number = Column(String, unique=True, index=True, nullable=False)
    emergency_contact = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)