from dataclasses import dataclass

@dataclass
class Game:
    id: str
    score: dict[str, int]
    stats: dict[str, dict[str, int]] 
    time: float
