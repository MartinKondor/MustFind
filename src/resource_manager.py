"""
Resource Manager is responsible for storing commonly used
variables like fonts, textures, music and images.

Already declared as the global ```RM``` variable,
which must be loaded later on.
"""
from consts import BASE_FOLDER, IMAGE_FOLDER
from config import CONFIG


class ResourceManager:

    def __init__(self):
        self.gui_font = None
        self.readable_font = None
        self.background_image = None

    def load(self, pygame):
        self.gui_font = pygame.font.Font(BASE_FOLDER + 'fonts/knewave.ttf', CONFIG.CHARACTER_SIZE)
        self.readable_font = pygame.font.Font(BASE_FOLDER + 'fonts/FreeSans.ttf', CONFIG.CHARACTER_SIZE)
        self.background_image = pygame.image.load(IMAGE_FOLDER + 'bg.png')


RM = ResourceManager()
