"""
Playable entity.
"""
import pygame

from map import Map
from consts import Screens, IMAGE_FOLDER, BASE_SPEED, GRAVITY_CONST
from config import CONFIG


class MovingDirection:
    UP = 0
    LEFT = 1
    RIGHT = 2
    DOWN = 3


class Player:
    
    def __init__(self, x_pos=0, y_pos=0, x_speed=0, y_speed=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.camera_x = 0
        self.camera_y = 0
        self.width = 95
        self.height = 159

        self.jump_count = 0
        self.jump_limit = 1
        self.jump_power = 12

        self.direction = MovingDirection.RIGHT

        # Animations are: 96x159
        self.animation_index = 0
        self.animation_frames = []

        # Get animation frames from image file
        anim_img = pygame.image.load(IMAGE_FOLDER + 'player.png')

        for j in range(4):
            direction_frames = []

            for i in range(12):
                anim_img.set_clip(pygame.Rect(self.width * i, j * self.height, self.width, self.height))
                direction_frames.append(anim_img.subsurface(anim_img.get_clip()))
            
            self.animation_frames.append(direction_frames)

    def display(self, screen, map):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[CONFIG.KEY_UP]:
            self.y_speed = -BASE_SPEED
        if pressed_keys[CONFIG.KEY_RIGHT]:
            self.x_speed = BASE_SPEED
        if pressed_keys[CONFIG.KEY_DOWN]:
            self.y_speed = BASE_SPEED
        if pressed_keys[CONFIG.KEY_LEFT]:
            self.x_speed = -BASE_SPEED

        d = Map.masked_top_v_area(map, 4, self.x_pos + self.width / 2, self.y_pos + self.height / 2, self.height, self.width)
        if d == 0:
            self.y_speed = 0
        else:
            self.y_speed += GRAVITY_CONST

        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        self.camera_x = self.x_pos - CONFIG.WINDOW_WIDTH // 2
        self.camera_y = self.y_pos - CONFIG.WINDOW_HEIGHT // 2

        screen.blit(self.animation_frames[self.direction][self.animation_index], (self.x_pos - self.camera_x - self.width // 2, self.y_pos - self.camera_y - self.height // 2,))
        self.animation_index += 1
        if self.animation_index == len(self.animation_frames[0]):
            self.animation_index = 0

        """
        pressed_keys = pygame.key.get_pressed()
        dist_from_ground = Map.masked_top_v_area(map, 4, self.x_pos - 14, self.y_pos + 31, self.width - 4, 10);

        if dist_from_ground < 10 and dist_from_ground <= self.y_speed:
            self.y_pos += dist_from_ground
            self.y_speed = 0
            self.jump_count = 0

            if pressed_keys[CONFIG.KEY_UP] and self.jump_count < self.jump_limit:
                self.y_speed = -self.jump_power
                self.jump_count += 1   
            else:
                self.y_speed += GRAVITY_CONST
                
                if self.y_speed < 0 and self.jump_count > 0 and not pressed_keys[CONFIG.KEY_UP]:
                    self.y_speed /= 1.5

        dist_from_ceiling = Map.masked_top_v_area(map, 4, self.x_pos - self.width / 2, self.y_pos - self.width, self.width, -10);

        if dist_from_ceiling > -10 and dist_from_ceiling >= self.y_speed:
            self.y_speed = 1
            self.y_pos += dist_from_ceiling

        if pressed_keys[CONFIG.KEY_LEFT]:
            if self.x_speed <= -6:
                self.x_speed -= .3
            else:
                self.x_speed = -6

            temp = Map.masked_top_v_line(map, 4, self.x_pos - 14, self.y_pos + 27, 8)
            if temp < 8:
                self.y_pos += -4 + temp
                if temp < 2 and self.x_speed > -4:
                    self.x_speed = -4

        elif pressed_keys[CONFIG.KEY_RIGHT]:
            if self.x_speed <= 6:
                self.x_speed += .3
            else:
                self.x_speed = 6

            temp = Map.masked_top_v_line(map, 4, self.x_pos + 13, self.y_pos + 27, 8)
            if temp < 8:
                self.y_pos += -4 + temp
                if temp < 2 and self.x_speed > 4:
                    self.x_speed = 4

        l_wall_intrusion = Map.masked_first_h_area(map, 4, self.x_pos - 10, self.y_pos - 30, -8, self.height - 9)
        r_wall_intrusion = Map.masked_first_h_area(map, 4, self.x_pos + 9, self.y_pos - 30, 8, self.height - 9)

        if self.x_speed <= 0 and l_wall_intrusion > -8:
            self.x_speed = 0
            self.x_pos += 7 + l_wall_intrusion
        if self.x_speed >= 0 and r_wall_intrusion < 8:
            self.x_speed = 0
            self.x_pos += -7 + r_wall_intrusion

        self.x_pos += self.x_speed
        self.y_pos += self.y_speed
        self.camera_x = self.x_pos - CONFIG.WINDOW_WIDTH / 2
        self.camera_y = self.y_pos - CONFIG.WINDOW_HEIGHT / 2

        screen.blit(self.animation_frames[self.direction][self.animation_index], (self.x_pos - self.camera_x - self.width // 2, self.y_pos - self.camera_y - self.height // 2,))
        self.animation_index += 1
        if self.animation_index == len(self.animation_frames[0]):
            self.animation_index = 0
        """
