import uuid
from app.models.incident import Incident


class IncidentService:

    @staticmethod
    def create_incident(db, data):
        incident = Incident(
            id=str(uuid.uuid4()),
            tourist_id=data.tourist_id,
            incident_type=data.incident_type,
            description=data.description,
            location=data.location,
            status="OPEN"
        )

        db.add(incident)
        db.commit()
        db.refresh(incident)
        return incident

    @staticmethod
    def get_incident(db, incident_id: str):
        return db.query(Incident).filter(Incident.id == incident_id).first()