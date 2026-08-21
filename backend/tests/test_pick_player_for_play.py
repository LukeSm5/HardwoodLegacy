import pytest

from backend.app.models.player import Player
from backend.simulation.play_generator import pick_player_for_play

def create_base_roster(loop: int = 15) -> list[Player]:
    roster = []
    for i in range(loop):
        player = make_test_player(id = f"p{i+1}")
        roster.append(player)
    return roster

def make_test_player(id="p1", **rating_overrides):
    default_ratings = {
        "3pt": 60, "inside_scoring": 60, "mid_range": 60,
        "driving_dunk": 60, "standing_dunk": 60,
        "passing": 60, "pass_iq": 60, "dribbling": 60,
        "steal": 60, "speed": 60, "perimeter_defense": 60,
        "block": 60, "interior_defense": 60,
        "offensive_rebound": 60, "defensive_rebound": 60,
    }
    default_ratings.update(rating_overrides)
    return Player(id=id, name="Test Player", team_id="t1", position="G",
                   height_feet=6, height_inches=6, weight=190, year="Jr",
                   archetype="test", ratings=default_ratings)

def test_shooter():
    roster = create_base_roster()
    result = pick_player_for_play(roster, "shooter", "3pt")
    assert result in roster

def test_rebounder():
    roster = create_base_roster()
    result = pick_player_for_play(roster, "rebounder", "offensive")
    assert result in roster

def test_assister():
    roster = create_base_roster()
    result = pick_player_for_play(roster, "assister")
    assert result in roster

def test_turnover_recipient():
    roster = create_base_roster()
    result = pick_player_for_play(roster, "turnover_recipient")
    assert result in roster

def test_stealer():
    roster = create_base_roster()
    result = pick_player_for_play(roster, "stealer")
    assert result in roster

def test_blocker():
    roster = create_base_roster()
    result = pick_player_for_play(roster, "blocker")
    assert result in roster

def test_fouler():
    roster = create_base_roster()
    result = pick_player_for_play(roster, "fouler")
    assert result in roster

def test_invalid():
    roster = create_base_roster()
    with pytest.raises(ValueError):
        pick_player_for_play(roster, "fake_role")

def test_pick_player_for_play_favors_higher_weighted_player():
    strong_shooter = make_test_player(id="strong", **{"3pt": 95})
    weak_shooter = make_test_player(id="weak", **{"3pt": 20})
    roster = [strong_shooter, weak_shooter]

    results = [pick_player_for_play(roster, "shooter", "3pt") for _ in range(2000)]
    strong_count = sum(1 for p in results if p.id == "strong")
    weak_count = sum(1 for p in results if p.id == "weak")

    assert strong_count > weak_count