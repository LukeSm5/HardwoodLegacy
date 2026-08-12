from dataclasses import dataclass
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
    time_consumed: int

POSSESION_OUTCOMES = {
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

FOUL_TYPES = {
    "defensive": {

    }, 
    "offensive": {}
}


def generate_play(game_state) -> str:
    pass

def pick_player_for_play(roster, role) -> str:
    pass

def resolve_outcome() -> PlayResult: 
    pass

def consume_time(outcome) -> int:
    pass

def update_game_state() -> GameState:
    pass

def simulate_possession() -> PlayResult:
    pass