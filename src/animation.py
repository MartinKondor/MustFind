import time

import pygame


class AnimationType:
    STAND = 2
    BACK = 0
    RIGHT = 1
    FRONT = 2
    LEFT = 3

class BotAnimationType:
    STAND = 2
    BACK = 0
    RIGHT = 1
    FRONT = 2
    LEFT = 3


class Animation:

    def __init__(self, file_name, width, height):
        self.animation_clock = time.time()
        self.animation_type = AnimationType.FRONT
        self.animation_index = 0
        self.animation_frames = []
        self.animation_frames_per_second = 12

        # Get animation frames from image file
        anim_img = pygame.image.load(file_name)

        for j in range(4):
            anim_frames = []
            for i in range(3):
                anim_img.set_clip(pygame.Rect(i * width, j * height, width, height))
                anim_frames.append(anim_img.subsurface(anim_img.get_clip()))
            
            self.animation_frames.append(anim_frames)

    def play(self, screen, entity):
        screen.blit(self.animation_frames[self.animation_type][self.animation_index],
            (entity.x_pos - entity.camera_x - entity.width / 2, entity.y_pos - entity.camera_y - entity.height / 2,))

        if self.animation_type != AnimationType.STAND and (time.time() - self.animation_clock) >= 1 / self.animation_frames_per_second:
            self.animation_clock = time.time()
            self.animation_index += 1

            if self.animation_index == len(self.animation_frames[0]):
                self.animation_index = 0

    def get_frame(self):
        return self.animation_frames[self.animation_type][self.animation_index]
