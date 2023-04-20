import pygame
import pygame.draw
from pygame.constants import *
from settings import *
from Item import Item


class Box(Item):
    def __init__(self, surface, pos_x, pos_y, width, height, color):
        super().__init__(surface, pos_x, pos_y, width, height, color)
        self.rect = pygame.draw.rect(self.surface, self.color, (self.pos_x, self.pos_y, self.width, self.height))
