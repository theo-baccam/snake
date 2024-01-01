# Fonction pour gérer les collisions avec les bords, la pomme et le corps
# du serpent
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
