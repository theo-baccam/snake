from functools import partial

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

border_top = pygame.Rect((0, 0), (608, 32))
border_right = pygame.Rect((608, 0), (32, 448))
border_bottom = pygame.Rect((32, 448), (608, 32))
border_left = pygame.Rect((0, 32), (32, 448))

border_list = [border_top, border_right, border_bottom, border_left]

snake_head_x, snake_head_y = (
    320,
    224,
)
snake_head = pygame.Rect((snake_head_x, snake_head_y), (32, 32))

apple_x, apple_y = (
    64,
    64,
)
apple = pygame.Rect((apple_x, apple_y), (32, 32))


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
        return 1
    else:
        return 0


def calculate_snake_positions(snake_positions, snake_length, snake_head):
    if len(snake_positions) == snake_length:
        snake_positions.pop(0)
    snake_positions.append((snake_head[0], snake_head[1]))


def render_snake(snake_positions, screen, FOREGROUND):
    for i in snake_positions:
        snake_cell = pygame.Rect((i), (32, 32))
        pygame.draw.rect(screen, FOREGROUND, snake_cell)


direction = "right"
new_direction = ""
snake_length = 3
snake_positions = []

while running:
    screen.fill(BACKGROUND)

    draw_border(screen, FOREGROUND, border_list)

    pygame.draw.rect(screen, FOREGROUND, apple)

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

    if border_collision(snake_head, border_list):
        running = False

    snake_length += apple_collision(snake_head, apple)

    calculate_snake_positions(snake_positions, snake_length, snake_head)

    render_snake(snake_positions, screen, FOREGROUND)

    pygame.display.flip()
    clock.tick(MAX_FPS)


pygame.quit()
