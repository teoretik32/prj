"""Factory for the default enemy troops."""

from unit import Unit
from constants import ENEMY_COLOR, COLS_PER_SIDE


def create_enemies() -> list[Unit]:
    """Return a list with enemy units."""
    return [
        Unit(
            name="Goblin Scout",
            species="Goblin",
            age=20,
            atk=12,
            defense=5,
            hp=35,
            stamina=10,
            position=(COLS_PER_SIDE + 3, 1),
            color=ENEMY_COLOR,
            description="A sneaky goblin on patrol",
        ),
    ]
