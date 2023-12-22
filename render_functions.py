import os
from functools import partial

import pygame

from file_functions import font_path, sprite_path

BORDER_COLOR = (57, 43, 53)
APPLE_COLOR = (187, 71, 79)
SNAKE_BODY_COLOR = (72, 107, 127)
SNAKE_HEAD_COLOR = (122, 156, 150)
BACKGROUND_COLOR = (209, 191, 176)

pygame.font.init()

FONT_SIZE = 32
FONT = pygame.font.Font(font_path, FONT_SIZE)


def draw_background(screen):
    screen.fill(BACKGROUND_COLOR)


def draw_border(screen, border_list):
    for border in border_list:
        pygame.draw.rect(screen, BORDER_COLOR, border)


def rotate_image(angle, image, position, screen):
    rotated = pygame.transform.rotate(image, angle)
    screen.blit(rotated, position)


rotation_dict = {
    "up up": partial(rotate_image, 0),
    "left left": partial(rotate_image, 90),
    "down down": partial(rotate_image, 180),
    "right right": partial(rotate_image, 270),

    "up left": partial(rotate_image, 0),
    "left down": partial(rotate_image, 90),
    "down right": partial(rotate_image, 180),
    "right up": partial(rotate_image, 270),

    "right down": partial(rotate_image, 0),
    "up right": partial(rotate_image, 90),
    "left up": partial(rotate_image, 180),
    "down left": partial(rotate_image, 270),
}


def render_snake(snake_cell_positions, snake_cell_turning, screen):
    tail = pygame.image.load(os.path.join(sprite_path, "snake-tail.png"))
    screen.blit(tail, snake_cell_positions[0])

    body_straight = pygame.image.load(
        os.path.join(sprite_path, "snake-body-straight.png")
    )
    body_turning = pygame.image.load(
        os.path.join(sprite_path, "snake-body-turning.png")
    )
    for index, value in enumerate(snake_cell_positions[1:-1]):
        if not snake_cell_turning[1:-1][index][0]:
            rotation_dict[snake_cell_turning[1:-1][index][1]](
                body_straight, value, screen
            )
        else:
            rotation_dict[snake_cell_turning[1:-1][index][1]](
                body_turning, value, screen
            )

    head = pygame.image.load(os.path.join(sprite_path, "snake-head.png"))
    screen.blit(head, snake_cell_positions[-1])


def draw_apple(screen, apple):
    pygame.draw.rect(screen, APPLE_COLOR, apple)


def draw_score(screen, score, xy_position):
    SCORE_SURFACE = FONT.render(f"SCORE: {score}", True, BACKGROUND_COLOR)
    screen.blit(SCORE_SURFACE, (xy_position[0] + 3, xy_position[1] + 3))


def draw_high_score(screen, high_score, xy_position):
    SCORE_SURFACE = FONT.render(f"HI-SCORE: {high_score}", True, BACKGROUND_COLOR)
    SCORE_WIDTH = SCORE_SURFACE.get_width()
    screen.blit(SCORE_SURFACE, (xy_position[0] + 32 - SCORE_WIDTH, xy_position[1] + 3))


def draw_game_over_text(screen, xy_position):
    GAME_OVER_SURFACE = FONT.render(f"GAME OVER", True, BORDER_COLOR)
    GAME_OVER_MIDDLE = GAME_OVER_SURFACE.get_width() / 2
    screen.blit(
        GAME_OVER_SURFACE, (xy_position[0] - GAME_OVER_MIDDLE + 3, xy_position[1] + 3)
    )


def draw_game_over_score(screen, score, xy_position):
    score_surface = FONT.render(f"SCORE: {score}", True, BORDER_COLOR)
    score_middle = score_surface.get_width() / 2
    screen.blit(score_surface, (xy_position[0] - score_middle + 3, xy_position[1] + 3))
