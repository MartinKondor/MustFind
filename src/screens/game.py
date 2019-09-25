"""
Game screen where we show the game.
"""
from threading import Thread
from enum import Enum

import pygame

from map import Map
from .screen import Screen
from consts import Screens, MAP_FOLDER, IMAGE_FOLDER
from config import CONFIG
from player import Player
from bot import Bot
from gui import Button, ButtonState
from game_utils import save_game, load_save_game


class GameSubScreen(Enum):
    START_MENU = 0
    IN_GAME_MENU = 1
    GAME = 2


class GameScreen(Screen):

    def __init__(self):
        self.subscreen = GameSubScreen.START_MENU
        self.map = Map(MAP_FOLDER + CONFIG.CURRENT_LEVEL + '.tcm')  # Stores the current map
        self.player = Player(len(self.map.layers[4].tiles[0]), 32)
        self.bot = Bot(len(self.map.layers[4].tiles[0]) + 32, 32)
        self.in_game_menu_bg = None

        # In game menu elements
        button_margin = 50
        self.in_game_resume_button = Button(96, CONFIG.WINDOW_HEIGHT - 96 - 3 * button_margin, label='RESUME')
        self.in_game_save_button = Button(96, CONFIG.WINDOW_HEIGHT - 96 - 2 * button_margin, label='SAVE GAME')
        self.in_game_exit_button = Button(96, CONFIG.WINDOW_HEIGHT - 96 - button_margin, label='EXIT')

        if CONFIG.SAVE_GAME != '':
            load_save_game(self)
            CONFIG.SAVE_GAME = ''

    def display_start_menu(self, screen):
        self.subscreen = GameSubScreen.GAME
        return Screens.GAME

    def display_in_game_menu(self, screen):
        screen.blit(self.in_game_menu_bg, (0, 0))
        self.in_game_resume_button.display(screen)
        self.in_game_save_button.display(screen)
        self.in_game_exit_button.display(screen)

        if self.in_game_exit_button.state == ButtonState.RELEASED:
            return Screens.MAIN_MENU
        elif self.in_game_resume_button.state == ButtonState.RELEASED:
            self.subscreen = GameSubScreen.GAME
            return Screens.GAME
        elif self.in_game_save_button.state == ButtonState.RELEASED:
            save_game(self)
            return Screens.GAME
        return Screens.GAME

    def display_game(self, screen):
        self.map.draw(screen, self.player, 0, 5)
        self.bot.display(screen, self.map, self.player)
        self.player.display(screen, self.map)
        self.map.draw(screen, self.player, 5, 8)

        if pygame.key.get_pressed()[pygame.locals.K_ESCAPE]:

            # Save game screenshot as a background
            pygame.image.save(screen, IMAGE_FOLDER + 'screenshot.png')
            self.in_game_menu_bg = pygame.image.load(IMAGE_FOLDER + 'screenshot.png')
            self.in_game_menu_bg.set_alpha(150)

            self.subscreen = GameSubScreen.IN_GAME_MENU
            return Screens.GAME
        return Screens.GAME

    def display(self, screen):
        if self.subscreen == GameSubScreen.GAME:
            return self.display_game(screen)
        elif self.subscreen == GameSubScreen.START_MENU:
            return self.display_start_menu(screen)
        else:
            return self.display_in_game_menu(screen)
        return Screens.GAME
