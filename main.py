from string import ascii_uppercase
from functools import partial
from random import choice

import pygame

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BACKGROUND = (64, 128, 32)
FOREGROUND = (16, 64, 16)

clock = pygame.time.Clock()
MAX_FPS = 3
running = True


def calculate_grid():
    grid_coordinate = {}
    GRID_WIDTH = 20
    GRID_HEIGHT = 15
    for index, letter in enumerate(ascii_uppercase[:GRID_HEIGHT]):
        for num in range(GRID_WIDTH):
            name = f"{letter}{num + 1}"
            grid_coordinate[name] = (num * 32, index * 32)
    return grid_coordinate


def choose_random_coordinate(grid_coordinate, snake_cell_positions):
    while True:
        random_coordinate = choice(list(grid_coordinate.values()))
        if (
            (random_coordinate[0] == 0) or
            (random_coordinate[0] == 608) or
            (random_coordinate[1] == 0) or
            (random_coordinate[1] == 448)
        ):
            continue
        elif random_coordinate in snake_cell_positions:
            continue
        return random_coordinate


def move(increment_x, increment_y):
    return snake_head.move(increment_x, increment_y)


movement_keys = {
    "up": partial(move, 0, -32),
    "down": partial(move, 0, 32),
    "left": partial(move, -32, 0),
    "right": partial(move, 32, 0),
}


def is_opposite_direction(direction, new_direction):
    if (
        (direction == "up" and new_direction == "down")
        or (direction == "down" and new_direction == "up")
        or (direction == "left" and new_direction == "right")
        or (direction == "right" and new_direction == "left")
    ):
        return True


def draw_border(screen, FOREGROUND, border_list):
    for border in border_list:
        pygame.draw.rect(screen, FOREGROUND, border)


def border_collision(snake_head, border_list):
    for border in border_list:
        if snake_head.colliderect(border):
            return True


def apple_collision(snake_head, apple):
    if snake_head.colliderect(apple):
        return True

def body_collision(snake_cell_positions):
    for cell in snake_cell_positions[:-1]:
        if cell == snake_cell_positions[-1]:
            return True


def calculate_snake_cell_positions(snake_cell_positions, snake_length, snake_head):
    if len(snake_cell_positions) == snake_length:
        snake_cell_positions.pop(0)
    snake_cell_positions.append((snake_head[0], snake_head[1]))


def render_snake(snake_cell_positions, screen, FOREGROUND):
    for i in snake_cell_positions:
        snake_cell = pygame.Rect((i), (32, 32))
        pygame.draw.rect(screen, FOREGROUND, snake_cell)


grid_coordinate = calculate_grid()

border_top = pygame.Rect(grid_coordinate["A1"], (608, 32))
border_right = pygame.Rect(grid_coordinate["A20"], (32, 448))
border_bottom = pygame.Rect(grid_coordinate["O2"], (608, 32))
border_left = pygame.Rect(grid_coordinate["B1"], (32, 448))
border_list = [border_top, border_right, border_bottom, border_left]

snake_head_x, snake_head_y = grid_coordinate["H11"]
snake_head = pygame.Rect((snake_head_x, snake_head_y), (32, 32))


direction = "right"
new_direction = ""
snake_length = 3
snake_cell_positions = []

random_coordinate = choose_random_coordinate(grid_coordinate, snake_cell_positions)
apple_x, apple_y = random_coordinate
apple = pygame.Rect((apple_x, apple_y), (32, 32))

while running:
    for event in pygame.event.get():
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_ESCAPE:
            running = False
        key_name = pygame.key.name(event.key)
        if key_name in movement_keys:
            new_direction = key_name
        if not is_opposite_direction(direction, new_direction):
            direction = new_direction

    snake_head = movement_keys[direction]()
    calculate_snake_cell_positions(snake_cell_positions, snake_length, snake_head)

    if body_collision(snake_cell_positions):
        running = False
        break

    if apple_collision(snake_head, apple):
        snake_length += 1
        apple[0], apple[1] = choose_random_coordinate(grid_coordinate, snake_cell_positions)

    screen.fill(BACKGROUND)

    draw_border(screen, FOREGROUND, border_list)
    pygame.draw.rect(screen, FOREGROUND, apple)
    render_snake(snake_cell_positions, screen, FOREGROUND)

    if border_collision(snake_head, border_list):
        running = False
        break

    pygame.display.flip()
    clock.tick(MAX_FPS)


pygame.quit()
