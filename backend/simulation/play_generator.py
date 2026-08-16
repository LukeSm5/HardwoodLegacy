import random

from backend.app.models.player import Player
from backend.app.models.result import PlayResult
from backend.app.models.state import GameState
from backend.simulation.play_constants import ( 
    POSSESSION_OUTCOMES,
    ASSIST_PROBABILITY, 
    REBOUND_WEIGHTS, 
    TIME_RANGES_BY_OUTCOME, 
    TURNOVER_TYPES, 
    FOUL_TYPES, 
    BONUS_THRESHOLD, 
    DOUBLE_BONUS_THRESHOLD,
    TWO_POINT_SHOTS,
    REBOUNDING_CHANCE,
    FOUL_WEIGHTS)
from backend.simulation.play_weights import (
    calculate_rebound_weight,
    calculate_assister_weight,
    calculate_blocker_weight,
    calculate_scorer_weight,
    calculate_stealer_weight,
    calculate_turnover_weight,
    calculate_fouler_weight,
    evaluate_three_point_make_probability,
    evaluate_two_point_make_probability,
    roll_shot_outcome,
    roll_assist_outcome
)

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

def generate_play(game_state: GameState) -> str:
    outcomes = list(POSSESSION_OUTCOMES.keys())
    weights = list(POSSESSION_OUTCOMES.values())
    return random.choices(outcomes, weights=weights, k=1)[0]

def pick_player_for_play(roster: list[Player], role: str, sub_type: str = None) -> Player:
    if role == "shooter":
        weights = [calculate_scorer_weight(player, sub_type) for player in roster]
    elif role == "rebounder":
        weights = [calculate_rebound_weight(player, sub_type) for player in roster]
    elif role == "assister":
        weights = [calculate_assister_weight(player) for player in roster]
    elif role == "turnover_recipient":
        weights = [calculate_turnover_weight(player) for player in roster]
    elif role == "stealer":
        weights = [calculate_stealer_weight(player) for player in roster]
    elif role == "blocker":
        weights = [calculate_blocker_weight(player) for player in roster]
    elif role == "fouler":
        weights = [calculate_fouler_weight(player, sub_type) for player in roster]
    else:
        raise ValueError(f"Unknown role: {role}")
    return random.choices(roster, weights=weights, k=1)[0]

def determine_rebound_type() -> str:
    types = list(REBOUNDING_CHANCE.keys())
    weights = list(REBOUNDING_CHANCE.values())
    return random.choices(types, weights=weights, k=1)[0]

def determine_foul_type() -> str:
    types = list(FOUL_WEIGHTS.keys())
    weights = list(FOUL_WEIGHTS.values())
    return random.choices(types, weights=weights, k=1)[0]

def determine_two_point_shot_type() -> str:
    types = list(TWO_POINT_SHOTS.keys())
    weights = list(TWO_POINT_SHOTS.values())
    return random.choices(types, weights=weights, k=1)[0]

def resolve_outcome(outcome: str, game_state: GameState, offense: list[Player], defense: list[Player]) -> PlayResult:
    defending_team = "away" if game_state.possession_team == "home" else "home"
    rebounder = None
    if outcome == "2pt":
        shooter = pick_player_for_play(offense, "shooter")
        two_point_shot = determine_two_point_shot_type()
        make_chance = evaluate_two_point_make_probability(shooter, two_point_shot)
        made = roll_shot_outcome(make_chance)
        if made:
            points_scored = 2
            next_possession_team = defending_team
            if assist:
                assister = pick_player_for_play(offense, "assister")
        else:
            points_scored = 0
            rebounding_type = determine_rebound_type()
            if rebounding_type == "offensive":
                rebounder = pick_player_for_play(offense, "rebounder", rebounding_type)
                next_possession_team = game_state.possession_team
            else:
                rebounder = pick_player_for_play(defense, "rebounder", rebounding_type)
                next_possession_team = defending_team
        time_consumed = consume_time("2pt")
        if rebounder:
            return PlayResult("2pt", points_scored, time_consumed, {"shooter": shooter.id, "rebounder": rebounder.id}, next_possession_team)
        elif assister:
            return PlayResult("2pt", points_scored, time_consumed, {"shooter": shooter.id, "assister": assister.id}, next_possession_team)
        else:
            return PlayResult("2pt", points_scored, time_consumed, {"shooter": shooter.id}, next_possession_team)

    elif outcome == "3pt":
        shooter = pick_player_for_play(offense, "shooter")
        make_chance = evaluate_three_point_make_probability(shooter)
        made = roll_shot_outcome(make_chance)
        if made:
            points_scored = 3
            next_possession_team = defending_team
            assist = roll_assist_outcome()
            if assist:
                assister = pick_player_for_play(offense, "assister")
        else:
            points_scored = 0
            rebounding_type = determine_rebound_type()
            if rebounding_type == "offensive":
                rebounder = pick_player_for_play(offense, "rebounder", rebounding_type)
                next_possession_team = game_state.possession_team
            else:
                rebounder = pick_player_for_play(defense, "rebounder", rebounding_type)
                next_possession_team = defending_team
        time_consumed = consume_time("3pt")
        if rebounder:
            return PlayResult("3pt", points_scored, time_consumed, {"shooter": shooter.id, "rebounder": rebounder.id}, next_possession_team)
        elif assister:
            return PlayResult("3pt", points_scored, time_consumed, {"shooter": shooter.id, "assister": assister.id}, next_possession_team)
        else:
            return PlayResult("3pt", points_scored, time_consumed, {"shooter": shooter.id}, next_possession_team)
            
    elif outcome == "foul":
        foul_type = determine_foul_type()
        if foul_type == "offensive":
            fouler = pick_player_for_play(offense, "fouler", "offensive")
            next_possession_team = defending_team
        else:
            fouler = pick_player_for_play(defense, "fouler", "defensive")
            next_possession_team = game_state.possession_team
        time_consumed = consume_time("foul")
        return PlayResult("foul", 0, time_consumed, {"fouler": fouler.id}, next_possession_team)
    elif outcome == "turnover":
        turnover_recipient = pick_player_for_play(offense, "turnover_recipient")
        time_consumed = consume_time("turnover")
        if game_state.possession_team == "home":
            next_possession_team = "away"
        else:
            next_possession_team = "home"
        return PlayResult("turnover", 0, time_consumed, {"turnover_recipient": turnover_recipient.id}, next_possession_team)
        

def consume_time(outcome: str) -> float:
    low, high, mode = TIME_RANGES_BY_OUTCOME.get(outcome, (4, 30, 15))
    return float(random.triangular(low, high, mode))

def update_game_state(game_state: GameState, play_result: PlayResult) -> GameState:
    game_state.time_remaining -= play_result.time_consumed
    if game_state.time_remaining < 0:
        if game_state.half == 1:
            game_state.time_remaining = 1200.0
            game_state.half = 2
        else:
            game_state.time_remaining = 0
    if play_result.points_scored != 0:
        if game_state.possession_team == "home":
            game_state.home_score += play_result.points_scored
        else:
            game_state.away_score += play_result.points_scored
    if play_result.outcome in ["foul"]:
        fouling_player_id = play_result.player_involved["fouler"]
        game_state.player_fouls[fouling_player_id] += 1
        if play_result.next_possession_team == game_state.possession_team:
            opposing_team = "away" if game_state.possession_team == "home" else "home"
            game_state.team_fouls[opposing_team] += 1
    game_state.possession_team = play_result.next_possession_team
    return game_state

def simulate_possession(game_state: GameState, offense: list[Player], defense: list[Player]) -> PlayResult:
    play = generate_play(game_state)
    result = resolve_outcome(play, game_state, offense, defense)
    game_state = update_game_state(game_state, result)
    return result