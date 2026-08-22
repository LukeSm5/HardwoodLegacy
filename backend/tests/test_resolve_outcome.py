import pytest

from backend.simulation.play_generator import resolve_outcome
from backend.tests.test_pick_player_for_play import create_base_roster
from backend.tests.test_update_game_state import make_base_state

def test_2pt_made_no_assist(monkeypatch):
    monkeypatch.setattr("backend.simulation.play_generator.roll_shot_outcome", lambda *a, **k: True)
    monkeypatch.setattr("backend.simulation.play_generator.roll_assist_outcome", lambda *a, **k: False)

    state = make_base_state()
    offense = create_base_roster()
    defense = create_base_roster()

    result = resolve_outcome("2pt", state, offense, defense)

    assert result.outcome == "2pt"
    assert result.points_scored == 2
    assert result.next_possession_team == "away"
    assert "shooter" in result.player_involved
    assert "assister" not in result.player_involved
    assert "rebounder" not in result.player_involved


def test_2pt_made_with_assist(monkeypatch):
    monkeypatch.setattr("backend.simulation.play_generator.roll_shot_outcome", lambda *a, **k: True)
    monkeypatch.setattr("backend.simulation.play_generator.roll_assist_outcome", lambda *a, **k: True)

    state = make_base_state()
    offense = create_base_roster()
    defense = create_base_roster()

    result = resolve_outcome("2pt", state, offense, defense)

    assert result.points_scored == 2
    assert "assister" in result.player_involved


def test_2pt_miss_offensive_rebound(monkeypatch):
    monkeypatch.setattr("backend.simulation.play_generator.roll_shot_outcome", lambda *a, **k: False)
    monkeypatch.setattr("backend.simulation.play_generator.determine_rebound_type", lambda: "offensive")

    state = make_base_state()
    offense = create_base_roster()
    defense = create_base_roster()

    result = resolve_outcome("2pt", state, offense, defense)

    assert result.points_scored == 0
    assert result.next_possession_team == "home"
    assert "rebounder" in result.player_involved


def test_2pt_miss_defensive_rebound(monkeypatch):
    monkeypatch.setattr("backend.simulation.play_generator.roll_shot_outcome", lambda *a, **k: False)
    monkeypatch.setattr("backend.simulation.play_generator.determine_rebound_type", lambda: "defensive")

    state = make_base_state()
    offense = create_base_roster()
    defense = create_base_roster()

    result = resolve_outcome("2pt", state, offense, defense)

    assert result.points_scored == 0
    assert result.next_possession_team == "away"
    assert "rebounder" in result.player_involved

def test_3pt_make_unassisted(monkeypatch):
    pass

def test_3pt_make_assisted(monkeypatch):
    pass

def test_3pt_miss_defensive_rebound(monkeypatch):
    pass

def test_3pt_miss_offensive_rebound(monkeypatch):
    pass

def test_offensive_foul(monkeypatch):
    pass

def test_defensive_foul(monkeypatch):
    pass

def test_turnover(monkeypatch):
    pass