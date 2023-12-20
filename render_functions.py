import pygame


def draw_border(screen, COLOR, border_list):
    for border in border_list:
        pygame.draw.rect(screen, COLOR, border)


def render_snake(snake_cell_positions, screen, COLOR, COLOR_HEAD):
    for i in snake_cell_positions[:-1]:
        snake_cell = pygame.Rect((i), (32, 32))
        pygame.draw.rect(screen, COLOR, snake_cell)
    head = pygame.Rect((snake_cell_positions[-1]), (32, 32))
    pygame.draw.rect(screen, COLOR_HEAD, head)

def draw_apple(screen, COLOR, apple):
    pygame.draw.rect(screen, COLOR, apple)
