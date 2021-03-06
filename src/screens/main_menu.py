"""
Main menu screen.
"""
import pygame

from .screen import Screen
from consts import Screens, IMAGE_FOLDER
from config import CONFIG
from gui import Button, ButtonState
from resource_manager import RM
from game_utils import LoadGameWindow


class MainMenuScreen(Screen):

    def __init__(self):
        self.logo = self.logo = pygame.image.load(IMAGE_FOLDER + 'logo.png')
        self.logo_size = self.logo.get_rect().size
        self.show_game_loader = False
        self.game_loader = LoadGameWindow()

        button_margin = 50
        self.new_game_button = Button(96, CONFIG.WINDOW_HEIGHT - 96 - 3 * button_margin, 'NEW GAME')
        self.load_game_button = Button(96, CONFIG.WINDOW_HEIGHT - 96 - 2 * button_margin, 'LOAD GAME')
        self.settings_button = Button(96, CONFIG.WINDOW_HEIGHT - 96 - button_margin, 'SETTINGS')
        self.exit_button = Button(96, CONFIG.WINDOW_HEIGHT - 96, 'EXIT')

    def display(self, screen):
        screen.blit(self.logo, (CONFIG.WINDOW_WIDTH - self.logo_size[0], 0,))
        self.new_game_button.display(screen)
        self.load_game_button.display(screen)
        self.settings_button.display(screen)
        self.exit_button.display(screen)

        if self.show_game_loader:
            self.show_game_loader = self.game_loader.display(screen)
        else:
            if self.game_loader.file_list.selected_index != -1:
                CONFIG.SAVE_GAME = self.game_loader.list[self.game_loader.file_list.selected_index] + '.save'
                self.game_loader.file_list.selected_index = -1  # Unselect the current save file
                return Screens.GAME

        # Check buttons
        if self.exit_button.state == ButtonState.RELEASED:
            return Screens.EXIT
        if self.new_game_button.state == ButtonState.RELEASED:
            return Screens.GAME
        if self.load_game_button.state == ButtonState.RELEASED:
            self.show_game_loader = True
            return Screens.MAIN_MENU
        if self.settings_button.state == ButtonState.RELEASED:
            return Screens.SETTINGS

        return Screens.MAIN_MENU
