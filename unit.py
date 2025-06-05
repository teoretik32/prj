import pygame
from constants import CELL_SIZE, MARGIN

class Unit:
    def __init__(self, name, atk, defense, hp, stamina, position, color,
                 gender=None, age=None, species=None, description=""):
        self.name = name
        self.gender = gender
        self.age = age
        self.species = species
        self.atk = atk
        self.defense = defense
        self.hp = hp
        self.stamina = stamina
        self.position = position  # (col, row)
        self.color = color
        self.description = description

    def draw(self, surface):
        x = self.position[0] * CELL_SIZE + MARGIN
        y = self.position[1] * CELL_SIZE + MARGIN
        rect = pygame.Rect(x, y, CELL_SIZE - MARGIN * 2, CELL_SIZE - MARGIN * 2)
        pygame.draw.rect(surface, self.color, rect)
