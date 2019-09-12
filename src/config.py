import os

from pygame import locals as keys

from consts import *


class Config:

    def __init__(self, file_name):
        """
        Loading config form the given file
        """

        # Set default attributes
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.FPS_LIMIT = 60
        self.CHARACTER_SIZE = 12
        self.SKIN_FILENAME = "media/base.png"

        # Keyboard configuration
        self.KEY_UP = keys.K_w
        self.KEY_DOWN = keys.K_s
        self.KEY_LEFT = keys.K_a
        self.KEY_RIGHT = keys.K_d
        self.KEY_JUMP = keys.K_SPACE
        self.KEY_SHOOT = keys.K_t
        self.KEY_ROLL = keys.K_t
        self.KEY_AIM_LOCK = keys.K_t

        # Sound configuration
        self.MASTER_VOLUME = 100
        self.SOUND_VOLUME = 100
        self.MUSIC_VOLUME = 100
        self.FULLSCREEN = False

        # Create the file if it doesn't exists
        if not os.path.isfile(file_name):
            open(file_name, 'w+').close()
        else:
            # Start reading config from file
            pass


# Loading configuration
CONFIG = Config(BASE_FOLDER + 'config.ini')    
