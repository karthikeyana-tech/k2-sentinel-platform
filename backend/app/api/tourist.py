from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.services.tourist_service import TouristService
from app.schemas.tourist import TouristCreate

router = APIRouter(tags=["Tourists"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_tourist(payload: TouristCreate, db: Session = Depends(get_db)):
    return TouristService.create_tourist(db, payload)


@router.get("/{tourist_id}")
def get_tourist(tourist_id: str, db: Session = Depends(get_db)):
    return TouristService.get_tourist(db, tourist_id)