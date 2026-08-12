from dataclasses import dataclass

@dataclass
class Player:
    id: int
    name: str
    team_id: int
    position: str
    height_feet: int
    height_inches: int
    weight: int
    year: str
    archetype: str
    ratings: dict[str, int]
