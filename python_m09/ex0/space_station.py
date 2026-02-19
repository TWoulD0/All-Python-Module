from datetime import datetime
from pydantic import BaseModel, Field, ValidationError
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_szie: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: Optional[datetime] = None
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    try:
        print("Space Station Data Validation")
        print("========================================")
        print("Valid station created:")
        space1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_szie=6,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True
        )
        print(f"ID: {space1.station_id}")
        print(f"Name: {space1.name}")
        print(f"Crew: {space1.crew_szie}")
        print(f"Power: {space1.power_level}")
        print(f"Oxygen: {space1.oxygen_level}")
        if space1.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: None")

        print("\n========================================")
        print("Expected validation error:")
        space2 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_szie=21,
            power_level=85.5,
            oxygen_level=92.3,
            is_operational=True
        )
        print(f"ID: {space2.station_id}")
        print(f"Name: {space2.name}")
        print(f"Crew: {space2.crew_szie}")
        print(f"Power: {space2.power_level}")
        print(f"Oxygen: {space2.oxygen_level}")
        if space2.is_operational is True:
            print("Status: Operational")
        else:
            print("Status: None")
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
