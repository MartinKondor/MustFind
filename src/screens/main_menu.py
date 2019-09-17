"""
Main menu screen.
"""
import pygame

from .screen import Screen
from consts import Screens, IMAGE_FOLDER
from config import CONFIG
from gui.button import SimpleButton, Button, ButtonState
from resource_manager import RM


class MainMenuScreen(Screen):

    def __init__(self):
        self.logo = self.logo = pygame.image.load(IMAGE_FOLDER + 'logo.png')
        self.logo_size = self.logo.get_rect().size

        button_margin = 50
        self.new_game_button = SimpleButton(96, CONFIG.WINDOW_HEIGHT - 96 - 3 * button_margin, 'NEW GAME')
        self.load_game_button = SimpleButton(96, CONFIG.WINDOW_HEIGHT - 96 - 2 * button_margin, 'LOAD GAME')
        self.settings_button = SimpleButton(96, CONFIG.WINDOW_HEIGHT - 96 - button_margin, 'SETTINGS')
        self.exit_button = SimpleButton(96, CONFIG.WINDOW_HEIGHT - 96, 'EXIT')

    def display(self, screen):
        self.new_game_button.display(screen)
        self.load_game_button.display(screen)
        self.settings_button.display(screen)
        self.exit_button.display(screen)
        screen.blit(self.logo, (CONFIG.WINDOW_WIDTH - self.logo_size[0], 0))

        # Check buttons
        if self.exit_button.state == ButtonState.RELEASED:
            return Screens.EXIT
        if self.new_game_button.state == ButtonState.RELEASED:
            return Screens.GAME
        if self.load_game_button.state == ButtonState.RELEASED:
            return Screens.LOAD_GAME
        if self.settings_button.state == ButtonState.RELEASED:
            return Screens.SETTINGS

        return Screens.MAIN_MENU
