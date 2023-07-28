import pygame
from settings import *

class WinScreen:
    def __init__(self):
        pygame.init()
        self.window_width = WINDOW_WIDTH
        self.window_height =  WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        self.font = pygame.font.Font(None, 36)
        self.text_color = (255, 255, 255)
        self.background_color = (0,0,0)
        self.background_image = pygame.image.load('textures/background_win2.png').convert()
        self.message = "Bravo petit guerrier!"
        self.is_open = True
        self.button_rect = pygame.Rect(self.window_width/2-100,  self.window_height/2-100 , 200, 50)
        self.button_color = (255, 128, 0)
        self.button_text = "Nouvelle partie"
        self.button_font = pygame.font.Font(None, 24)
        self.button_text_color = (255, 255, 255)

    def draw_button(self):
        pygame.draw.rect(self.screen, self.button_color, self.button_rect)
        button_text_surface = self.button_font.render(self.button_text, True, self.button_text_color)
        button_text_rect = button_text_surface.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text_surface, button_text_rect)
        
    
    def run(self):
        while self.is_open:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_open = False
                    

            self.screen.fill(self.background_color)
            self.screen.blit(self.background_image, (20, self.window_height/2-300))


            text_surface = self.font.render(self.message, True, self.text_color)
            text_rect = text_surface.get_rect(center=(self.window_width // 2, self.window_height // 2))
            self.screen.blit(text_surface, text_rect)

            
            self.draw_button()


            mouse_pos = pygame.mouse.get_pos()
            if self.button_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]: 
                    self.is_open = False
                    break

            pygame.display.flip()
