"""
Simple GUI button.
"""
from enum import Enum

import pygame

from consts import IMAGE_FOLDER, BG_COLOR
from config import CONFIG
from resource_manager import RM


class ButtonState(Enum):
    NORMAL = 0
    CLICKED = 1
    HOVERED = 2
    RELEASED = 3


class Button:

    def __init__(self, x_pos, y_pos, label, font_color=(37, 37, 37), gui_img_path=IMAGE_FOLDER + 'gui.png', font_family=None):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.state = ButtonState.NORMAL
        self.label = label
        self.label_sprite = font_family.render(label, 1, font_color) if font_family is not None else RM.gui_font.render(label, 1, font_color)

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


class SimpleButton:

    def __init__(self, x_pos, y_pos, label, width=None, height=None,
                font_color=(240, 240, 255), outline_color=(200, 200, 255),
                outline_thickness=4, font_family=None):
        self.state = ButtonState.NORMAL
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.label = label
        self.width = width if width is not None else len(label) * CONFIG.CHARACTER_SIZE + 2 * CONFIG.CHARACTER_SIZE
        self.height = height if height is not None else len(label.splitlines()) * 2 * CONFIG.CHARACTER_SIZE
        self.outline_thickness = outline_thickness

        self.outline_color = outline_color
        self.clicked_outline_color = (255 - outline_color[0], 255 - outline_color[1], 255 - outline_color[2])

        self.font_color = font_color
        self.hover_font_color = (255 - font_color[0], 255 - font_color[1], 255 - font_color[2])
        self.label_sprite = None
        self.hover_label_sprite = None
        self.set_label(label, font_family)
     
    def set_label(self, label, font_family=None):
        self.label_sprite = font_family.render(label, 1, self.font_color) \
            if font_family is not None else RM.gui_font.render(label, 1, self.font_color)
        self.hover_label_sprite = font_family.render(label, 1, self.hover_font_color) \
            if font_family is not None else RM.gui_font.render(label, 1, self.hover_font_color)

    def display(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] > self.x_pos and mouse_pos[1] > self.y_pos and mouse_pos[0] < self.x_pos + self.width and mouse_pos[1] < self.y_pos + self.height:
            if pygame.mouse.get_pressed()[0]:
                self.state = ButtonState.CLICKED
            elif self.state == ButtonState.CLICKED:
                self.state = ButtonState.RELEASED
            else:
                self.state = ButtonState.HOVERED
        else:
            self.state = ButtonState.NORMAL

        # Show the body the outline and the label of the button
        # Change button according to state
        if self.state == ButtonState.HOVERED:
            pygame.draw.rect(screen, self.outline_color, (self.x_pos, self.y_pos, self.width, self.height))
            screen.blit(self.hover_label_sprite, (self.x_pos + self.width // 4, self.y_pos + self.height // 4))
        elif self.state == ButtonState.CLICKED or self.state == ButtonState.RELEASED:
            pygame.draw.rect(screen, self.clicked_outline_color, (self.x_pos, self.y_pos, self.width, self.height))
            screen.blit(self.label_sprite, (self.x_pos + self.width // 4, self.y_pos + self.height // 4))
        else:
            pygame.draw.rect(screen, self.outline_color, (self.x_pos, self.y_pos, self.width, self.height))
            pygame.draw.rect(screen, BG_COLOR, (self.x_pos + self.outline_thickness // 2,
                                        self.y_pos + self.outline_thickness // 2,
                                        self.width - self.outline_thickness,
                                        self.height - self.outline_thickness))
            screen.blit(self.label_sprite, (self.x_pos + self.width // 4, self.y_pos + self.height // 4))
