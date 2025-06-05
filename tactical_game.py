"""Main entry point for the simple tactical battle game."""

from __future__ import annotations

import pygame

from constants import (
    CELL_SIZE,
    COLS_PER_SIDE,
    ROWS,
    HEIGHT,
    MARGIN,
    WIDTH,
    WHITE,
    BLACK,
)
from players import create_players
from enemies import create_enemies


# ----------------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------------

def draw_grid(surface: pygame.Surface) -> None:
    """Draw the battlefield grid."""
    for row in range(ROWS):
        for col in range(COLS_PER_SIDE * 2):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, WHITE, rect, 1)


# ----------------------------------------------------------------------------
# Game loop
# ----------------------------------------------------------------------------

def main() -> None:
    """Initialize pygame and run the main loop."""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tactical Battle")

    players = create_players()
    enemies = create_enemies()
    selected = 0  # index of the active player unit

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                unit = players[selected]
                col, row = unit.position
                if event.key == pygame.K_TAB:
                    selected = (selected + 1) % len(players)
                elif event.key == pygame.K_LEFT and col > 0:
                    col -= 1
                elif event.key == pygame.K_RIGHT and col < COLS_PER_SIDE * 2 - 1:
                    col += 1
                elif event.key == pygame.K_UP and row > 0:
                    row -= 1
                elif event.key == pygame.K_DOWN and row < ROWS - 1:
                    row += 1
                unit.position = (col, row)

        screen.fill(BLACK)
        draw_grid(screen)
        for idx, player in enumerate(players):
            player.draw(screen)
            if idx == selected:
                # highlight the selected unit
                x = player.position[0] * CELL_SIZE + MARGIN
                y = player.position[1] * CELL_SIZE + MARGIN
                rect = pygame.Rect(
                    x,
                    y,
                    CELL_SIZE - MARGIN * 2,
                    CELL_SIZE - MARGIN * 2,
                )
                pygame.draw.rect(screen, WHITE, rect, 2)

        for e in enemies:
            e.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
