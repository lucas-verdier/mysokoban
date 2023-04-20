import pygame


class Item:
    def __init__(self, surface, pos_x: int, pos_y: int, width: int, height: int, color):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        pygame.draw.rect(surface, color, (pos_x, pos_y, width, height))
