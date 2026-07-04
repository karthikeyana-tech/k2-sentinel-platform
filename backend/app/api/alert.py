from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.services.alert_service import AlertService

router = APIRouter(tags=["Alerts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{incident_id}")
def create_alert(incident_id: str, db: Session = Depends(get_db)):
    return AlertService.generate_alert(db, incident_id)


@router.get("/{alert_id}")
def get_alert(alert_id: str, db: Session = Depends(get_db)):
    return AlertService.get_alert(db, alert_id)