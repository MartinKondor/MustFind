"""
Resource Manager is responsible for storing commonly used
variables like fonts, textures, music and images.

Already declared as the global ```RM``` variable,
which must be loaded later on.
"""
from consts import BASE_FOLDER
from config import CONFIG


class ResourceManager:

    def __init__(self):
        self.gui_font = None

    def load(self, pygame):
        self.gui_font = pygame.font.Font(BASE_FOLDER + 'fonts/knewave.ttf', CONFIG.CHARACTER_SIZE)


RM = ResourceManager()
