import pygame
import pygame.draw
from pygame.constants import *
from settings import *


class Item:
    def __init__(self, surface, pos_x, pos_y, width, height, color):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.draw.rect(surface, color, (pos_x, pos_y, width, height))

    def draw(self):
        pygame.draw.rect(self.surface, self.color, (self.pos_x, self.pos_y, self.width, self.height))

    def move(self, event, walls=None, type = 'all'):
        
        if type == 'box':
            next_x = self.pos_x
            next_y = self.pos_y
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    next_x -= CELL_WIDTH
                if event.key == K_RIGHT:
                    next_x += CELL_WIDTH
                if event.key == K_UP:
                    next_y -= CELL_HEIGHT
                if event.key == K_DOWN:
                    next_y += CELL_HEIGHT

        
            next_item_rect = pygame.Rect(next_x, next_y, self.width, self.height)
        
        
            for wall in walls:
                if next_item_rect.colliderect(wall.rect):
                    self.pos_x = self.pos_x
                    self.pos_y = self.pos_y
                    return
            
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self.rect = self.rect.move(-CELL_WIDTH, 0)
                self.pos_x -= CELL_WIDTH
            if event.key == K_RIGHT:
                self.rect = self.rect.move(CELL_WIDTH, 0)
                self.pos_x += CELL_WIDTH
            if event.key == K_UP:
                self.rect = self.rect.move(0, -CELL_HEIGHT)
                self.pos_y -= CELL_HEIGHT
            if event.key == K_DOWN:
                self.rect = self.rect.move(0, CELL_HEIGHT)
                self.pos_y += CELL_HEIGHT

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)