"""
Emergency Contact Domain Entity.

Represents a person who can be contacted during an emergency involving a tourist.
"""

from dataclasses import dataclass
from uuid import UUID


@dataclass
class EmergencyContact:
    """
    Domain entity representing an emergency contact for a tourist.
    """

    id: UUID
    tourist_id: UUID

    name: str
    relationship: str
    phone_number: str
    email: str

    is_primary: bool

    def is_primary_contact(self) -> bool:
        """
        Check if this is the primary emergency contact.
        """
        return self.is_primary

    def contact_summary(self) -> str:
        """
        Return a readable summary of the contact.
        """
        return (
            f"{self.name} ({self.relationship}) - "
            f"{self.phone_number}"
        )

    def update_phone(self, new_number: str) -> None:
        """
        Update the phone number of the contact.
        """
        self.phone_number = new_number

    def update_email(self, new_email: str) -> None:
        """
        Update the email of the contact.
        """
        self.email = new_email