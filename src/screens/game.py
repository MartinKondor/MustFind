"""
Game screen where we show the game.
"""
from enum import Enum

import pygame

import map
from .screen import Screen
from consts import Screens, MAP_FOLDER


class GameSubScreen(Enum):
    START_MENU = 0
    IN_GAME_MENU = 1
    GAME = 2


class GameScreen(Screen):

    def __init__(self):
        self.subscreen = GameSubScreen.START_MENU
        self.map = None  # Stores the current map
        self.player = None

        # Test
        self.map = map.Map(MAP_FOLDER + 'sky.tcm')

    def display_start_menu(self, screen):
        self.subscreen = GameSubScreen.GAME
        return Screens.GAME

    def display_in_game_menu(self, screen):
        return Screens.MAIN_MENU

    def display_game(self, screen):
        for event in pygame.event.get():
            if event.type != pygame.KEYDOWN:
                continue                        
            if event.key == pygame.locals.K_ESCAPE:
                self.subscreen = GameSubScreen.IN_GAME_MENU
                break

        self.map.draw_background(screen, self.player)
        # TODO: Draw entities
        self.map.draw_foreground(screen, self.player)
        return Screens.GAME

    def display(self, screen):
        if self.subscreen == GameSubScreen.GAME:
            return self.display_game(screen)
        if self.subscreen == GameSubScreen.START_MENU:
            return self.display_start_menu(screen)
        else:
            return self.display_in_game_menu(screen)
        return Screens.GAME
