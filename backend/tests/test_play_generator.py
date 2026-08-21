import pytest
from collections import Counter
from backend.app.models.state import GameState
from backend.simulation.play_generator import generate_play
from backend.simulation.play_constants import POSSESSION_OUTCOMES

def make_test_player():
    pass

def make_test_team():
    pass

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

def test_generate_play_distribution():
    state = make_base_state()
    num_trials = 10000
    results = [generate_play(state) for _ in range(num_trials)]
    counts = Counter(results)
    for outcome, expected_probability in POSSESSION_OUTCOMES.items():
        expected_count = expected_probability * num_trials
        actual_count = counts[outcome]
        tolerance = expected_count * 0.10   # allow 10% deviation

        assert abs(actual_count - expected_count) <= tolerance, (
            f"{outcome}: expected ~{expected_count}, got {actual_count}"
        )