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

# Constants
CELL_SIZE = 64
ROWS = 3
COLS_PER_SIDE = 5
MARGIN = 2
WIDTH = CELL_SIZE * COLS_PER_SIDE * 2
HEIGHT = CELL_SIZE * ROWS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
ENEMY_COLOR = (255, 0, 0)

class Unit:
    def __init__(self, name, atk, defense, hp, stamina, position, color):
        self.name = name
        self.atk = atk
        self.defense = defense
        self.hp = hp
        self.stamina = stamina
        self.position = position  # (col, row)
        self.color = color

    def draw(self, surface):
        x = self.position[0] * CELL_SIZE + MARGIN
        y = self.position[1] * CELL_SIZE + MARGIN
        rect = pygame.Rect(x, y, CELL_SIZE - MARGIN * 2, CELL_SIZE - MARGIN * 2)
        pygame.draw.rect(surface, self.color, rect)



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

    players = [
        Unit("Hero1", 10, 5, 30, 10, (1, 0), PLAYER_COLOR),
        Unit("Hero2", 8, 6, 25, 10, (1, 1), PLAYER_COLOR),
        Unit("Hero3", 9, 4, 20, 10, (1, 2), PLAYER_COLOR),
    ]
    enemy = Unit("Enemy", 12, 5, 35, 10, (COLS_PER_SIDE + 3, 1), ENEMY_COLOR)


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

        enemy.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
