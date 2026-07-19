# PlayerArchetypes.py
# Define player archetypes

ARCHETYPES={
    "facilitator": {
        "name": "Facilitator",
        "description":"Pass first player that sets up teammates for scoring opportunities",
        "valid_positions": ["PG", "SG"],
        "profile_weights": {
            "passing": 0.4,
            "pass_iq": 0.3,
            "dribbling": 0.15,
            "speed": 0.05,
            "shot_iq": 0.05,
            "defensive_iq": 0.05
        },
        "development_weights": {
            "passing": 1.4,
            "dribbling": 1.2,
            "pass_iq": 1.2,
            "3pt": 0.8,
            "mid_range": 0.8,
            "inside_scoring": 0.8
        },
    },
    "sniper": {
        "name": "Sniper",
        "description":"Elite shooter",
        "valid_positions": ["PG", "SG", "SF"],
        "profile_weights": {
            "3pt": 0.4,
            "mid_range": 0.3,
            "shot_iq": 0.2,
            "free_throw": 0.1
        },
        "development_weights": {
            "3pt": 1.4,
            "mid_range": 1.2,
            "free_throw": 1.2,
            "inside_scoring": 0.8,
            "dribbling": 0.8
        },
    },
    "slasher": {
        "name": "Slasher",
        "description":"Aggressive finisher around the rim",
        "valid_positions": ["PG", "SG", "SF", "PF", "C"],
        "profile_weights": {
            "inside_scoring": 0.35,
            "driving_dunk": 0.30,
            "speed": 0.20,
            "strength": 0.15,
        },
        "development_weights": {
            "inside_scoring": 1.4,
            "driving_dunk": 1.2,
            "3pt": 0.8,
            "mid_range": 0.8
        },
    },
    "lockdown_defender": {
        "name": "Lockdown Defender",
        "description": "Defensive specialist that can guard multiple positions",
        "valid_positions": ["PG", "SG", "SF", "PF", "C"],
        "profile_weights": {
            "perimeter_defense": 0.30,
            "interior_defense": 0.25,
            "defensive_iq": 0.20,
            "steal": 0.15,
            "block": 0.10,
        },
        "development_weights": {
            "steal": 1.3,
            "block": 1.3,
            "perimeter_defense": 1.3,
            "interior_defense": 1.3,
            "3pt": 0.8,
            "mid_range": 0.8,
            "inside_scoring": 0.9
        },
    },
    "3_and_d": {
        "name": "3 And D",
        "description":"Player that can shoot from outside and play solid defense",
        "valid_positions": ["PG", "SG", "SF"],
        "profile_weights": {
            "3pt": 0.35,
            "perimeter_defense": 0.35,
            "steal": 0.20,
            "shot_iq": 0.10,
        },
        "development_weights": {
            "3pt": 1.3,
            "steal": 1.3,
            "perimeter_defense": 1.3,
            "passing": 0.8,
            "dribbling": 0.8
        },
    },
    "rebounder": {
        "name": "Rebounder",
        "description":"Player that excels at grabbing rebounds and controlling the boards",
        "valid_positions": ["PF", "C"],
        "profile_weights": {
            "defensive_rebounding": 0.40,
            "offensive_rebounding": 0.35,
            "strength": 0.15,
            "vertical": 0.10,
        },
        "development_weights": {
            "offensive_rebounding": 1.4,
            "defensive_rebounding": 1.4,
            "3pt": 0.8,
            "mid_range": 0.8
        },
    },
    "rim_protector": {
        "name": "Rim Protector",
        "description": "Player that excels at blocking shots and protecting the rim",
        "valid_positions": ["PF", "C"],
        "profile_weights": {
            "block": 0.40,
            "interior_defense": 0.30,
            "defensive_iq": 0.20,
            "vertical": 0.10,
        },
        "development_weights": {
            "block": 1.4,
            "interior_defense": 1.4,
            "3pt": 0.8,
            "mid_range": 0.8
        }
    },
    "all_around": {
        "name": "All Around",
        "description":"Well-rounded player that contributes in multiple areas",
        "valid_positions": ["PG", "SG", "SF", "PF", "C"],
        "profile_weights": { 
            "3pt": 0.10,
            "mid_range": 0.10,
            "inside_scoring": 0.10,
            "passing": 0.10,
            "dribbling": 0.10,
            "defensive_rebounding": 0.10,
            "offensive_rebounding": 0.10,
            "perimeter_defense": 0.10,
            "steal": 0.10,
            "shot_iq": 0.10,
        },
        "development_weights": {
            "3pt": 1.0,
            "mid_range": 1.0,
            "inside_scoring": 1.0,
            "block": 1.0,
            "steal": 1.0,
            "interior_defense": 1.0,
            "perimeter_defense": 1.0,
            "shot_iq": 1.0,
            "passing": 1.0,
            "dribbling": 1.0,
            "offensive_rebounding": 1.0,
            "defensive_rebounding": 1.0,
            "defensive_iq": 1.0,
            "pass_iq": 1.0,
            "driving_dunk": 1.0,
            "standing_dunk": 1.0,
            "free_throw": 1.0
        },
    "post_scorer": {
        "name": "Post Scorer",
        "description":"Player that excels at scoring in the post and around the basket",
        "valid_positions": ["SF", "PF", "C"],
        "profile_weights": {
            "inside_scoring": 0.35,
            "standing_dunk": 0.30,
            "strength": 0.20,
            "offensive_rebounding": 0.15,
        },
        "development_weights": {
            "inside_scoring": 1.4,
            "standing_dunk": 1.4,
            "3pt": 0.8,
            "dribbling": 0.8
        },
    },
    "stretch_big": {
        "name": "Stretch Big",
        "description":"Big man that can shoot from outside and stretch the floor",
        "valid_positions": ["PF", "C"],
        "profile_weights": {
            "3pt": 0.40,
            "mid_range": 0.30,
            "free_throw": 0.20,
            "shot_iq": 0.10,
        },
        "development_weights": {
            "3pt": 1.3,
            "mid_range": 1.3,
            "free_throw": 1.3,
            "inside_scoring": 0.8,
            "offensive_rebounding": 0.8
        },
    },
    "shot_creator": {
    "name": "Shot Creator",
        "description":"Player that can create their own shot and score in isolation situations",
        "valid_positions": ["PG", "SG", "SF", "PF", "C"],
        "profile_weights": {
            "dribbling": 0.30,
            "mid_range": 0.25,
            "shot_iq": 0.25,
            "3pt": 0.20,
        },
        "development_weights": {
            "dribbling": 1.3,
            "mid_range": 1.3,
            "3pt": 1.3,
            "passing": 0.8,
            "shot_iq": 1.2
        },
    },
    "elite_athlete": {
        "name": "Elite Athlete",
        "description":"Raw athleticism and physical tools that could translate to elite play",
        "valid_positions": ["PG", "SG", "SF", "PF", "C"],
        "profile_weights": {
            "speed": 0.30,
            "vertical": 0.30,
            "strength": 0.20,
            "driving_dunk": 0.20,
        },
        "development_weights": {
            "driving_dunk": 1.3,
            "defensive_rebounding": 1.3,
            "speed": 1.3,
            "offensive_rebounding": 1.3,
            "3pt": 0.8,
            "mid_range": 0.9,
            "free_throw": 0.7
        },
    },
    "paint_beast": {
        "name": "Paint Beast",
        "description":"Purely dominant force in the paint",
        "valid_positions": ["PF", "C"],
        "profile_weights": {
            "inside_scoring": 0.30,
            "strength": 0.25,
            "defensive_rebounding": 0.25,
            "offensive_rebounding": 0.20,
        },
        "development_weights": {
            "inside_scoring": 1.4,
            "defensive_rebounding": 1.4,
            "offensive_rebounding": 1.4,
            "3pt": 0.8,
            "mid_range": 0.8
            },
        }
    }
}

def calculate_archetype_score(player_ratings: dict, archetype: str) -> float:
    pass

def determine_archetype(player_ratings: dict, position: str) -> str:
    archetype = ""
    bestArchetypeScore = -1
    validArchetypes = get_valid_archetypes(position)

    if not validArchetypes:
        raise ValueError(f"No valid archetypes found for position: {position}")
    
    for currArchetype in validArchetypes:
        currArchetypeScore = calculate_archetype_score(player_ratings, currArchetype)
        if currArchetypeScore > bestArchetypeScore:
            archetype = currArchetype
            bestArchetypeScore = currArchetypeScore
    return archetype

def get_development_bonus(archetype: str, stat: str) -> float:
    pass

def get_valid_archetypes(position: str) -> list:
    archetypes = []
    for archetype in ARCHETYPES:
        if position in ARCHETYPES[archetype]["valid_positions"]:
            archetypes.append(archetype)
    return archetypes


def get_archetype_scores(player_ratings: dict, position: str) -> dict:
    scores = {}
    archetypeList = get_valid_archetypes(position)
    for archetype in archetypeList:
        scores[archetype] = calculate_archetype_score(player_ratings, archetype)
    return scores

def is_archetype_transition(old_archetype: str, new_archetype: str) -> bool:
    return old_archetype != new_archetype