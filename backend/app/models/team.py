from dataclasses import dataclass
from backend.app.models.player import Player

@dataclass
class Team:
    id: str
    name: str
    city: str
    state: str
    home_arena: str
    coach_id: int
    conference: str
    roster: list[Player]
    record: dict[str, int]
    prestige: int
