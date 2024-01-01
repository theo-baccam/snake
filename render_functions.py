import os

import pygame

from file_functions import font_path

# Palette de couleur
BORDER_COLOR = (57, 43, 53)
APPLE_COLOR = (187, 71, 79)
SNAKE_BODY_COLOR = (72, 107, 127)
SNAKE_HEAD_COLOR = (122, 156, 150)
BACKGROUND_COLOR = (209, 191, 176)

pygame.font.init()

# Police
FONT_SIZE = 32
FONT = pygame.font.Font(font_path, FONT_SIZE)


# Fonction pour afficher fond
def draw_background(screen):
    screen.fill(BACKGROUND_COLOR)


# Fonction pour afficher bords
def draw_border(screen, border_list):
    for border in border_list:
        pygame.draw.rect(screen, BORDER_COLOR, border)


# Fonction pour afficher serpent
def render_snake(snake_cell_positions, screen):
    for i in snake_cell_positions[:-1]:
        snake_cell = pygame.Rect((i), (32, 32))
        pygame.draw.rect(screen, SNAKE_BODY_COLOR, snake_cell)
    head = pygame.Rect((snake_cell_positions[-1]), (32, 32))
    pygame.draw.rect(screen, SNAKE_HEAD_COLOR, head)


# Fonction pour afficher pomme
def draw_apple(screen, apple):
    pygame.draw.rect(screen, APPLE_COLOR, apple)


# Fonction pour afficher score
def draw_score(screen, score, xy_position):
    SCORE_SURFACE = FONT.render(f"SCORE: {score}", True, BACKGROUND_COLOR)
    screen.blit(SCORE_SURFACE, (xy_position[0] + 3, xy_position[1] + 3))


# Fonction pour afficher high score
def draw_high_score(screen, high_score, xy_position):
    SCORE_SURFACE = FONT.render(f"HI-SCORE: {high_score}", True, BACKGROUND_COLOR)
    SCORE_WIDTH = SCORE_SURFACE.get_width()
    screen.blit(SCORE_SURFACE, (xy_position[0] + 32 - SCORE_WIDTH, xy_position[1] + 3))


# Fonction pour afficher écran game over
def draw_game_over_text(screen, xy_position):
    GAME_OVER_SURFACE = FONT.render(f"GAME OVER", True, BORDER_COLOR)
    GAME_OVER_MIDDLE = GAME_OVER_SURFACE.get_width() / 2
    screen.blit(
        GAME_OVER_SURFACE, (xy_position[0] - GAME_OVER_MIDDLE + 3, xy_position[1] + 3)
    )


# Fonction pour afficher score dans écran game over
def draw_game_over_score(screen, score, xy_position):
    score_surface = FONT.render(f"SCORE: {score}", True, BORDER_COLOR)
    score_middle = score_surface.get_width() / 2
    screen.blit(score_surface, (xy_position[0] - score_middle + 3, xy_position[1] + 3))
