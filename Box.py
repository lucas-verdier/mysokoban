import os

import pygame
import pygame.draw
from Item import Item


class Box(Item):
    def __init__(self, surface, pos_x, pos_y, width, height, color):
        super().__init__(surface, pos_x, pos_y, width, height, color)
        self.rect = pygame.draw.rect(self.surface, self.color, (self.pos_x, self.pos_y, self.width, self.height))
        self.image = pygame.transform.scale(pygame.image.load('textures/box3.png'), (self.width, self.height))
        self.surface.blit(self.image, self.rect)


    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
        self.surface.blit(self.image, self.rect)
        