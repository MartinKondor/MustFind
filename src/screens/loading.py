"""
Temporarly showing the loading screen for the user.
"""
import time

import pygame

from .screen import Screen
from consts import Screens


class LoadingScreen(Screen):

    def __init__(self):
        # self.logo = pygame.image.load()
        pass

    def display(self, screen):



        # time.sleep(0.5)
        return Screens.MAIN_MENU
