import os

import pygame

from render_functions import snake_directory


pygame.mixer.init()

hh_closed_path = os.path.join(snake_directory, "hi-hat-closed.mp3")
hh_closed = pygame.mixer.Sound(hh_closed_path)

hh_open_path = os.path.join(snake_directory, "hi-hat-open.mp3")
hh_open = pygame.mixer.Sound(hh_open_path)


def play_hh_closed():
    closed_hh = pygame.mixer.Channel(0)
    closed_hh.play(hh_closed)


def play_hh_open():
    open_hh = pygame.mixer.Channel(1)
    open_hh.play(hh_open)
