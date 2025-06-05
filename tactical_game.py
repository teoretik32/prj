import pygame

from constants import (
    CELL_SIZE,
    COLS_PER_SIDE,
    ROWS,
    HEIGHT,
    MARGIN,
    PLAYER_COLOR,
    ENEMY_COLOR,
    WIDTH,
    WHITE,
    BLACK,
)
from unit import Unit
from players import create_players
from enemies import create_enemies


def draw_grid(surface):
    for row in range(ROWS):
        for col in range(COLS_PER_SIDE * 2):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, WHITE, rect, 1)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tactical Battle")

    players = create_players()
    enemies = create_enemies()

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        draw_grid(screen)
        for p in players:
            p.draw(screen)
        for e in enemies:
            e.draw(screen)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
