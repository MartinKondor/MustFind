"""
Temporarly showing the loading screen for the user.
"""
import time

from .screen import Screen
from consts import Screens


class LoadingScreen(Screen):

    def __init__(self):
        pass

    def display(self, screen):
        print('Loading')
        time.sleep(0.5)
        return Screens.MAIN_MENU
