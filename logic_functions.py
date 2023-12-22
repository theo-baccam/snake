from string import ascii_uppercase
from random import choice
from functools import partial

INITIAL_SNAKE_LENGTH = 4
snake_length = INITIAL_SNAKE_LENGTH
score = snake_length - INITIAL_SNAKE_LENGTH

direction = ""
new_direction = ""

snake_cell_directions = []
snake_cell_turning = []


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


def calculate_snake_cell_positions(snake_cell_positions, snake_head):
    if len(snake_cell_positions) == snake_length:
        snake_cell_positions.pop(0)
    snake_cell_positions.append((snake_head[0], snake_head[1]))


def calculate_snake_cell_directions(snake_head):
    if len(snake_cell_directions) == snake_length:
        snake_cell_directions.pop(0)
    snake_cell_directions.append(direction)


def calculate_snake_cell_turning(snake_head):
    if len(snake_cell_directions) < 3:
        return
    snake_cell_turning.clear()

    for index, direction in enumerate(snake_cell_directions):
        if index == 0 or direction == snake_cell_directions[-1]:
            turn = (False, f"{direction} {direction}")
            snake_cell_turning.append(turn)
            continue

        if direction == snake_cell_directions[index + 1]:
            turn = (False, f"{direction} {snake_cell_directions[index + 1]}")
            snake_cell_turning.append(turn)
        else:
            turn = (True, f"{direction} {snake_cell_directions[index + 1]}")
            snake_cell_turning.append(turn)

grid_coordinate = calculate_grid()


movement_keys = {
    "up": partial(move, 0, -32),
    "down": partial(move, 0, 32),
    "left": partial(move, -32, 0),
    "right": partial(move, 32, 0),
}
