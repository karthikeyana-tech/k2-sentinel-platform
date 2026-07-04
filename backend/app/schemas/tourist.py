from pydantic import BaseModel


class TouristCreate(BaseModel):
    full_name: str
    nationality: str
    passport_number: str
    emergency_contact: str