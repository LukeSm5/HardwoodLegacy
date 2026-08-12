from dataclasses import dataclass

@dataclass
class Coach:
    id: str 
    name: str
    age: int
    team_id: str
    coaching_style: str
    experience: int
