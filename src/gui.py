"""
Simple GUI button.
"""
from enum import Enum

import pygame

from consts import IMAGE_FOLDER, BG_COLOR, BG_COLOR_2
from config import CONFIG
from resource_manager import RM


class ButtonState(Enum):
    NORMAL = 0
    CLICKED = 1
    HOVERED = 2
    RELEASED = 3


class Button:

    def __init__(self, x_pos, y_pos, label, width=None, height=None,
                font_color=(250, 250, 255), outline_color=BG_COLOR_2,#(200, 200, 255),
                outline_thickness=8, font_family=None):
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


class List:

    def __init__(self, x_pos, y_pos, label_list, font_family=None,
                    font_color=(250, 250, 255)):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.label_list = label_list
        self.font_color = font_color
        self.box_color = (12, 63, 124,)
        self.box_hover_color = (83, 133, 193,)
        self.box_selected_color = (255, 131, 60,)
        self.selected_index = -1

        self.labels = [font_family.render(label, 1, self.font_color) \
            if font_family is not None else RM.readable_font.render(label, 1, self.font_color) for label in self.label_list]
        self.label_backgrounds = [
            pygame.Surface((len(label) * CONFIG.CHARACTER_SIZE + 2 * CONFIG.CHARACTER_SIZE, 1.5 * CONFIG.CHARACTER_SIZE,))
            for label in label_list]

        for label_background in self.label_backgrounds:
            label_background.fill(self.box_color)

    def display(self, screen):
        mouse_pos = pygame.mouse.get_pos()

        for i, label in enumerate(self.labels):
            bg_x = 25 + self.x_pos / 2
            bg_y = i * 33 + self.y_pos / 2

            if mouse_pos[0] > bg_x and mouse_pos[1] > bg_y and \
                    mouse_pos[0] < bg_x + self.label_backgrounds[i].get_width() and \
                    mouse_pos[1] < bg_y + self.label_backgrounds[i].get_height():
                self.label_backgrounds[i].fill(self.box_hover_color)

                if pygame.mouse.get_pressed()[0]:
                    self.selected_index = i

            elif self.selected_index == i:
                self.label_backgrounds[i].fill(self.box_selected_color)
            else:
                self.label_backgrounds[i].fill(self.box_color)

            screen.blit(self.label_backgrounds[i], (bg_x, bg_y,))
            screen.blit(label, (bg_x, bg_y,))
