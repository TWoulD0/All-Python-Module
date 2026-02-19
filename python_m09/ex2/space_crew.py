from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class CrewRanks(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1, le=10000)

    @model_validator(mode="after")
    def check(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        has_leader = any(m.rank in (CrewRanks.COMMANDER, CrewRanks.CAPTAIN)
                         for m in self.crew)
        if not has_leader:
            raise ValueError("Mission must have at least"
                             "one Commander or Captain")

        experienced_crew = 0
        half_crew = len(self.crew) / 2
        for c in self.crew:
            if c.years_experience > 5:
                experienced_crew += 1
        if self.duration_days > 365 and half_crew > experienced_crew:
            raise ValueError("Long missions (> 365 days) need 50%"
                             " experienced crew (5+ years)")

        if any(not c.is_active for c in self.crew):
            raise ValueError("All crew members must be active")

        return self


def main() -> None:
    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")

        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2028, 7, 17, 9, 30),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id='CM001',
                    name='Sarah Connor',
                    rank=CrewRanks.CAPTAIN,
                    age=57,
                    specialization='Mission Command',
                    years_experience=30,
                    is_active=True
                ),
                CrewMember(
                    member_id='CM002',
                    name='John Smith',
                    rank=CrewRanks.LIEUTENANT,
                    age=43,
                    specialization='Navigation',
                    years_experience=18,
                    is_active=True
                ),
                CrewMember(
                    member_id='CM003',
                    name='Alice Johnson',
                    rank=CrewRanks.OFFICER,
                    age=30,
                    specialization='Engineering',
                    years_experience=5,
                    is_active=True
                ),
            ],
            budget_millions=2500,
        )

        print(f"Mission: {mission1.mission_name}")
        print(f"ID: {mission1.mission_id}")
        print(f"Destination: {mission1.destination}")
        print(f"Duration: {mission1.duration_days}")
        print(f"Budget: {mission1.budget_millions}")
        print(f"Crew size: {len(mission1.crew)}")
        print("Crew members:")
        for member in mission1.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")

        print("=========================================")
        print("Expected validation error:")

        mission2 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2028, 7, 17, 9, 30),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id='CM001',
                    name='Sarah Connor',
                    rank=CrewRanks.LIEUTENANT,
                    age=57,
                    specialization='Mission Command',
                    years_experience=30,
                    is_active=True
                ),
                CrewMember(
                    member_id='CM002',
                    name='John Smith',
                    rank=CrewRanks.LIEUTENANT,
                    age=43,
                    specialization='Navigation',
                    years_experience=18,
                    is_active=True
                ),
                CrewMember(
                    member_id='CM003',
                    name='Alice Johnson',
                    rank=CrewRanks.OFFICER,
                    age=30,
                    specialization='Engineering',
                    years_experience=5,
                    is_active=True
                ),
            ],
            budget_millions=2500,
        )

        print(f"Mission: {mission2.mission_name}")
        print(f"ID: {mission2.mission_id}")
        print(f"Destination: {mission2.destination}")
        print(f"Duration: {mission2.duration_days}")
        print(f"Budget: {mission2.budget_millions}")
        print(f"Crew size: {len(mission2.crew)}")
        print("Crew members:")
        for member in mission2.crew:
            print(f"- {member.name} ({member.rank.value})"
                  f" - {member.specialization}")

    except ValidationError as e:
        print(e.errors()[0]["msg"].replace("Value error, ", ""))


if __name__ == "__main__":
    main()
