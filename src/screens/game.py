"""
Game screen where we show the game.
"""
from enum import Enum

import map
from .screen import Screen
from consts import Screens, MAP_FOLDER


class SubGameScreen(Enum):
    START_MENU = 0
    IN_GAME_MENU = 1
    GAME = 2


class GameScreen(Screen):

    def __init__(self):
        self.subscreen = SubGameScreen.START_MENU
        self.map = None  # Stores the current map

        # Test
        self.map = map.Map(MAP_FOLDER + 'sky.tcm')

    def display_start_menu(self, screen):
        return Screens.GAME

    def display_in_game_menu(self, screen):
        self.subscreen = SubGameScreen.GAME
        return Screens.GAME

    def display_game(self, screen):

        

        return Screens.GAME

    def display(self, screen):
        if self.subscreen == SubGameScreen.GAME:
            return self.display_game(screen)
        if self.subscreen == SubGameScreen.START_MENU:
            return self.display_start_menu(screen)
        else:
            return self.display_in_game_menu(screen)
        return Screens.GAME
