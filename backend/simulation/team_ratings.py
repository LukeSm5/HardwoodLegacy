from backend.simulation.team_constants import (PACE_STYLES, OFFENSIVE_SCHEMES, DEFENSIVE_SCHEMES)

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