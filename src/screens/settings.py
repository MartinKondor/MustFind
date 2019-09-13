"""
Settings screen, where the settings
can be checked and changed.
"""
from .screen import Screen
from consts import Screens
from config import CONFIG
from gui.button import SimpleButton, ButtonState


class SettingsScreen(Screen):

    def __init__(self):
        #self.KEY_UP
        #self.KEY_DOWN
        #self.KEY_LEFT
        #self.KEY_RIGHT
        #self.KEY_JUMP
        #self.KEY_SHOOT
        #self.KEY_ROLL
        #self.KEY_AIM_LOCK
        
        self.back_button = SimpleButton(50, CONFIG.WINDOW_HEIGHT - 4 * CONFIG.CHARACTER_SIZE, label='BACK')

    def display(self, screen, prev_screen=None):
        """
        :param prev_screen: the prevoius screen Screens enum value.
        """
        self.back_button.display(screen)

        if self.back_button.state == ButtonState.RELEASED:
            return Screens.MAIN_MENU if prev_screen is None else prev_screen
        return Screens.SETTINGS
