import uuid
from app.models.tourist import Tourist


class TouristService:

    @staticmethod
    def create_tourist(db, payload):

        new_tourist = Tourist(
            id=str(uuid.uuid4()),
            full_name=payload.full_name,
            nationality=payload.nationality,
            passport_number=payload.passport_number,
            emergency_contact=payload.emergency_contact
        )

        db.add(new_tourist)
        db.commit()
        db.refresh(new_tourist)

        return {
            "success": True,
            "message": "Tourist created successfully",
            "data": {
                "id": new_tourist.id,
                "full_name": new_tourist.full_name,
                "passport_number": new_tourist.passport_number
            }
        }

    @staticmethod
    def get_tourist(db, tourist_id):
        return db.query(Tourist).filter(Tourist.id == tourist_id).first()