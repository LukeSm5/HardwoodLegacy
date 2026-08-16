from backend.simulation.play_constants import ( MAX_HEIGHT_INCHES, 
                                               MIN_HEIGHT_INCHES, 
                                               REBOUND_WEIGHTS, 
                                               STEAL_WEIGHTS,
                                               BLOCK_WEIGHTS,
                                               MAX_RATING )
from backend.app.models.player import Player

def calculate_rebound_weight(player: Player, rebound_type: str) -> float:
    height_inches = height_to_inches(player.height_feet, player.height_inches)
    normalized_height = normalize_height(height_inches)
    height_weight = normalized_height * REBOUND_WEIGHTS[rebound_type]["height_factor"]
    skill_rating = player.ratings[f"{rebound_type}_rebound"] / MAX_RATING
    skill_weight = REBOUND_WEIGHTS[rebound_type]["skill_factor"] * skill_rating
    return skill_weight + height_weight

def calculate_scorer_weight(player: Player) -> float:
    pass

def calculate_assister_weight(player: Player) -> float:
    pass

def calculate_turnover_weight(player: Player) -> float:
    pass

def calculate_stealer_weight(player: Player) -> float:
    steal_rating = player.ratings["steal"] / MAX_RATING
    perimeter_defense_rating = player.ratings["perimeter_defense"] / MAX_RATING
    speed_rating = player.ratings["speed"] / MAX_RATING
    return steal_rating * STEAL_WEIGHTS["steal"] + perimeter_defense_rating * STEAL_WEIGHTS["perimeter_defense"] + speed_rating * STEAL_WEIGHTS["speed"]

def calculate_blocker_weight(player: Player) -> float:
    player_height = height_to_inches(player.height_feet, player.height_inches)
    player_height_factor = normalize_height(player_height)
    block_rating = player.ratings["block"] / MAX_RATING
    interior_defense_rating = player.ratings["interior_defense"] / MAX_RATING
    return block_rating * BLOCK_WEIGHTS["block"] + interior_defense_rating * BLOCK_WEIGHTS["interior_defense"] + player_height_factor * BLOCK_WEIGHTS["height"]

def height_to_inches(height_feet: int, height_inches: int) -> int:
    return height_feet * 12 + height_inches

def normalize_height(height_inches: int) -> float:
    clamped = max(MIN_HEIGHT_INCHES, min(height_inches, MAX_HEIGHT_INCHES))
    return (clamped - MIN_HEIGHT_INCHES) / (MAX_HEIGHT_INCHES - MIN_HEIGHT_INCHES)