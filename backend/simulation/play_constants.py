BONUS_THRESHOLD = 7
DOUBLE_BONUS_THRESHOLD = 10
MIN_HEIGHT_INCHES = 68 
MAX_HEIGHT_INCHES = 87
MAX_RATING = 99

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

STEAL_WEIGHTS = {
    "steal": 0.5,
    "speed": 0.3,
    "perimeter_defense": 0.2
}

BLOCK_WEIGHTS = {
    "height": 0.5,
    "block": 0.4,
    "interior_defense": 0.1
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