import pygame.draw
import pygame
from pygame.constants import *
from Item import Item
from settings import *


class Character(Item):
    last_move_x = 0
    last_move_y = 0

    def __init__(self, surface, pos_x, pos_y, width, height, color):
        super().__init__(surface, pos_x, pos_y, width, height, color)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = pygame.draw.rect(self.surface, self.color, (self.pos_x, self.pos_y, self.width, self.height))
        self.image = pygame.transform.scale(pygame.image.load('textures/link_f0.png'),
                                            (self.width, self.height))

    def set_image(self, direction):
        if direction == 'face':
            self.image = pygame.transform.scale(pygame.image.load('textures/link_f0.png'),
                                                (self.width, self.height))
        elif direction == 'left':
            self.image = pygame.transform.scale(pygame.image.load('textures/link_l0.png'),
                                                (self.width, self.height))
        elif direction == 'right':
            self.image = pygame.transform.scale(pygame.image.load('textures/link_r0.png'),
                                                (self.width, self.height))
        elif direction == 'back':
            self.image = pygame.transform.scale(pygame.image.load('textures/link_b0.png'),
                                                (self.width, self.height))

    def get_image(self):
        return self.image


    def move_player(self, event, walls, box):
        next_x = self.pos_x 
        next_y = self.pos_y
        print('box pos', box.pos_x, box.pos_y)
        print('player pos', self.pos_x, self.pos_y)

        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                next_x -= CELL_WIDTH
            if event.key == K_RIGHT:
                next_x += CELL_WIDTH
            if event.key == K_UP:
                next_y -= CELL_HEIGHT
            if event.key == K_DOWN:
                next_y += CELL_HEIGHT
                

        next_player_rect = pygame.Rect(next_x, next_y, self.width, self.height)
        

        for wall in walls:
            # # if box.rect.colliderect(wall.rect):
            # if next_player_rect.colliderect(box.rect):
            #     print('box collision')
            #     return
        
            if next_player_rect.colliderect(wall.rect):
                return
        

            


        if event.type == KEYDOWN:
            self.last_move_x = self.pos_x
            self.last_move_y = self.pos_y
            if event.key == K_LEFT:
                self.rect = self.rect.move(-CELL_WIDTH, 0)
                self.pos_x -= CELL_WIDTH
                self.set_image('left')
            if event.key == K_RIGHT:
                self.rect = self.rect.move(CELL_WIDTH, 0)
                self.pos_x += CELL_WIDTH
                self.set_image('right')
            if event.key == K_UP:
                self.rect = self.rect.move(0, -CELL_HEIGHT)
                self.pos_y -= CELL_HEIGHT
                self.set_image('back')
            if event.key == K_DOWN:
                self.rect = self.rect.move(0, CELL_HEIGHT)
                self.pos_y += CELL_HEIGHT
                self.set_image('face')
                

    def previous_pos(self):
        self.pos_x = self.last_move_x
        self.pos_y = self.last_move_y

    def draw(self):
        pygame.draw.rect(self.surface,self.color, self.rect)
        self.surface.blit(self.get_image(), self.rect)
        