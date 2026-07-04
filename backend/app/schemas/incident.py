from pydantic import BaseModel


class IncidentCreate(BaseModel):
    tourist_id: str
    incident_type: str
    description: str
    location: str


class IncidentResponse(BaseModel):
    id: str
    tourist_id: str
    incident_type: str
    description: str
    location: str
    status: str

    class Config:
        from_attributes = True