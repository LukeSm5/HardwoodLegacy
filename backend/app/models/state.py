from dataclasses import dataclass

@dataclass
class GameState:
    home_score: int
    away_score: int
    team_fouls: dict[str, int]
    player_fouls: dict[str, int]
    possession_team: str
    time_remaining: float
    half: int