import uuid
from app.models.alert import Alert
from app.models.incident import Incident


class AlertService:

    @staticmethod
    def generate_alert(db, incident_id: str):

        incident = db.query(Incident).filter(Incident.id == incident_id).first()

        if not incident:
            return {"success": False, "message": "Incident not found"}

        alert = Alert(
            id=str(uuid.uuid4()),
            incident_id=incident_id,
            message=f"Alert: {incident.incident_type} at {incident.location}",
            severity="HIGH"
        )

        db.add(alert)
        db.commit()
        db.refresh(alert)

        return {
            "success": True,
            "message": "Alert generated",
            "data": {
                "id": alert.id,
                "message": alert.message
            }
        }

    @staticmethod
    def get_alert(db, alert_id: str):
        return db.query(Alert).filter(Alert.id == alert_id).first()