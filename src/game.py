"""
Classes and functions for loading and saving games.
"""
from config import CONFIG


class ChooseGameWindow:
    """
    Loads an in game window for handling saved games
    """

    def __init__(self, x_pos=CONFIG.WINDOW_WIDTH // 2, y_pos=CONFIG.WINDOW_HEIGHT // 2):
        self.background = None

    def display(self, screen):
        pass
