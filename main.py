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


border_top_x, border_top_y = (
    0,
    0,
)
border_top = pygame.Rect((border_top_x, border_top_y), (608, 32))

border_right_x, border_right_y = (
    608,
    0,
)
border_right = pygame.Rect((border_right_x, border_right_y), (32, 448))

border_bottom_x, border_bottom_y = (
    32,
    448,
)
border_bottom = pygame.Rect((border_bottom_x, border_bottom_y), (608, 32))

border_left_x, border_left_y = (
    0,
    32,
)
border_left = pygame.Rect((border_left_x, border_left_y), (32, 448))


player_x, player_y = (
    320,
    224,
)
player = pygame.Rect((player_x, player_y), (32, 32))

def move(increment_x, increment_y):
    return player.move(increment_x, increment_y)


def is_opposite_direction(direction, new_direction):
    if (
        (direction == "up" and new_direction == "down")
        or (direction == "down" and new_direction == "up")
        or (direction == "left" and new_direction == "right")
        or (direction == "right" and new_direction == "left")
    ):
        return True


direction = "right"
new_direction = ""

while running:
    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, FOREGROUND, border_top)
    pygame.draw.rect(screen, FOREGROUND, border_right)
    pygame.draw.rect(screen, FOREGROUND, border_bottom)
    pygame.draw.rect(screen, FOREGROUND, border_left)
    movement_keys = {
        "up": partial(move, 0, -32),
        "down": partial(move, 0, 32),
        "left": partial(move, -32, 0),
        "right": partial(move, 32, 0),
    }
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
    pygame.display.flip()
    clock.tick(MAX_FPS)


pygame.quit()
