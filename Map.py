import pygame

from Character import Character
from Hole import Hole
from Box import Box
from Wall import Wall
from settings import *


class Map:
    def __init__(self, surface):
        self.player = None
        self.surface = surface
        self.hole_list: list = []
        self.box_list: list = []
        self.player = Character(self.surface, 0, 0, CELL_WIDTH, CELL_HEIGHT, (0, 255, 0))
        self.create_map()

    def create_map(self):
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                if MAP[row][col] == 'x':
                    Wall(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (155, 155, 155))
                elif MAP[row][col] == 'P':
                    self.player = Character(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (0, 255, 0))
                elif MAP[row][col] == 'H':
                    hole = Hole(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (0, 0, 0))
                    self.hole_list.append(hole)
                elif MAP[row][col] == 'B':
                    box = Box(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (164, 116, 20))
                    self.box_list.append(box)
                else:
                    pygame.draw.rect(self.surface, (255, 255, 255),
                                     (row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

    def update(self, event):
        self.player.move(event)
        for box in self.box_list:
            if pygame.Rect.colliderect(self.player.rect, box.rect):
                box.move(event)
                box.draw()
        self.player.draw()

