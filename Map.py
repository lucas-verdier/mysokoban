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
        self.wall_list: list = []
        self.player = Character(self.surface, 0, 0, CELL_WIDTH, CELL_HEIGHT, (0, 255, 0))
        self.create_map()

    def create_map(self):
        for row in range(MAP_HEIGHT):
            for col in range(MAP_WIDTH):
                if MAP[col][row] == 'x':
                    wall = Wall(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (155, 155, 155))
                    self.wall_list.append(wall)
                elif MAP[col][row] == 'P':
                    self.player = Character(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (255, 255, 255))
                elif MAP[col][row] == 'H':
                    hole = Hole(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (255, 255, 255))
                    self.hole_list.append(hole)
                elif MAP[col][row] == 'B':
                    box = Box(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (255, 255, 255))
                    self.box_list.append(box)
                else:
                    pygame.draw.rect(self.surface, (255, 255, 255),
                                     (row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

    def update(self, event):
        # print(len(self.hole_list))
        self.player.move_player(event)
        print(self.player.last_move_x)
        pygame.draw.rect(self.surface, (255, 255, 255), (self.player.last_move_x, self.player.last_move_y, CELL_WIDTH, CELL_HEIGHT))
        for wall in self.wall_list:
            if pygame.Rect.colliderect(self.player.rect, wall.rect):
                self.player.previous_pos()

        for box in self.box_list:
            for hole in self.hole_list:
                if pygame.Rect.colliderect(box.rect, hole.rect):
                    self.hole_list.remove(hole)
            if pygame.Rect.colliderect(self.player.rect, box.rect):
                box.move(event)
                box.draw_box()

        self.player.draw_player()

        if len(self.hole_list) <= 0:
            print('YOU WIN!!')
