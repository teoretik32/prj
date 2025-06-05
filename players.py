"""Predefined heroes for the tactical battle."""

from unit import Unit
from constants import PLAYER_COLOR


def create_players() -> list[Unit]:
    """Create three default player units."""
    return [
        Unit(
            name="Alena",
            gender="Female",
            age=27,
            atk=10,
            defense=5,
            hp=30,
            stamina=10,
            position=(1, 0),
            color=PLAYER_COLOR,
        ),
        Unit(
            name="Boris",
            gender="Male",
            age=32,
            atk=8,
            defense=6,
            hp=25,
            stamina=10,
            position=(1, 1),
            color=PLAYER_COLOR,
        ),
        Unit(
            name="Chloe",
            gender="Female",
            age=24,
            atk=9,
            defense=4,
            hp=20,
            stamina=10,
            position=(1, 2),
            color=PLAYER_COLOR,
        ),
    ]
