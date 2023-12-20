import os

import pygame

import logic_functions as lf
import render_functions as rf
import collide_functions as cf

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
MAX_FPS = 3
running = True

border_top = pygame.Rect(lf.grid_coordinate["A1"], (608, 32))
border_right = pygame.Rect(lf.grid_coordinate["A20"], (32, 448))
border_bottom = pygame.Rect(lf.grid_coordinate["O2"], (608, 32))
border_left = pygame.Rect(lf.grid_coordinate["B1"], (32, 448))
border_list = [border_top, border_right, border_bottom, border_left]

snake_head_x, snake_head_y = lf.grid_coordinate["H11"]
snake_head = pygame.Rect((snake_head_x, snake_head_y), (32, 32))


direction = "right"
new_direction = ""
snake_cell_positions = []

random_coordinate = lf.choose_random_coordinate(
    lf.grid_coordinate, snake_cell_positions
)
apple_x, apple_y = random_coordinate
apple = pygame.Rect((apple_x, apple_y), (32, 32))

while running:
    buffered_direction = direction
    for event in pygame.event.get():
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_ESCAPE:
            running = False
        key_name = pygame.key.name(event.key)
        if key_name in lf.movement_keys:
            new_direction = key_name
        if not lf.is_opposite_direction(buffered_direction, new_direction):
            direction = new_direction

    snake_head = lf.movement_keys[direction](snake_head)
    lf.calculate_snake_cell_positions(snake_cell_positions, lf.snake_length, snake_head)

    if cf.body_collision(snake_cell_positions):
        running = False
        break

    if cf.apple_collision(snake_head, apple):
        lf.snake_length += 1
        apple[0], apple[1] = lf.choose_random_coordinate(
            lf.grid_coordinate, snake_cell_positions
        )

    if cf.border_collision(snake_head, border_list):
        running = False
        break

    rf.draw_background(screen)
    rf.draw_border(screen, border_list)
    rf.draw_apple(screen, apple)
    rf.render_snake(snake_cell_positions, screen)
    rf.draw_score(screen)

    pygame.display.flip()
    clock.tick(MAX_FPS)

pygame.quit()
