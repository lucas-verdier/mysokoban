import pygame

from Character import Character
from Hole import Hole
from Box import Box
from Wall import Wall
from settings import *
from WinScreen import WinScreen

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
                    wall = Wall(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (102,205,170))
                    
                    
                    self.wall_list.append(wall)
                elif MAP[col][row] == 'P':
                    self.player = Character(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (102,205,170))
                elif MAP[col][row] == 'H':
                    hole = Hole(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (102,205,170))
                    self.hole_list.append(hole)
                elif MAP[col][row] == 'B':
                    box = Box(self.surface, row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT, (102,205,170))
                    self.box_list.append(box)
                else:
                    pygame.draw.rect(self.surface, (102,205,170),
                                     (row * CELL_WIDTH, col * CELL_HEIGHT, CELL_WIDTH, CELL_HEIGHT))

    def update(self, event):
 
        score = 0
        

        for box in self.box_list:
            self.player.move_player(event, self.wall_list, box)

            for hole in self.hole_list:
                # print(box.rect, hole.rect)
                if pygame.Rect.colliderect(box.rect, hole.rect):
           
                    score += 1
                    break
                    
            if pygame.Rect.colliderect(self.player.rect, box.rect):
                box.move(event, self.wall_list, 'box')
                box.draw()

        self.player.draw()


        if len(self.hole_list) == score:
   
            victory_window = WinScreen()
            victory_window.run()
            self.player = None
            self.hole_list: list = []
            self.box_list: list = []
            self.wall_list: list = []
            self.create_map()
  
            

    def draw(self):
        for wall in self.wall_list:
            wall.draw()

        for hole in self.hole_list:
            hole.draw()

        for box in self.box_list:
            box.draw()

        self.player.draw()
        
        
        

