from dataclasses import dataclass
import random

from backend.app.models.player import Player
# Outcomes:
# 2 pt (make/miss)
    # Make
        # Score += 2
        # Shooter attempts += 1
        # Shooter makes += 1
        # Teams change possession
    # Miss
        # Shooter attempts += 1
        # Player rebounds += 1
        # Teams MAY change possession
# Foul
    # Shooting
        # 2 pt
            # 2 Free Throws
                # Make
                    # Score += 1
                    # Shooter FT Attempts += 1
                    # Shooter FT Makes += 1
                    # Teams change possession
                # Miss
                    # Shooter FT Attempts += 1
                    # Last Free Throw Missed
                    # Non-Last Free Throw Missed
        # 3 pt
        # And-One/One-And-One
            # Make
                # Score += 1
            # Miss
                # Shooter FT Attempts += 1
                # Player Rebounds += 1
                # Teams MAY change possession   
    # Non-Shooting
        # Offensive
            # Player Fouls += 1
            # Teams Change Possession
        # Defensive
            # Player Fouls += 1
            # Possession Continues
            # Bonus -> One and One
            # Double Bonus -> 2 Free Throws
            # No Bonus -> Possession Continues 
# Turnover
    # Steal
        # Player TO += 1
        # Player Steal += 1
        # Teams switch possession
    # Unforced
        # Player TO += 1
        # Teams switch possession
# Block
    # Player Shot Attempts (2Pt/3Pt) += 1
    # Player Blocks += 1
    # Player who Rebounds += 1
    # Teams MAY switch possession
# 3 pt (make/miss)
    # Make
        # Score += 3
        # Shooter attempts += 1
        # Shooter makes += 1
        # Teams change possession
    # Miss
        # Shooter attempts += 1
        # Player Rebounds += 1
        # Teams MAY change possession

@dataclass
class GameState:
    home_score: int
    away_score: int
    team_fouls: dict[str, int]
    player_fouls: dict[str, int]
    possession_team: str
    time_remaining: float
    half: int

@dataclass
class PlayResult:
    outcome: str
    points_scored: int
    time_consumed: float
    player_involved: dict[str, str]
    next_possession_team: str

BONUS_THRESHOLD = 7
DOUBLE_BONUS_THRESHOLD = 10

POSSESSION_OUTCOMES = {
    "turnover": 0.13,
    "foul": 0.15,
    "2pt": 0.47,
    "3pt": 0.25
}

ASSIST_PROBABILITY = {
    "assist": 0.18
}

TURNOVER_TYPES = {
    "steal": 0.5,
    "offensive_foul": 0.2,
    "traveling": 0.02,
    "double_dribble": 0.01,
    "bad_pass": 0.15,
    "out_of_bounds": 0.12,
}

REBOUND_WEIGHTS = {
    "offensive": {
        "height_factor": 0.6,
        "skill_factor": 0.4
    },
    "defensive": {
        "height_factor": 0.4,
        "skill_factor": 0.6
    }
}

FOUL_TYPES = {
    "defensive": {
        "reach_in": 0.4,
        "block": 0.2, 
        "shooting": 0.3,
        "off_ball": 0.08,
        "technical": 0.02

    }, 
    "offensive": {
        "charge": 0.5,
        "illegal_screen": 0.3,
        "over_the_back": 0.05,
        "loose_ball_foul": 0.12,
        "three_seconds": 0.03
    }
}

TIME_RANGES_BY_OUTCOME = {
    "turnover": (2, 30, 10),
    "2pt": (4, 30, 18),
    "3pt": (4, 30, 20),
    "foul": (4, 25, 12)
}


def generate_play(game_state: GameState) -> str:
    pass

def pick_player_for_play(roster: list[Player], role: str) -> Player:
    pass

def resolve_outcome(outcome: str, game_state: GameState, offense: list[Player], defense: list[Player]) -> PlayResult:
    if outcome == "defensive_foul":
        pass
    if outcome == "offensive_foul":
        pass


def consume_time(outcome: str) -> float:
    low, high, mode = TIME_RANGES_BY_OUTCOME.get(outcome, (4, 30, 15))
    return float(random.triangular(low, high, mode))

def update_game_state(game_state: GameState, play_result: PlayResult) -> GameState:
    game_state.time_remaining -= play_result.time_consumed
    if play_result.points_scored != 0:
        if game_state.possession_team == "home":
            game_state.home_score += play_result.points_scored
        else:
            game_state.away_score += play_result.points_scored
    if play_result.outcome in ["foul"]:
        fouling_player_id = play_result.player_involved["foul"]
        game_state.player_fouls[fouling_player_id] += 1
        if play_result.next_possession_team == game_state.possession_team:
            opposing_team = "away" if game_state.possession_team == "home" else "home"
            game_state.team_fouls[opposing_team] += 1
    game_state.possession_team = play_result.next_possession_team
    return game_state

def simulate_possession(game_state: GameState, offense: list[Player], defense: list[Player]) -> PlayResult:
    pass