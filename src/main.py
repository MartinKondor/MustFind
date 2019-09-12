"""
Main file. Where the game starts.
"""
import pygame

from consts import *
from config import CONFIG
from screens.main_menu import MainMenuScreen


if __name__ == '__main__':
    if not pygame.font:
        print('ERROR: fonts are disabled')
        exit(1)
    if not pygame.mixer:
        print('ERROR: sounds are disabled')
        exit(1)

    # Starting the game
    pygame.init()
    screen = pygame.display.set_mode((CONFIG.WINDOW_WIDTH, CONFIG.WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.mouse.set_visible(1)

    gui_font = pygame.font.Font(BASE_FOLDER + 'fonts/knewave.ttf', CONFIG.CHARACTER_SIZE)

    # Loading screens
    main_menu = MainMenuScreen(gui_font)

    # Main loop
    exited = False
    while not exited:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exited = True

        if main_menu.display(screen) == 0:
            exited = True

        pygame.display.flip()

    pygame.quit()
