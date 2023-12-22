import sys

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
MAX_FPS = 0.5
running = True
playing = False


def pygame_init():
    pygame.init()


def pygame_quit():
    pygame.quit()
    sys.exit()
