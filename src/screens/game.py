"""
Game screen where we show the game.
"""
from enum import Enum

import pygame

import map
from .screen import Screen
from consts import Screens, MAP_FOLDER
from config import CONFIG
from player import Player
from bot import Bot
from gui.button import SimpleButton, ButtonState


class GameSubScreen(Enum):
    START_MENU = 0
    IN_GAME_MENU = 1
    GAME = 2


class GameScreen(Screen):

    def __init__(self):
        self.subscreen = GameSubScreen.START_MENU
        self.map = map.Map(MAP_FOLDER + 'sky.tcm')  # Stores the current map
        self.player = Player()
        self.bot = Bot()
        self.in_game_menu_bg = None

        # In game menu elements
        button_margin = 50
        self.in_game_resume_button = SimpleButton(96, CONFIG.WINDOW_HEIGHT - 96 - 3 * button_margin, 'RESUME')
        self.in_game_save_button = SimpleButton(96, CONFIG.WINDOW_HEIGHT - 96 - 3 * button_margin, 'SAVE')
        self.in_game_exit_button = SimpleButton(96, CONFIG.WINDOW_HEIGHT - 96 - 3 * button_margin, 'EXIT')

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
        if self.in_game_resume_button.state == ButtonState.RELEASED:
            return Screens.GAME

        return Screens.GAME

    def display_game(self, screen):
        for event in pygame.event.get():
            if event.type != pygame.KEYDOWN:
                continue                        
            if event.key == pygame.locals.K_ESCAPE:

                # Save game screenshot as a background
                self.in_game_menu_bg = pygame.Surface(screen.get_size())
                self.subscreen = GameSubScreen.IN_GAME_MENU
                return Screens.GAME

        self.map.draw(screen, self.player, 0, 5)
        self.bot.display(screen)
        self.player.display(screen)
        self.map.draw(screen, self.player, 5, 8)        
        return Screens.GAME

    def display(self, screen):
        if self.subscreen == GameSubScreen.GAME:
            return self.display_game(screen)
        if self.subscreen == GameSubScreen.START_MENU:
            return self.display_start_menu(screen)
        else:
            return self.display_in_game_menu(screen)
        return Screens.GAME
