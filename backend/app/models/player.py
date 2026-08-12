from dataclasses import dataclass
from backend.app.models.base import PersonBase

@dataclass
class Player(PersonBase):
    team_id: str
    ratings: dict[str, int]
