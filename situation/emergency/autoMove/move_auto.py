# situation/emergency/autoMove/move_auto.py
def move_auto(direction):
    move_x = 0
    move_y = 0
    if direction == 'go_left':
        move_x -= 0.4
    elif direction == 'go_right':
        move_x += 0.4
    return move_x, move_y