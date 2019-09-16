"""
Playable entity.
"""
import pygame

from map import Map
from consts import Screens, IMAGE_FOLDER, BASE_SPEED, GRAVITY_CONST
from config import CONFIG


class MovingDirection:
    BACK = 0
    RIGHT = 1
    FRONT = 2
    LEFT = 3


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
        self.animation_type = MovingDirection.RIGHT
        self.animation_index = 0
        self.animation_frames = []

        # Get animation frames from image file
        anim_img = pygame.image.load(IMAGE_FOLDER + 'player.png')

        for j in range(4):
            anim_frames = []

            for i in range(3):
                anim_img.set_clip(pygame.Rect(i * self.width, j * self.height, self.width, self.height))
                anim_frames.append(anim_img.subsurface(anim_img.get_clip()))
            
            self.animation_frames.append(anim_frames)

    def collision_detection(self, map):
        pressed_keys = pygame.key.get_pressed()

        ###########
        # Check the sides of the player
        dist_from_right = Map.masked_top_v_line(map, 4, self.x_pos + self.width / 2, self.y_pos, self.height / 2)
        dist_from_left = Map.masked_top_v_line(map, 4, self.x_pos - self.width / 2, self.y_pos, self.height / 2)
        
        if dist_from_left == 0:            
            self.x_speed -= BASE_SPEED
        elif dist_from_right == 0:    
            self.x_speed += BASE_SPEED
        ###########

        # Check if the bottom of the player is masked
        on_ground = Map.is_masked_h_line(map, 4, self.x_pos, self.y_pos + self.height / 2, self.width / 2)
        if on_ground:
            self.y_speed = 0
            self.jump_count = 0
        elif not on_ground and self.y_speed < 25:  # Gravity
            self.y_speed += GRAVITY_CONST
 
        # Jumping
        if on_ground and self.jump_count < self.jump_limit and pressed_keys[CONFIG.KEY_UP]:
            self.y_speed -= self.jump_power
            self.jump_count += 1

        # Move on keypress
        if pressed_keys[CONFIG.KEY_RIGHT]:
            self.x_speed += BASE_SPEED
        elif pressed_keys[CONFIG.KEY_LEFT]:
            self.x_speed -= BASE_SPEED
        else:
            self.x_speed = 0

            # Instead of stopping, slow down
            #if self.x_speed != 0 and self.x_speed < 0:
            #    self.x_speed += 2.5 * BASE_SPEED
            #elif self.x_speed != 0 and self.x_speed > 0:
            #    self.x_speed -= 2.5 * BASE_SPEED

        if self.x_speed > self.max_speed:
            self.x_speed = self.max_speed

        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        self.camera_x = self.x_pos - CONFIG.WINDOW_WIDTH / 2
        self.camera_y = self.y_pos - CONFIG.WINDOW_HEIGHT / 2

        if self.x_speed < 0:
            self.animation_type = MovingDirection.LEFT
        elif self.x_speed > 0:
            self.animation_type = MovingDirection.RIGHT

    def display(self, screen, map):
        self.collision_detection(map)
        screen.blit(self.animation_frames[self.animation_type][self.animation_index],
                    (self.x_pos - self.camera_x - self.width / 2, self.y_pos - self.camera_y - self.height / 2,))
        self.animation_index += 1
        if self.animation_index == len(self.animation_frames[0]):
            self.animation_index = 0
