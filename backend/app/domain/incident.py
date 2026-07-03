"""
Incident Domain Entity.

Represents an incident involving a tourist.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Incident:
    """
    Domain entity representing an incident involving a tourist.
    """

    id: UUID
    tourist_id: UUID

    incident_type: str
    description: str
    location: str

    status: str

    reported_at: datetime

    def is_open(self) -> bool:
        """
        Check whether the incident is currently open.
        """
        return self.status.strip().upper() == "OPEN"

    def is_resolved(self) -> bool:
        """
        Check whether the incident has been resolved.
        """
        return self.status.strip().upper() == "RESOLVED"

    def mark_in_progress(self) -> None:
        """
        Mark the incident as being processed.
        """
        self.status = "IN_PROGRESS"

    def mark_resolved(self) -> None:
        """
        Mark the incident as resolved.
        """
        self.status = "RESOLVED"

    def summary(self) -> str:
        """
        Return a concise summary of the incident.
        """
        return (
            f"[{self.incident_type}] "
            f"{self.description} "
            f"@ {self.location}"
        )