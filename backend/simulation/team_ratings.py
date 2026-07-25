PACE_STYLES={
    "fast_break": 1.2,
    "balanced": 1.0,
    "half_court": 0.8
}

OFFENSIVE_SCHEMES={
    "5_out": {
        "3pt": 1.2,
        "inside_scoring": 0.8
    },
    "motion": {
        "dribbling": 1.2,
        "passing": 1.2,
    },
    "pick_and_roll": {
        "inside_scoring": 1.2,
        "passing": 1.2
    },
    "triangle": {
        "speed": 0.8,
        "passing": 1.2,
        "pass_iq": 1.2
    },

}

DEFENSIVE_SCHEMES={
    "2-3": {
        "interior_defense": 1.2,
        "defensive_iq": 1.2,
        "perimeter_defense": 0.8,
    },
    "3-2": {
        "perimeter_defense": 1.2,
        "defensive_iq": 1.2,
        "interior_defense": 0.8,
    },
    "1-3-1": {
        "steal": 1.2,
        "defensive_iq": 1.2,
        "interior_defense": 0.8,
    },
    "full_court_press": {
        "steal": 1.3,
        "speed": 1.2
    },
    "trap": {
        "steal": 1.4,
        "perimeter_defense": 1.2
    },
    "man_to_man": {
        "perimeter_defense": 1.2,
        "interior_defense": 1.2
    },
}

def get_offensive_scheme_modifiers(scheme: str) -> dict:
    if scheme not in OFFENSIVE_SCHEMES:
        raise ValueError(f"Invalid offensive scheme: {scheme}")
    return OFFENSIVE_SCHEMES[scheme]

def get_defensive_scheme_modifiers(scheme: str) -> dict:
    if scheme not in DEFENSIVE_SCHEMES:
        raise ValueError(f"Invalid defensive scheme: {scheme}")
    return DEFENSIVE_SCHEMES[scheme]

def get_pace_multiplier(pace_style: str) -> float:
    if pace_style not in PACE_STYLES:
        raise ValueError(f"Invalid pace style: {pace_style}")
    return PACE_STYLES[pace_style]

def get_team_ratings(roster: list, offensive_scheme: str, defensive_scheme: str, pace_style: str) -> dict:
    offensive_modifiers = get_offensive_scheme_modifiers(offensive_scheme)
    defensive_modifiers = get_defensive_scheme_modifiers(defensive_scheme)
    pace_multiplier = get_pace_multiplier(pace_style)

    return {
        "offensive_modifiers": offensive_modifiers,
        "defensive_modifiers": defensive_modifiers,
        "pace_multiplier": pace_multiplier,
    }