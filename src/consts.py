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
WINDOW_TITLE = 'Must find (' + VERSION + ')'
GRAVITY_CONST = 0.375
