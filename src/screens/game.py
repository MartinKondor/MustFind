"""
Game screen where we show the game.
"""
from enum import Enum

from .screen import Screen
from consts import Screens


class SubGameScreen(Enum):
    START_MENU = 0
    IN_GAME_MENU = 1


class GameScreen(Screen):

    def __init__(self):
        self.subscreen = SubGameScreen.START_MENU

    def display(self, screen):
        return Screens.GAME
