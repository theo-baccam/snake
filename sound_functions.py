import os

import pygame

from file_functions import hh_closed_path, hh_open_path


pygame.mixer.init()

hh_closed = pygame.mixer.Sound(hh_closed_path)

hh_open = pygame.mixer.Sound(hh_open_path)


def play_hh_closed():
    closed_hh = pygame.mixer.Channel(0)
    closed_hh.play(hh_closed)


def play_hh_open():
    open_hh = pygame.mixer.Channel(1)
    open_hh.play(hh_open)
