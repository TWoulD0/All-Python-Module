from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=1000)
    contac_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def check(self):
        if not self.contact_id.startswith('AC'):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contac_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contac_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should"
                             "include received messages")

        return self


def main() -> None:
    try:
        print("Alien Contact Log Validation")
        print("======================================")
        print("Valid contact report:")

        alien1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contac_type=ContactType.RADIO,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
        )

        print(f"ID: {alien1.contact_id}")
        print(f"Type: {alien1.contac_type}")
        print(f"Location: {alien1.location}")
        print(f"Signal: {alien1.signal_strength}/10")
        print(f"Duration: {alien1.duration_minutes} minutes")
        print(f"Witnesses: {alien1.witness_count}")
        print(f"Message: '{alien1.message_received}'")

        print("\n======================================")
        print("Expected validation error:")

        alien2 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            contac_type=ContactType.TELEPATHIC,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli",
        )

        print(f"ID: {alien2.contact_id}")
        print(f"Type: {alien2.contac_type}")
        print(f"Location: {alien2.location}")
        print(f"Signal: {alien2.signal_strength}/10")
        print(f"Duration: {alien2.duration_minutes} minutes")
        print(f"Witnesses: {alien2.witness_count}")
        print(f"Message: '{alien2.message_received}'")

    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
