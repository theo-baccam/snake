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

player_x, player_y = (
    320,
    224,
)
player = pygame.Rect((player_x, player_y), (32, 32))

apple_x, apple_y = (
    64,
    64,
)
apple = pygame.Rect((apple_x, apple_y), (32, 32))


def move(increment_x, increment_y):
    return player.move(increment_x, increment_y)


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


def border_collision(player, border_list):
    for border in border_list:
        if player.colliderect(border):
            return True


def apple_collision(player, apple):
    if player.colliderect(apple):
        return 1
    else:
        return 0


direction = "right"
new_direction = ""
snake_length = 1

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
    player = movement_keys[direction]()
    pygame.draw.rect(screen, FOREGROUND, player)

    if border_collision(player, border_list):
        running = False

    snake_length += apple_collision(player, apple)

    pygame.display.flip()
    clock.tick(MAX_FPS)


pygame.quit()
