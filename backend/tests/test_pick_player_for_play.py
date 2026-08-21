import pytest

from backend.app.models.player import Player
from backend.simulation.play_generator import pick_player_for_play

def create_base_roster(loop: int = 15) -> list[Player]:
    roster = []
    for i in range(loop):
        player = make_base_player(id = f"p{i+1}")
        roster.append(player)
    return roster

def make_base_player(player_id: str) -> Player:
    pass

def test_shooter():
    roster = create_base_roster()

def test_rebounder():
    roster = create_base_roster()

def test_assister():
    roster = create_base_roster()

def test_turnover_recipient():
    roster = create_base_roster()

def test_stealer():
    roster = create_base_roster()

def test_blocker():
    roster = create_base_roster()

def test_fouler():
    roster = create_base_roster()

def test_invalid():
    roster = create_base_roster()
    with pytest.raises(ValueError):
        pick_player_for_play(roster, "fake_role")