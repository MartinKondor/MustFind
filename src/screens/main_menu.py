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

        button_margin = 15
        self.singleplayer_button = SimpleButton(96, 200, 'SINGLE PLAYER')
        self.multiplayer_button = SimpleButton(96, 232 + button_margin, 'MULTI PLAYER')
        self.settings_button = SimpleButton(96, 264 + 2 * button_margin, 'SETTINGS')
        self.exit_button = SimpleButton(96, 296 + 3 * button_margin, 'EXIT')

    def display(self, screen):
        self.singleplayer_button.display(screen)
        self.multiplayer_button.display(screen)
        self.settings_button.display(screen)
        self.exit_button.display(screen)
        screen.blit(self.logo, (CONFIG.WINDOW_WIDTH - self.logo_size[0], 0))

        # Check buttons
        if self.exit_button.state == ButtonState.RELEASED:
            return Screens.EXIT
        if self.singleplayer_button.state == ButtonState.RELEASED:
            return Screens.GAME
        if self.multiplayer_button.state == ButtonState.RELEASED:
            return Screens.MULTIPLAYER_GAME
        if self.settings_button.state == ButtonState.RELEASED:
            return Screens.SETTINGS

        return Screens.MAIN_MENU
