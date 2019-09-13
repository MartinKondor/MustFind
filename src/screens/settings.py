"""
Settings screen, where the settings
can be checked and changed.
"""
from .screen import Screen
from consts import Screens


class SettingsScreen(Screen):

    def __init__(self):
        pass

    def display(self, screen):
        return Screens.SETTINGS
