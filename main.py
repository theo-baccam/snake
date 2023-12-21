import sys
import os

import pygame

import object_coordinates as oc
import logic_functions as lf
import render_functions as rf
import collide_functions as cf
import sound_functions as sf

pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
MAX_FPS = 5
running = True
playing = True

while running and playing:
    buffered_direction = lf.direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_ESCAPE:
            running = False
            break
        key_name = pygame.key.name(event.key)
        if key_name in lf.movement_keys:
            lf.new_direction = key_name
        if not lf.is_opposite_direction(buffered_direction):
            lf.direction = lf.new_direction

    oc.snake_head = lf.movement_keys[lf.direction](oc.snake_head)
    lf.calculate_snake_cell_positions(oc.snake_cell_positions, lf.snake_length, oc.snake_head)
    sf.play_hh_closed()

    if cf.body_collision(oc.snake_cell_positions):
        playing = False

    if cf.apple_collision(oc.snake_head, oc.apple):
        lf.snake_length += 1
        oc.apple[0], oc.apple[1] = lf.choose_random_coordinate(
            lf.grid_coordinate, oc.snake_cell_positions
        )
        sf.play_hh_open()

    if cf.border_collision(oc.snake_head, oc.border_list):
        playing = False
    
    if not running:
        pygame.quit()
        sys.exit()
        break

    if not playing:
        rf.draw_game_over(screen)
        pygame.display.update()
        pygame.time.delay(3600)
        pygame.quit()
        sys.exit()
    rf.draw_background(screen)
    rf.draw_border(screen, oc.border_list)
    rf.draw_apple(screen, oc.apple)
    rf.render_snake(oc.snake_cell_positions, screen)
    rf.draw_score(screen)

    pygame.display.flip()

    clock.tick(MAX_FPS)
