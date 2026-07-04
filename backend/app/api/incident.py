from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.services.incident_service import IncidentService
from app.schemas.incident import IncidentCreate

router = APIRouter(tags=["Incidents"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_incident(payload: IncidentCreate, db: Session = Depends(get_db)):
    return IncidentService.create_incident(db, payload)


@router.get("/{incident_id}")
def get_incident(incident_id: str, db: Session = Depends(get_db)):
    return IncidentService.get_incident(db, incident_id)