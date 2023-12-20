from string import ascii_uppercase
from random import choice
from functools import partial

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
            (random_coordinate[0] == 0)
            or (random_coordinate[0] == 608)
            or (random_coordinate[1] == 0)
            or (random_coordinate[1] == 448)
        ):
            continue
        elif random_coordinate in snake_cell_positions:
            continue
        return random_coordinate


def move(increment_x, increment_y, snake_head):
    return snake_head.move(increment_x, increment_y)


def is_opposite_direction(direction, new_direction):
    if (
        (direction == "up" and new_direction == "down")
        or (direction == "down" and new_direction == "up")
        or (direction == "left" and new_direction == "right")
        or (direction == "right" and new_direction == "left")
    ):
        return True


def calculate_snake_cell_positions(snake_cell_positions, snake_length, snake_head):
    if len(snake_cell_positions) == snake_length:
        snake_cell_positions.pop(0)
    snake_cell_positions.append((snake_head[0], snake_head[1]))


grid_coordinate = calculate_grid()


movement_keys = {
    "up": partial(move, 0, -32),
    "down": partial(move, 0, 32),
    "left": partial(move, -32, 0),
    "right": partial(move, 32, 0),
}


