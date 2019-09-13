"""
Main menu screen.
"""
from .screen import Screen
from consts import Screens
from config import CONFIG
from button import Button, ButtonState
from resource_manager import RM


class MainMenuScreen(Screen):

    def __init__(self):
        button_margin = 5
        self.singleplayer_button = Button(CONFIG.WINDOW_WIDTH // 2 - 48, 200 + 10, 'SINGLE PLAYER', RM.gui_font)
        self.multiplayer_button = Button(CONFIG.WINDOW_WIDTH / 2 - 48, 232 + button_margin + 10, 'MULTI PLAYER', RM.gui_font)
        self.settings_button = Button(CONFIG.WINDOW_WIDTH / 2 - 48, 264 + 2 * button_margin + 10, 'SETTINGS', RM.gui_font)
        self.exit_button = Button(CONFIG.WINDOW_WIDTH / 2 - 48, 296 + 3 * button_margin + 10, 'EXIT', RM.gui_font)

    def display(self, screen):
        self.singleplayer_button.display(screen)
        self.multiplayer_button.display(screen)
        self.settings_button.display(screen)
        self.exit_button.display(screen)

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
