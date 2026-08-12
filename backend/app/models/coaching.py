from dataclasses import dataclass

@dataclass
class Coach:
    id: int 
    name: str
    age: int
    team_id: int
    coaching_style: str
    experience: int
