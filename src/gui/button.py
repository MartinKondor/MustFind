"""
Simple GUI button.
"""
from enum import Enum

import pygame

from consts import BASE_FOLDER
from config import CONFIG


class ButtonState(Enum):
    NORMAL = 0
    CLICKED = 1
    HOVERED = 2
    RELEASED = 3


class Button:

    def __init__(self, x_pos, y_pos, label, font_family, font_color=(37, 37, 37), gui_img_path=BASE_FOLDER + 'images/gui.png'):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.state = ButtonState.NORMAL
        self.label = label
        self.label_sprite = font_family.render(label, 1, font_color)

        # Load sprites
        gui_img = pygame.image.load(gui_img_path)
        gui_img.set_clip(pygame.Rect(0, 0, 96, 32))
        self.normal_sprite = gui_img.subsurface(gui_img.get_clip())

        gui_img.set_clip(pygame.Rect(96, 0, 96, 32))
        self.hover_sprite = gui_img.subsurface(gui_img.get_clip())

        gui_img.set_clip(pygame.Rect(2 * 96, 0, 96, 32))
        self.clicked_sprite = gui_img.subsurface(gui_img.get_clip())

    def display(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        window_size = screen.get_size()
        # label_size = self.label_sprite.get_size()

        if mouse_pos[0] > self.x_pos and mouse_pos[1] > self.y_pos and mouse_pos[0] < self.x_pos + 96 and mouse_pos[1] < self.y_pos + 32:
            if pygame.mouse.get_pressed()[0]:
                self.state = ButtonState.CLICKED
            elif self.state == ButtonState.CLICKED:
                self.state = ButtonState.RELEASED
            else:
                self.state = ButtonState.HOVERED
        else:
            self.state = ButtonState.NORMAL

        # Blit the correct sprite
        if self.state == ButtonState.NORMAL:
            screen.blit(self.normal_sprite, pygame.Rect(self.x_pos, self.y_pos, window_size[0], window_size[1]))
        elif self.state == ButtonState.HOVERED:
            screen.blit(self.hover_sprite, pygame.Rect(self.x_pos, self.y_pos, window_size[0], window_size[1]))
        elif self.state == ButtonState.CLICKED:
            screen.blit(self.clicked_sprite, pygame.Rect(self.x_pos, self.y_pos, window_size[0], window_size[1]))

        # Show the label
        screen.blit(self.label_sprite, (self.x_pos + len(self.label) // 2, self.y_pos + CONFIG.CHARACTER_SIZE // 2))
