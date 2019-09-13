"""
Main file. Where the game starts.
"""
import pygame

from consts import WINDOW_TITLE, Screens, BG_COLOR
from config import CONFIG
from screens.main_menu import MainMenuScreen
from screens.game import GameScreen
from screens.settings import SettingsScreen
from screens.loading import LoadingScreen
from resource_manager import RM


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
    RM.load(pygame)

    # Loading the current screen
    current_screen_enum = Screens.LOADING
    last_screen_enum = Screens.LOADING
    current_screen = LoadingScreen()

    # Main loop
    exited = False

    while not exited:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exited = True
                break

        screen.fill(BG_COLOR)
        current_screen_enum = current_screen.display(screen)

        if current_screen_enum == Screens.EXIT:
            exited = True
        elif current_screen_enum != last_screen_enum:
            if current_screen_enum == Screens.LOADING:
                current_screen = LoadingScreen()
            elif current_screen_enum == Screens.MAIN_MENU:
                current_screen = MainMenuScreen()
            elif current_screen_enum == Screens.GAME:
                current_screen = GameScreen()
            elif current_screen_enum == Screens.SETTINGS:
                current_screen = SettingsScreen(last_screen_enum)

            last_screen_enum = current_screen_enum

        pygame.display.update()
        pygame.display.flip()

    pygame.quit()
