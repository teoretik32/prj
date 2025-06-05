"""Basic unit implementation used by both players and enemies."""

from dataclasses import dataclass
from typing import Optional, Tuple

import pygame

from constants import CELL_SIZE, MARGIN


@dataclass
class Unit:
    """A single unit on the battlefield."""

    name: str
    atk: int
    defense: int
    hp: int
    stamina: int
    position: Tuple[int, int]
    color: Tuple[int, int, int]
    gender: Optional[str] = None
    age: Optional[int] = None
    species: Optional[str] = None
    description: str = ""

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the unit as a filled rectangle."""
        x = self.position[0] * CELL_SIZE + MARGIN
        y = self.position[1] * CELL_SIZE + MARGIN
        rect = pygame.Rect(
            x,
            y,
            CELL_SIZE - MARGIN * 2,
            CELL_SIZE - MARGIN * 2,
        )
        pygame.draw.rect(surface, self.color, rect)
