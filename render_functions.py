import os

import pygame

import logic_functions as lf

BORDER_COLOR = (57, 43, 53)
APPLE_COLOR = (187, 71, 79)
SNAKE_BODY_COLOR = (72, 107, 127)
SNAKE_HEAD_COLOR = (122, 156, 150)
BACKGROUND_COLOR = (209, 191, 176)

pygame.font.init()

snake_directory = os.path.dirname(os.path.abspath(__file__))
font_path = os.path.join(snake_directory, "Pixolletta8px.ttf")

FONT_SIZE = 32
FONT = pygame.font.Font(font_path, FONT_SIZE)


def draw_background(screen):
    screen.fill(BACKGROUND_COLOR)


def draw_border(screen, border_list):
    for border in border_list:
        pygame.draw.rect(screen, BORDER_COLOR, border)


def render_snake(snake_cell_positions, screen):
    for i in snake_cell_positions[:-1]:
        snake_cell = pygame.Rect((i), (32, 32))
        pygame.draw.rect(screen, SNAKE_BODY_COLOR, snake_cell)
    head = pygame.Rect((snake_cell_positions[-1]), (32, 32))
    pygame.draw.rect(screen, SNAKE_HEAD_COLOR, head)


def draw_apple(screen, apple):
    pygame.draw.rect(screen, APPLE_COLOR, apple)


def draw_score(screen):
    SCORE_SURFACE = FONT.render(f"SCORE: {lf.snake_length - lf.INITIAL_SNAKE_LENGTH}", True, BACKGROUND_COLOR)
    screen.blit(
        SCORE_SURFACE,
        (lf.grid_coordinate["A1"][0] + 3, lf.grid_coordinate["A1"][1] + 3),
    )

def draw_game_over(screen):
    GAME_OVER_SURFACE = FONT.render(f"GAME OVER", True, BORDER_COLOR)
    GAME_OVER_MIDDLE = GAME_OVER_SURFACE.get_width() / 2
    screen.blit(
        GAME_OVER_SURFACE,
        (lf.grid_coordinate["G11"][0] + 3 - GAME_OVER_MIDDLE, lf.grid_coordinate["G11"][1] + 3)
    )

    SCORE_SURFACE = FONT.render(f"SCORE: {lf.snake_length - lf.INITIAL_SNAKE_LENGTH}", True, BORDER_COLOR)
    SCORE_MIDDLE = SCORE_SURFACE.get_width() / 2
    screen.blit(
        SCORE_SURFACE,
        (lf.grid_coordinate["H11"][0] + 3 - SCORE_MIDDLE, lf.grid_coordinate["H11"][1] + 3)
    )
