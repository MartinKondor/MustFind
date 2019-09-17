"""
Settings screen, where the settings
can be checked and changed.
"""
import pygame

from .screen import Screen
from consts import Screens, KEYBOARD
from config import CONFIG
from gui import Button, ButtonState
from resource_manager import RM


class SettingsScreen(Screen):

    def __init__(self, last_screen_enum=None):
        self.last_screen_enum = last_screen_enum

        label_margin = 75
        self.labels = [
            (RM.readable_font.render('CONTROLS', 1, (255, 255, 255)), (75, 50),),
            (RM.readable_font.render('UP', 1, (240, 240, 240)), (75, 50 + 2 * label_margin),),
            (RM.readable_font.render('DOWN', 1, (240, 240, 240)), (75, 50 + 3 * label_margin),),
            (RM.readable_font.render('RIGHT', 1, (240, 240, 240)), (75, 50 + 4 * label_margin),),
            (RM.readable_font.render('LEFT', 1, (240, 240, 240)), (75, 50 + 5 * label_margin),)
        ]
        self.buttons = [
            (Button(2 * 75, 40 + 2 * label_margin, label=pygame.key.name(CONFIG.KEY_UP), font_family=RM.readable_font), 'Up'),
            (Button(2 * 75, 40 + 3 * label_margin, label=pygame.key.name(CONFIG.KEY_DOWN), font_family=RM.readable_font), 'Down'),
            (Button(2 * 75, 40 + 4 * label_margin, label=pygame.key.name(CONFIG.KEY_RIGHT), font_family=RM.readable_font), 'Right'),
            (Button(2 * 75, 40 + 5 * label_margin, label=pygame.key.name(CONFIG.KEY_LEFT), font_family=RM.readable_font), 'Left')
        ]
        self.back_button = Button(50, CONFIG.WINDOW_HEIGHT - 4 * CONFIG.CHARACTER_SIZE, label='BACK')

    def check_for_choosing_key(self, button, label):
        if button.state == ButtonState.RELEASED:
            in_key_choosing = True

            while in_key_choosing:
                for event in pygame.event.get():
                    if event.type != pygame.KEYDOWN:
                        continue                        
                    if event.key == pygame.locals.K_ESCAPE:
                        in_key_choosing = False
                        break

                    button.set_label(pygame.key.name(KEYBOARD[event.key]), RM.readable_font)
                    in_key_choosing = False

                    # Change key in configuration, too
                    if label == 'Up':
                        CONFIG.KEY_UP = KEYBOARD[event.key]
                    elif label == 'Down':
                        CONFIG.KEY_DOWN = KEYBOARD[event.key]
                    elif label == 'Right':
                        CONFIG.KEY_RIGHT = KEYBOARD[event.key]
                    elif label == 'Left':
                        CONFIG.KEY_LEFT = KEYBOARD[event.key]
                    CONFIG.save()
                    break

    def display(self, screen):
        for label in self.labels:
            screen.blit(label[0], label[1])
        for button, button_label in self.buttons:
            self.check_for_choosing_key(button, button_label)
            button.display(screen)

        self.back_button.display(screen)

        if self.back_button.state == ButtonState.RELEASED:
            return Screens.MAIN_MENU if self.last_screen_enum is None else self.last_screen_enum
        return Screens.SETTINGS
