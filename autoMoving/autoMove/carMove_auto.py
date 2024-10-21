# carMove_auto.py
from autoMoving import shared_state


def movingAuto(direction, give_pos):
    move_x = 0
    move_y = 0
    if give_pos == 'move_x':
        return  move_x
    elif give_pos == 'move_y':
        return move_y

    if shared_state.nearest_distance is not None and shared_state.nearest_distance <= 60:
        if shared_state.car_up:
            if shared_state.car_right:
                move_x += 0.3
                move_y -= 0.3
            elif shared_state.car_left:
                move_x -= 0.3
                move_y -= 0.3
            else:
                move_y -= 0
                move_x = 0
        elif shared_state.car_down:
            if shared_state.car_right:
                move_x += 0.3
                move_y += 0.3
            elif shared_state.car_left:
                move_x -= 0.3
                move_y += 0.3
            else:
                move_y = 0
                move_x = 0
        else:
            if shared_state.car_right:
                move_x += 0.1
                move_y = 0
            elif shared_state.car_left:
                move_x -= 0.1
                move_y = 0
            else:
                move_x = 0
                move_y = 0

    if direction == 'x':
        return move_x
    elif direction == 'y':
        return move_y