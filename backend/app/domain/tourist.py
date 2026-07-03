"""
Tourist domain entity.

Represents a tourist within the K² Sentinel domain.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class Tourist:
    """
    Core Tourist domain entity.
    """

    id: UUID
    full_name: str
    nationality: str
    passport_number: str
    emergency_contact: str
    created_at: datetime

    def has_emergency_contact(self) -> bool:
        """
        Check whether an emergency contact exists.
        """
        return bool(self.emergency_contact.strip())

    def display_name(self) -> str:
        """
        Return the tourist's display name.
        """
        return self.full_name.title()

    def is_indian(self) -> bool:
        """
        Check whether the tourist is from India.
        """
        return self.nationality.strip().lower() == "india"