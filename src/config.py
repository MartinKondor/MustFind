"""
Configuration, where the settings are stored.

Already declared as the ```CONFIG``` global variable.
"""
import os

from pygame import locals as keys

from consts import *


class Config:

    def __init__(self, file_name):
        """
        Loading config form the given file
        """
        self.file_name = file_name

        # Set default attributes
        self.WINDOW_WIDTH = 800
        self.WINDOW_HEIGHT = 600
        self.FPS_LIMIT = 30
        self.CHARACTER_SIZE = 17

        # Keyboard configuration
        self.KEY_UP = keys.K_w
        self.KEY_DOWN = keys.K_s
        self.KEY_LEFT = keys.K_a
        self.KEY_RIGHT = keys.K_d

        # Sound configuration
        self.MASTER_VOLUME = 100
        self.SOUND_VOLUME = 100
        self.MUSIC_VOLUME = 100
        self.FULLSCREEN = False
        self.CURRENT_LEVEL = '0'

        # Create the file if it doesn't exists
        if not os.path.isfile(file_name):
            open(file_name, 'w+').close()
        else:
            # Start reading config from file
            self.load(file_name)

    def load(self, file_name):
        file = open(file_name, 'r')
        lines = file.read()
        file.close()

        lines = lines.splitlines()

        for line in lines:
            parts = line.split('=')

            if parts[0] == 'WINDOW_WIDTH':
                self.WINDOW_WIDTH = int(parts[1])
            if parts[0] == 'WINDOW_HEIGHT':
                self.WINDOW_HEIGHT = int(parts[1])
            if parts[0] == 'FPS_LIMIT':
                self.FPS_LIMIT = int(parts[1])
            if parts[0] == 'CHARACTER_SIZE':
                self.CHARACTER_SIZE = int(parts[1])
            if parts[0] == 'KEY_UP':
                self.KEY_UP = int(parts[1])
            if parts[0] == 'KEY_DOWN':
                self.KEY_DOWN = int(parts[1])
            if parts[0] == 'KEY_LEFT':
                self.KEY_LEFT = int(parts[1])
            if parts[0] == 'KEY_RIGHT':
                self.KEY_RIGHT = int(parts[1])
            if parts[0] == 'MASTER_VOLUME':
                self.MASTER_VOLUME = int(parts[1])
            if parts[0] == 'SOUND_VOLUME':
                self.SOUND_VOLUME = int(parts[1])
            if parts[0] == 'MUSIC_VOLUME':
                self.MUSIC_VOLUME = int(parts[1])
            if parts[0] == 'FULLSCREEN':
                self.FULLSCREEN = parts[1] == 'True'
            if parts[0] == 'CURRENT_LEVEL':
                self.CURRENT_LEVEL = parts[1]

    def save(self, file_name=None):
        if file_name is not None:
            self.file_name = file_name

        with open(self.file_name, 'w+') as file:
            file.write('WINDOW_WIDTH=' + str(self.WINDOW_WIDTH) + '\n')
            file.write('WINDOW_HEIGHT=' + str(self.WINDOW_HEIGHT) + '\n')
            file.write('FPS_LIMIT=' + str(self.FPS_LIMIT) + '\n')
            file.write('CHARACTER_SIZE=' + str(self.CHARACTER_SIZE) + '\n')
            file.write('KEY_UP=' + str(self.KEY_UP) + '\n')
            file.write('KEY_DOWN=' + str(self.KEY_DOWN) + '\n')
            file.write('KEY_LEFT=' + str(self.KEY_LEFT) + '\n')
            file.write('KEY_RIGHT=' + str(self.KEY_RIGHT) + '\n')
            file.write('MASTER_VOLUME=' + str(self.MASTER_VOLUME) + '\n')
            file.write('SOUND_VOLUME=' + str(self.SOUND_VOLUME) + '\n')
            file.write('MUSIC_VOLUME=' + str(self.MUSIC_VOLUME) + '\n')
            file.write('FULLSCREEN=' + str(self.FULLSCREEN) + '\n')
            file.write('CURRENT_LEVEL=' + str(self.CURRENT_LEVEL) + '\n')


# Loading configuration
CONFIG = Config(BASE_FOLDER + 'config.ini')    
