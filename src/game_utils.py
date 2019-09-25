"""
Classes and functions for loading and saving games.
"""
import os

import pygame

from map import Map
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
        self.list = [fn.replace('.save', '') for fn in os.listdir(SAVE_FOLDER)]
        self.file_list = List(self.x_pos, self.y_pos, self.list)
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
            return False
        elif self.back_button.state == ButtonState.RELEASED:
            return False
        return True


def save_game(game):
    """
    Saves game object after asking for a filename.
    """
    with open(SAVE_FOLDER + 'first.save', 'w+') as save_file:
        save_file.write('player.x_pos=' + str(game.player.x_pos) + '\n')
        save_file.write('player.y_pos=' + str(game.player.y_pos) + '\n')
        
        save_file.write('bot.x_pos=' + str(game.bot.x_pos) + '\n')
        save_file.write('bot.y_pos=' + str(game.bot.y_pos) + '\n')

        save_file.write('map.file_name=' + str(game.map.file_name) + '\n')


def load_save_game(game):
    """
    Loads save game data from the CONFIG.SAVE_GAME to the given GameScreen object
    """
    save_file = open(SAVE_FOLDER + CONFIG.SAVE_GAME, 'r')
    lines = save_file.read().splitlines()
    save_file.close()

    for line in lines:
        if not line:
            continue

        parts = [p.strip() for p in line.split('=')]
        
        if parts[0] == 'player.x_pos':
            game.player.x_pos = float(parts[1])
        elif parts[0] == 'player.y_pos':
            game.player.y_pos = float(parts[1])
        elif parts[0] == 'bot.x_pos':
            game.bot.x_pos = float(parts[1])
        elif parts[0] == 'bot.y_pos':
            game.bot.y_pos = float(parts[1])
        if parts[0] == 'map.file_name':
            game.map = Map(parts[1])
