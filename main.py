import sys
import os

import pygame

import pygame_functions as pf
import object_coordinates as oc
import logic_functions as lf
import render_functions as rf
import collide_functions as cf
import sound_functions as sf

while pf.running and pf.playing:
    buffered_direction = lf.direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pf.running = False
            break
        if event.type != pygame.KEYDOWN:
            continue
        if event.key == pygame.K_ESCAPE:
            pf.running = False
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
        pf.playing = False

    if cf.apple_collision(oc.snake_head, oc.apple):
        lf.snake_length += 1
        oc.apple[0], oc.apple[1] = lf.choose_random_coordinate(
            lf.grid_coordinate, oc.snake_cell_positions
        )
        sf.play_hh_open()

    if cf.border_collision(oc.snake_head, oc.border_list):
        pf.playing = False
    
    if not pf.running:
        pf.pygame_quit()
        break

    if not pf.playing:
        rf.draw_game_over(pf.screen)
        pygame.display.update()
        pygame.time.delay(3600)
        pf.pygame_quit()
    rf.draw_background(pf.screen)
    rf.draw_border(pf.screen, oc.border_list)
    rf.draw_apple(pf.screen, oc.apple)
    rf.render_snake(oc.snake_cell_positions, pf.screen)
    rf.draw_score(pf.screen)

    pygame.display.flip()

    pf.clock.tick(pf.MAX_FPS)
