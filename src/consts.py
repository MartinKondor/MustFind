"""
Global constants.
"""
import os
from enum import Enum


class Screens(Enum):
    EXIT = 0
    LOADING = 1
    MAIN_MENU = 2
    SETTINGS = 3
    GAME = 4
    MULTIPLAYER_GAME = 5


VERSION = '0.0.1-beta'
BASE_FOLDER = os.getcwd() + '/bin/'

MAP_FOLDER = BASE_FOLDER + 'maps/'
TILESET_FOLDER = BASE_FOLDER + 'tilesets/'
IMAGE_FOLDER = BASE_FOLDER + 'images/'

WINDOW_TITLE = 'Must find (' + VERSION + ')'
BG_COLOR = (255, 255, 255)
GRAVITY_CONST = 0.375
