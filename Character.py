from pygame.constants import *
from settings import *
from Item import Item


class Character(Item):
    def __init__(self, surface, pos_x, pos_y, width, height, color):
        super().__init__(surface, pos_x, pos_y, width, height, color)

    def move(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.pos_x -= CELL_WIDTH
            if event.key == K_RIGHT:
                self.pos_x += CELL_WIDTH
            if event.key == K_UP:
                self.pos_y -= CELL_HEIGHT
            if event.key == K_DOWN:
                self.pos_y += CELL_HEIGHT
