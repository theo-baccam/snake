import pygame

import logic_functions as lf

border_top = pygame.Rect(lf.grid_coordinate["A1"], (608, 32))
border_right = pygame.Rect(lf.grid_coordinate["A20"], (32, 448))
border_bottom = pygame.Rect(lf.grid_coordinate["O2"], (608, 32))
border_left = pygame.Rect(lf.grid_coordinate["B1"], (32, 448))
border_list = [border_top, border_right, border_bottom, border_left]

snake_head_x, snake_head_y = lf.grid_coordinate["H11"]
snake_head = pygame.Rect((snake_head_x, snake_head_y), (32, 32))

snake_cell_positions = []

random_coordinate = lf.choose_random_coordinate(
    lf.grid_coordinate, snake_cell_positions
)
apple_x, apple_y = random_coordinate
apple = pygame.Rect((apple_x, apple_y), (32, 32))
