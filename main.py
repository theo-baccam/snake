import pygame

import pygame_functions as pf
import file_functions as ff
import object_coordinates as oc
import logic_functions as lf
import render_functions as rf
import collide_functions as cf
import sound_functions as sf

# Boucle principale
while pf.running and pf.playing:
    # buffered_direction permet d'empêcher les auto collisions
    buffered_direction = lf.direction

    # Boucle pour gérer les inputs du joueur
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pf.running = False
            break

        if event.type != pygame.KEYDOWN:
            continue

        key_name = pygame.key.name(event.key)
        if not key_name in lf.movement_keys:
            continue

        lf.new_direction = key_name

        if not lf.is_opposite_direction(buffered_direction, lf.new_direction):
            lf.direction = lf.new_direction

    oc.snake_head = lf.movement_keys[lf.direction](oc.snake_head)

    lf.calculate_snake_cell_positions(oc.snake_cell_positions, oc.snake_head)

    sf.play_hh_closed()

    # Si le joueur fait collision avec soi-même, fin de partie
    if cf.body_collision(oc.snake_cell_positions):
        pf.playing = False

    # Si le joeur mange une pomme, ajouter au score et à la longuer du serpent
    if cf.apple_collision(oc.snake_head, oc.apple):
        lf.snake_length += 1
        lf.score += 1
        oc.apple[0], oc.apple[1] = lf.choose_random_coordinate(
            lf.grid_coordinate, oc.snake_cell_positions
        )
        sf.play_hh_open()

    # Si le joueur touche un mur, fin de partie
    if cf.border_collision(oc.snake_head, oc.border_list):
        pf.playing = False

    if not pf.running:
        pf.pygame_quit()
        ff.new_high_score(lf.score)
        break

    # Si la partie est fini, afficher écran game_over
    if not pf.playing:
        rf.draw_game_over_text(pf.screen, lf.grid_coordinate["G11"])
        rf.draw_game_over_score(pf.screen, lf.score, lf.grid_coordinate["H11"])
        ff.new_high_score(lf.score)
        pygame.display.update()
        pygame.time.delay(3600)
        pf.pygame_quit()

    # Fonctions pour afficher jeu
    rf.draw_background(pf.screen)
    rf.draw_border(pf.screen, oc.border_list)
    rf.draw_apple(pf.screen, oc.apple)
    rf.render_snake(oc.snake_cell_positions, pf.screen)
    rf.draw_high_score(pf.screen, ff.high_score, lf.grid_coordinate["A20"])
    rf.draw_score(pf.screen, lf.score, lf.grid_coordinate["A1"])

    pygame.display.flip()

    pf.clock.tick(pf.MAX_FPS)
