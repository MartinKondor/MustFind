from .screen import Screen
from consts import *
from config import CONFIG
from button import Button, ButtonState


class MainMenuScreen(Screen):

    def __init__(self, gui_font):
        button_margin = 5
        self.singleplayer_button = Button(CONFIG.WINDOW_WIDTH // 2 - 48, 200 + 10, 'SINGLE PLAYER', gui_font)
        self.multiplayer_button = Button(CONFIG.WINDOW_WIDTH / 2 - 48, 232 + button_margin + 10, 'MULTI PLAYER', gui_font)
        self.settings_button = Button(CONFIG.WINDOW_WIDTH / 2 - 48, 264 + 2 * button_margin + 10, 'SETTINGS', gui_font)
        self.exit_button = Button(CONFIG.WINDOW_WIDTH / 2 - 48, 296 + 3 * button_margin + 10, 'EXIT', gui_font)

    def display(self, screen):
        self.singleplayer_button.display(screen)
        self.multiplayer_button.display(screen)
        self.settings_button.display(screen)
        self.exit_button.display(screen)

        if self.exit_button.state == ButtonState.RELEASED:
            return 0
