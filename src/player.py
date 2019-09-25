"""
Playable entity.
"""
import pygame

from map import Map
from consts import Screens, IMAGE_FOLDER, BASE_SPEED, GRAVITY_CONST
from config import CONFIG
from animation import Animation, AnimationType


class Player:
    
    def __init__(self, x_pos=0, y_pos=0, x_speed=0, y_speed=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.camera_x = x_pos
        self.camera_y = y_pos
        self.max_speed = 12
        self.jump_count = 0
        self.jump_limit = 1
        self.jump_power = 7
        self.width = 64
        self.height = 64
        self.animation = Animation(IMAGE_FOLDER + 'player.png', self.width, self.height)

    def collision_detection(self, map):
        pressed_keys = pygame.key.get_pressed()

        # Move on keypress
        if pressed_keys[CONFIG.KEY_RIGHT]:
            self.x_speed += BASE_SPEED
        elif pressed_keys[CONFIG.KEY_LEFT]:
            self.x_speed -= BASE_SPEED
        else:
            self.x_speed = 0

            # Instead of stopping, slow down
            #if self.x_speed != 0 and self.x_speed < 0:
            #    self.x_speed += self.x_speed / 2
            #elif self.x_speed != 0 and self.x_speed > 0:
            #    self.x_speed -= self.x_speed / 2

        # Check if the bottom of the player is masked
        on_ground = Map.is_masked_h_line(map, 4, self.x_pos, self.y_pos + self.height / 2 + self.y_speed / 2, self.width / 2)
        if on_ground:
            self.y_speed = 0
            self.jump_count = 0
        elif not on_ground and self.y_speed < 25:  # Gravity
            self.y_speed += GRAVITY_CONST

        # Jumping
        if on_ground and self.jump_count < self.jump_limit and pressed_keys[CONFIG.KEY_UP]:
            self.y_speed -= self.jump_power
            self.jump_count += 1
            self.animation.animation_type = AnimationType.FRONT

        # Check the sides of the player
        dist_from_right = Map.masked_top_v_line(map, 4, self.x_pos + self.width / 2, self.y_pos, self.height)
        dist_from_left = Map.masked_top_v_line(map, 4, self.x_pos - self.width / 2, self.y_pos, self.height)
        
        if dist_from_left == 0:
            self.y_speed = 0
            if self.x_speed < 0:
                self.x_speed = 0
        if dist_from_right == 0:
            self.y_speed = 0
            if self.x_speed > 0:
                self.x_speed = 0

        # Check max speed
        if self.x_speed > self.max_speed:
            self.x_speed = self.max_speed
        if self.x_speed < -self.max_speed:
            self.x_speed = -self.max_speed

        # Apply changes
        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        self.camera_x = self.x_pos - CONFIG.WINDOW_WIDTH / 2
        self.camera_y = self.y_pos - CONFIG.WINDOW_HEIGHT / 2

        # Change animation on direction change
        if self.x_speed < 0:
            self.animation.animation_type = AnimationType.LEFT
        elif self.x_speed > 0:
            self.animation.animation_type = AnimationType.RIGHT
        elif self.x_speed == 0 and self.y_speed == 0:
            self.animation.animation_type = AnimationType.STAND

    def display(self, screen, map):
        self.collision_detection(map)
        self.animation.play(screen, self)
