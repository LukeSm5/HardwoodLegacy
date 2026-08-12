from dataclasses import dataclass
from backend.app.models.base import PersonBase

@dataclass
class Recruit(PersonBase):
    rating: str
    high_school: str
    ratings: dict[str, str] # Wouldn't be actual ratings, would be more like grades so you can't know exactly what player you are getting