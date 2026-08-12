from dataclasses import dataclass

@dataclass
class PersonBase:
    id: str
    name: str
    position: str
    height_feet: int
    height_inches: int
    weight: int
    year: str
    archetype: str