"""
Temporarly showing the loading screen for the user.
"""
import time

import pygame

from .screen import Screen
from consts import Screens, IMAGE_FOLDER
from config import CONFIG


class LoadingScreen(Screen):

    def __init__(self):
        self.time_counter = time.time()
        self.loading_screen_screentime = 0.
        self.logo = pygame.image.load(IMAGE_FOLDER + 'logo.png')
        
        self.pygame_logo = pygame.image.load(IMAGE_FOLDER + 'pygame_logo.gif')
        pygame_logo_size = self.pygame_logo.get_rect().size
        self.pygame_logo = pygame.transform.scale(self.pygame_logo, (pygame_logo_size[0] // 3, pygame_logo_size[1] // 3))

    def display(self, screen):
        logo_size = self.logo.get_size()
        screen.blit(self.logo, (CONFIG.WINDOW_WIDTH // 2 - logo_size[0] // 2, CONFIG.WINDOW_HEIGHT // 2 - logo_size[1]))
        screen.blit(self.pygame_logo, (50, CONFIG.WINDOW_HEIGHT - 100))

        if time.time() - self.time_counter >= self.loading_screen_screentime:
            return Screens.MAIN_MENU
        return Screens.LOADING
