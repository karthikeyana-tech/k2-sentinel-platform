"""
Alert Domain Entity.

Represents system-generated alerts for tourist safety events.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Alert:
    """
    Domain entity representing a system-generated alert.

    Alerts are triggered during emergencies, risk detection,
    or escalation events involving tourists.
    """

    id: UUID
    tourist_id: UUID
    incident_id: UUID | None

    alert_type: str
    message: str

    severity: str

    is_read: bool

    created_at: datetime