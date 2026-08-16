from dataclasses import dataclass

@dataclass
class PlayResult:
    outcome: str
    points_scored: int
    time_consumed: float
    player_involved: dict[str, str]
    next_possession_team: str