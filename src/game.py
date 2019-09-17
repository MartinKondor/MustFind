"""
Classes and functions for loading and saving games.
"""
import os

import pygame

from config import CONFIG
from consts import BG_COLOR_2, SAVE_FOLDER
from gui import List, Button, ButtonState


class LoadGameWindow:
    """
    Loads an in game window for handling saved games
    """

    def __init__(self, x_pos=CONFIG.WINDOW_WIDTH // 2, y_pos=CONFIG.WINDOW_HEIGHT // 2,
                    width=0.5 * CONFIG.WINDOW_WIDTH, height=0.8 * CONFIG.WINDOW_HEIGHT):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.file_list = List(self.x_pos, self.y_pos, [fn for fn in os.listdir(SAVE_FOLDER)])
        self.background = pygame.Surface((self.width, self.height,))
        self.background.fill(BG_COLOR_2)

        common_y = self.y_pos + self.height // 2 - 3 * CONFIG.CHARACTER_SIZE
        self.back_button = Button(self.x_pos + self.width // 4 - 15, common_y, 'BACK')
        self.load_button = Button(self.x_pos + self.width // 4 - self.back_button.width - 15, common_y, 'LOAD')

    def display(self, screen):
        """
        :returns bool: true if the window is still opened, false if it can be closed
        """
        screen.blit(self.background, (self.x_pos - self.width // 2, self.y_pos - self.height // 2,))
        self.load_button.display(screen)
        self.back_button.display(screen)
        self.file_list.display(screen)

        if self.load_button.state == ButtonState.RELEASED:
            print(self.file_list.selected_index)
        elif self.back_button.state == ButtonState.RELEASED:
            return False
        return True
