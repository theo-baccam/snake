from string import ascii_uppercase
from random import choice
from functools import partial

# La longueur initiale du serpent est 4 car c'est la longueur maximale
# que le serpent peut avoir sans pouvoir faire collision avec son propre corps
INITIAL_SNAKE_LENGTH = 4
snake_length = INITIAL_SNAKE_LENGTH
score = snake_length - INITIAL_SNAKE_LENGTH

direction = "right"
new_direction = ""


# Fonction qui divise l'écran en grille, et qui attribue à chaque grille
# un nom et une valeur
def calculate_grid():
    grid_coordinate = {}
    GRID_WIDTH = 20
    GRID_HEIGHT = 15
    for index, letter in enumerate(ascii_uppercase[:GRID_HEIGHT]):
        for num in range(GRID_WIDTH):
            name = f"{letter}{num + 1}"
            grid_coordinate[name] = (num * 32, index * 32)
    return grid_coordinate


# Fonction pour choisir une position aléatoirement pour la pomme
def choose_random_coordinate(grid_coordinate, snake_cell_positions):
    while True:
        random_coordinate = choice(list(grid_coordinate.values()))
        # Pour que la pomme n'apparaît pas dans un mur ou dans le corps
        # du serpent.
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


# Pour déplacer la tête du serpent
def move(increment_x, increment_y, snake_head):
    return snake_head.move(increment_x, increment_y)


# Pour vérifier si le joueur ne va pas dans la direction opposé,
# permet d'empêcher auto collision
def is_opposite_direction(direction, new_direction):
    if (
        (direction == "up" and new_direction == "down")
        or (direction == "down" and new_direction == "up")
        or (direction == "left" and new_direction == "right")
        or (direction == "right" and new_direction == "left")
    ):
        return True


# Pour calculer la position des cellules du corps du serpent
def calculate_snake_cell_positions(snake_cell_positions, snake_head):
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
