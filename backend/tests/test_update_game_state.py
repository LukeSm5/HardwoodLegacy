import pytest
from backend.simulation.play_generator import (
    GameState, 
    PlayResult, 
    update_game_state)

def make_base_state():
    return GameState(
        home_score=0,
        away_score=0,
        team_fouls={"home": 0, "away": 0},
        player_fouls={"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0},
        possession_team="home",
        time_remaining=1200.0,
        half=1,
    )

def test_2pt_make():
    state = make_base_state()
    result = PlayResult(
        outcome = "2pt",
        points_scored = 2,
        time_consumed = 16,
        player_involved = {
            "scorer" : "p1"
        },
        next_possession_team="away"
    )
    state = update_game_state(state, result)
    assert state.home_score == 2
    assert state.possession_team == "away"
    assert state.time_remaining == 1184
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 0}

def test_2pt_miss_oboard():
    state = make_base_state()
    result = PlayResult(
            outcome = "2pt",
            points_scored = 0,
            time_consumed = 18,
            player_involved = {
                "shooter": "p1",
                "rebounder" : "p2"
            },
            next_possession_team="home"
        )
    state = update_game_state(state, result)
    assert state.home_score == 0
    assert state.possession_team == "home"
    assert state.time_remaining == 1182
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 0}

def test_3pt_make():
    state = make_base_state()
    result = PlayResult(
            outcome = "3pt",
            points_scored = 3,
            time_consumed = 20,
            player_involved = {
                "shooter": "p1",
            },
            next_possession_team="away"
        )
    state = update_game_state(state, result)
    assert state.home_score == 3
    assert state.possession_team == "away"
    assert state.time_remaining == 1180
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 0}

def test_3pt_miss_oboard():
    state = make_base_state()
    result = PlayResult(
                outcome = "3pt",
                points_scored = 0,
                time_consumed = 18,
                player_involved = {
                    "shooter": "p1",
                    "rebounder" : "p2"
                },
                next_possession_team="home"
            )
    state = update_game_state(state, result)
    assert state.home_score == 0
    assert state.possession_team == "home"
    assert state.time_remaining == 1182
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 0}

def test_3pt_miss():
    state = make_base_state()
    result = PlayResult(
        outcome = "3pt",
        points_scored = 0,
        time_consumed = 18,
        player_involved = {
            "shooter": "p1",
            "rebounder" : "p2"
        },
        next_possession_team="away"
    )
    state = update_game_state(state, result)
    assert state.home_score == 0
    assert state.possession_team == "away"
    assert state.time_remaining == 1182
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 0}

def test_turnover():
    state = make_base_state()
    result = PlayResult(
            outcome = "turnover",
            points_scored = 0,
            time_consumed = 18,
            player_involved = {
                "shooter": "p1",
                "rebounder" : "p2"
            },
            next_possession_team="away"
        )
    state = update_game_state(state, result)
    assert state.home_score == 0
    assert state.possession_team == "away"
    assert state.time_remaining == 1182
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 0, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 0}

def test_offensive_foul():
    state = make_base_state()
    result = PlayResult(
            outcome = "foul",
            points_scored = 0,
            time_consumed = 18,
            player_involved = {
                "foul": "p1",
            },
            next_possession_team="away"
        )
    state = update_game_state(state, result)
    assert state.home_score == 0
    assert state.possession_team == "away"
    assert state.time_remaining == 1182
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 1, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 0}

def test_defensive_foul():
    state = make_base_state()
    result = PlayResult(
            outcome = "foul",
            points_scored = 0,
            time_consumed = 18,
            player_involved = {
                "foul": "p1",
            },
            next_possession_team="home"
        )
    state = update_game_state(state, result)
    assert state.home_score == 0
    assert state.possession_team == "home"
    assert state.time_remaining == 1182
    assert state.away_score == 0
    assert state.player_fouls == {"p1": 1, "p2": 0, "p3": 0, "p4": 0, "p5": 0}
    assert state.team_fouls == {"home": 0, "away": 1}

def test_end_of_half():
    state = make_base_state()
    state.time_remaining = 29
    result = PlayResult(
        outcome = "2pt",
        points_scored = 0,
        time_consumed = 30,
        player_involved = {
            "shooter": "p1",
        },
        next_possession_team="home"
    )
    state = update_game_state(state, result)
    assert state.time_remaining == 1200.0
    assert state.half == 2

def test_end_of_game():
    state = make_base_state()
    state.time_remaining = 29
    state.half = 2
    result = PlayResult(
        outcome = "2pt",
        points_scored = 0,
        time_consumed = 30,
        player_involved = {
            "shooter": "p1",
        },
        next_possession_team="home"
    )
    state = update_game_state(state, result)
    assert state.time_remaining == 0
    assert state.half == 2