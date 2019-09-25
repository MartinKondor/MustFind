"""
AI driven entity.
"""
from enum import Enum

import pygame

from map import Map
from config import CONFIG
from consts import Screens, IMAGE_FOLDER, BASE_SPEED, GRAVITY_CONST
from animation import Animation, BotAnimationType


class BotMoveType(Enum):
    UP = 0
    RIGHT = 1
    LEFT= 2
    STAND = 3


class Bot:
    
    def __init__(self, x_pos=0, y_pos=0, x_speed=0, y_speed=0):
        self.bot_move = BotMoveType.RIGHT
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.max_speed = 2
        self.jump_count = 0
        self.jump_limit = 1
        self.jump_power = 7
        self.camera_x = 0
        self.camera_y = 0
        self.width = 64
        self.height = 64
        self.animation = Animation(IMAGE_FOLDER + 'player.png', self.width, self.height)

    def collision_detection(self, map):

        # Move on keypress
        if self.bot_move == BotMoveType.RIGHT:
            self.x_speed += BASE_SPEED
        elif self.bot_move == BotMoveType.LEFT:
            self.x_speed -= BASE_SPEED
        else:
            self.x_speed = 0

        # Check if the bottom of the player is masked
        on_ground = Map.is_masked_h_line(map, 4, self.x_pos, self.y_pos + self.height + self.y_speed, self.width / 2)
        if on_ground:
            self.y_speed = 0
            self.jump_count = 0
        elif self.y_speed < 25:  # Gravity
            self.y_speed += GRAVITY_CONST

        # Jumping
        if on_ground and self.jump_count < self.jump_limit and self.bot_move == BotMoveType.UP:
            self.y_speed -= self.jump_power
            self.jump_count += 1
            self.animation.animation_type = BotAnimationType.FRONT

        # Check the sides of the bot        
        if Map.masked_top_v_line(map, 4, self.x_pos - self.width, self.y_pos, self.height) == 0:
            self.y_speed = 0
            if self.x_speed < 0:
                self.x_speed = 0
        elif Map.masked_top_v_line(map, 4, self.x_pos + self.width, self.y_pos, self.height) == 0:
            self.y_speed = 0
            if self.x_speed > 0:
                self.x_speed = 0

        # Check max speed
        if self.x_speed > self.max_speed:
            self.x_speed = self.max_speed
        elif self.x_speed < -self.max_speed:
            self.x_speed = -self.max_speed

        # Apply changes
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed

        # Change animation on direction change
        if self.x_speed < 0:
            self.animation.animation_type = BotAnimationType.LEFT
        elif self.x_speed > 0:
            self.animation.animation_type = BotAnimationType.RIGHT
        elif self.x_speed == 0 and self.y_speed == 0:
            self.animation.animation_type = BotAnimationType.STAND

    def update_bot_state(self):
        self.bot_move = BotMoveType.UP  # Just jump for now

    def display(self, screen, map, player):
        self.camera_x = player.camera_x
        self.camera_y = player.camera_y

        self.collision_detection(map)
        self.update_bot_state()
        self.animation.play(screen, self)
